The PE table uses notation `[[Ps]](d) = [[P]](s, d)` with `P`, `Ps`, `s`, `d` defined in the surrounding prose, so the table itself is adequately grounded. However, the inline formula appears without enough inline definition of the double-bracket denotation operator:

> "Standard PE specialises a program P with respect to known **static** inputs s, producing a **residual program** Ps that needs only the remaining **dynamic** inputs d"

The symbols `P`, `s`, `d`, `Ps` are defined in the sentence above the formula block. The formula itself — `[[Ps]](d) = [[P]](s, d)` — uses `[[·]]` (denotational semantics brackets) without explaining this notation. A reader unfamiliar with denotational semantics cannot decode the formula without external knowledge. The note would be cleaner replacing the formula with plain language, since the surrounding prose already conveys the same content.
