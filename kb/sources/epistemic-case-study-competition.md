---
source: https://www.lesswrong.com/posts/frizRHnA6AZpJSDqw/lab-leaks-black-holes-and-eggs-epistemic-case-study
description: Future of Life Foundation competition brief for AI-assisted epistemic investigations and compounding knowledge bases, including its ingestion, structure, assessment, and personal-use implications.
captured: 2026-07-12
capture: web-fetch
type: kb/sources/types/snapshot.md
genre: official-statement
tags: [epistack, epistemology, knowledge-bases]
---

# Lab Leaks, Black Holes, and Eggs: Epistemic Case Study Competition

Author: Oliver Sourbut, Josh Jacobson, Future of Life Foundation (FLF)
Source: https://www.lesswrong.com/posts/frizRHnA6AZpJSDqw/lab-leaks-black-holes-and-eggs-epistemic-case-study
Date: 4 June 2026

FLF is running a competition to find the best workflows and methodologies for using AI to produce reliable, trustworthy knowledge bases, grounded in real-world cases. We’re open-minded on the types of submissions we receive and on how they address the problem. We’ve set aside approximately $200k for prizes. Winning submissions may receive a prize from $5k-$50k and, if submissions warrant, multiple $50k prizes are possible. Winners may be offered opportunities for further funded work.

The heights of human epistemic investigation are impressive and valuable, but rare and difficult to reach — see our abridged collection of strong examples. The limiting factor is rarely exquisite insight (though this helps!), and more often diligence, a curious and open mindset, and the time and effort needed to do the thorough work investigating background on a topic: activities AI is well placed to assist with.

Existing AI-assisted knowledge base work demonstrates real pieces of this — agent memory (e.g., Claude Code's memory and skills), LLM-curated personal wikis (Karpathy's perhaps the highest-profile), and deep-research tools. But these mostly produce single-user artifacts tuned to one investigator's context, not the kind that travel, combine, or survive (especially adversarial) scrutiny.

We’re particularly excited by the compounding potential — if structured analyses become reusable, refineable artifacts, every serious investigation enables future work, on the same or related topics, and by the same or different people, to reach further from a more solid epistemic foundation.

This competition provides three challenging case studies — with deliberately varied challenge profiles — and invites you to produce tooling and techniques to help people navigate them. First, the debated and impactful question of COVID-19 origins. Second, the risk that the Large Hadron Collider (LHC) creates synthetic black holes (perhaps destroying the Earth). Third, the health impact of eggs (as a human food source).

The tooling should be general: we’ll judge against these and also other difficult case studies.

## What we're looking for

We want to see workflows and methodologies using AI that advance the state of the art in carrying out epistemic investigations and producing compounding knowledge bases. We aren’t asking you to build an entire, robust, fully-featured system. Instead, we’re excited by any submission that advances the state-of-the-art on a component.

We’ve found it useful to think of these investigations as being split into several different layers: ingestion, structure, and assessment. When stacked together and operating in concert, they’d create useful trusted artifacts — something like a superior deep research, generating and interacting with a structured knowledge base, aimed at the truly epistemically discerning consumer.

### Ingestion

How do you take a messy, multi-source evidence base and turn it into something structured enough to reason over?

- Extract and attribute claims to specific sources, with provenance metadata (who said what, when, in what context).
- Identify when the same claim appears across multiple sources in different forms.
- Search for resources with bearing on topics and subtopics at hand.
- Capture useful metadata tags, for example relating sources and claims to topics and other sources, or about methodologies, deference, and assumptions.

### Structure

How do you document the relationships between claims so that the full shape of the argument becomes navigable?

- Resolve the inference structure: which claims and evidence are offered as support for which other claims.
- Represent the discourse structure: where people are addressing different sub-questions and perhaps how they are tracking those relating to an overall inquiry — including explicit and implicit differences of emphasis.
- Capture relationships regarding “similar but not identical” claims, such as different framings of conditions or caveats, or different estimates of uncertainty for quantities or propositions.
- Track how the structure evolves over time.

### Assessment

How do you evaluate what to actually believe, or what to look at next, given everything above?

- Identify rhetorical moves that carry more persuasive weight than evidential weight.
- Flag correlated evidence being treated as independent.
- Identify cruxes: the specific factual or inferential disagreements that, if resolved, would most change the overall picture.
- Surface what’s missing — important sources or perspectives that aren’t represented in the working knowledge base, toward further data collection or additional primary information collection and reasoning.
- Provide frameworks for calibrating confidence that account for out-of-model error, adversarial information environments, and the limits of any single analyst’s expertise.
- Distinguish what the debate settled from what it merely performed settling.

