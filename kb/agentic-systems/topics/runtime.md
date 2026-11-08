# Runtime & Control

Runtime architecture determines how a system chooses, authorizes and executes its next action.

## Research questions

- Where does control live: a fixed loop, a model-written program or an external scheduler?
- How are tools and delegated workers authorized, and where are permissions enforced?
- How is execution context assembled, and which state survives a restart?
- What can a trace establish about the actions actually taken?

## Inspect implementations

The [current runtime accounts](../comparisons/runtime/systems.md) link directly
to the corresponding member of each accepted analysis. Start with the system's
overview and boundary when interpreting a route: different analyses inspect
different versions and scopes.

The [runtime lens landing](../comparisons/runtime/README.md) explains that member's
scope. There is no structured comparison table or cross-system synthesis for
this lens yet. These questions are a research agenda, not findings about every
listed system.

[Agent Memory](./memory.md) provides related comparisons of retention and later
consumption. [Methods & Data](../methods.md) explains evidence levels;
[All research topics](./README.md) returns to the topic index.
