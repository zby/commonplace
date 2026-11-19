"""A retried physical launch is the boundary between Workjig lookup and audit evidence."""
import sys
from pathlib import Path

import pytest
from workjig import Request, RetryPolicy, Run

from commonplace.headless.harness import Harness, Profile
from commonplace.lib.agentic_analysis.audit import collect
from commonplace.lib.agentic_analysis.workflow import UNATTENDED

# Respond to the harness arguments that Workjig actually injects. In particular,
# Claude reports an arbitrary project path through its SessionStart hook.
WORKER = r'''
import json, os, shlex, subprocess, sys, time
from pathlib import Path
sid = sys.argv[sys.argv.index('--session-id') + 1]
if '--settings' in sys.argv:
    hook = json.loads(sys.argv[sys.argv.index('--settings') + 1])['hooks']['SessionStart'][0]['hooks'][0]['command']
    path = Path(os.environ['CLAUDE_CONFIG_DIR']) / 'projects' / 'not-derived-from-cwd' / (sid + '.jsonl')
    path.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(shlex.split(hook), input=json.dumps({'hook_event_name':'SessionStart', 'session_id':sid,
                   'transcript_path':str(path)}).encode(), check=True)
    records = [{'type':'assistant','sessionId':sid,'message':{'role':'assistant','content':[]}}]
    terminal = [{'type':'result','subtype':'success','is_error':False}]
else:
    path = Path(sys.argv[sys.argv.index('--session-dir') + 1]) / ('now_' + sid + '.jsonl')
    records = [{'type':'session','id':sid}]
    terminal = [{'type':'message_end','message':{'role':'assistant','stopReason':'stop'}},
                {'type':'agent_settled','aborted':False}]
path.write_text('\n'.join(map(json.dumps, records)))
flag = Path('first')
if not flag.exists():
    flag.touch()
    time.sleep(60)
frame = Path(sys.argv[-1].split('`')[1]).read_text()
Path(frame.split('- report.md: ')[1].splitlines()[0]).write_text('Report')
for event in terminal: print(json.dumps(event))
'''


@pytest.mark.parametrize('name,protocol', [('pi', 'pi-json'), ('claude-code', 'claude-stream-json')])
def test_expired_first_attempt_does_not_invalidate_retry(tmp_path, monkeypatch, name, protocol):
    monkeypatch.setenv('CLAUDE_CONFIG_DIR', str(tmp_path / 'claude'))
    monkeypatch.setenv('PI_CODING_AGENT_SESSION_DIR', str(tmp_path / 'pi'))
    script = tmp_path / 'fake.py'
    script.write_text(WORKER)
    harness = Harness(sys.executable, {'_subcommand': str(script)}, lambda p: {}, protocol)
    worker = harness.worker(Profile(name, 'fixture', 'medium', UNATTENDED[name]))
    root = tmp_path / 'run'
    with Run(root / 'calls', tmp_path) as records:
        result = records.call(Request('audit-fixture', 'Write report', {}, ('report.md',), worker,
                                      timeout_seconds=1.5, max_launches=2, retry=RetryPolicy(on=('timeout',))))
    assert [attempt.status for attempt in result.launches] == ['timeout', 'delivered']
    (first, retry), _ = collect(root)
    assert first['scan_status'] == retry['scan_status'] == 'scanned'
    assert first['session_id'] != retry['session_id']
    assert (Path(result.launches[1].launch_dir) / 'stdout.log').stat().st_size  # normal Workjig retention
    Path(first['trace']).unlink()
    (missing, unchanged), _ = collect(root)
    assert missing['scan_status'] == 'unscanned' and missing['session_status'] == 'unavailable'
    assert missing['session_id'] == first['session_id'] and unchanged == retry
    with Path(retry['trace']).open('a') as stream:
        stream.write('\n')
    (_, changed), _ = collect(root)
    assert changed['reason'] == 'native session hash mismatch'
