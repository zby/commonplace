# An index can retain where a previous result applies

This thought experiment illustrates a possible efficiency benefit of indexed
traces. It is not a measured result or a condition of conjectural learning.
Assume a fixed deterministic LLM and a mechanical trace scan that can locate
calls and results by identifiers or literal text, without interpreting
semantic relationships.

Suppose an earlier LLM call concluded:

> Retrying after a timeout can duplicate a write, because the server may have
> committed it before the response was lost.

A future task concerns duplicate charges after reconnecting. The trace keeps
the earlier call and its result, but the new task supplies neither its
identifier nor necessarily its wording. A scan can find the earlier words
without determining that their conclusion applies to the new situation.
Even scanning the full trace leaves that relationship to be established.

An index could retain the result's applicability condition, linked to the
call that produced it:

> Applies when an operation may have completed, but its caller did not receive
> confirmation.

This retains an interpretation of where the result applies. Future work need
not formulate that condition again. Determining whether the current situation
meets it may still require an LLM. Mechanical lookup would additionally need
suitable structured attributes on the current task or an established link.

The possible saving is repeated interpretation of applicability, not merely
finding text. Determinism guarantees reproduction from identical complete
inputs; it does not make mechanical scanning recognize an unstated semantic
relationship. If the trace already states and identifies the applicability
condition, an index may save only lookup work.

Whether this avoids another model call depends on the workflow: the consuming
call might perform the interpretation anyway. A comparison should allow full
trace scanning and count calls, input tokens, and correctness, including the
cost of producing and maintaining the index. The example motivates that
comparison; it does not establish an advantage.

Related: [the efficiency conjecture](./notes/commonplace-studies-conjectural-learning-through-retained-theories.md#three-conjectures).
