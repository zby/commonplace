"""Import each stdlib C extension in turn and report which ones load.

A Smart App Control refusal surfaces as ImportError ("DLL load failed ...
application control policy") with a matching Code Integrity 3077 event.
"""
import importlib
import sys

MODULES = [
    "_decimal", "_ssl", "_hashlib", "_sqlite3", "_ctypes", "_bz2", "_lzma",
    "_socket", "select", "_asyncio", "_elementtree", "pyexpat", "_queue",
    "_overlapped", "_multiprocessing", "unicodedata", "_uuid", "_zoneinfo",
    "_wmi", "winsound", "_ctypes_test",
]
print(sys.executable, sys.version.split()[0])
failed = 0
for name in MODULES:
    try:
        mod = importlib.import_module(name)
        print(f"ok    {name}  {getattr(mod, '__file__', '(builtin)')}")
    except Exception as exc:  # report every failure kind, including OSError
        failed += 1
        print(f"FAIL  {name}  {type(exc).__name__}: {str(exc)[:120]}")
print(f"{len(MODULES) - failed} of {len(MODULES)} loaded")
raise SystemExit(1 if failed else 0)
