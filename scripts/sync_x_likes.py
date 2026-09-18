"""Sync a disposable Markdown reading inbox from X likes.

Run: uv run python scripts/sync_x_likes.py
See scripts/README.md for retention, credentials, and API limitations.
"""
from __future__ import annotations

import argparse
import base64
import fcntl
import json
import os
import re
import tempfile
from datetime import UTC, datetime, timedelta
from pathlib import Path
from urllib.error import HTTPError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from dotenv import dotenv_values

ROOT = Path(__file__).resolve().parents[1]


def atomic_write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(dir=path.parent, prefix='.sync-')
    try:
        with os.fdopen(fd, 'w') as stream:
            stream.write(text)
        os.replace(name, path)
    finally:
        if os.path.exists(name):
            os.unlink(name)


class XClient:
    def __init__(self, env_path: Path, confidential: bool = False):
        self.env_path = env_path
        self.values = dict(dotenv_values(env_path))
        self.confidential = confidential
        if not self.values.get('X_ACCESS_TOKEN'):
            raise ValueError(f'Missing X_ACCESS_TOKEN in {env_path}')

    def request(self, path: str, *, form=None, headers=None):
        request = Request(
            'https://api.x.com/2/' + path,
            data=urlencode(form).encode() if form else None,
            headers=headers or {'Authorization': 'Bearer ' + self.values['X_ACCESS_TOKEN']},
        )
        with urlopen(request, timeout=30) as response:
            return json.load(response)

    def refresh(self):
        if not all(self.values.get(k) for k in ('X_REFRESH_TOKEN', 'X_CLIENT_ID')):
            raise ValueError('Token expired; need X_REFRESH_TOKEN and X_CLIENT_ID in .env')
        form = {'grant_type': 'refresh_token',
                'refresh_token': self.values['X_REFRESH_TOKEN'],
                'client_id': self.values['X_CLIENT_ID']}
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        if self.confidential:
            secret = self.values.get('X_CLIENT_SECRET')
            if not secret:
                raise ValueError('Confidential client needs X_CLIENT_SECRET')
            pair = self.values['X_CLIENT_ID'] + ':' + secret
            headers['Authorization'] = 'Basic ' + base64.b64encode(pair.encode()).decode()
        tokens = self.request('oauth2/token', form=form, headers=headers)
        updates = {'X_ACCESS_TOKEN': tokens['access_token']}
        if tokens.get('refresh_token'):
            updates['X_REFRESH_TOKEN'] = tokens['refresh_token']
        text = self.env_path.read_text()
        for key, value in updates.items():
            line = key + '=' + json.dumps(value)
            pattern = r'^' + key + r'=.*$'
            if re.search(pattern, text, re.MULTILINE):
                text = re.sub(pattern, lambda m, replacement=line: replacement, text, flags=re.MULTILINE)
            else:
                text = text.rstrip('\n') + '\n' + line + '\n'
        atomic_write(self.env_path, text)
        self.values.update(updates)

    def get(self, path: str):
        try:
            result = self.request(path)
        except HTTPError as exc:
            if exc.code != 401:
                raise
            self.refresh()
            result = self.request(path)
        if result.get('errors'):
            raise ValueError('X returned a partial response; sync not published')
        return result


def collect(client, user_id: str, seen: dict, max_pages: int):
    """Fetch before writing. Stop at prior history; initial run takes one page."""
    posts, authors = {}, {}
    cursor = None
    cursors = set()
    for _ in range(max_pages):
        params = {'max_results': 100,
                  'tweet.fields': 'created_at,author_id,entities,note_tweet,article',
                  'expansions': 'author_id', 'user.fields': 'username,name'}
        if cursor:
            params['pagination_token'] = cursor
        page = client.get(f'users/{user_id}/liked_tweets?' + urlencode(params))
        authors.update({u['id']: u for u in page.get('includes', {}).get('users', [])})
        overlap = False
        for post in page.get('data', []):
            post_id = post['id']
            if not re.fullmatch(r'[0-9]+', post_id):
                raise ValueError('Invalid post ID')
            if post_id in seen:
                overlap = True
                break
            posts[post_id] = post
        cursor = page.get('meta', {}).get('next_token')
        if not seen or overlap or not cursor:
            return posts, authors
        if cursor in cursors:
            raise ValueError('Repeated pagination cursor; sync not published')
        cursors.add(cursor)
    raise ValueError(f'No overlap after {max_pages} pages; cache unchanged. '
                     'Increase --max-pages to catch up.')


