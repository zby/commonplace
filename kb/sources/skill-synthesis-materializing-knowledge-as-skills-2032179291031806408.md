---
source: https://x.com/zeeg/status/2032179291031806408
captured: 2026-03-13T00:00:00+00:00
capture: webfetch
type: x-post
status_id: 2032179291031806408
linked_url: https://cra.mr/skill-synthesis
---

# Skill Synthesis: Materializing Knowledge as Skills

Author: @zeeg (David Cramer)
Post: https://x.com/zeeg/status/2032179291031806408
Created: 2026-03-12T19:37:00.000Z

I took the workflow we used to build our security skill and packaged it up into our skill-writer: `npx skills add getsentry/skills --skill skill-writer` So far its working really well for materializing knowledge as skills https://cra.mr/skill-synthesis

---

## Linked Article: Skill Synthesis

Source: https://cra.mr/skill-synthesis
Author: David Cramer
Published: 2026-02-23

David Cramer describes discovering IDORs (Insecure Direct Object References) in Sentry and developing an AI-powered solution called Warden to prevent such vulnerabilities systematically.

The core innovation is "Skill Synthesis" — a technique for creating specialized LLM agents by feeding trustworthy source material into Claude Code. Rather than relying on generic security guidance, Cramer synthesized skills from Sentry's actual commit history, past security patches, and internal documentation.

### Process

1. Collect domain-specific source material (OWASP cheat sheets, security patches, internal docs)
2. Feed into Claude Code via `/skill-creator`
3. Iterate based on results and false positives
4. Refine through multiple optimization passes

### Results

After two refinement iterations, Warden identified 17 potential vulnerabilities in Sentry's codebase, with 8 validated as genuine security issues — "some [undetected] for years" despite professional pen testing and code review practices.

### Key Claims

- Accuracy improves dramatically when LLMs receive organization-specific context rather than generic patterns
- "Skills are just files in a repo" — enabling version control and collaborative refinement
- The technique works because you feed the LLM trustworthy source material rather than asking it to generalize from scratch
- Plans to explore applying this technique to production data for performance prediction