## What a good entry looks like

We’ll offer a minimum of $5k to entries which we judge to meaningfully improve on the state of the art in faithful, scalable AI-assisted investigations, and up to $50k for entries which are truly inspiring to us. This might be by reliably producing accessible, thorough, highly-interoperable knowledge-enabling content across diverse domains which is readily shared and expanded on by others.

We aren’t prescribing a single, specific type of submission. Possible shapes include:

- A spec describing a step-by-step process of a human-AI workflow for producing a structured epistemic analysis of a complex dispute. Demonstrate it on multiple parts of at least two cases. The workflow can incorporate human steering and be subjective in places, but should let others (even with differing beliefs and preferences) usefully pick up where another left off, and should gracefully scale to mostly-or-entirely hands-free. Make clear where design choices are uncertain, and be transparent about tradeoffs and why.
- A prototype tool, most likely a pipeline involving LLMs, that implements one or multiple layers of the stack, demonstrated repeatably on each case study. Minimally, it should substantially accelerate users’ investigation of a topic, and ideally produce reusable, shareable knowledge artifacts that stand up to adversarial pressure.
- A protocol enabling interoperability and compounding without flattening the underlying material, demonstrated with reference to the cases. The protocol should address the tension between interoperability and nuance: how to link diverse subtopics and complex, multi-perspective investigations while preserving important detail, and how to maintain them as sources, users, and AI capabilities change.
- A comparative analysis repeatably applying two or more AI assessment methodologies to the same subquestions, with explicit discussion of where they agree and diverge, what downstream considerations they enable, their strengths and shortcomings, and what supporting epistemic metadata would help them work better.
- A critique with counterexamples of an otherwise promising approach, demonstrating the importance of further work or indicating less tractability than expected.

What we care about most: Would this actually help someone reason better about this case? Does it generalize? Does it scale with improvements to AI or more compute? Does it compound, with multiple people or teams building on each others’ work?

Entries are assessed using the competition’s judging criteria. Submissions are due by 19 July 2026. Strong entries that demonstrate real promise may also lead to an offer for further funded work.

## Why we're doing this

We're building toward what we call a full epistemic stack: layered infrastructure for making the provenance, structure, and assessment of knowledge transparent and traversable at scale. We think recent AI advances make this newly tractable, but the hard problems are in methodology and workflow design, as well as capability, not just capability alone.

Not only do we expect these tools to be of widespread benefit, but we expect some organizations like ours to be eager early adopters. FLF hopes to meaningfully inform its strategy and prioritisation based on insights from these tools, meaning that great work here could move millions of dollars per year and help us (and others) be more effective.

## The case studies

### COVID

In early 2024, a $100,000 judged debate took place between Saar Wilf (founder of Rootclaim) and Peter Miller on the origins of COVID-19. Over 15 hours of structured argument, two smart people marshalled epidemiological data, viral genetics, Bayesian inference, and institutional analysis to reach opposite conclusions. Two expert judges ruled decisively for zoonosis. Six independent Bayesian analyses of the same evidence spanned 23 orders of magnitude.

All this information is still incredibly difficult to navigate, interrogate, and use to inform one’s beliefs. It requires significant background expertise to understand the state of play and make a considered judgement, and the live video debate may not be the optimal way for a judge to interact with the material. This intense epistemic effort also represents a point in time in a conversation which continues to evolve. FLF presents it as a stress test for tools and methods that aim to make reasoning more transparent, traversable, updateable, and trustworthy.

Your job: craft the AI-assisted methodologies that build a structure to help people navigate this topic successfully.

### Black holes

CERN, home of the world’s largest particle accelerator, has a frequently asked question about whether the LHC will generate a black hole. Some participants had apocalyptic concerns about unprecedented outcomes. How were these put to rest? Were they truly? What does this hinge on?

Unlike COVID, this is (we hope!) essentially a closed case, and uncontested. It nevertheless rests on a huge body of accumulated and interacting knowledge which enabled scientists (and the officials and public supporting them) to move forward with confidence.

The key challenge may be probing this argument for its dependencies and key considerations, and perhaps noting the weakest or most speculative points — all in an accessible way.

### Eggs

Are eggs good to eat? Bad to eat? Great in moderation? How can we tell? Does it vary across people, and what predicts this? What else should we be paying attention to here?

This vague and open-ended topic, though mundane, is representative of a huge number of everyday questions — and hopefully also a microcosm of many more impactful debates. Sometimes getting resolution on what are the important things to answer and what are the appropriate ways of knowing is (more than) half of the challenge.

The competition envisions these as eventually becoming living knowledge bases, not merely snapshots in time.
