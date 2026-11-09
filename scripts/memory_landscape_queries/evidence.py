"""Extract selected committed member sections for local semantic verification.

No source acquisition, live runs, checksum recomputation or retained-set writes.
Run only after directory validation. Matrix identity comes from snapshot.json.
"""
import json
import re
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
SNAPSHOT = json.loads((HERE / 'outputs-2026-11-09/snapshot.json').read_text())
COMMIT = SNAPSHOT['inputs_commit']
SELECTED = {
    'mozilla-ai--cq': ['RT-CLM-proposal-approval', 'RT-RTE-knowledge-proposal'],
    'dicklesworthstone--cass_memory_system': ['MEM-RTE-trauma-admission', 'EPI-RTE-curator-inversion'],
    'vectorize-io--hindsight': ['RT-RTE-claude-hooks'],
    'wujiangxu--a-mem-sys': ['RT-RTE-neighbor-evolution', 'MEM-ABS-usage-feedback'],
    'satyammistari--rem': ['MEM-OBJ-retrieval-count', 'RT-ABS-writeback-routes'],
    'aiming-lab--skillrl': ['RT-RTE-policy-update', 'RT-RTE-validation-admission'],
    'mcollina--pi-self-learning': ['RT-RTE-task-reflection', 'RT-RTE-context-injection'],
    'signet-ai--signetai': ['MEM-RTE-aggregate-recall', 'EPI-RTE-aggregate-guard', 'EPI-RTE-aggregate-retention'],
    'umezy--team-ai-workflows': ['MEM-ABS-trace-update'],
    'alfadur7--llm-wiki-newsroom': ['EPI-OBJ-experiment-ledger', 'EPI-RTE-judge-measurement'],
    '2601-01885v1': ['MEM-RTE-store-maintenance', 'RT-RTE-context-summary', 'RT-RTE-policy-update'],
    'nimbalyst--nimbalyst-wiki': ['RT-RTE-session-capture', 'RT-RTE-wiki-recall'],
}


def committed(path):
    return subprocess.check_output(['git', 'show', f'{COMMIT}:{path}'], text=True)


for stratum in SNAPSHOT['strata'].values():
    for row in stratum['identities']:
        directory = Path(row['review_file']).parent
        if directory.name not in SELECTED:
            continue
        print(f"# {row['system_name']}\n\n" + json.dumps(row, indent=2))
        for member in ['boundary.md', 'reconciliation.md']:
            print(f'\n## {directory / member}\n\n{committed(directory / member)}')
        for member in ['runtime.md', 'memory.md', 'epistemic.md']:
            text = committed(directory / member)
            for section in re.split(r'(?=^#### )', text, flags=re.MULTILINE):
                if any(section.startswith('#### ' + record + '\n')
                       for record in SELECTED[directory.name]):
                    print(f'\n## {directory / member}\n\n{section}')
        # Retain only units whose findings cite the selected canonical records.
        # AgeMem is the document-only contrast: retain its trace axes directly.
        text = committed(directory / 'memory-profile.md')
        import yaml
        profile = yaml.safe_load(text.split('---', 2)[1])['memory-comparison']
        selected = {}
        for axis, detail in profile['axes'].items():
            if axis not in ['write_agency', 'read_back_signal', 'curation_operations', 'trace_learning']:
                continue
            matching = [u for u in detail['units'] if any(
                any(ref.rsplit('#', 1)[-1] == record.lower()
                    for record in SELECTED[directory.name])
                for ref in u['records'])]
            if directory.name == '2601-01885v1' and axis in ['trace_learning', 'trace_source']:
                matching = detail['units']
            if matching:
                selected[axis] = {'assessment': detail['assessment'], 'units': matching}
        print('\n## Selected profile units\n\n' + json.dumps(selected, indent=2))
