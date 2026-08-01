# Read-trace audit

Observer event streams contained 443 completed command events. Every observer command targeted one or more `packets/` files; one observer pass also used `rg`/`sed` over those same packet files for headings and links. No checkout, manifest, contract, catalogue, or history path appeared.

Mapper event streams contained 12 completed command events. Every mapper command targeted the corresponding `observations/pass-*.jsonl` file. No packet, checkout, manifest, contract, catalogue, or history path appeared.

The fixture root was outside the checkout and remained read-only to scored processes. This is instruction- and trace-audited isolation, not a technically complete filesystem boundary.
