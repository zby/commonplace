---
source: https://www.answer.ai/posts/2026-08-19-llms-code-simpler.html
description: Pol Alvarez Vecino's Answer.AI billing-system case argues that code-complexity metrics cannot substitute for the tacit program theory needed to judge simplification trade-offs.
captured: 2026-08-20
capture: web-fetch
genre: practitioner-report
type: kb/sources/types/snapshot.md
---

# Why LLMs can’t make your code simpler

Author: Pol Alvarez Vecino
Source: https://www.answer.ai/posts/2026-08-19-llms-code-simpler.html
Date: 2026-08-19

*This post was originally published [on
Medium](https://medium.com/@pol.avec/why-llms-cant-make-your-code-simpler-fc2cd36bc0c8).*

> tl;dr Peter Naur’s “Programming as Theory building” states that the
> real programs, what he calls Theory, with capital T, are in the mind
> of the engineers. The code & documentation are just downstream (and
> thus incomplete) artifacts. One of my main complaints about LLMs is
> how verbose the code is and how complexity creeps in everywhere. I
> always had some faith that we might improve that using metrics like
> LoC or the number of independent code paths to constrain them.
> However, after reading Naur I realized that the complexity we are
> trying to reduce is the Theory one, not the code, and there are no
> relevant measures for that because it’s very subjective.

<figure>
<img src="https://www.answer.ai/posts/2026-08-19-llms-code-simpler_assets/naur.jpeg"
alt="Peter Naur" />
<figcaption aria-hidden="true">Peter Naur</figcaption>
</figure>

I recently read the fantastic paper [“Programming as Theory building” by
Peter Naur](https://pages.cs.wisc.edu/~remzi/Naur.pdf). It has changed
quite substantially my views on what current LLMs can or can’t do, how
to prompt them, what are the main limits to current agentic systems or
why pair programming is so effective.

Today I will focus on its relation to code complexity.

If you haven’t read the paper, I really suggest that you do. In fact, my
main goal in writing this post is to get some of you to read the
original paper. It is worth the effort. It is also the perfect chance to
practice (or learn!) to do close reading in
[Solveit](https://solve.it.com/) because it’s much easier: you can ask
any questions throughout the text, go down any rabbit holes you like, or
just ask Solveit to make the language clearer to you. More information
on close reading in [this
blogpost](https://www.fast.ai/posts/2026-01-21-reading-LLMs/) and you
can quickly get started by [forking my own
dialog](https://share.solveit.pub/d/2ec584e79ecd9aed714c438d43f48f8e).

With that in mind, if you still decide not to read it, here’s the
paper’s tl;dr:

> A program is the Theory held by the people who build and maintain it:
> an understanding of how the program relates to the real-world problem,
> which constraints and trade-offs shaped it, why it works, and which
> changes would fit its design. Code and documentation are downstream
> artifacts of that Theory, and can never capture it completely.
>
> Engineers develop this understanding through experience: talking to
> users, observing failures, learning the domain, and seeing how the
> system behaves in the real world. This understanding guides judgments
> of relevance, similarity, simplicity, and good design.

LLMs aren’t great at continual learning, talking to users, or
experiencing things in the real world. But why is this relevant to
complexity?

I think we can all agree that LLMs in general tend to increase the
complexity of codebases if left unchecked. The reasons are many: they
fail to realize a method already existed and duplicate it, they write
overdefensive code like protecting against edge cases that can’t happen,
or overoptimizing things too early. Tangentially, most frontier labs
make a hefty sum the more tokens you consume, so they are kind of
incentivized to promote tokenmaxxing. All in all, LLMs rarely follow the
KISS principle. This issue is at its worst when vibe-coding w/o checking
the output. But even when you review code, if you want to keep a program
concise it requires an active effort to cut down complexity as much as
possible.

In my naive days (about two weeks ago), I used to think we would get out
of this complexity pit at some point. Frontier labs would just add some
complexity penalization to their RL training. They could use total LoC
as a metric to minimize, but we can all agree that sometimes a one-liner
can be more complex than 2–3 lines. Another option would be cyclomatic
complexity which measures the total number of independent code paths.
After reading Peter Naur I realized that those things can’t really solve
the problem (maybe they can alleviate it a bit though). Let’s see why.

## Why Code Complexity is the wrong metric

In the (invented) example below we want to support calling OpenAI &
Anthropic. Imagine all the message preparation and retries are handled
identically, but the request body params are slightly different so we
have 2 different methods `call_openai` and `call_anthropic`.

In the first naive version we have 2 different classes with duplicated
boilerplate code (ie `prepare` and `with_retries`).

``` python
# Separate — duplication a metric would flag

class OpenAIClient:
    def complete(self, prompt):
        msgs = prepare(prompt)         # shared boilerplate
        y = call_openai(msgs)          # the only line that differs
        return with_retries(y)         # shared boilerplate

class AnthropicClient:
    def complete(self, prompt):
        msgs = prepare(prompt)
        y = call_anthropic(msgs)
        return with_retries(y)
```

A straightforward refactor would be to create a single class so we DRY.
By many metrics this is a better implementation: it has fewer lines of
code, better Halstead volume — calculated as V=N×log2(n) for program
length (N) and vocabulary (n) — and better [Maintainability
Index](https://radon.readthedocs.io/en/latest/intro.html#maintainability-index).

``` python
# Merged — genuinely better by the metrics: DRY, fewer lines

class LLMClient:
    def __init__(self, provider): self.provider = provider
    def complete(self, prompt):
        msgs = prepare(prompt)
        y = call_openai(msgs) if self.provider == "openai" else call_anthropic(msgs)
        return with_retries(y)
```

In general, the second version (or similar versions that reduce LoC and
duplication) are less complex. However, what if I told you that it is
very likely that next month we will stop supporting Anthropic. In that
situation I find it preferable to keep them separated so when the time
comes I can simply remove the file containing the `AnthropicClient`.

Of course a simple example like this is easy to solve, especially now
that LLMs can code for you. But what if instead of 2 providers you want
to support 165+ providers like LiteLLM does? Well in that case just use
LiteLLM. But then you will be putting over +1.2M python LoC between you
and the final provider. Is it worth it?

Well-designed APIs are a great way to abstract complexity. You have a
clear contract and you don’t need to understand what happens behind.
Even if the LiteLLM is a huge package, it might not count towards your
total Theory complexity. The early days of LLM inference endpoints were
like this: “you send text in, you get text out”. However, this breaks
down when the contract is not reliable anymore. This can happen because
it’s buggy, or because there’s a lot of state hidden behind the API which
you can’t get, or simply because you’re not sure if a new provider
feature is supported.

Whenever you are forced to peer into the abyss beyond the API
abstraction layer, that complexity becomes your problem. This problem is
becoming more common. Providers like OpenAI and Anthropic increasingly
hide data server-side like encrypted compaction data or reasoning tokens
([more on this](https://earendil.com/posts/session-portability/)).
Anyone aiming to offer an abstraction layer on top of them is forced to
either expose provider-specific details, reimplement increasingly
brittle compatibility logic, or accept that the abstraction cannot
faithfully represent the systems beneath it.

![](https://www.answer.ai/posts/2026-08-19-llms-code-simpler_assets/api-abstraction.png)

If you are moving fast, using basic features and want to try many
providers then LiteLLM or similar libs might be worth it for you. If on
the other hand you value control, debugging and in understanding your
stack, then probably not. There’s no right “complexity” (although I very
much prefer the second option).

## Enter the Theory

The information to decide which path to take does not live in the code.
This information is part of what Naur calls the *Theory* of the program.
LLMs so far have little to no access to this information because it
lives in people’s minds. They can get hints about it in IM, email, or
other kind of written docs but all of those will always be partial (best
case).

Some of this information can be supplied to an LLM as context like
business priorities, expected product changes, operational constraints,
and the reasons behind earlier decisions. Doing so might improve its
choices, but these are still artifacts of the Theory. They cannot
completely transfer the experience and judgment through which the team
developed that Theory.

![](https://www.answer.ai/posts/2026-08-19-llms-code-simpler_assets/theory.png)

This is all good, but what if I am all-in with vibe-coding &
tokenmaxxing, what if I don’t care at all about the code. Well in that
situation the rest of the blog post won’t convince you otherwise. If on
the other hand you’re in-between I will describe a real situation we
went through at Answer.AI with our billing system for Solveit.

Spoiler alert, at Answer.AI we are heavily invested in minimizing
complexity at all costs. This investment actually tends to result in
simpler code that is easier to hold in your mind.

## The initial billing system

[Solveit](https://solve.it.com) is a platform where you can use AI to
work in a notebook-like environment. The environment is persistent so we
charge for LLM usage, cpu, disk, memory and bandwidth.

The initial plan was to charge users a monthly subscription fee
(e.g. $5). This monthly subscription amount would then become credits to
be consumed during the month, if you consume them all then you’d have to
top up your balance before next month. We tested this approach in a
smaller scale project first to validate it.

This approach turned out to be more complex than we wanted. First, the
credit + subscription mechanism would make some people (like myself)
confused. Second, it made the code more complex at multiple levels. You
have to deal with all the logic of consuming “monthly subscription
credits” first, and then normal credits or what to do with leftover
credits. On the Stripe side of things it had 2 distinct code paths:
manual top up and the subscription service.

For those of you not familiar with it, Stripe subscriptions is a fully
managed service. Stripe manages the lifecycle (recurrence, invoicing,
retries all happen on their side).

You just create the subscription roughly like:

``` python
stripe.Subscription.create(customer=cust_id, items=[{"price": "price_5usd_monthly"}])
```

and listen to their webhooks to update your DB when subscription status
changes or when payments arrive (or many other options you can decide
on).

The direct charge requires you to start a checkout session so users land
in Stripe’s domain and fill in their card. It requires you to provide a
customer ID. Where should you create the stripe customer? when your user
signs up? when they try to pay, something else? all are valid options.

``` python
stripe.checkout.Session.create(mode="payment", customer=cust_id,
    line_items=[{"price": "price_5usd", "quantity": 1}],
    success_url="https://yoursite.com/done")
```

Good so far? If you don’t have a lot of experience with Stripe or
payments, chances are you will be already struggling to hold it all in
your head. Maybe you have managed to simplify it into your mind like:

- Subscriptions -> managed by stripe subscriptions
- Top up -> stripe checkout

A problem that is not obvious is that using Stripe managed service means
that you have duplicated data. Half of the data lives in Stripe’s
backend and you have to make sure your local DB is synchronized with it.
Another problem is that while debugging, you have to both query Stripe
services AND check your own DB. For example, if a payment does not show
up is it because Stripe did not send the webhook (“their fault”), or
because we failed to store it in our DB (“our fault”)?

Stripe subscription service is great and easy to set up, but it is
designed to support a huge number of use cases. That means that, even if
well designed (which it certainly is), the API abstraction ends up being
quite complex. In this case you are trading the complexity of rolling up
your sleeves and writing that code yourself, for the complexity of
learning the Stripe API.

LiteLLM and Stripe illustrate the same trade-off at different scales: an
external abstraction can greatly simplify your Theory while its contract
holds, but its hidden complexity becomes yours whenever you must debug,
modify, or reason beyond that contract.

![](https://www.answer.ai/posts/2026-08-19-llms-code-simpler_assets/tradeoff.png)

## The AAI way

At [Answer.AI](https://www.answer.ai/) we try to own all the stack. The
reason why merits a full article (or multiple ones) so I won’t delve
into it. So we were not pleased with the state of affairs discussed
above.

After many days of exploration and discussion we settled on a much
simpler system.

First of all, we would do credits only and charge based on usage. This
is a super simple model (and Theory!): you pay for what you use by adding
credits.

Once subscriptions were out of the way, we could remove a big chunk of
code related to keeping them in sync. Only 2 payment paths remained,
manual top up and auto topup. To do auto topup you need to be able to
save the customer CC so you can charge it at will. In the case of Stripe
checkouts, you don’t save the CC, you just ask Stripe to process the
payment in their UI.

Long story short, we eventually figured out that the simplest way would
be to save users’ credit card as soon as they sign up. Once they have a
card on file, they can either use it to manually top up their account, or
they can set it to auto topup. Because we handle it all manually the
sync problems are almost nil. We only listen to payment success events
(no subscriptions!).

The result is that the Theory of our payment system can be summarized in
a single sentence:

> Customers add their CC when they sign up and then we charge that card
> either manually (topup) or automatically when the credit goes low

Both manual and automatic top up now use the same payment path. Our
entire payment stack — split between Solveit & faststripe — is roughly
300 lines of code.

The result is very low complexity but it was the result of multiple
hours of exploration, attempts, and discussions. My explanations here
scratch the surface at best.

## Enter India

So what happened on launch day? Did everything go smoothly? No. After
launching we realized that Indian cards do not support charging a card
*off-session* whenever you choose. The manual top up, which is
on-session, would still work because they would be shown a 3DS-like
approval flow in our UI but not the automatic top up.

When exploring for solutions, we discovered that Stripe managed
subscriptions actually work in India. Why? Well Stripe works around all
that complexity for you. They create & hold the off-session payment
intent the day before, so the banks can send a pre-debit notification or
authentication request to the users before the actual charge.

When migrating away from managed subscriptions we lost that feature. I
asked a frontier LLM — I think it was GPT 5.5 — how could we handle this.
Do you care to guess at the proposed solution?

> Use Stripe subscriptions to handle it

The LLM was proposing to use again the solution we just migrated away
from. If you have read this far, what would you say, what’s your opinion?
Should we migrate back?

The LLM outlined two options, either to support both systems (ready to
code, just say the word!) or to fully migrate back into the old one.
What did we do? Nothing. We greatly value the Theory complexity so we
decided that requiring Indian users to manually top up was ok (sorry
guys!) in exchange for a simpler and more robust platform.

If you don’t agree with our choice, reflect on why not. Like, seriously,
stop right now and think about it.

There is no right answer and one of the points of this post is to help
you realize where **your answer** comes from. What are your arguments
and, more specifically, where do they come from?

There are many situations where Stripe managed services are a superior
choice. Here are some examples:

- Company revenue is the most important, so the extra friction of manual
  top up might make us lose some India sales, we should migrate back (or
  support both)
- The sales team uses the Stripe Dashboard UI, having all the payment
  system information in our DB is not ideal because they can’t manage
  it.

My point is that the complexity of your code really depends on a lot of
factors that have NOTHING to do with code and that information is NOT in
the code.

## The hidden advantage

So why not let LLMs fully manage these things for you? The beautiful
answer in my opinion is that our way of working uncovered a possible
business opportunity. India does not support debit mandates in the same
way the rest of the world does. Stripe tries to solve this, but it is far
from a complete solution.

In the process of understanding and simplifying the process and the
Theory we learned something valuable beyond the product we built. These,
in my opinion, are the kind of insights that can turn into competitive
advantages.

Striving to understand is essentially a process of
Theory-simplification. If you let your LLM free rein in complexity you
can churn out a lot of code quickly. Choosing the simplification route
is longer and takes more effort, but in the long run I think it pays
off, and you might find hidden gems along the way.