def render(record: dict) -> str:
    post, author = record['post'], record['author']
    username = author.get('username', post.get('author_id', 'unknown'))
    url = f"https://x.com/{username}/status/{post['id']}"
    note = post.get('note_tweet') or post.get('note_post') or {}
    text = note.get('text') or post.get('text', '')
    entities = note.get('entities') or post.get('entities') or {}
    links = [u.get('unwound_url') or u.get('expanded_url') or u.get('url')
             for u in entities.get('urls', [])]
    article = post.get('article') or {}
    title = article.get('title') or f'Liked post by @{username}'
    lines = [f'# {title}', '', f'Source: {url}',
             f"Author: {author.get('name', username)} (@{username})",
             f"Published: {post.get('created_at', 'unknown')}",
             f"First observed: {record['first_seen_at']}",
             'Like time: unavailable from X', '', text]
    if links:
        lines += ['', 'Links:', ''] + [f'- {link}' for link in dict.fromkeys(links) if link]
    return '\n'.join(lines) + '\n'


def sync(root: Path, client, handle: str, max_pages: int, now: datetime):
    state_path = root / 'kb/reports/state/x-likes' / handle / 'sync.json'
    cache = root / 'kb/reports/cache/x-likes' / handle
    state = json.loads(state_path.read_text()) if state_path.exists() else {
        'version': 1, 'seen': {}, 'active': {}}
    if state.get('version') != 1:
        raise ValueError('Unknown sync state version')
    user = client.get('users/me')['data']
    if user['username'].lower() != handle.lower():
        raise ValueError('Authenticated account does not match --handle')
    if state.get('user_id', user['id']) != user['id']:
        raise ValueError('Authenticated account differs from sync history')
    posts, authors = collect(client, user['id'], state['seen'], max_pages)
    timestamp = now.isoformat()
    for post_id, post in posts.items():
        state['seen'][post_id] = timestamp
        state['active'][post_id] = {'post': post,
            'author': authors.get(post.get('author_id'), {}), 'first_seen_at': timestamp}
    cutoff = now - timedelta(days=21)
    state['active'] = {key: rec for key, rec in state['active'].items()
                       if datetime.fromisoformat(rec['first_seen_at']) > cutoff}
    state.update(user_id=user['id'], last_sync_at=timestamp)
    # State is authoritative for rebuilding the cache after interrupted writes.
    atomic_write(state_path, json.dumps(state, ensure_ascii=False, indent=2) + '\n')
    for post_id, record in state['active'].items():
        atomic_write(cache / f'{post_id}.md', render(record))
    removed = 0
    for path in cache.glob('*.md'):
        if path.stem.isdigit() and path.stem not in state['active']:
            path.unlink()
            removed += 1
    return {'new': len(posts), 'cached': len(state['active']), 'removed': removed}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    parser.add_argument('--handle', default='zby')
    parser.add_argument('--max-pages', type=int, default=10,
                        help='Catch-up cap; exceeding it leaves cache/history unchanged')
    parser.add_argument('--confidential-client', action='store_true',
                        help='Use client-secret authentication when refreshing (web/bot apps)')
    args = parser.parse_args()
    if not re.fullmatch(r'[A-Za-z0-9_]{1,15}', args.handle) or args.max_pages < 1:
        parser.error('Need a valid handle and positive --max-pages')
    root = args.root.resolve()
    # One lock for all handles: token rotation also shares .env.
    lock_path = root / 'kb/reports/state/x-likes/.sync.lock'
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        with lock_path.open('a') as lock:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
            client = XClient(root / '.env', args.confidential_client)
            result = sync(root, client, args.handle.lower(), args.max_pages, datetime.now(UTC))
        print(json.dumps(result))
        return 0
    except HTTPError as exc:
        print(f'X API HTTP {exc.code}; sync failed. Check access, credits, or rate limits.')
    except BlockingIOError:
        print('Another likes sync is running.')
    except (OSError, ValueError, KeyError) as exc:
        # Avoid printing server bodies, request objects, or credential values.
        print(f'Sync failed ({type(exc).__name__}). Cache may need a successful rerun.')
        if isinstance(exc, ValueError) and not isinstance(exc, json.JSONDecodeError):
            print(str(exc))
    return 1


if __name__ == '__main__':
    raise SystemExit(main())
