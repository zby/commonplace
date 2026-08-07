---
source: https://www.erichgrunewald.com/posts/why-i-think-you-should-almost-never-use-ai-to-write-anything-substantive/
description: Erich Grunewald's argument that delegating substantive prose to current AI models bypasses thinking-through-writing, hides subtle errors, and breaks the reader-writer trust contract.
captured: 2026-08-06
capture: web-fetch
genre: conceptual-essay
type: kb/sources/types/snapshot.md
---

# Why You Should Almost Never Use AI to Write Anything Substantive

Author: Erich Grunewald
Source: https://www.erichgrunewald.com/posts/why-i-think-you-should-almost-never-use-ai-to-write-anything-substantive/
Date: 2026-08-06

2026-08-06 • 12 min read • comment via [LW](https://www.lesswrong.com/posts/kjQdL3dxaACSbjkSx/why-you-should-almost-never-use-ai-to-write-anything-1), [EAF](https://forum.effectivealtruism.org/posts/stmA3cmXY8jaZahtg/why-you-should-almost-never-use-ai-to-write-anything), [Substack](https://erichgrunewald.substack.com/p/why-you-should-almost-never-use-ai)

![img](https://www.erichgrunewald.com/img/hero/writing.png)

I think you should almost never use AI to write – that is, to do the thing you’re doing when you type words on a page – whether for a blog post, a research report, a memo, a thoughtful email, a novel, or any other text aimed at conveying an idea, an argument, an analysis, or other substantive[[1]](https://www.erichgrunewald.com/posts/why-i-think-you-should-almost-never-use-ai-to-write-anything-substantive/#fn1) thoughts. I think this is the case even when you give the AI very detailed bullet points, dictated thoughts, or other context, and even when you edit the AI-written text.[[2]](https://www.erichgrunewald.com/posts/why-i-think-you-should-almost-never-use-ai-to-write-anything-substantive/#fn2)

I think so because (1) the writing process is an essential part of the thinking process, (2) AI writing is vague and wrong in hard-to-notice ways, and (3) writing with AI (and not labeling it as such) is rude and misleading. I’ll explain these points in more detail below, but first, a few throat clearings.

As you may know, I’m not anti-AI. I think it makes a lot of sense to use AI for many other parts of the research and writing processes, such as transcribing audio, analyzing data, searching for information, brainstorming, and giving feedback on drafts. I also think using AI for line and copy editing, or for rewriting a passage to make it clearer or tighter, is fine, as long as all the edits are deliberately accepted or rejected by a human. It’s just using AI to write text that I’m against.[[3]](https://www.erichgrunewald.com/posts/why-i-think-you-should-almost-never-use-ai-to-write-anything-substantive/#fn3)

And yes, there are various advantages to using AI for writing. For example, it’s less effortful and much faster than writing yourself. So the disadvantages of using AI for writing need to be substantial for it to be bad overall. As you may have guessed by now, I think they are.

And finally, I’m just making a claim about the AI models that exist now and that I expect to exist in the near future. There will likely exist models at some point that are good enough that it makes sense to delegate the writing to them (although at that point it might make more sense to delegate the entire research or writing process end-to-end, since in addition to the writing they will also need to be doing all or most of the thinking).

## The Writing Process Is the Thinking Process

The point of doing any kind of research is to form accurate beliefs about important questions, which you can then communicate to an audience. One of the best ways of doing that is in my opinion [by writing](https://www.cold-takes.com/learning-by-writing/).

Paul Graham [has written](https://paulgraham.com/words.html)[[4]](https://www.erichgrunewald.com/posts/why-i-think-you-should-almost-never-use-ai-to-write-anything-substantive/#fn4) that

> Writing about something, even something you know well, usually shows you that you didn’t know it as well as you thought. Putting ideas into words is a severe test. […] Half the ideas that end up in an essay will be ones you thought of while you were writing it. Indeed, that’s why I write them.

On an [episode](https://www.complexsystemspodcast.com/episodes/llms-and-writers-with-clara-collier-of-asterisk-magazine/) of Patrick McKenzie’s podcast, Clara Collier says that

> When I am writing something, something substantive, there’s no part of that writing process in which I am not thinking and changing my mind. Everything from the outline to turning it into text to just the sentence. Often I’ll have an experience where I’m trying to turn an outline into a finished product, and I’m playing with a transition, and it’s not working, and I realize, oh, the reason this transition isn’t working is because actually these two points should not be juxtaposed. The thing that I’m trying to do here is wrong. And if I feed the outline into an LLM, it is not going to stop and consider maybe the outline is bad. […]

Patrick replies:

> I absolutely agree that the writing process is the thinking process, and I think we now have empirical demonstration of this, because you make a machine that does writing and thinking just *pops out* as a side effect.

> But when writing a multi-page piece, even if you have a strong thesis, the act of forcing yourself to write that down into sentences and paragraphs to structure the argument will show you where the holes are in the argument. It will show you where your research process has been inadequate. It will surface things like: oh, actually, there is something that is contradictory to the thing that I want to say. And, being a reasonably ethical person, I think I will acknowledge that there are counterarguments, or have to add that the full claimable conclusion is less than the one that I would, quote-unquote, “like to write”.

I basically agree with these takes. When I write something, I must first know what I want to say, i.e., I must think about evidence and arguments and arrive at some beliefs. So writing forces me to do those things, which are necessary for any writing or research project. For any such project, someone has to have the entire thing in their head – all the bits of evidence, considerations, arguments, and how these fit together. Writing with AI makes it easier to avoid the necessary thinking.

## AI Writing Is Vague and Wrong in Hard-to-Notice Ways

When I write something, I make a lot of small decisions about specific wording and phrasing. Together, these small decisions contribute to the overall clarity and correctness of the text.

For example, if I ask Claude Fable 5 to “write a short paragraph introducing the problem of AI chip smuggling”, a topic that’s been [written about](https://www.the-substrate.net/p/how-banned-ai-chips-end-up-in-china) and reported on extensively, it outputs:

> Since October 2022, the United States has restricted exports of advanced AI chips to China, aiming to slow Chinese progress at the frontier of AI. But export controls are only as strong as their enforcement, and AI chips are compact, extraordinarily valuable, and sold through sprawling global supply chains — properties that make them attractive and feasible to smuggle. Diversion networks route controlled GPUs through intermediaries in places like Singapore, Malaysia, and the UAE, using shell companies and falsified paperwork to move them into China. Estimates of the scale vary widely, from tens of thousands to perhaps more than a hundred thousand high-end chips per year, and even the lower end represents enough compute to matter for training and deploying capable AI systems. Meanwhile, the Bureau of Industry and Security, tasked with policing a multi-hundred-billion-dollar trade, operates with a budget and headcount better suited to a far smaller problem. Chip smuggling thus threatens to quietly hollow out one of the central pillars of US AI policy.

That’s not terrible, and perhaps even quite reasonable, but is that how I would write it? No, in fact, Claude made a lot of choices that I find subtly wrong or bad:

- Claude writes that “export controls are only as strong as enforcement”, but what does this mean? It either says something obvious (of course policies that are not enforced or poorly enforced are less effective) or nothing at all.[[5]](https://www.erichgrunewald.com/posts/why-i-think-you-should-almost-never-use-ai-to-write-anything-substantive/#fn5)

- Claude writes that AI chips are “compact”, which is true, but what is usually smuggled are AI servers, which are not compact. Anyway, more importantly, this doesn’t matter, because AI chip smuggling rarely involves hiding products to get through customs; usually the products are just relabeled as some other kind of good and shipped in plain sight, so to speak.

- Claude writes that being “sold through sprawling global supply chains” makes AI chips “attractive and feasible to smuggle”. What does this mean? Is it that smugglers can more easily buy chips from companies outside the US? (Until recently, smugglers seem to have been able to procure AI chips from US-headquartered companies with relatively little difficulty.) Is it that it makes smugglers buying a lot of AI chips in countries such as Malaysia less conspicuous? (This is closer to being true, I think.) Or is it something else?

- Claude writes that estimates of the scale of smuggling “vary widely, from tens of thousands to perhaps more than a hundred thousand high-end chips per year”. This is literally true, but the low estimates are almost certainly wrong, and the true number is probably much closer to the higher end mentioned by Claude, i.e., hundreds of thousands.[[6]](https://www.erichgrunewald.com/posts/why-i-think-you-should-almost-never-use-ai-to-write-anything-substantive/#fn6) So this is misleading. Also, Claude doesn’t specify a year, but smuggling volumes have fluctuated widely since October 2022, nor does Claude specify what a “high-end” chip is (it sounds like a luxury good handcrafted and sold exclusively to Saudi royals and dowager duchesses).

- Claude writes that “even the lower end represents enough compute to matter for training and deploying capable AI systems”. This phrase has no informational value. In some sense, a single AI chip “matters” for training and deploying AI systems, capable or not. (And what’s a “capable AI system”, anyway? Why does a small amount of compute matter more for a *capable* AI system than for an incompetent AI system? If anything, you might think the reverse would be true, that the weaker AI system would benefit more from a small amount of compute.)

- Claude writes that the Bureau of Industry and Security (BIS) is “tasked with policing a multi-hundred-billion-dollar trade”. Here, it would be much better to just mention [the number](https://epoch.ai/data/ai-chip-sales).

- Claude writes that BIS “operates with a budget and headcount better suited to a far smaller problem”. First, we know BIS’s [budget and headcount](https://www.the-substrate.net/p/bis-is-getting-more-fundingheres), so it would be better to mention those numbers and contextualize them. Second, what does it mean for a problem to be “smaller”? Does it mean that it is less important, or that it requires less effort to solve, or something else? Isn’t the important thing that more resources for BIS would likely improve enforcement substantially, not that the amount of resources BIS currently has is better suited to some other problem?

- Claude’s final sentence, that AI chip smuggling “thus threatens to quietly hollow out one of the central pillars of US AI policy”, is pure uninformative [applause light](https://www.lesswrong.com/posts/dLbkrPu5STNCBLRjr/applause-lights).

One or two issues like that in a text may not matter much, but AI writing is in my experience very dense with unnecessarily vague and subtly wrong phrases. Note that this problem also exists when you give the AI a lot of context such as written notes and outlines.[[7]](https://www.erichgrunewald.com/posts/why-i-think-you-should-almost-never-use-ai-to-write-anything-substantive/#fn7)

Similarly, Eric Schwitzgebel [writes](https://eschwitz.substack.com/p/ai-slop-and-evidence-about-evidence) that

> Human experts think *differently* and *better* than LLMs. Their word choices, even subtle ones, reflect sensitivities that they might not themselves be aware of. Typically, an expert’s prose will be more sensitive to the matters on which they are expert than the output of a language model. […]

> You might object as follows: Of course I read the LLM outputs before sending, and I wouldn’t send the email, much less submit the article, unless I endorsed every word! So, the objection continues, you *did* think the thoughts expressed. The text reflects your expert best judgment – maybe even something better than your expert best judgment: your expert best judgment combined with the expertise of an LLM.

> I reply: There’s a huge cognitive difference between nodding along while reading something and *actually productively generating* a text. Two reasons: First, once the text is on the page, it’s easy to passively let the approximate word suffice, rather than thinking about word choice in the same effortful, active way we do when generating prose de novo. Second, as I suggested above, I doubt that human beings, even experts, have a good sense of all the factors that shape word choice – everything they’re being sensitive to. You would have phrased it slightly differently, and even if you don’t know that, or why, a different signal is sent and received.

I agree with this. But it’s actually much worse than that! Not only do AIs write text that is unnecessarily vague and subtly wrong, but they do so in a way that is almost maximally convincing! If an AI doesn’t positively “know” a thing you ask it to write about, it usually won’t stop and tell you it doesn’t know; instead it will write something that’s vague and meaningless enough to be true or something that sounds true but isn’t, or isn’t necessarily. Humans are of course often wrong and vague, but I think we tend to be wrong and vague in ways that are less convincing and easier to notice.

It takes a lot of effort to read AI-written text and spot all the little issues the way I did earlier with the AI chip smuggling text. If I didn’t know a lot about AI chip smuggling, I probably wouldn’t have spotted most of the issues I listed, unless I had thought very hard about the text. But if I had instead written the text myself, I could not have avoided noticing where I was confused.

## Writing with AI (and Not Labeling It as Such) Is Rude and Misleading

Sometimes when I write a text, I write it intending for other people to read it. For example, I may want to publish it online, or share it with colleagues for feedback, or send it as an email, or send it to a publisher. When I publish or share a text, the person who reads it probably expects that I put some thought into what I wrote, and in particular that the text represents *my* thoughts. Or at least they should expect that, and I want them to. That’s the implicit contract between reader and writer, that the reader offers their attention and the writer repays that with something of value, like information or entertainment.

On the same [episode](https://www.complexsystemspodcast.com/episodes/llms-and-writers-with-clara-collier-of-asterisk-magazine/) of Patrick McKenzie’s podcast, Clara Collier also says that

> Maybe I’m being precious here, but the version of my writing that an LLM could produce is always going to be missing something that I could add. Which, again, is not because – there are many areas where the models know more than me. But anybody can ask Claude about anything whenever they want.

> If they’re reading something that I wrote, or that as an editor I chose to put in front of them, it’s because there’s an implicit contract. I am offering them something that they couldn’t get somewhere else. This is going to be a better use of their time than just asking the model directly. And that’s why I wouldn’t use directly LLM-generated text – or if I did, I would want to be very clear about what you’re getting into before you’ve spent time on it.

All the stuff I wrote about above, about subtle errors and vagueness, and all the stuff about how, when a text is AI-written, you have no idea whether the author put a lot of thought into it – all these things violate that contract. So when I read a text and notice that it is fully or partly AI-written, my trust in the text and in the author is immediately, and I think rationally, lowered.

And for all those reasons, when you promote AI-written text, or send a draft of AI-written text to someone, I think you are being rude. I think it’s sort of like sending a really sloppily written draft to someone and hiding the fact that it’s really sloppily written. And unless you label the AI-written outputs clearly, you are misleading the reader who will expect your text to be *your* text, carefully thought through and representing *your* beliefs specifically.

Of course you can get around the issues of being rude and misleading by labeling the text as AI-written, or substantively AI-written. I suspect that’s not something most people want to do, though.

## Aren’t There Exceptions?

Question: Can’t I include AI-written outputs in a text *if I clearly label them as such*? Answer: Yes, that seems mostly fine to me. For example, sometimes I might do a shallow investigation into something and rely on Claude for a piece of information, and then I might write something like, “Claude Fable 5 tells me that so-and-so is the case.”[[8]](https://www.erichgrunewald.com/posts/why-i-think-you-should-almost-never-use-ai-to-write-anything-substantive/#fn8) This can be useful when it doesn’t make sense to spend a lot of time vetting that particular claim. The important thing is that the output is clearly marked as AI-written, so the reader can discount it (or not) as they see fit.

Question: Then I can just do this for the entire text, can I not? Answer: I think it’s almost never a good idea to use AI to write an *entire* substantive text, even if it is labeled as such, at least if you intend anyone else to read it. That’s because I think one, the result will likely be much worse than had you written it yourself, and two, people will (rightly) not read your text if you label it as AI-written. I think it’s probably also often a mistake to write texts with AI even if the only person who will read them is yourself, since by doing that you lose out on the benefits outlined in the first two sections above.

Question: Can I, a non-native English speaker who struggles to write in English, use AI to write in English? Answer: It is sometimes suggested that this is acceptable, including doing so without disclosure. I disagree for all the reasons mentioned above. I think it can be acceptable to [use AI to translate](https://www.lesswrong.com/posts/s58hDHX2GkFDbpGKD/linch-s-shortform?commentId=aeWcFXjfgATnDoajE) a text written in one’s native language, but even then I think it’s better to disclose that. Overall, my sense is that AIs are better at retaining clarity and precision when translating than when, say, drafting from bullet-point notes.

Question: What if the stakes are very high and it’s just very important and valuable to use AI to accelerate necessary writing, say for example, to write policy memos related to AI? Answer: I don’t think using AI to write actually speeds me up much? Or, I think in practice the way that it would speed things up is by compromising on quality, and I don’t think you should on the margin compromise on quality. For example, DC is already drowning in reports and issue briefs that approximately nobody reads; what’s scarce, and what really helps policymakers, are more-accurate and more-thoughtful analyses on important topics.

## Footnotes

1. I think it can be fine in some circumstances to use AI to write short texts that serve mainly a coordinating or logistics function. For example, if in your corporate job you need to repeatedly write short, very formulaic emails, that seems okay to draft with AI and lightly edit before sending. [↩︎](https://www.erichgrunewald.com/posts/why-i-think-you-should-almost-never-use-ai-to-write-anything-substantive/#fnref1)

2. There may be one or two exceptions here. For example, if you extremely closely vet and heavily edit the AI-written text yourself, that *might* be fine. But it might not, and anyway doing that doesn’t seem much easier or quicker than writing it yourself from scratch. I think in practice the way writing like this would speed the process up is by compromising on quality. [↩︎](https://www.erichgrunewald.com/posts/why-i-think-you-should-almost-never-use-ai-to-write-anything-substantive/#fnref2)

3. Is it contradictory that I endorse using AI for brainstorming and analysis, both of which also involve effortful thinking? I’m not sure, but I think using AI for these things is probably fine so long as you also put your beliefs through the gauntlet of writing them down in words. [↩︎](https://www.erichgrunewald.com/posts/why-i-think-you-should-almost-never-use-ai-to-write-anything-substantive/#fnref3)

4. He later revisited this argument in [a post about AI specifically](https://www.paulgraham.com/writes.html). [↩︎](https://www.erichgrunewald.com/posts/why-i-think-you-should-almost-never-use-ai-to-write-anything-substantive/#fnref4)

5. There are some other ways of interpreting this phrase, though I think they’re wrong. For example, you could take “export controls are only as strong as enforcement” to mean that, if we could somehow quantify how good an overall export control regime is, and quantify how good its enforcement is, there’s a point past which the regime just cannot get any better unless enforcement does. But I don’t think that’s true, because there are probably always other ways of improving the export regime, for example, by adjusting export policy. [↩︎](https://www.erichgrunewald.com/posts/why-i-think-you-should-almost-never-use-ai-to-write-anything-substantive/#fnref5)

6. All right, this is partly my fault for underestimating the scale of future AI chip smuggling [back in October 2023](https://www.iaps.ai/research/ai-chip-smuggling-into-china), which might have gotten into Fable’s training data. I think I got a lot of things right in that report, including the mechanistic description of AI chip smuggling and my policy recommendations, but the forecast of the scale of the problem was off by an order of magnitude, probably. Remember that, at the time, all we had to go on was [one measly Reuters story](https://www.reuters.com/technology/inside-chinas-underground-market-high-end-nvidia-ai-chips-2023-06-19/) on small-scale Shenzhen black market activity. [↩︎](https://www.erichgrunewald.com/posts/why-i-think-you-should-almost-never-use-ai-to-write-anything-substantive/#fnref6)

7. For example, I sometimes use Claude to summarize meeting notes for sharing with colleagues. Even when I use a carefully written prompt that includes several examples of meeting takeaways I’d written myself and Claude has access to the full meeting transcript, it still introduces subtle vagueness and errors. (Quite a lot of these errors are by the way seemingly the result of Claude not quite understanding who the takeaways are for and what they can be expected to know and not know, despite my trying to provide that context.) [↩︎](https://www.erichgrunewald.com/posts/why-i-think-you-should-almost-never-use-ai-to-write-anything-substantive/#fnref7)

8. For bonus points, it also seems good to mention which specific model produced the output. [↩︎](https://www.erichgrunewald.com/posts/why-i-think-you-should-almost-never-use-ai-to-write-anything-substantive/#fnref8)
