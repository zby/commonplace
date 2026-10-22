"""Q8b-Q10c: manual-admission basis split and curation-operation spread."""
from common import *  # noqa: F403
w=[r for r in code if any(f['value']=='manual' for u,f in findings(r,'write_agency')) and not any(f['value']=='manual' and f['basis'] in STRONG for u,f in findings(r,'write_agency'))]
print('Q8b weak-only manual systems', len(w), 'with claimed', sum(1 for r in w if any(f['value']=='manual' and f['basis']=='claimed' for u,f in findings(r,'write_agency'))), 'with afforded', sum(1 for r in w if any(f['value']=='manual' and f['basis']=='afforded' for u,f in findings(r,'write_agency'))))
print('Q8c total write_agency units', sum(len(units(r,'write_agency')) for r in code))
print('Q10c systems with 3-7 strong curation ops', sum(1 for r in code if 3<=len({f['value'] for u,f in findings(r,'curation_operations') if f['basis'] in STRONG})<=7))
