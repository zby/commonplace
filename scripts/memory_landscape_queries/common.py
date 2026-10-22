"""Shared loading for the memory-landscape query ledger.

Reads the memory matrix (default: the public memory-systems.csv; pass another
path as the first argument) and defines the population splits and helpers the
ledger scripts use.
"""
import csv, json, collections, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
P = sys.argv[1] if len(sys.argv) > 1 else ROOT / 'kb/agentic-systems/comparisons/memory/memory-systems.csv'
csv.field_size_limit(sys.maxsize)
R=list(csv.DictReader(open(P)))
AX=['storage_substrate','representational_form','lineage','behavioral_authority','write_agency','curation_operations','read_back_direction','read_back_signal','trace_learning','trace_source']
STRONG={'wired','observed','causally supported'}
C=collections.Counter
def units(r,a): return json.loads(r[a+'_units'] or '[]')
def findings(r,a):
    for u in units(r,a):
        for f in u['findings']: yield u,f
code=[r for r in R if r['source_tier']=='code-grounded']
doc=[r for r in R if r['source_tier']=='doc-grounded']
def sv(r,a): return {f['value'] for u,f in findings(r,a) if f['basis'] in STRONG}
def wv(r,a): return {f['value'] for u,f in findings(r,a)}
