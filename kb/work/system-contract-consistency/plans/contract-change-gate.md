# Workshop-wide outcome — Promote a contract-change implementation gate

**State:** open; required before workshop closure.

**Audited against:** commit `6660bd2a`; motivated by the [witness
ledger](../baseline-2026-08-27.md) and the workshop's repeated consumer-drift
mechanism.

## Outcome selected

Promote one small implementation/review instruction for changes to
cross-cutting operative contracts. It complements the ADR type's operativity
path. It does not turn ADRs into file inventories and does not claim to detect
semantic contradictions automatically.

The instruction requires a change packet to identify:

1. authoritative declaration;
2. declared scope;
3. current operative consumer classes;
4. generated or projected forms;
5. fresh-install consequence;
6. existing-install migration;
7. acceptance test;
8. drift guard;
9. retained witnesses that are explicitly historical.

“Consumer classes” means behavioral roles such as validator, generator,
runtime skill, routing template, installed projection, and published view. A
change may name concrete files while implementing the packet, but the durable
instruction should not freeze today's paths as a universal list.

## Work

1. Read the instructions collection contract and content-routing guidance.
2. Select the narrowest existing implementation/review instruction that can own
   this gate, or write a short new instruction if none has that purpose.
3. Exercise the checklist against at least I2's projection change and one
   independent migration packet. Revise fields that fail to expose a consumer
   or produce work the implementer cannot use.
4. Add a narrow discoverability route from the change workflow that needs it.
5. Validate the durable artifact and record the worked applications here.

## Completion

The gate is operative when a current change workflow loads it, both worked
applications identify their independent consumers and migration boundary, and
the instruction has a concrete maintenance path. Workshop prose alone does not
complete this outcome.
