"""Behavioral tests for the local X likes inbox."""
import importlib.util
import json
from datetime import UTC, datetime, timedelta
from pathlib import Path
from urllib.error import HTTPError

import pytest

SPEC = importlib.util.spec_from_file_location(
    'sync_x_likes', Path(__file__).resolve().parents[2] / 'scripts/sync_x_likes.py')
mod = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(mod)
NOW = datetime(2026, 9, 17, tzinfo=UTC)


def post(post_id):
    return {'id': str(post_id), 'text': 'Short text', 'author_id': '9',
            'created_at': '2020-01-01T00:00:00Z'}


def page(*ids, next_token=None):
    return {'data': [post(i) for i in ids],
            'includes': {'users': [{'id': '9', 'username': 'author', 'name': 'Author'}]},
            'meta': {'next_token': next_token}}


class Client:
    def __init__(self, *pages, handle='zby'):
        self.pages = iter(pages)
        self.handle = handle
        self.calls = []

    def get(self, path):
        self.calls.append(path)
        if path == 'users/me':
            return {'data': {'id': '6059512', 'username': self.handle}}
        value = next(self.pages)
        if isinstance(value, Exception):
            raise value
        return value


def run(root, client, now=NOW, max_pages=10):
    return mod.sync(root, client, 'zby', max_pages, now)


def state_path(root):
    return root / 'kb/reports/state/x-likes/zby/sync.json'


def cache(root):
    return root / 'kb/reports/cache/x-likes/zby'


def test_bootstrap_ignores_publication_age_then_catches_up(tmp_path):
    c = Client(page(5, 4, next_token='older'))
    assert run(tmp_path, c)['new'] == 2
    assert len(c.calls) == 2  # bootstrap is deliberately one page
    assert '2020-01-01' in (cache(tmp_path) / '5.md').read_text()
    c = Client(page(8, 7, next_token='next'), page(6, 5, 4, 3))
    assert run(tmp_path, c, NOW + timedelta(days=1))['new'] == 3
    assert 'pagination_token=next' in c.calls[-1]
    state = json.loads(state_path(tmp_path).read_text())
    assert state['seen']['5'] == NOW.isoformat()
    assert '3' not in state['seen']  # don't import pre-bootstrap history
    assert run(tmp_path, Client(page(8, 7, 6)))['new'] == 0


def test_expiration_and_rebuild_do_not_reintroduce_old_likes(tmp_path):
    run(tmp_path, Client(page(5, 4)))
    (cache(tmp_path) / '5.md').unlink()
    run(tmp_path, Client(page(5, 4)), NOW + timedelta(days=1))
    assert (cache(tmp_path) / '5.md').exists()
    result = run(tmp_path, Client(page(6, 5, 4)), NOW + timedelta(days=21))
    assert result == {'new': 1, 'cached': 1, 'removed': 2}
    result = run(tmp_path, Client(page(6, 5, 4)), NOW + timedelta(days=22))
    assert result['new'] == 0
    assert set(json.loads(state_path(tmp_path).read_text())['seen']) == {'4', '5', '6'}
    assert [p.name for p in cache(tmp_path).glob('*.md')] == ['6.md']


@pytest.mark.parametrize('pages,limit', [
    ([page(6, next_token='next'), OSError('offline')], 10),
    ([page(6, next_token='next')], 1),
])
def test_incomplete_fetch_preserves_history_and_expired_cache(tmp_path, pages, limit):
    run(tmp_path, Client(page(5)))
    before = state_path(tmp_path).read_bytes()
    with pytest.raises((ValueError, OSError)):
        run(tmp_path, Client(*pages), NOW + timedelta(days=30), limit)
    assert state_path(tmp_path).read_bytes() == before
    assert (cache(tmp_path) / '5.md').exists()
    assert not (cache(tmp_path) / '6.md').exists()


def test_wrong_account_does_not_write(tmp_path):
    with pytest.raises(ValueError, match='account'):
        run(tmp_path, Client(handle='someone_else'))
    assert not state_path(tmp_path).exists()


def test_full_text_and_links():
    record = {'post': {**post(1), 'note_tweet': {
        'text': 'Full long post', 'entities': {'urls': [
            {'expanded_url': 'https://example.com/paper'}]}},
        'article': {'title': 'An article'}},
        'author': {'username': 'author'}, 'first_seen_at': NOW.isoformat()}
    text = mod.render(record)
    assert 'Full long post' in text and 'Short text' not in text
    assert 'https://example.com/paper' in text and '# An article' in text


def test_refresh_rotates_tokens_preserves_other_entries_and_retries(tmp_path, monkeypatch):
    env = tmp_path / '.env'
    env.write_text('X_ACCESS_TOKEN=old\nX_REFRESH_TOKEN=refresh\nX_CLIENT_ID=id\n'
                   'X_BEARER_TOKEN=keep\n# keep comment\n')
    client = mod.XClient(env)
    calls = []

    def request(path, **kwargs):
        calls.append((path, kwargs))
        if len(calls) == 1:
            raise HTTPError('https://api.x.com/2/users/me', 401, 'expired', {}, None)
        if path == 'oauth2/token':
            assert kwargs['form']['refresh_token'] == 'refresh'
            assert 'Authorization' not in kwargs['headers']  # native public client
            return {'access_token': 'new', 'refresh_token': 'rotated'}
        assert client.values['X_ACCESS_TOKEN'] == 'new'
        return {'data': {'id': '6059512'}}

    monkeypatch.setattr(client, 'request', request)
    assert client.get('users/me')['data']['id'] == '6059512'
    saved = mod.dotenv_values(env)
    assert saved['X_REFRESH_TOKEN'] == 'rotated'
    assert saved['X_BEARER_TOKEN'] == 'keep'
    assert '# keep comment' in env.read_text()
    assert env.stat().st_mode & 0o777 == 0o600


def test_partial_api_response_is_not_accepted(tmp_path, monkeypatch):
    env = tmp_path / '.env'
    env.write_text('X_ACCESS_TOKEN=token\n')
    client = mod.XClient(env)
    monkeypatch.setattr(client, 'request', lambda path: {'data': [post(1)], 'errors': [{}]})
    with pytest.raises(ValueError, match='partial'):
        client.get('users/6059512/liked_tweets')
