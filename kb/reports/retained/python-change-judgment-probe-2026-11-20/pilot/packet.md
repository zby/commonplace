# Evidence packet: Python 2.5 and Python 3.13

Use this file as the entire evidence packet. These are selected language behaviors, not a representative survey of twenty years. Links identify the sources; no lookup is needed. The teams in the task are fictional. Treat their requirements as given, not as facts about Python users generally.

**S1 — Earlier behavior.** The Python project's [Unicode HOWTO, CPython v2.5.6](https://github.com/python/cpython/blob/v2.5.6/Doc/howto/unicode.rst#L315-L326), demonstrates a Unicode string's search method accepting an 8-bit argument. ASCII input works. Its non-ASCII example fails because the implicit conversion uses ASCII. This is not evidence that Python 2 could not handle Unicode: explicitly decoded text works there too.

**S2 — Changed behavior and compatibility.** The Python project's [What's New in Python 3.0, text and data section, as retained at v3.13.1](https://github.com/python/cpython/blob/v3.13.1/Doc/whatsnew/3.0.rst#L237-L256), contrasts Python 2's input-dependent conversion with Python 3's distinction between text and bytes. For concatenation the distinction matters even for ASCII input. Source code relying on the old conversion needs to change. The document advocates the change; its authors' preference is not a measurement of users' costs.

**S3 — A capability already present.** The Python project's [What's New in Python 2.5, with statement](https://github.com/python/cpython/blob/v3.13.1/Doc/whatsnew/2.5.rst#L586-L620), shows the future import and a file opened in a `with` statement. The file closes when the block exits, including on an exception. Python 3.13 does not require that future import. Do not infer a new ability to ensure cleanup merely from seeing it in modern code.

**S4 — A later library facility.** The Python project's [Python 3.13.1 asyncio task-group documentation](https://github.com/python/cpython/blob/v3.13.1/Doc/library/asyncio-task.rst#L318-L380) describes `TaskGroup`, added in 3.11. On exit it waits for its tasks. When a child fails with an exception other than cancellation it cancels the remaining tasks and waits for them. This concerns tasks in that group. It describes a standard-library facility, not the impossibility of writing equivalent coordination in an older language.

**S5 — Small execution check, CPython 3.13.1.** For each byte string below the workshop author evaluated `'Name: ' + raw` and `'Name: ' + raw.decode('utf-8')`. The input contract for this check was UTF-8.

| Raw bytes in hex | Direct addition | After explicit decoding |
|---|---|---|
| `416461` | TypeError | Name: Ada |
| `4a6f73c3a9` | TypeError | Name: José |

No 2.5 interpreter was run. For the historical comparison the analogous prefix is Unicode (`u'Name: '`), not a Python 2 byte-string literal. No timing, failure rate, porting effort, or user preference was measured.
