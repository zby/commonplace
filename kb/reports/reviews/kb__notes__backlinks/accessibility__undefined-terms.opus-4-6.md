"ingest reports" / "/ingest pipeline" — used in use case 2 and in the Trade-offs section: "The /ingest pipeline deliberately keeps connections in the ingest report rather than modifying KB notes." The term "ingest" as a KB-specific pipeline operation is not defined inline. A reader new to this KB's vocabulary cannot tell from context what "ingest" means as a pipeline step (as opposed to the ordinary English meaning of ingesting data).

"cold-start orientation" — used in use case 1: "This matters most during cold-start orientation in an unfamiliar area." "Cold-start" is borrowed from recommendation-system vocabulary but applied here in a KB context. The meaning can be inferred (starting fresh in an unfamiliar area), but it is KB-applied jargon worth a brief gloss.

"/connect skill" — used in design option C: "The /connect skill already has a 'Bidirectional Check' gate, but it's applied sporadically." The `/connect` skill is a KB-specific automation tool. It is introduced by name without any inline description of what it does. A reader cannot tell from "The /connect skill already has a 'Bidirectional Check' gate" what /connect is (a script, an agent command, a workflow).

Suggested fix: on first body mention, gloss as "/connect (a skill that discovers and reports connections between notes)."
