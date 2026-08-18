---
source: https://news.ycombinator.com/item?id=49336573
description: "Hacker News discussion of AI-generated prose as a costly-to-read signal of missing judgment, editing, and accountability"
captured: 2026-08-18
capture: web-fetch
genre: conversation-thread
type: kb/sources/types/snapshot.md
---

# AI;DR (AI; Didn't Read) — Hacker News discussion

Author: Hacker News participants (submission by mooreds)
Source: https://news.ycombinator.com/item?id=49336573
Date: 2026-08-17

Original submission: [AI;DR (AI; Didn't Read)](https://www.rickmanelius.com/p/aidr-ai-didnt-read)
Snapshot metadata: 938 points; 572 comments shown by Hacker News at capture time.

## Discussion

- **LPisGood** ([comment](https://news.ycombinator.com/item?id=49336573#49337050), 2026-08-17 20:21:29 UTC)
  My coworkers continue to dump hundreds of lines of AI documentation in every PR and every other line of code has between one and ten lines of AI generated comments, talking about the real unlock and how things are byte for byte identical on the load bearing path or how the acceptance ladder is misleading.

  Features are coming out and metrics are improving, but we’re basically in a post readability code base, with the occasional performative comment about a variable name.

  I don’t really know how to address this situation or if it needs addressed. I certainly don’t read the long-winded AI comments or the AI documentation, but perhaps it’s useful for the AI on its next pass.

  - **aaaronic** ([comment](https://news.ycombinator.com/item?id=49336573#49338341), 2026-08-17 22:08:00 UTC)
    My "favorite" Claudism is when I critique its work and ask it to remove some unnecessary part of the design -- and then the diff has more green than red because it added comments about why the code is no longer there -- the code that was never in the mainline and never asked for!

    - **roarcher** ([comment](https://news.ycombinator.com/item?id=49336573#49340650), 2026-08-18 02:51:39 UTC)
      Oh god this has been driving me nuts since Opus 5 landed. Every docblock is filled with long-winded jargon explaining why this design is superior to some other design, which never existed as far as any dev who might read that comment is concerned.

      - **tehlike** ([comment](https://news.ycombinator.com/item?id=49336573#49341248), 2026-08-18 04:27:02 UTC)
        This has been a thing for long while, on codex too.

        You ask it to do something, then tell it to do something in a different way, then it assumes it needs to do the refactor in a backward compatible way, or creates migrations for it etc.

        - **geysersam** ([comment](https://news.ycombinator.com/item?id=49336573#49341912), 2026-08-18 06:09:25 UTC)
          Omg the "backwards compatible fix" in a one-off script, I feel my ptsd coming on ...

        - **theshrike79** ([comment](https://news.ycombinator.com/item?id=49336573#49343591), 2026-08-18 10:17:56 UTC)
          This is why I started adding a PROJECT.md file to all my projects and a hook for claude to read it.

          It contains (Among other things) stuff like "this is a single user personal project, I'm the only user, this will never be open to the public internet" etc.

          It kinda-sorta tones down the proclivity to worry about backwards compatibility and slight edge cases where if someone has edited some template and the new code doesn't support it.

        - **stelonix** ([comment](https://news.ycombinator.com/item?id=49336573#49343222), 2026-08-18 09:09:54 UTC)
          Oh good I thought I was doing something wrong! Using ChatGPT web for planning, ask for a prompt then notice something weird in the prompt and whether I:

          1) use the edit in-place functionality; or

          2) ask it to rewrite to remove something

          It'll write the prompt as if the agent (codex) knew about the conversation and add "don't do X" etc. At first that bothered but I realized it doesn't really change the output so I stopped caring.

          Still, no experience is unique I guess.

        - **Uptrenda** ([comment](https://news.ycombinator.com/item?id=49336573#49343774), 2026-08-18 10:46:55 UTC)
          I remember when I was updating some formats for my apps data files and it ended up writing v2 and laying it on top of the old one. Ended up just telling it to delete the entire feature and start again. I do think claude.md instructions help though.

      - **foolserrandboy** ([comment](https://news.ycombinator.com/item?id=49336573#49340926), 2026-08-18 03:33:16 UTC)
        Oh no, you said "landed"! It's dug into our brains!

        - **doix** ([comment](https://news.ycombinator.com/item?id=49336573#49341936), 2026-08-18 06:12:43 UTC)
          I hate that I have to change the way I write to avoid AI-isms. I loved using "load bearing" to describe weird code that you think you can delete but is actually holding everything together.

          Now people think I'm just parroting what Claude said. It sucks. I want my catch phrases back, I guess this is how em dash users felt

          - **roarcher** ([comment](https://news.ycombinator.com/item?id=49336573#49342159), 2026-08-18 06:42:53 UTC)
            As a former em-dash enjoyer, I indeed feel your pain.

            - **algoth1** ([comment](https://news.ycombinator.com/item?id=49336573#49343391), 2026-08-18 09:41:45 UTC)
              Same here for em-dashes

            - **filterfish** ([comment](https://news.ycombinator.com/item?id=49336573#49342598), 2026-08-18 07:35:13 UTC)
              I'm with you an that one. RIP em-dash.

          - **account42** ([comment](https://news.ycombinator.com/item?id=49336573#49342783), 2026-08-18 08:00:37 UTC)
            I feel like a lot of these have been LinkedIn-isms or PR-isms long before they have been AI-isms so not much is lost.

            - **roarcher** ([comment](https://news.ycombinator.com/item?id=49336573#49343158), 2026-08-18 09:01:06 UTC)
              I used to use em-dashes for explanatory clauses--like this one, for example--when using commas would make the sentence difficult to parse due to other nearby commas.

              They're only a LinkedIn-ism when used to create an unduly dramatic juxtaposition for an otherwise mundane idea. But now they set off people's AI radar when used for any reason at all.

              - **account42** ([comment](https://news.ycombinator.com/item?id=49336573#49343435), 2026-08-18 09:49:22 UTC)
                Perhaps I am biased because I find the use of em-dashes without spaces (as is common in English typesetting) to be inherently ugly so I'm not too unhappy to see their use discouraged.

        - **dag11** ([comment](https://news.ycombinator.com/item?id=49336573#49341136), 2026-08-18 04:08:13 UTC)
          You could say it landed cleanly.

          - **hexasquid** ([comment](https://news.ycombinator.com/item?id=49336573#49341295), 2026-08-18 04:34:19 UTC)
            Good instinct. Fair challenge. This corrects my framing. It makes your point sharp. This is a significant finding. Positively confirmed. That settles it, and it flips the picture. Honest verdict - this is not small. Let me wire it in.

            - **roarcher** ([comment](https://news.ycombinator.com/item?id=49336573#49341818), 2026-08-18 05:57:09 UTC)
              There's got to be a Weird Al song like this coming soon.

              - **Yizahi** ([comment](https://news.ycombinator.com/item?id=49336573#49343546), 2026-08-18 10:11:14 UTC)
                Behold, The Masterpiece :)

                [https://news.ycombinator.com/item?id=49251221](https://news.ycombinator.com/item?id=49251221)

              - **bkaae** ([comment](https://news.ycombinator.com/item?id=49336573#49342396), 2026-08-18 07:12:33 UTC)
                Bless the lord that it's not been presented to us yet, because you just know that it exists already.

        - **roarcher** ([comment](https://news.ycombinator.com/item?id=49336573#49340943), 2026-08-18 03:34:42 UTC)
          Oh. Oh no.

      - **masto** ([comment](https://news.ycombinator.com/item?id=49336573#49343410), 2026-08-18 09:45:05 UTC)
        There needs to be a pithy name for this. I have been calling it context leak.

        - **chester_r** ([comment](https://news.ycombinator.com/item?id=49336573#49343740), 2026-08-18 10:42:23 UTC)
          I like ‘accretive editing’: [https://justindfuller.com/programming/accretive-editing](https://justindfuller.com/programming/accretive-editing)

    - **koyote** ([comment](https://news.ycombinator.com/item?id=49336573#49338429), 2026-08-17 22:18:16 UTC)
      It's not just claude, all AI is unable to produce something concise. On the surface everything looks 'good' whether code or prose, but then if you dig a bit, try and understand the whole text you quickly realise that 80% of it is unecessary and the whole thing could have been re-worded/re-coded into something a fraction of its size and complexity.

      I asked Sol to reduce the length of some documentation we had by making it more concise. It came back after 20 minutes of work, did a line count and was aghast that the line count had somehow increased...

      - **andreyf** ([comment](https://news.ycombinator.com/item?id=49336573#49342382), 2026-08-18 07:11:09 UTC)
        It's not that it fundamentally isn't able to produce something concise, it's that the business model of the companies developing these models rests on selling tokens...

      - **koe123** ([comment](https://news.ycombinator.com/item?id=49336573#49342070), 2026-08-18 06:28:37 UTC)
        I have a theory that AI code looks good because you never subsequently come up with your own alternative.

        - **Perepiska** ([comment](https://news.ycombinator.com/item?id=49336573#49342266), 2026-08-18 06:54:26 UTC)
          "AI code looks good for you because you are a bad developer"?

          - **a96** ([comment](https://news.ycombinator.com/item?id=49336573#49342542), 2026-08-18 07:29:15 UTC)
            Or non-developer.

            - **dosisking** ([comment](https://news.ycombinator.com/item?id=49336573#49343442), 2026-08-18 09:50:23 UTC)
              Or Rust programmer

            - **Perepiska** ([comment](https://news.ycombinator.com/item?id=49336573#49342666), 2026-08-18 07:44:25 UTC)
              .. but pretend to be a developer?

      - **preg_match** ([comment](https://news.ycombinator.com/item?id=49336573#49339942), 2026-08-18 01:19:04 UTC)
        I have to ask Claude to compact the comments every time, and I give specific criteria for it. Never ever reiterate what’s in the code, never mention decisions not made, never mention the conversation, etc etc.

        Even then it is conservative. For the love of God, compact the comments.

        Comments become a huge maintenance burden, especially in the age of AI. They just grow and grow, and then mislead the AI later on.

        - **Taek** ([comment](https://news.ycombinator.com/item?id=49336573#49342055), 2026-08-18 06:27:32 UTC)
          I just wrote a utility to rip all comments out of the code. Now the code is fully uncommented and it has saved lots of input tokens and also lots of meandering because the model is no longer getting stuck on bad ideas it told itself about.

          - **mrweasel** ([comment](https://news.ycombinator.com/item?id=49336573#49343007), 2026-08-18 08:36:24 UTC)
            That's is something I did not consider, the model using the existing comments as input. Comments that it may itself have written.

        - **gritzko** ([comment](https://news.ycombinator.com/item?id=49336573#49342512), 2026-08-18 07:26:49 UTC)
          I set a line budget for comments (also wiki page parts, chat responses, etc). That only helps when I ask it to do a second pass to reword everything to the budget and add links. I think they tuned it this way to stash reasoning dumps in the code. Unlike human developers, it has no context in its head, other than general GitHub knowledge.

          That is a dramatic shortcoming, but I fix it with permalinks to other files. [https://replicated.live/blog/link](https://replicated.live/blog/link)

    - **unknownfuture** ([comment](https://news.ycombinator.com/item?id=49336573#49340619), 2026-08-18 02:48:11 UTC)
      Oh Jesus this. I've tried to include rules that tell Claude to only include relevant, evergreen comments but it's to no avail.

      I also love how it'll build local plans with phases, tasks, or decisions, then reference those numbers in those same useless comments.

      - **arcanemachiner** ([comment](https://news.ycombinator.com/item?id=49336573#49342685), 2026-08-18 07:47:28 UTC)
        Or when it references "item 06" from some plan you wrote as if it had any relevance to you whatsoever.

    - **_--__--__** ([comment](https://news.ycombinator.com/item?id=49336573#49338569), 2026-08-17 22:31:40 UTC)
      Yeah this is awful. Every codebase becomes a graveyard of references to ideas or behaviors that were barely considered. It's probably also a compounding source of context poisoning when a minority of the comments/documentation are about how the current code actually works.

      - **ryandrake** ([comment](https://news.ycombinator.com/item?id=49336573#49340011), 2026-08-18 01:28:41 UTC)
        It also likes to spew references to documents that are not, and never have been, in the repo. So if you're not careful you'l have comments all over your codebase saying things like: foo() - Perform foo action as documented in PRIVATE_INTERNAL.doc

        - **abustamam** ([comment](https://news.ycombinator.com/item?id=49336573#49340184), 2026-08-18 01:54:45 UTC)
          I found this as well, but I found it usually refers to a scratch file it made and purposely did not commit (either by my decision or its). Not that this makes it better, but at least it makes the AI world make a bit more sense to me

    - **geysersam** ([comment](https://news.ycombinator.com/item?id=49336573#49341844), 2026-08-18 05:59:47 UTC)
      *shudder*

      I wish they trained the bots to be a notch more relaxed and less hysterical.
      Less is more.

      But maybe that's just a consequence of the RL training being essentially AI torture to make them do what we want.

    - **ulrikrasmussen** ([comment](https://news.ycombinator.com/item?id=49336573#49340988), 2026-08-18 03:41:32 UTC)
      This is a common problem, and I don't get why LLMs have not been tuned to stop this nonsense. It is writing comments as if the audience is you, the user in the session, while obviously code comments are meant for future readers.

      - **soupspaces** ([comment](https://news.ycombinator.com/item?id=49336573#49341527), 2026-08-18 05:12:07 UTC)
        Follow the tokens

  - **noman-land** ([comment](https://news.ycombinator.com/item?id=49336573#49337333), 2026-08-17 20:41:58 UTC)
    Have you considered talking about it? You're in a professional environment collectively working in a new way with a group of people. It's up to somebody to have opinions about what does and doesn't suck. If you silently go along and don't say anything you're dooming yourself and all of us to a lifetime of this garbage.

    - **corndoge** ([comment](https://news.ycombinator.com/item?id=49336573#49337537), 2026-08-17 20:58:14 UTC)
      Fighting the ocean is futile

      - **delecti** ([comment](https://news.ycombinator.com/item?id=49336573#49337682), 2026-08-17 21:09:58 UTC)
        It's not the ocean, it's the poster's own team. A simple "AI comments suck" in a sprint retro would be trivially easy and would at least start the conversation.

        - **wavemode** ([comment](https://news.ycombinator.com/item?id=49336573#49340653), 2026-08-18 02:51:48 UTC)
          While I agree with the spirit of what you're saying, it is very similar to whenever anyone complains about things where they work. "Well, why don't you just raise it with management?" You're assuming that management

          1) Understands the problem ("what are comments?")

          2) Accepts that it is a problem ("how can more comments be a bad thing?")

          3) Cares enough to solve the problem ("is this issue really a priority to solve right now? just accept the PR and we'll go back and fix if needed some other time *cough* never *cough*")

          4) Believes you (this can take many forms, but the most common is, subconsciously, "this other engineer says it's not a problem, so I'll just assume it's not since that's easier")

          All of these logistical, political and social factors are "the ocean"

          - **delecti** ([comment](https://news.ycombinator.com/item?id=49336573#49341019), 2026-08-18 03:45:51 UTC)
            Sprint retro is with your own team. And disagreement isn't a problem, at least then there would be the potential to come to a common understanding between the GP comment and their coworkers.

          - **Perepiska** ([comment](https://news.ycombinator.com/item?id=49336573#49342299), 2026-08-18 07:00:29 UTC)
            I usually require to file an issue in bug tracker about problem in #3 and then follow all its updates to prevent silent closing by management. It won't help but annoys management a lot and they afraid to get more backlog issues of such sort from me in the future.

          - **tripledry** ([comment](https://news.ycombinator.com/item?id=49336573#49342404), 2026-08-18 07:12:50 UTC)
            Seems to me if technical decisions on the level of "no more AI comments" go through management the organization doesn't know what they are doing.

            To be fair, I would not be surprised.

        - **stronglikedan** ([comment](https://news.ycombinator.com/item?id=49336573#49338305), 2026-08-17 22:03:26 UTC)
          Doesn't matter. You'll come off as the baddie. It's the foreseeable future. Best just to learn how to interpret AI generated shit, or learn how to run it through AI and have it translate it to a more concise format without all the buzzwords. It'll take getting used to, but it'll save your career.

          - **stAInley** ([comment](https://news.ycombinator.com/item?id=49336573#49344058), 2026-08-18 11:20:52 UTC)
            This reply is not directed to you specifically, but that attitude is why improvement doesn't happen.

            "My peers are all bad", "Management has no idea what's going on", "My boss is out of touch", "My staff keep screwing up".

            But if you're consistently seeing the problems while everyone else becomes defensive, you (that think that way) need to learn how to communicate effectively in a way that doesn't result in being 'the baddie' and solve the interpersonal dynamic along with the technical problems. "Crucial Conversations" is a good place to start.

          - **wpietri** ([comment](https://news.ycombinator.com/item?id=49336573#49339881), 2026-08-18 01:10:09 UTC)
            You don't have to come across as the baddie. There are plenty of neutral ways to start the conversation. E.g., "I notice that there's a lot more generated comments lately. How much are people finding those useful?"

            If you really want to save your career, learning how to have real conversations is a vital skill.

            - **mannanj** ([comment](https://news.ycombinator.com/item?id=49336573#49340265), 2026-08-18 02:06:19 UTC)
              Have you worked in corporate recently or at a particularly toxic one?

              Asking because when I was at capital one, certain comments or questions about topics like this, would actually get you noticed negatively by your manager and being disruptive to what leadership wants hurts your career.

              In fact being the one to ask and point out questions like yours ultimately got me PIP'ed and removed from the company. So, like, yeah, being vulnerable and the first one to tell the truth is risky. That's why the bystander effect can happen and in politics or risky situations silence is a common response, and why we don't have more courageous people doing the right thing - because the risk is higher on the person speaking up and the rewards aren't disproportionately in their favor (but are evenly distributed though, so its not favorable for you as I learned from a game theory perspective to voice up / defend certain stances).

              - **annzabelle** ([comment](https://news.ycombinator.com/item?id=49336573#49341327), 2026-08-18 04:38:38 UTC)
                Capital One is a particularly toxic work environment, and I'm not sure that your experiences there apply to other companies.

                I started my first post-Capital One job a few months ago, and I'm still not used to the fact that this company expects everybody working here to still be working here in two years. Most employers are not going through everybody with a fine tooth comb every 6 months hunting for any hint of an excuse to PIP them.

          - **ulrikrasmussen** ([comment](https://news.ycombinator.com/item?id=49336573#49341046), 2026-08-18 03:50:00 UTC)
            What is this defeatist attitude? I don't know where you work, but it is not my impression that AI has instantly turned all developers into mindless AI-pilled sheep. If you feel like a simple suggestion like that will cost you your career, then it doesn't sound like a place where any constructive criticism would have been accepted even before AI.

            - **akomtu** ([comment](https://news.ycombinator.com/item?id=49336573#49341110), 2026-08-18 04:03:35 UTC)
              AI is more or less a religion right now in the corporate world. Speaking against AI amounts to heresy.

              - **ulrikrasmussen** ([comment](https://news.ycombinator.com/item?id=49336573#49341501), 2026-08-18 05:06:40 UTC)
                There is no single conforming "corporate world" that applies to all companies. If AI is treated religion in your company that sounds like a local problem, even if it seems like a trend.

                Besides, GP was not talking about corporate, but about the inability to even suggest an improved usage of LLMs among their developer peers, as if every line of code generated by AI is now gospel and questioning it is treated as heresy. This level of defeatism is beyond cynical and approaching childish.

          - **dragontamer** ([comment](https://news.ycombinator.com/item?id=49336573#49341023), 2026-08-18 03:46:27 UTC)
            Bring it up in a bar or otherwise off work.

            There's a reason 3rd places exists. There's a social construct that off-work discussion (even when on-work) stays off work.

            If your coworker is professional and cares about keeping channels open, they too will respect the unspoken rules that govern 3rd place neutral locations.

            Blame it on the alcohol later on if it actually pisses someone off.

            - **febusravenga** ([comment](https://news.ycombinator.com/item?id=49336573#49341589), 2026-08-18 05:23:33 UTC)
              This is the third place. There is no real 3rd place in real companies usually. Not in mine, when i work remotely for company from other side of continent.

            - **johnnyanmac** ([comment](https://news.ycombinator.com/item?id=49336573#49341475), 2026-08-18 05:01:11 UTC)
              >There's a reason 3rd places exists.

              Not anymore these days.

          - **atomicnumber3** ([comment](https://news.ycombinator.com/item?id=49336573#49341550), 2026-08-18 05:17:12 UTC)
            The number one rule of corpo programming: never, ever solve a problem you haven't been asked to solve.

        - **VohuMana** ([comment](https://news.ycombinator.com/item?id=49336573#49338182), 2026-08-17 21:51:37 UTC)
          I think the biggest issue might not be the immediate team but upper leadership. Companies which have mandated AI usage override a lot of what an individual or individual team wants. If that’s the case then it would be a lot like fighting the ocean, especially if your immediate team sees having AI write docs as an easy way to move the needle on LT’s AI monitoring dashboard.

        - **a2ff6eeb0** ([comment](https://news.ycombinator.com/item?id=49336573#49341274), 2026-08-18 04:31:06 UTC)
          It's the management desired direction, if the place is anything like my workplace. Everyone is all in on AI, and if you're not using it for everything possible, you're on the chopping block.

          And, really, it works. You can copy and paste between tickets and Claude, and then do manual testing. Then you tell Claude to self-review for clarity and minimalism, and stop worrying. Sure, today it's not as good as a human, but for almost all the code out there, it gets the job done. There's no skill needed any more, and if the boss doesn't care about quality, I don't see why I should.

          - **NateEag** ([comment](https://news.ycombinator.com/item?id=49336573#49341727), 2026-08-18 05:45:49 UTC)
            Your boss can get Claude to make unreadable, noisy, confusing code just as well as you can.

            There may not be a career left in software development with these monstrosities, but if there is, it's in using decades of experience to get the abominations to produce something other than unreadable dreck.

            If the code itself truly doesn't matter any more, programmers will no longer be paid.

        - **swat535** ([comment](https://news.ycombinator.com/item?id=49336573#49338573), 2026-08-17 22:32:03 UTC)
          You're going to have convince upper management why the team's velocity is suddenly affected in feature releases once they stop using AI.

          All the execs know that they can refresh the screen faster and see the features for marketing and sales.

          When has engineering ever had a voice anyway? The bean counters have been looking to cut us out since the inception of our industry.

      - **trip-zip** ([comment](https://news.ycombinator.com/item?id=49336573#49337655), 2026-08-17 21:07:48 UTC)
        So is completely eliminating litter, but I still pick it up when I pass it.

        - **noisy_boy** ([comment](https://news.ycombinator.com/item?id=49336573#49340148), 2026-08-18 01:47:57 UTC)
          Everybody generally agrees on what is garbage. Lot of senior management doesn't think AI is garbage or even if they privately think so, they don't say that openly. Falling in line, peer pressure, not wanting to come across as anti-AI luddite etc. All those issues affect the individual contributors too + the added challenge of perception in front of those who decide the bonus and lately, continued employment.

          In this fucked up job market, it is easier said than done.

          - **abustamam** ([comment](https://news.ycombinator.com/item?id=49336573#49340216), 2026-08-18 01:59:15 UTC)
            I feel like the chain kinda goes all the way to the top, to the level of shareholders. My boss needs to give his boss the perception that the engineering team is firing on all cylinders and has high velocity, so that he can sell that story to shareholders who could easily invest in another "AI-native" company and make more money because they're growing like crazy.

            I feel like it's all just perception and how companies can sell their stories to investors or potential acquirers, and everything else can be punted and dealt with later when we get acquired or when share prices are a zillion dollars etc.

            It's a race to the bottom, for sure.

      - **a34729t** ([comment](https://news.ycombinator.com/item?id=49336573#49337782), 2026-08-17 21:18:08 UTC)
        Literally pissing in an ocean of piss.

        - **anon7725** ([comment](https://news.ycombinator.com/item?id=49336573#49337938), 2026-08-17 21:31:45 UTC)
          Analogy-wise, wouldn't it be adding a cup of water to an ocean of piss?

          - **abustamam** ([comment](https://news.ycombinator.com/item?id=49336573#49340197), 2026-08-18 01:56:09 UTC)
            It'd be taking a cup of piss out of the ocean of piss i think!

    - **LPisGood** ([comment](https://news.ycombinator.com/item?id=49336573#49337965), 2026-08-17 21:33:29 UTC)
      Yes, talking about it repeatedly has been my process. Individual PRs have been changed but the 4 the next day look the same. The typical response is that they did change the (massive and wordy) PR overview from what AI said, even if it was obviously a minimal change at best. I can’t really argue against lying and going through and picking out every LLMism is not so productive in my opinion.

      I don’t have time to go through and flag everything or even read the thousands of lines of code changes that are happening.

    - **eudamoniac** ([comment](https://news.ycombinator.com/item?id=49336573#49340311), 2026-08-18 02:12:58 UTC)
      I've tried doing this, politely pushing back on problems happening from AI use, and it led to a not-so-subtle implication from my manager that I need to STFU or I'll be out of here (Cisco).

    - **atomicnumber3** ([comment](https://news.ycombinator.com/item?id=49336573#49341521), 2026-08-18 05:11:06 UTC)
      No, if he speaks against it he gets labeled "anti-AI" and laid off or not promoted. If he stays silent he retains his job.

      Corporate Capitalism's main innovation was virtualizing feudalism. Now anyone with a bit of cash flow can be a feudal lord with peasants to do his will. No need to maintain land or fight over it with other feudal lords. There's still fighting, naturally, but now the game isn't zero sum.

      The serfs don't get any real say in this model. At best you can bend the lord's ear if you're sufficiently trusted an advisor. But part of the reason you're trusted is to be trusted not to treat the lord like he's too much of an idiot.

      A huge problem is that capitalism rewards cash flows and accumulated capital so powerfully that lots of other things just don't matter, potentially for a very long time. Look at GitHub. This leads to immensely extended fuck around phases and "find out" looks like IBM (fossilization and bizarre holdings corporation / dead company parking lot) just as often as it looks like Enron.

      - **brabel** ([comment](https://news.ycombinator.com/item?id=49336573#49341726), 2026-08-18 05:45:44 UTC)
        > The serfs don't get any real say in this model

        I am a programmer but also in management, and if I knew my team thought like that I would be horrified. We absolutely care about what the team members want , like, hate etc. I for once would love someone to bring up stuff like this to me. As long as they are as open minded about things as they would like me to be, there is no issue. But it’s a serious issue to pretend everything is fine while thinking like you say.

        - **keosak** ([comment](https://news.ycombinator.com/item?id=49336573#49342877), 2026-08-18 08:15:00 UTC)
          > We absolutely care about what the team members want , like, hate etc.

          Do the people above you in management care as much? It's the top levels of management that decide hiring, firing and budgets.

      - **munksbeer** ([comment](https://news.ycombinator.com/item?id=49336573#49344218), 2026-08-18 11:41:08 UTC)
        I was nodding to your post for a short period, then you just had to throw in the usual anti-capitalism zeitgeist rant.

        Reframe your context, pretend you're in a communist society, and you could be making the exact same point about speaking up against the grain being bad for you. It feels as though people are brainwashed by anti-capitalism sentiment at the moment, unable to see outside of that context.

  - **joshmoody24** ([comment](https://news.ycombinator.com/item?id=49336573#49338208), 2026-08-17 21:53:21 UTC)
    My team uses a Claude Code hook that blocks any comment more than 2 lines long, and when tripped it encourages the agent to rewrite the comment more concisely and focus only on the "why" not the "what" of the code. I've found this extremely useful for code reviews.

  - **rbongers** ([comment](https://news.ycombinator.com/item?id=49336573#49338947), 2026-08-17 23:09:32 UTC)
    Two very useful directives to give AI when it comes to documentation:

    1) Document what's there, not the diff. Documentation of how code was removed or changed to fix a bug or add a feature is not useful and difficult to maintain; documentation should explain how code works now.

    2) Documentation should live close to the source as possible. Prefer line based comments and standardized function documentation. Top-level sweeping architectural essays are not maintainable for every change.

    The last will depend on your codebase. It CAN be very useful to have a human-readable spec documented for the entire program and have it updated when anything changes. But the key is again, you're CHANGING it every time. If you add a whole new disconnected documentation file it should set off alarm bells; nothing in one system is truly disconnected.

    - **ninkendo** ([comment](https://news.ycombinator.com/item?id=49336573#49340136), 2026-08-18 01:45:44 UTC)
      > Document what's there, not the diff

      We recently added a similar thing to our style guide, It’s astonishing to me that we have to spell this out, that something as obvious as this needs to be explained to LLM’s at all. They’re supposed to be exceeding human intelligence, at least at things like programming, but can’t understand basic things like what code comments are.

      - **paldepind2** ([comment](https://news.ycombinator.com/item?id=49336573#49343311), 2026-08-18 09:27:56 UTC)
        My theory (which might be completely wrong) is that models do this because it improves quality for vibe coders.

        When vibe coding the content of user prompts is ground truth and the only way any human thought affect the code base. So if the vibe coder says "do X not Y", recording int comments that "we shouldn't do Y" is important. It ensures that the agent doesn't accidentally decide to do Y tomorrow, which would frustrate the vibe coder who'd feel that the agent doesn't "remember" what it was told yesterday.

        So for people who look at the code the comments are obvious and completely superfluous, but for the vibe coder it's a way to ensure that their tiny (relative to the size of the code base) input is not forgotten.

      - **epidemian** ([comment](https://news.ycombinator.com/item?id=49336573#49342322), 2026-08-18 07:03:47 UTC)
        > It’s astonishing to me that we have to spell this out, that something as obvious as this needs to be explained to LLM’s at all.

        Hehe. Yeah, that tendency of LLMs to document "the story" of the code instead of its current purpose (or non-obvious implementation details) is a pet peeve of mine too. I've added a slew of guidelines to try to sway Claude to not do this, but it still does it often.

        At the same time, it feels like something to be expected to have this "failure mode". The model has its context to work on, and what is on its context if not the conversation you've been having (and its internal monologue) and the files it has read? It makes sense that it references the story on its text generations, because that behavior is usually a good thing for an LLM to do. Otherwise, what would it generate? If it generated things that had nothing to do with the conversation in its context, in many cases those things would be seen as "hallucinations", and they'd tend to be RLHF'ed out. So the models that we end up having are the ones that have been reinforced to be most "contextually relevant" and less "hallucinatory".

        I might be completely wrong on that of course. It's just my intuitive reasoning of why this seems to be such a prevalent behavior.

      - **silverwind** ([comment](https://news.ycombinator.com/item?id=49336573#49342204), 2026-08-18 06:47:59 UTC)
        Most models are trained to be as "helpful" as possible which may work for a chatbot but not for code.

      - **eru** ([comment](https://news.ycombinator.com/item?id=49336573#49341163), 2026-08-18 04:12:54 UTC)
        It's a bit weird, because that seems like something that approximately the same in every code base, so should be relatively easy to train generically.

      - **johnnyanmac** ([comment](https://news.ycombinator.com/item?id=49336573#49341525), 2026-08-18 05:11:58 UTC)
        >They’re supposed to be exceeding human intelligence, at least at things like programming

        This perception is a good part of why this market is irrational. LLM's aren't "intelligent". They do not reason, they are a very fancy kitbash of whatever it trains on.

        Ad yeah, I'm not surprised that a lot of documentation on every bit of readable code online is awful. "Document the diff" sounds like an anti-pattern learned from people with an incentive to get as many PR's submmitted as possible, not make the most friendly documentation for people maintaining a project.

  - **kristjansson** ([comment](https://news.ycombinator.com/item?id=49336573#49340656), 2026-08-18 02:51:57 UTC)
    And the tests. Oh god the tests. Personal recent favorite: I asked for some changes to a Dockerfile, which it did ably, and then promptly tested by writing a pytest module that traversed up to the root, read the Dockerfile, and checked that the added lines were present.

    - **eru** ([comment](https://news.ycombinator.com/item?id=49336573#49341169), 2026-08-18 04:14:12 UTC)
      Try property based testing perhaps.

      - **kqr** ([comment](https://news.ycombinator.com/item?id=49336573#49341804), 2026-08-18 05:55:36 UTC)
        Code-generating robots are pretty bad at property-based testing, in my experience. They can do it but they still need a lot of hand-holding. They often regress to writing a mirror implementation as the oracle and trying to enumerate a fixed set of examples they find meaningful.

      - **kristjansson** ([comment](https://news.ycombinator.com/item?id=49336573#49341510), 2026-08-18 05:08:49 UTC)
        I'm generally happy with the tests I ask it for, some of which are PBT.  It's just the insistence upon memorializing every single change with a test.  Maybe encouraging / forcing PBT will dissuade it?

      - **LPisGood** ([comment](https://news.ycombinator.com/item?id=49336573#49341468), 2026-08-18 05:00:20 UTC)
        I’ve heard of this, but I’m not really sure at all how to even get started. Are there any good guides out there?

        - **eru** ([comment](https://news.ycombinator.com/item?id=49336573#49342499), 2026-08-18 07:25:40 UTC)
          Many people like [https://fsharpforfunandprofit.com/series/property-based-test...](https://fsharpforfunandprofit.com/series/property-based-testing/)

          In this day and age, [https://hypothesis.works/articles/claude-code-plugin/](https://hypothesis.works/articles/claude-code-plugin/) might be useful.

    - **LPisGood** ([comment](https://news.ycombinator.com/item?id=49336573#49340681), 2026-08-18 02:55:13 UTC)
      I regret this but at some point I stopped reading generated tests. It feels pointless when our test files are already tens of thousands of lines of — at best — tautological slip which says that the codes does what it does.

      - **fireflash38** ([comment](https://news.ycombinator.com/item?id=49336573#49344204), 2026-08-18 11:39:50 UTC)
        I think reading and writing test code is harder than the underlying code itself. You must know both the desired behavior of the code-under-test and whether the test correctly stresses that behavior. And then if you're working on anything more complicated than a single unit test you must also make sure that it doesn't blow up anything adjacent to it (preserve state).

        I think enforcing black box testing is the best way to get useful tests out of both humans and robots. They must not know the internals, or it will lead them to do bad things.

  - **hinkley** ([comment](https://news.ycombinator.com/item?id=49336573#49339713), 2026-08-18 00:44:26 UTC)
    I told someone this week, who (or whose AI) chose to do a problem the hard way that it's usually a bad sign if you need more comments than code to solve a problem, and then suggested a couple lines of code that accomplished the same thing and used, are you sitting down? MEANINGFUL VARIABLE NAMES to document the purpose of each calculation.

    I wonder if I can get a MacArthur grant for this epiphany...

  - **Fordec** ([comment](https://news.ycombinator.com/item?id=49336573#49337296), 2026-08-17 20:38:08 UTC)
    I have five enforcement mechanisms: 1000 line max edit, PR comment character limits (get to the point of your description), ISO 24495 conformance check, and enforced code line citation that must exist, be a function declaration for the start of all paragraphs and inline commentary must be three lines or less and inline comments contribute max 10% of the PR. Fail any of these, automatic PR denial with no human intervention.

    - **LPisGood** ([comment](https://news.ycombinator.com/item?id=49336573#49337314), 2026-08-17 20:40:10 UTC)
      This sound pretty good, but every single attempt to put an actual character limit meets incredible resistance on my team. ISO 24495 looks interesting, how do you enforce that? Do you have some agent?

      - **Fordec** ([comment](https://news.ycombinator.com/item?id=49336573#49337983), 2026-08-17 21:34:39 UTC)
        Table of words LLM generated, Binary Searched on the output going forward and local skill/CLAUDE.md line with instruction to conform. The comparison then is pretty fast due to the word limitation rules. Also standardized PR format so a bunch of what a dev would usually communicate is just a series of checkboxes and a place for adding an optional link for "additional discussion" on slack as the escape hatch for people who like to waffle.

    - **CSMastermind** ([comment](https://news.ycombinator.com/item?id=49336573#49337873), 2026-08-17 21:26:20 UTC)
      > ISO 24495 conformance check

      How do you enforce that?

      - **Fordec** ([comment](https://news.ycombinator.com/item?id=49336573#49337919), 2026-08-17 21:30:54 UTC)
        Binary Searched against a table of words. It's rough at first, but once you add contextual exceptions the false positives calm down. Also the CLAUDE.md file has an instruction to conform before even submitting the PR and there's a skill too for it to self iterate.

  - **rfgplk** ([comment](https://news.ycombinator.com/item?id=49336573#49337316), 2026-08-17 20:40:19 UTC)
    Prune the comments? Instruct the LLM to print less comments (this one is genuinely hard though). What's really happening is that you don't have a strong enough review process (or a code standards process) to offset this. The one issue I see with this is that your team is almost certainly _NOT_ doing any kind of code review (especially if they're leaving comments like that). The other problem is that excessive comments actually harm LLM output, I've done tons of A/B testing, and pruning comments actually helps LLMs spot bugs, among other things.

  - **eithed** ([comment](https://news.ycombinator.com/item?id=49336573#49343821), 2026-08-18 10:52:54 UTC)
    Be the change you want to see :)

    I've created myself a pre-commit harness hook to explicitly discard superfluous or too lengthy comments. Within code-review I also added comment review as blockers

  - **kqr** ([comment](https://news.ycombinator.com/item?id=49336573#49341839), 2026-08-18 05:59:35 UTC)
    I think your last sentence is getting close to the truth. You're no longer the audience for those descriptions. Other robots are.

    I'm not saying that's good or bad because I don't know, but I think that's the idea of dumping all that junk into PR descriptions.

    However, annoyingly, we still need to review those descriptions very closely, because the robots are trained to put a lot of weight into things they read in the documentation. And they tend tospresent loose speculation as fact. They often end up documenting some assumption that isn't true, then end up writing code as if it were.

    - **anematode** ([comment](https://news.ycombinator.com/item?id=49336573#49342001), 2026-08-18 06:20:13 UTC)
      Even worse, in a brownfield codebase that was once fairly light with comments, that's now being subject to these modifications, the insane amounts of commentary around the parts newly touched by AI lead to an excessive emphasis on those parts, for both human and AI readers (who think, well if this one part is commented so thoroughly, it must be unusually subtle)

  - **giancarlostoro** ([comment](https://news.ycombinator.com/item?id=49336573#49337346), 2026-08-17 20:42:37 UTC)
    Honestly, if you saved a ton of hours with the model coding for you, at least give me 30 minutes of your own words, show me you know what you're shipping, if you can't do that, then I don't know if I want to approve the PR. My first job we always did peer review in a meeting room when a PR looked a little too much, you can't exactly bring in GPT into a meeting so its a good time to ask simple questions about the change to ensure you understand it just as much as they do.

    - **febusravenga** ([comment](https://news.ycombinator.com/item?id=49336573#49341611), 2026-08-18 05:27:11 UTC)
      (usually) You're not in position of power to effectively keep that position. As comments aroiund - standing against will mark you as anti-ai luddite and will now end well for you, not AI-spammer.

    - **fragmede** ([comment](https://news.ycombinator.com/item?id=49336573#49337971), 2026-08-17 21:33:55 UTC)
      > you can't exactly bring in GPT into a meeting

      They totally gotta be doing that at OpenAI. Meeting invitees: You, co-workers, GPT 5.6.

      - **giancarlostoro** ([comment](https://news.ycombinator.com/item?id=49336573#49338103), 2026-08-17 21:44:28 UTC)
        Well yeah, they'll keep burning the VC bucks.

  - **dimgl** ([comment](https://news.ycombinator.com/item?id=49336573#49338360), 2026-08-17 22:11:01 UTC)
    Congratulations: now only AI can iterate on your codebase!

    - **Gigachad** ([comment](https://news.ycombinator.com/item?id=49336573#49338684), 2026-08-17 22:43:40 UTC)
      Even the AI degrades as the codebase gets shittier

      - **duskdozer** ([comment](https://news.ycombinator.com/item?id=49336573#49343300), 2026-08-18 09:26:05 UTC)
        Degrades? Nonsense. Sounds like you need the latest model and more tokens.

    - **LPisGood** ([comment](https://news.ycombinator.com/item?id=49336573#49338598), 2026-08-17 22:34:49 UTC)
      That’s probably not completely true, but it’s approximately true.

  - **72deluxe** ([comment](https://news.ycombinator.com/item?id=49336573#49343215), 2026-08-18 09:09:23 UTC)
    It's like people didn't realise that it was unmaintainable before and now we have a new level of unmaintainability. The insane amount of code produced means it's only maintainable with AI.

  - **BeetleB** ([comment](https://news.ycombinator.com/item?id=49336573#49337401), 2026-08-17 20:46:58 UTC)
    It's a code review, right?

    Give feedback that about the docs and block merging till the issue is resolved.

    - **LPisGood** ([comment](https://news.ycombinator.com/item?id=49336573#49338007), 2026-08-17 21:37:21 UTC)
      This sounds easy in principle, but a half dozen of these sort sorts of massive PR’s per week is basically untenable. I’m not gonna read the hundreds of lines of added documentation to decide if they’re correct or not. The price of generating new words is just so much higher than the price of evaluating it that I can’t be bothered.

      - **tcmart14** ([comment](https://news.ycombinator.com/item?id=49336573#49341082), 2026-08-18 03:56:37 UTC)
        Just hit "deny." I've been training my co-workers that the AI-isms their "AI Assisted coding" do that some shit just isn't acceptable. I leave a comment and hit deny. It also helps that I control the policies on the repo and they can't merge in with a denial from anyone. So it's either a fix it, or explain why your work isn't getting done. My manager is also 100% with this.

        I've denied for poor branch names and commits from AI. I've denied for too verbose of comments from AI. I've denied for parts of the code base being touched that are not relevant to the case they are working on (login isn't broken, your case is to add a check box in the settings pane, remove the changes made to login).

        Pre-AI I wasn't fine with PRs with multiple features and touching irrelevant areas of the code base. Why would I be fine with it because my co-workers got new toys? You want AI to refactor a part of the codebase? Fine. Separate branch, new PR, and in the description, present an argument for it. Don't shoe horn it into something else. Also, I'm not obligated to hit approved on shit.

        I may also be a bit privileged because I can be a pain in the ass to whole team. I may be slower, but I've got the numbers, my code is creating way less bugs then my "fast more efficient" co-workers.

        - **LPisGood** ([comment](https://news.ycombinator.com/item?id=49336573#49341149), 2026-08-18 04:10:50 UTC)
          Now suppose four of your teammates, each have three PR’s in the backlog and you have to explain to your manager that you’re the bottleneck.

          - **tcmart14** ([comment](https://news.ycombinator.com/item?id=49336573#49341158), 2026-08-18 04:12:23 UTC)
            As quoted from my comment: "My manager is also 100% with this."

            - **select1** ([comment](https://news.ycombinator.com/item?id=49336573#49341185), 2026-08-18 04:16:14 UTC)
              And he has bosses. And are they okay with some whatever being an obstacle to work getting done? Probably not.

              - **tcmart14** ([comment](https://news.ycombinator.com/item?id=49336573#49341197), 2026-08-18 04:17:59 UTC)
                That's on him to handle and it hasn't been a problem.

                - **select1** ([comment](https://news.ycombinator.com/item?id=49336573#49341204), 2026-08-18 04:19:20 UTC)
                  When it's a problem, you should both expect to be unemployed fairly rapidly. Progress isn't going to stop solely because you want to pick 'excessively long comments' as a hill to die on.

                  - **johnnyanmac** ([comment](https://news.ycombinator.com/item?id=49336573#49341627), 2026-08-18 05:31:29 UTC)
                    You're really insistent on project your personal biases onto a person and company you do not even know the identity of.

                    Turns out not every team has the idea of "progress" being yet another iteration of "more code submitted = better code". Some people actually desire or need to make quality products.

                  - **Sharlin** ([comment](https://news.ycombinator.com/item?id=49336573#49341734), 2026-08-18 05:46:38 UTC)
                    "Progress"

        - **matheusmoreira** ([comment](https://news.ycombinator.com/item?id=49336573#49341347), 2026-08-18 04:40:16 UTC)
          ... Poor branch names?

        - **select1** ([comment](https://news.ycombinator.com/item?id=49336573#49341140), 2026-08-18 04:08:52 UTC)
          [comment text unavailable]

          - **dofm** ([comment](https://news.ycombinator.com/item?id=49336573#49341685), 2026-08-18 05:39:37 UTC)
            Coupled with the other comment of yours that was flagged, the tone of this is completely unacceptable.

          - **Sharlin** ([comment](https://news.ycombinator.com/item?id=49336573#49341790), 2026-08-18 05:53:49 UTC)
            Maybe consider some anger management therapy? Nothing you’re talking about is in any way acceptable. Physical violence at work? You can’t be serious.

          - **tcmart14** ([comment](https://news.ycombinator.com/item?id=49336573#49341166), 2026-08-18 04:13:33 UTC)
            Its not petty is, Im not changing our standards because people got hot new toys. These are code policies we've had. If your AI usage can not conform to them, that's on you, not me.

            - **select1** ([comment](https://news.ycombinator.com/item?id=49336573#49341181), 2026-08-18 04:15:09 UTC)
              [comment text unavailable]

              - **tcmart14** ([comment](https://news.ycombinator.com/item?id=49336573#49341188), 2026-08-18 04:17:00 UTC)
                Why can't people just follow the *guidelines*. You really want to get into a fight over not following established and agreed upon guidelines and code quality standards?

      - **BeetleB** ([comment](https://news.ycombinator.com/item?id=49336573#49338157), 2026-08-17 21:49:45 UTC)
        > but a half dozen of these sort sorts of massive PR’s per week is basically untenable.

        Actually, rejecting them is precisely what will make them easy.

        "Sorry, the comments are so bad I'm stopping here. Please fix them and then I'll resume the code review."

        You're giving everybody (including yourself) more work by:

        1. Reviewing the code (even if you skip the documentation).

        2. Letting too many abstruse comments in which everyone in the team will have to read.

        3. Allowing the behavior to continue.

        Become the bottleneck so the team can talk about it. If they decide this shouldn't be a blocker, just declare you won't review the comments going forward.

        - **matheusmoreira** ([comment](https://news.ycombinator.com/item?id=49336573#49341399), 2026-08-18 04:49:28 UTC)
          > "Sorry, the comments are so bad I'm stopping here. Please fix them and then I'll resume the code review."

          This is also how I do code review of AI work on my projects. If the work is offensive to the point I can't complete the review, I simply reject the code and tell the AI why. Then it goes off and fixes it. This repeats until the issues are either gone or are small enough that I can just fix them myself and move on.

          There is no need to be upset. Just iterate until it's right. If it's cheap to write, it's equally cheap to rewrite.

        - **LPisGood** ([comment](https://news.ycombinator.com/item?id=49336573#49338580), 2026-08-17 22:33:05 UTC)
          I think you’re overestimating how easy it is to just declare I won’t be doing my job.

          - **BeetleB** ([comment](https://news.ycombinator.com/item?id=49336573#49339015), 2026-08-17 23:18:28 UTC)
            I am actually asking you to do your job. Pre-LLMs, if I got comments that were difficult to read in a code review, that PR isn't getting merged until they fix it. So: Review the docs. If it's that bad, just say "I don't understand these comments" and send it back.

            - **LPisGood** ([comment](https://news.ycombinator.com/item?id=49336573#49339129), 2026-08-17 23:31:15 UTC)
              What I’m trying to say is that they can generate many more hundreds of lines of code and comments than I can reasonably review. Maybe the comments do make sense they’re just five lines longer than they ought to be. Multiply that by 20 times and then add in 150 lines of documentation that is not technically incorrect.

              Not to mention that the response to each review will come with its own set of new comments and new documentation. The ability of people to write things has exploded tenfold. You can’t out review the slop.

              Every PR can be rewritten and re-architected on a whim.

              - **BeetleB** ([comment](https://news.ycombinator.com/item?id=49336573#49339503), 2026-08-18 00:16:34 UTC)
                Sure - but the volume is a separate problem from the quality of comments. Even if the comments were the best possible your complaint would still stand.

                - **latentsea** ([comment](https://news.ycombinator.com/item?id=49336573#49341065), 2026-08-18 03:53:22 UTC)
                  Tbh if the AI just followed the prompt to not add the comments, that'd be sufficient. It feels maddening and burnout inducing to tell it not to only to have it ignore that and you deal with the same problem every time without things meaningfully improving.

              - **27183** ([comment](https://news.ycombinator.com/item?id=49336573#49341025), 2026-08-18 03:47:06 UTC)
                Your bosses don't want you actually reviewing it anyway. They want you to *approve the PR*. Just give them what they want.

                I'm currently not working in tech, but I will again sometime within the next year or so, and I've been reflecting on my career in light of the recent AI madness. I think the biggest mistakes I've made over the last decade+ in tech as a software engineer have been *caring*. I've worked at small, medium, and large companies. Famous big names you've definitely heard of, less famous ones you probably haven't. In every case, in retrospect, as an individual contributor (non founder, non board member, etc) being personally invested in some outcome--quality, efficiency, cost, ux, customer value--is a mistake.

                If you aren't actually in a position to change something, caring about it is futile. [edit] And I don't mean in the sense of "feeling empowered" or some such, but actually having the clout to steer the ship and make it happen. Very few people in a tech organization actually have that power, by design.

                The industry wants to do away with code review, meaningful testing, computer security, and reliable services. Why swim upstream? You can't actually do anything about it so why try?

                When I go back to work I'm going to do my 9-5 40hr/wk, smile, nod, punch the clock, and make the bosses smile or whatever. But I'll be damned if I'll ever give a shit again.

                - **account42** ([comment](https://news.ycombinator.com/item?id=49336573#49343837), 2026-08-18 10:55:40 UTC)
                  I think that's just too cynical when you apply it to the entire industry. I'm sure there are coding jobs where you are just a cog in a factory line but IME there are also those where a lot of things really are up to the individual contributor because either no one else has even given them any though or higher up defer to your judgement (which is part of what they are paying you for).

                - **johnnyanmac** ([comment](https://news.ycombinator.com/item?id=49336573#49341756), 2026-08-18 05:49:37 UTC)
                  >The industry wants to do away with code review, meaningful testing, computer security, and reliable services. Why swim upstream? You can't actually do anything about it so why try?

                  Because habits beget habits, and in form imprint into your identity. I'm not the biggest fan of GPA fixation, but it does have the side effect of imprinting work habits (I won't say "ethics", because the extremes I saw peers go to to get A's is anything but). It doesn't necessarily imply mastery of your class, but your ability to adjust to someone's standards and meet them. Which is something that will follow you into the workforce, and roughly correlate with people who will meet the standards of their company.

                  If I don't give a damn about code quality in a place I spend a third of my life, why do I expect to give a damn when I want to work on my own project in the future? Even if I try those habits will wear into something I can call my own. This might be fine if your overall goals have nothing to do with your work; that you are fine just going through the motions and getting a paycheck to empower your non-tech hobbies or focus on supporting your family. But that's not the path I've chosen.

        - **eudamoniac** ([comment](https://news.ycombinator.com/item?id=49336573#49340361), 2026-08-18 02:18:54 UTC)
          This doesn't work because then you get fired for being a bottleneck.

          - **BeetleB** ([comment](https://news.ycombinator.com/item?id=49336573#49340447), 2026-08-18 02:28:13 UTC)
            The bottleneck existed before LLMs. Amdahl's Law applies. Just because code can be produced 10x faster doesn't mean much if other parts of the flow can't be sped up.

            As I said here and elsewhere: If management is concerned code review is a bottleneck, let management be aware that the process has to change. Either the human is not as thorough, or he uses some combination of his brain + LLM to conduct the review.

            It's a basic fact: They have a machine that produces a lot of code, but don't have a machine to review that code. The bottleneck is obvious. I'd love to build planes for $1 too, but physics applies.

            - **eudamoniac** ([comment](https://news.ycombinator.com/item?id=49336573#49340631), 2026-08-18 02:49:15 UTC)
              Management is not a logical formula. Management says all code must be reviewed, your coworkers are approving (rubber stamping) PRs 10x faster than you, why aren't you able to keep up? Why are you being difficult?

              - **account42** ([comment](https://news.ycombinator.com/item?id=49336573#49343894), 2026-08-18 11:02:23 UTC)
                Management also doesn't have to be as simplistic as "more code faster = better" without any understanding  of the consequences.

    - **Gigachad** ([comment](https://news.ycombinator.com/item?id=49336573#49338702), 2026-08-17 22:45:18 UTC)
      You can't keep up with the slop. And before you finish a first pass read on the wall of diff, another AI sloperator on the team has hit approve and the PR is merged.

      - **LPisGood** ([comment](https://news.ycombinator.com/item?id=49336573#49338791), 2026-08-17 22:52:30 UTC)
        Exactly this. Even if I spend a bunch of time requesting a review — and our team does respect each other enough to at least nominally respond to comments before merging — the update itself will be another thousand line diff from the original that requires again the same level of review or I just accept that it looks fine.

      - **account42** ([comment](https://news.ycombinator.com/item?id=49336573#49343908), 2026-08-18 11:04:18 UTC)
        At that point maybe go looking for a company with a better work environment.

  - **theptip** ([comment](https://news.ycombinator.com/item?id=49336573#49340260), 2026-08-18 02:05:26 UTC)
    I have my agent write up a summary of the diffs that land each day in my org. If there is something you interesting I’ll ask for an html explainer with code pointers and scan the code in parallel.

    I wouldn’t say “post reading code” but it’s definitely trending in that direction.

    I’d rather the agents put jumbo verbose descriptions in the PR description than in code comments TBH.

  - **cuddlyogre** ([comment](https://news.ycombinator.com/item?id=49336573#49337773), 2026-08-17 21:17:31 UTC)
    You forgot the smoke tests that passed.

    - **donkeyboy** ([comment](https://news.ycombinator.com/item?id=49336573#49339573), 2026-08-18 00:25:10 UTC)
      So many smoke tests in every PR i make with AI. Not that i mind, I just find that phrase funny.

  - **sebastiennight** ([comment](https://news.ycombinator.com/item?id=49336573#49337615), 2026-08-17 21:04:39 UTC)
    Am I the only one who's had Claude almost systematically *remove* human-written comments?

    It might be touching one line of actual code in a file, and take advantage of it to remove 20+ lines of actual useful comments.

    Everybody is talking about the opposite, so I'm wondering if this is rare.

    - **panopticon** ([comment](https://news.ycombinator.com/item?id=49336573#49338871), 2026-08-17 23:00:05 UTC)
      Is this in one of the skills or CLAUDE.md? This was happening in our codebase, but turned out it was interpreting an instruction to not add "what" comments as license to strip out comments.

      Sometimes I have luck interrogating Claude on why it did something. It'll either point to a skill or agent file with the culprit, or it'll respond with some vapid nonsense and apologize.

    - **MattGrommes** ([comment](https://news.ycombinator.com/item?id=49336573#49337853), 2026-08-17 21:24:53 UTC)
      I've definitely seen this. One of my least favorite parts of developing with AI is when I add print statements or small changes and the LLM removes them in the process of doing the next thing. I want to work _with_ the AI, not have it stomp all over my code.

      - **aaaronic** ([comment](https://news.ycombinator.com/item?id=49336573#49338381), 2026-08-17 22:12:48 UTC)
        Do you think it's actively deciding to remove them or just not noticing you added them and then overwriting?

        I ask because when I started informing it I made personal edits, it stopped doing this kind of thing so often and let me work _with_ it more.

        My saved prompt now says never to assume a file has not been edited since the last time it was read between prompts.

  - **broast** ([comment](https://news.ycombinator.com/item?id=49336573#49340951), 2026-08-18 03:36:22 UTC)
    Most ai output is meant for other ai's to read, in my experience. The humans job is to compress it for humans

  - **hrk5** ([comment](https://news.ycombinator.com/item?id=49336573#49340183), 2026-08-18 01:53:34 UTC)
    I think at this point all the info added by AI which certainly would be too much to read for every PR, it just serves the purpose of context for the next action. Which it could be good or bad depending on how big of a window of context you are working on

  - **seer** ([comment](https://news.ycombinator.com/item?id=49336573#49341059), 2026-08-18 03:52:13 UTC)
    Honestly, I’ve stopped caring about code readability for a few months now. I want the code readable _to the agent_ not so much to me.

    I don’t trust it with code anyway - every feature needs comprehensive test, and then a live deploy on a real working test system before it is approved - I mostly measure success with - after deployment is it doing what it’s supposed to be doing.
    It’s like “helping another team managing their work stream” experience rather than coding yourself.

    Funny enough models seem to have personalities and the dis on each other - when I had an opus orchestrator dispatching fable workers, they would comment on how “unreliable” it was and it had “evidence to prove it” and fable thinks opus is too rigid and needs more hand holding… it really starts to feel like managing team egos and verifying work.
    And I code scan mostly to just spot check if it’s not doing anything super stupid. But my goal is to make sure anything shipped is easy to change and fix, and every mistake has a test behind it so it doesn’t happen again.

    I ship more problems, but they get discovered and fixed quicker. Before they reach prod of course.
    And from time to time you do reorganisation and refactoring passes where I brainstorm how things could have been better with the help of evidence- chat sessions, tests, bugs etc.

    It feels less like rigorous engineering and more like gentle gardening. Or like “project management” not “coding”.

    Honestly given my age now I’m fine with that. Have enough “hard” projects under my belt (ORMs, sql parsers, etc) that I don’t feel I need to prove anything to anybody, but I don’t think that’s even relevant- the velocity change is … I guess around 5-10x for me - with provable metrics, so I try not to lent the good old days but figure out how I can now live in this brave new world and be happy with my work.

    - **hbcdbff** ([comment](https://news.ycombinator.com/item?id=49336573#49342497), 2026-08-18 07:25:22 UTC)
      > I’ve stopped caring about code readability for a few months now. […] I don’t trust it with code anyway

      If you don’t trust it with code, surely you need the code to be readable so you can understand what it is writing?

  - **CuriouslyC** ([comment](https://news.ycombinator.com/item?id=49336573#49340850), 2026-08-18 03:22:01 UTC)
    I'm looking forward to when AI labs focus more on conciseness of code and writing.

  - **EastSmith** ([comment](https://news.ycombinator.com/item?id=49336573#49337138), 2026-08-17 20:26:58 UTC)
    I dump AI output in PRs, because it ads context for the AI reviewer.

  - **apical_dendrite** ([comment](https://news.ycombinator.com/item?id=49336573#49340463), 2026-08-18 02:29:31 UTC)
    With one colleague, I was leaving PR comments and he would just put my feedback into the AI and paste its response. So I decided to cut out the middleman and now I just @cursor and tell it to trim unnecessarily long comments.

  - **the_af** ([comment](https://news.ycombinator.com/item?id=49336573#49340313), 2026-08-18 02:13:25 UTC)
    > *I don’t really know how to address this situation or if it needs addressed.*

    My worry is that after several passes this compounds and starts introducing errors or biases, a bit like in the "telephone game" children play.

  - **bitwize** ([comment](https://news.ycombinator.com/item?id=49336573#49342173), 2026-08-18 06:44:58 UTC)
    > My coworkers continue to dump hundreds of lines of AI documentation in every PR and every other line of code has between one and ten lines of AI generated comments, talking about the real unlock and how things are byte for byte identical on the load bearing path or how the acceptance ladder is misleading.

    They're just helping you understand the whole picture!

    > Features are coming out and metrics are improving, but we’re basically in a post readability code base, with the occasional performative comment about a variable name.

    You futilely grasp for control and it eludes you. The Way is to ride the tides of life, move with the forces that shape you. Your code base is in the hands of the Machines now.

  - **mawadev** ([comment](https://news.ycombinator.com/item?id=49336573#49337187), 2026-08-17 20:30:16 UTC)
    Just wait until you see vibe contracts, vibe requirements and vibe legal documents

    - **RealityVoid** ([comment](https://news.ycombinator.com/item?id=49336573#49340994), 2026-08-18 03:42:34 UTC)
      I'm... Actually fine with that. In one direction. I use AI to fill in forma and usually it has really good pointers. I do not trust it to do it itself, but it does simplify things quite a bit.

  - **fnord77** ([comment](https://news.ycombinator.com/item?id=49336573#49340808), 2026-08-18 03:13:56 UTC)
    I always as for CONCISE documentation.

    still get walls of text sometimes

  - **Bombthecat** ([comment](https://news.ycombinator.com/item?id=49336573#49342555), 2026-08-18 07:30:44 UTC)
    You use AI to summarise it! That's the way to go lol

  - **moltar** ([comment](https://news.ycombinator.com/item?id=49336573#49337155), 2026-08-17 20:27:58 UTC)
    I address it with AI.

    Write REVIEW.md.

    I have CC check itself pretty well.

    I also put into agent/claude/review instructions to write using simple English skill and humanizer skill. Then not to write redundant comments.

    It’s not perfect but definitely catches lots of slop.

    - **rfgplk** ([comment](https://news.ycombinator.com/item?id=49336573#49337338), 2026-08-17 20:42:13 UTC)
      It's actually insanely difficult to get LLMs not to produce comments. Even with explicit "NEVER LEAVE ANY COMMENTS WHATSOEVER", they still do, across basically all providers.

      - **atombender** ([comment](https://news.ycombinator.com/item?id=49336573#49339226), 2026-08-17 23:43:26 UTC)
        No problems with GPT-5.6 Sol here. I have an agent file that says, among other things, only to document purpose and intent, not just what the code does, and not write obvious comments. It's been so effective that it often doesn't comment anything at all, including some stuff that's so niche that it must be explained carefully. As a result, I've had to pull back a bit and tell it explicitly which areas to actually add comments for.

  - **golergka** ([comment](https://news.ycombinator.com/item?id=49336573#49337387), 2026-08-17 20:45:38 UTC)
    > perhaps it’s useful for the AI on its next pass

    Yes, that's the entire point. And it is extremely useful. Why wouldn't I want this?

    - **minus7** ([comment](https://news.ycombinator.com/item?id=49336573#49337986), 2026-08-17 21:35:12 UTC)
      Is it really, or do you just think so and it could actually mislead you and your LLM the next time? In my experience, the information in the comments tends to be quite redundant, often even with other comments in the same file

      - **plmpsu** ([comment](https://news.ycombinator.com/item?id=49336573#49340733), 2026-08-18 03:00:40 UTC)
        Often even wrong.

- **afr0ck** ([comment](https://news.ycombinator.com/item?id=49336573#49337297), 2026-08-17 20:38:11 UTC)
  I think the main reason many people (including me), very often, lack the motivation to read content that is likely generated by AI is the suspicion that it comes from a place of intellectual laziness. Another reason, based on personal experience, is that AI content may suffer from too much verbosity, too much jargon and over-confidence, which makes the reading experience feel fake and border-line irritating. In many cases the content may have very little to no nuance, which is ultimately a waste of time.
  As an anecdote, someone posted a blogpost on Linkedin on using agents to implement a driver to access PCIe devices over TCP/IP. I was intrigued because that's not an easy task for several reasons, like handling PCIe interrupts and DMA. For exmaple, how does the remote machine map the device's PCIe BARs? And when it issues I/O to the devices registers, how are these reads and writes transferred to the remote device. In the end, this is just some virtual memory. In a local machine, this is either directly mapped to the PCIe physical addresses or some IOMMU virtual address space which is then translated by the hardware upon CPU/device/VM access.

  After reading the long verbose promising article, in the end, the guy (with the help of the agent) only managed to implement access to the PCIe config space so that lspci on the remote machine works and shows the remote PCIe device, but that's all. It never addressed the issues above nor even mentioned them. The code was AI generated. The article was AI-written. The article never made a reference to DMA, interrupts, MSIX-X, IOMMU, IOTLB, virtual memory, etc, but it made big claims on next-gen datacenter disaggregated architecture, boosting GPU utilization, reducing large scale inference costs, etc.

  Anyway, you get my point: big long beautiful words, but zero nuance.

  - **Ekaros** ([comment](https://news.ycombinator.com/item?id=49336573#49342057), 2026-08-18 06:27:34 UTC)
    It is extremely annoying when you have a certain problem that surely should have someone making a solution for it and then you find a blog post. And in the end blog post doesn't actually solve the issue as it does has final step. But actually never implemented the most important middle bits. Thankfully I found someone who had actually solved that middle bit in workable hack. But still those blogs are really annoying pollution.

  - **hinkley** ([comment](https://news.ycombinator.com/item?id=49336573#49339736), 2026-08-18 00:47:54 UTC)
    My question is always, "Am I willing to maintain this code?"

    Sometimes that's a yes, even if AI generated it and I can tell despite someone making half an effort to be a human for a minute during the PR process. But sometimes it's not.

    It gets really dicey when you've kept an architecture a certain shape because there's a difficult feature you intend to slot into the negative space. There are two or three ways to implement that feature, and the one they chose just stomps all through your potential. But that's why we have code reviews. You don't have to read my mind if I just tell you. But it can be frustrating if someone asks you to do it a different way, and then has comments on how you accomplished that, and then comments on the fixes for your other comments.

- **hypertexthero** ([comment](https://news.ycombinator.com/item?id=49336573#49344303), 2026-08-18 11:49:52 UTC)
  > If, however, prose is LLM-generated, this social contract becomes ripped up: a reader cannot assume that the writer understands their ideas because they might not so much have read the product of the LLM that they tasked to write it. If one is lucky, these are LLM hallucinations: obviously wrong and quickly discarded. If one is unlucky, however, it will be a kind of LLM-induced cognitive dissonance: a puzzle in which pieces don’t fit because there is in fact no puzzle at all. This can leave a reader frustrated: why should they spend more time reading prose than the writer spent writing it?

  > This can be navigated, of course, but it is truly perilous: our writing is an important vessel for building trust — and that trust can be quickly eroded if we are not speaking with our own voice.

  From [https://rfd.shared.oxide.computer/rfd/0576#_llms_as_writers](https://rfd.shared.oxide.computer/rfd/0576#_llms_as_writers)

  Be careful not to [give up your own voice][1] to the [machine][2].

  [1]: [https://bookshop.org/p/books/you-are-not-a-gadget-jaron-lani...](https://bookshop.org/p/books/you-are-not-a-gadget-jaron-lanier/45705114ad835402)

  [2]: [https://www.youtube.com/watch?v=Jh20cMEgvqc](https://www.youtube.com/watch?v=Jh20cMEgvqc)

- **gortok** ([comment](https://news.ycombinator.com/item?id=49336573#49336966), 2026-08-17 20:16:25 UTC)
  The part that astonishes me is that in the year of our common era two thousand twenty-six that it's not universally offensive and reviling to post an AI-generated response to another person.

  If I'm reading something on the internet, I'm either reading it to learn, or I'm reading it to be persuaded.  If I wanted the LLM to teach me (thank you, no), I would ask an LLM.  I'm reading your website/newsletter/email because *I want to hear from you.*. If you can't be bothered to put your time into writing it and teaching me what you think, why should I be bothered to read it?

  - **Insimwytim** ([comment](https://news.ycombinator.com/item?id=49336573#49338279), 2026-08-17 22:00:35 UTC)
    I think there are some, who couldn't be a part of the public conversation, precisely because of they inability to add anything to said conversation.

    LLMs enables them to post (or, rather, paste) something, in an attempt to trick others into believing they do have something to say.

    They think they sound smart now, because LLMs are "very much the “stupid person’s idea of an intelligent person”"[1]

    So now we are flooded with stupid people's attempts to show us how smart they are.

    [1] [https://news.ycombinator.com/item?id=49300763](https://news.ycombinator.com/item?id=49300763)

    - **yoyohello13** ([comment](https://news.ycombinator.com/item?id=49336573#49338557), 2026-08-17 22:29:59 UTC)
      Wow! that comment you linked speaks to me. I was watching a review video for a game yesterday that was so obviously written by AI it was actually painful to listen to. I started reading the comments and there were several people praising this Youtuber on their great use of metaphor. Literally "subbed because you're such an amazing writer." It actually shook me to my core. If those were real people making those comments, there is no hope for us. I need to believe those were mostly bot comments just to maintain my sanity.

      - **kennyadam** ([comment](https://news.ycombinator.com/item?id=49336573#49338954), 2026-08-17 23:10:26 UTC)
        At least you didn’t over-react. Some people seem so afraid of consuming AI-generated content that they see it everywhere. A popular YouTuber says “thanks for the pushback” in a YouTube video and has the mob at his door, instantly, despite it not being written by AI. In the comments for any blog post or article that hits the HN front page, there is always someone confidently calling it out for being unmistakeably written by Claude. It’s so tiring. Let’s say the YouTube video that rocked the very foundation of your being was scripted with AI assistance. It was apparently good enough for people to praise it specifically. Why is that a problem? If it wasn’t AI, which may well be the case, would your soul be calmed?

        - **DennisP** ([comment](https://news.ycombinator.com/item?id=49336573#49339441), 2026-08-18 00:07:32 UTC)
          What I find tiring: the same. writing. style. everywhere.

          Various youtubers I subscribe to are using apparently AI-written scripts now. They all wrote and spoke just fine before, each with their own particular style. Now they just sound like Claude. I know it's still their thoughts, and I'm still interested in what they have to say. Maybe they're using AI to save time, or maybe they've read too much AI text and now that's how they write. But it kinda takes the sparkle and personality out of everything.

        - **account42** ([comment](https://news.ycombinator.com/item?id=49336573#49344040), 2026-08-18 11:18:50 UTC)
          What's tiring is being spammed with AI slop every where. A strong counter reaction that may occasionally have false positives is only natural.

        - **johnnyanmac** ([comment](https://news.ycombinator.com/item?id=49336573#49341968), 2026-08-18 06:16:32 UTC)
          >A popular YouTuber says “thanks for the pushback” in a YouTube video and has the mob at his door, instantly, despite it not being written by AI.

          In this era, I live by two principles

          1. Do my best to avoid AI slop. If you agree, this is straightforward. I don't always succeed and I'm sure I've "fallen for it" in quite a few places, but I disengage if I sense it.

          2. Let sleeping dogs lie. Because I'm not some almighty judge of AI, I'm not going around accusing others of doing so. There is zero benefit for me to call out random internet pieces on if something is AI. And ultimately, I'm in discussions to engage with humans, not to monitor bots nor even to argue about the existence of bots (I feel I've said all I can on the topic, I have moved on internally in terms of discussion).

          >It was apparently good enough for people to praise it specifically. Why is that a problem?

          Writing is subjective, but I can certainly see some dangerous anti-patterns develop if you take bad advice as a beginner, especially advice that ultimately came from hallucinations in an LLM.

          I was watching a Youtube video about "developing taste" and how culture has been impacted in the modern age. TYou risk becoming "tasteless" consuming AI slop, because AI by its nature is trying to average out all the inputs and cut of all the edges of any given culture. That's not necessarily a bad thing if you just wanted to get a brief overview of a culture, but is poison if it comes time to try and become part of that culture.

          as a huge summation of an interesting video: There's 3 aspects of a culture: embodied,objectified, and institutionalized. it's never been easier to pretend to be a "poser" in this era of AI and be rewarded for it, because AI makes objectified easier than ever. But it doesn't mean it truly embodies you into the culture. And that's dangerous for multiple reasons (in my eyes).

      - **urbnspacecowboy** ([comment](https://news.ycombinator.com/item?id=49336573#49339447), 2026-08-18 00:08:23 UTC)
        > If those were real people making those comments

        Really, does it matter? Lots of YouTube comments are zero-effort attempts to juice a video/channel's engagement metrics (aka "commenting for the algorithm"), and whether they're accomplices/sockpuppets, or just unimaginative parasocial parasites, is basically unknowable from the outside.

      - **zombot** ([comment](https://news.ycombinator.com/item?id=49336573#49342860), 2026-08-18 08:13:11 UTC)
        LLMs output the average of their training data. On average, people are tasteless and clueless. So it's to be expected that average and especially below-average people find LLM output appealing. Or the tasteless work of an average person.

      - **CuriouslyC** ([comment](https://news.ycombinator.com/item?id=49336573#49340888), 2026-08-18 03:27:46 UTC)
        You realize that when people aren't told an image or text is AI generated, on average they prefer it to human created content, and it's only when they know it's AI that they rate it lower than the human content? You shouldn't be shocked by this, the last 20 years of Hollywood and pop music clearly indicates the the mass market doesn't care about craft or art, it likes to ride the vibes of what's trending.

        - **customguy** ([comment](https://news.ycombinator.com/item?id=49336573#49341600), 2026-08-18 05:25:30 UTC)
          Yeah, and you might enjoy a meal, and when someone tells you it contained 5 percent human eyeballs to give the sauce that awesome texture, and you know they're not lying, you will puke it out right on the spot.

          Then you say "it's because I don't like human eyeballs in my food", and someone and replies "but the mass market clearly doesn't care. You shouldn't be shocked by this."

      - **tessierashpool** ([comment](https://news.ycombinator.com/item?id=49336573#49339207), 2026-08-17 23:40:37 UTC)
        > If those were real people making those comments, there is no hope for us.

        they probably weren't.

    - **notahacker** ([comment](https://news.ycombinator.com/item?id=49336573#49338432), 2026-08-17 22:18:25 UTC)
      I believe you've just described 95% of things posted to LinkedIn...

      - **Quekid5** ([comment](https://news.ycombinator.com/item?id=49336573#49338511), 2026-08-17 22:25:07 UTC)
        LinkedIn was overtaken by LLM nonsense at about the release of ChatGPT 3... I mean it was incredibly stupid and transparent engagement slop before that, but still.

        I remember talking to a business type who was so incredibly proud that GPT could turn his incredibly vapid thoughts into bland pointlessness on LinkedIn... not realizing that everyone in *his* feed was doing the same thing. We never did business with him for ... reasons, obviously :)

    - **jdidjsjdjw** ([comment](https://news.ycombinator.com/item?id=49336573#49339639), 2026-08-18 00:34:50 UTC)
      > So now we are flooded with stupid people's attempts to show us how smart they are.

      *Now*? My friend, we’ve been flooded with stupid people’s attempts to show us how smart they are ever since internet forums came to be. Heck, just look at 90% of the comments on any given HN post. It’s mind-numbingly stupidity by the handful disguised as PhD talk—big words, fancy terms, heavy phrasing, all to say a bunch of nothing or just pretend they have a part in said conversation.

  - **BeetleB** ([comment](https://news.ycombinator.com/item?id=49336573#49337471), 2026-08-17 20:51:41 UTC)
    > The part that astonishes me is that in the year of our common era two thousand twenty-six that it's not universally offensive and reviling to post an AI-generated response to another person.

    Because it wasn't pre-AI. It was normal for people to post links as arguments, counterarguments, etc. It annoyed me, and I didn't bother clicking most of them, and would occasionally tell them "If you can't bother articulating your thoughts, I can't be bothered with that link".

    But I was always in the minority. If that behavior is acceptable to the masses, so is AI generated content.

    (And, BTW, the "link as argument" bugs me a lot more than AI responses. If I know the person, I can assume the person has done some due diligence in reviewing the AI response before sending it to me.)

    > If I wanted the LLM to teach me (thank you, no), I would ask an LLM. I'm reading your website/newsletter/email because I want to hear from you.

    To play the devil's advocate: it's far from a given that had you asked the LLM it would have given you a comparable response to the one you got. You're precluding the possibility that the other party instructed the LLM to write what he intended to say.

    - **sebastiennight** ([comment](https://news.ycombinator.com/item?id=49336573#49337843), 2026-08-17 21:23:29 UTC)
      I would have said the opposite: I'd assume the link to be to a blog post, or Wikipedia page, that articulates the idea in a clearer more succint way than the person might be able of.

      This is, of course, before people started sending Instagram Reel or YouTube Short links. Or, maybe worse, links to 3-hour-long YouTube podcasts.

      - **BeetleB** ([comment](https://news.ycombinator.com/item?id=49336573#49338066), 2026-08-17 21:42:03 UTC)
        > I'd assume the link to be to a blog post, or Wikipedia page, that articulates the idea in a clearer more succint way than the person might be able of.

        As with everything, it depends on who is sending it. For some people, yes. For the rest (majority), it's a case of

        He: Makes some claim

        Me: I question some aspect of it.

        ... Potential back and forth

        He: Oh, just look at this video/article/book that explains and answers all your concerns.

        Thing is, in the majority of the cases, it *didn't* address my concern. I'd write up something in detail, and get back either silence or yet another link. Took way too long for me to realize I shouldn't bother clicking the link to begin with.

        - **robocat** ([comment](https://news.ycombinator.com/item?id=49336573#49340320), 2026-08-18 02:15:07 UTC)
          You are just collateral damage.

          Too many people put up a lazy comment when it is clear they haven't thought about $it, googled $it, or asked AI about $it. Where $it == {whatever they are unsure about or arguing about}.

          The lazy commenter desires a human to waste their time writing a response. Often others judge that the commenter doesn't deserve the time or effort, so instead  of a thoughtful response others often just reply with a relevant link - giving the commenter a chance to learn or reply.

          Unfortunately offhand responses like LMGTFY become a common behaviour in forums, even when wildly inappropriate (as you note).

          When it happens to you, it isn't personal, you are just a victim because everyone has been trained to a pattern of behaviour by thoughtless commenters.

          It is also likely your comments get pattern matched as not worthwhile reasoning clearly to. You can do something to change your writing to avoid appearing waffly/bullshitty/unworthy (or whatever the reason responders are not replying to the meat of your point). Here's where I've done that pattern match in the past although usually spent time writing reply too: [https://hn.algolia.com/?query=by%3Arobocat%20duckduckgo&sort...](https://hn.algolia.com/?query=by%3Arobocat%20duckduckgo&sort=byDate&type=comment)

          See also: [https://meta.stackexchange.com/questions/19665/the-help-vamp...](https://meta.stackexchange.com/questions/19665/the-help-vampire-problem)

          Sorry in advance if I've misunderstood your point or if I'm being Captain Obvious.

          - **BeetleB** ([comment](https://news.ycombinator.com/item?id=49336573#49340406), 2026-08-18 02:24:08 UTC)
            You're totally on point, but I do think you're missing my wider point:

            People replying with LLM responses is not really functionally different from lazily responding with a link. If the OP is astounded that LLM responses are tolerated, where was he all those years when people were lazily responding with links?

            - **robocat** ([comment](https://news.ycombinator.com/item?id=49336573#49340608), 2026-08-18 02:47:05 UTC)
              I am likely agreeing with you: but perhaps I just failed to follow what you were trying to say.

              Perhaps it is a wider problem of "flipping the bozo bit", that someone perceives they are being treated as worthless (or worse) and then they respond similarly?

              A considered AI response can be good if quoted correctly. Unfortunately I've seen a lot of AI-hate, where even fantastic AI answers (carefully vetted/curated) are shot down.

      - **aliasxneo** ([comment](https://news.ycombinator.com/item?id=49336573#49338089), 2026-08-17 21:43:39 UTC)
        Eh, but it can become just as low-effort as AI slop. I've participated in a number of conversations here where it appears the person I was interacting with (this was pre-AI) was just googling off some keywords and pasting links with one or two sentences attached. Even in cases where they legitimately read the thing they posted, the static nature of the link leaves no room for actually responding to any nuance I might have added (i.e. the author missed something critical).

        After a few years of this I also just stopped clicking thinks and refused to engage in conversations that seemed to be going that direction.

        - **BeetleB** ([comment](https://news.ycombinator.com/item?id=49336573#49338169), 2026-08-17 21:50:53 UTC)
          Yes - I would think this is obvious to HN commenters. Generally, when someone leaves a comment on HN that is nothing but a link, it gets downvoted.

    - **erikschoster** ([comment](https://news.ycombinator.com/item?id=49336573#49337980), 2026-08-17 21:34:29 UTC)
      I think you're right, and we've been training ourselves for the shortest path of least resistance for quite a while while kidding ourselves that we're able to somehow preserve the result as worthwhile. Before I ever tried using LLMs for search I had already been training myself for years to offload my thinking to a quick web search and a skim of some plausible result served up.

      Arguably things like Cliff's Notes and "for dummies" books were sating this impulse before that, I wouldn't be surprised if the line can be traced back further.

      Since dropping LLMs altogether I've made the connection to the impulse for a superficial jump to the conclusion just by noticing how I use web search, or feverishly scan some text to get to the point.

      Theoretically I studied critical thinking and have learned decades ago how to recognize when this is OK and when it's a superficial placation of some addiction to closing the book on a subject or micro-subject... but boy whatever good instincts I might have developed back then have significantly eroded over time. Trying to reclaim that again is pretty humbling.

    - **thatjoeoverthr** ([comment](https://news.ycombinator.com/item?id=49336573#49337934), 2026-08-17 21:31:32 UTC)
      "Because it wasn't ..."

      Not so. Posting links is not the same. If you were to copy+paste someone's blog post into the forum and post is as your own, without attribution, it would be seen as plagiarism. Everyone understands this; you're trying to pass another's work as your own.

      On X there's actually a good modern equivalent to "posting links" which is @grok, and letting Grok add to the thread. There is occasional teasing but it's nothing like posting slop under your own name.

      ChatGPT actually allows something like this; you can share a link to the conversation.

      Everyone is free to do this, instead of using ChatGPT as a ghostwriter.

      - **BeetleB** ([comment](https://news.ycombinator.com/item?id=49336573#49338110), 2026-08-17 21:45:14 UTC)
        So I take it you'll be fine with responses that begin with:

        "ChatGPT says ... "?

        > Everyone is free to do this, instead of using ChatGPT as a ghostwriter.

        I guess the bulk of folks use ChatGPT as the preferred chatbot, but people like me have a completely different interface that doesn't use ChatGPT. I can't send someone links to my conversation.

        (And as an aside, over 80% of ChatGPT conversation links I click on don't work - not sure if they clean them after some time, or I need to be logged in, etc).

        And even if it did work, I really don't want to read the whole conversation. Just send me the relevant part that ChatGPT said!

        - **thatjoeoverthr** ([comment](https://news.ycombinator.com/item?id=49336573#49338240), 2026-08-17 21:55:52 UTC)
          "ChatGPT says" can be annoying but it's unequivocally better than passing ChatGPT off as yourself. Quoting it for convenience ("the relevant part") --- ok, great.

          Does it look lazy? Well, if you respond _as its sockpuppet_ you look like a hustler, too.

    - **watwut** ([comment](https://news.ycombinator.com/item?id=49336573#49337831), 2026-08-17 21:21:59 UTC)
      >  If that behavior is acceptable to the masses, so is AI generated content.

      No, linking blog post and posting AI generated content is not the same. One is ok, other is not.

      - **BeetleB** ([comment](https://news.ycombinator.com/item?id=49336573#49338123), 2026-08-17 21:46:30 UTC)
        > No, linking blog post and posting AI generated content is not the same. One is ok, other is not.

        Meet "the masses".

        Sorry, but no. Sending me a link as an alternative to having a conversation is totally not OK.

        - **watwut** ([comment](https://news.ycombinator.com/item?id=49336573#49343733), 2026-08-18 10:41:21 UTC)
          I recommend this great book, blog or whatever is completely fine in the middle of the conversation.

          And it is not the same as "I had AI generate this".

    - **b112** ([comment](https://news.ycombinator.com/item?id=49336573#49338187), 2026-08-17 21:51:58 UTC)
      *You're precluding the possibility that the other party instructed the LLM to write what he intended to say.*

      That is not currently possible.  At best, you could train on millions of personal examples of style, eg historical emails, reports, etc, and you'd still never get what the person would have written.

      I'd be astonished if an LLM didn't even miss important nuance, data, and focus on the wrong point.

      It think the parent's point was, hearing a summary of what someone was thinking, from a second party isn't interesting as data from the primary source.

      When you come to listen to Bob the Great, having a minion walk put and paraphrase Bob's words isnt the same.  Human, LLM, or not.

      - **preg_match** ([comment](https://news.ycombinator.com/item?id=49336573#49339907), 2026-08-18 01:14:27 UTC)
        I will use LLMs to find spelling and grammar mistakes, as well as voice inconsistencies. I then carefully review the diff.

        Yes there are deterministic tools for this, but grammar is actually kind of complicated and the tools either miss mistakes, or suggest obviously worse edits. Looking at you, Microsoft Word.

        All the writing is my own and I read all of it. Naturally there’s no LLM-isms because I wrote 99.9% of the original text. But, it was AI assisted. So, I don’t think it’s cut and dry.

        - **BeetleB** ([comment](https://news.ycombinator.com/item?id=49336573#49340419), 2026-08-18 02:25:08 UTC)
          Many do as you, and I completely endorse this usage. Unfortunately, too many of us here make the giant leap of "If it went through the LLM, the original person was too lazy."

          - **b112** ([comment](https://news.ycombinator.com/item?id=49336573#49344503), 2026-08-18 12:08:08 UTC)
            Of course, the start of the thread really had nothing to do with the concept you're espousing here.  At all.  It was more about "Some guy writes instructions into an LLM, and gets a blog entry", which is entirely on a different scale.  And yes, that's the scope and scale we've been discussing.

            Personally, in this new, different context you've stated, I don't think many have an issue with that.  If you write 6 pages of text, and then ask an LLM to look for errors, that's not remotely the same, and it is more like a spell checker, or a second set of eyes.

      - **BeetleB** ([comment](https://news.ycombinator.com/item?id=49336573#49338259), 2026-08-17 21:58:14 UTC)
        > At best, you could train on millions of personal examples of style, eg historical emails, reports, etc, and you'd still never get what the person would have written.

        You wouldn't get it verbatim, but your mistrust in AI reflecting what you intended to say is unwarranted.

        I use LLMs to clean up poorly OCR'd hand written notes. It's the exception where I need to "fix" its output. It figures out what the notes intended, and writes it up fairly well.

        > It think the parent's point was, hearing a summary of what someone was thinking, from a second party isn't interesting as data from the primary source.

        For a lot (most?) of AI slop, I agree. But pre-LLMs, this was universally a bad idea. The first draft always sucked, and was easy to misunderstand. A good LLM, with a good system prompt, will usually produce something better than the input it is fed. Most people are poor at expressing their thoughts.

        > When you come to listen to Bob the Great, having a minion walk put and paraphrase Bob's words isnt the same. Human, LLM, or not.

        Most people aren't Bob The Great, but Bob The Incoherent.

  - **fluidcruft** ([comment](https://news.ycombinator.com/item?id=49336573#49337041), 2026-08-17 20:20:54 UTC)
    It's like when you type a search in Google and get a wall of SEO spam.

    I do feel like there is some middle ground where AI helps, but there's this one guy who keeps emailing everyone with walls of dumbass text and does not integrate or understand the feedback he gets when we are telling him what he needs to do. He just runs it though the LLM and replies and then forgets half of it in the next email engagement which functions as /clear on his end apparently. Like... dude I have ChatGPT and Claude, too. Actually read your goddamn emails.

    - **paimapi** ([comment](https://news.ycombinator.com/item?id=49336573#49337275), 2026-08-17 20:36:33 UTC)
      I was going to say, the acceptance of bottom-of-the-barrel and subsequent capital investment in SEO as some industry-standard practice has pretty much lowered our standards for writing and comprehensibility across the board

      it probably doesn't help that the US education system is so deeply broken with how rooted it is in segregation-era practices [0][1][2]. the average gets dragged down quite a bit when some districts receive so much money that they're flying their Spell Bowl teams to nationals and putting them up in hotels while another one a few miles away can't afford to pay for textbooks. average reading levels suffer and consequently so too does the effort that people put into writing well and reading critically

      [0] [https://www.shankerinstitute.org/segfunding](https://www.shankerinstitute.org/segfunding)

      [1] [https://www.jchs.harvard.edu/research-areas/working-papers/s...](https://www.jchs.harvard.edu/research-areas/working-papers/shared-future-interdependence-housing-and-school-segregation)

      [2] [https://edlawcenter.org/research/the-color-of-opportunity/](https://edlawcenter.org/research/the-color-of-opportunity/)

  - **venzaspa** ([comment](https://news.ycombinator.com/item?id=49336573#49337291), 2026-08-17 20:37:46 UTC)
    People are posting on this very website and commenting on Reddit using AI. I can't get myself into the headspace that would enable this behaviour. What exactly is the point of not engaging in conversation yourself and getting a bot to post it for you on an free platform. Crazy.

    - **otterley** ([comment](https://news.ycombinator.com/item?id=49336573#49337372), 2026-08-17 20:44:32 UTC)
      The HN Guidelines explicitly forbid posting AI-generated comments; they will be deleted if detected or reported.

      I'd like them to go further and delete links to AI-generated content, but I haven't been able to persuade management to do that yet.

      - **miyoji** ([comment](https://news.ycombinator.com/item?id=49336573#49337679), 2026-08-17 21:09:25 UTC)
        The HN guidelines prohibit a lot of behaviors that remain unmoderated, you can see it in any thread that goes over 80 comments.

        - **Barbing** ([comment](https://news.ycombinator.com/item?id=49336573#49338239), 2026-08-17 21:55:51 UTC)
          Community mostly keeps us in check though.

          (Sharing next sentence for the newbies, since you know-) All our jobs to flag on site & even email the worst offenders to hn@ycombinator.com . That said I rarely flag or even downvote anything. People either really behave, or perhaps the rulebreakers break rules that don’t grind my gears. Politely admonishing good faith rulebreakers is another tactic in the arsenal.

          AI-generated comment posters with comment histories of exclusively slop get email alerts from me. Don’t know whether they’re planning to sell or spam but they clearly need help finding the door :)

        - **nick__m** ([comment](https://news.ycombinator.com/item?id=49336573#49338152), 2026-08-17 21:49:18 UTC)
          If those behaviors bothers you enough you can always mail hn@ycombinator.com because dang is not omniscient even if sometimes it looks like he is...

          - **HDBaseT** ([comment](https://news.ycombinator.com/item?id=49336573#49338469), 2026-08-17 22:21:33 UTC)
            How many active moderators are there? This site has a lot of comments, far too many for one person to read.

        - **ThrowawayR2** ([comment](https://news.ycombinator.com/item?id=49336573#49339418), 2026-08-18 00:04:42 UTC)
          HN relies heavily on moderation by users through flagging and downvotes.  Hacker News is only going to survive if its community is willing to go to the effort to protect it.

    - **plorg** ([comment](https://news.ycombinator.com/item?id=49336573#49337517), 2026-08-17 20:55:43 UTC)
      I get the sense that people who spend all day interacting with software can start to see every interaction, especially in online text platforms, as a kind of API or user interface. You might learn to instrumentalize your interactions and relationships with people. Chatbots, including coding agents, only reinforce this kind of behavior, as they don't have the kind of limits of patience or of bodily or emotional needs that humans have.

    - **cheschire** ([comment](https://news.ycombinator.com/item?id=49336573#49337315), 2026-08-17 20:40:12 UTC)
      What drives people to cheat at competitive games? I imagine it’s the same genes.

      - **mister_mort** ([comment](https://news.ycombinator.com/item?id=49336573#49341121), 2026-08-18 04:05:11 UTC)
        Some people have an inner drive like a rat that likes pushing the reward button in the cell to dose them with opium. They want to see the YOU WIN screen and *absolutely do not care what it takes to get them there*. Hence the booming market for custom memory modding cheat devices and subscription cheat services. They don't want to improve their skills, they just want to be number one on the board.

      - **xdennis** ([comment](https://news.ycombinator.com/item?id=49336573#49339078), 2026-08-17 23:26:48 UTC)
        As a previous massive cheater in RPG games (when a was young and it was easy to write your own tools) the reason to cheat is because many games (especially RPGs) have bullshit mechanics. You have to perform a lot of repetitive stuff to get ahead. Cheating is seen as honorable because it's about getting back at a system which forces you into unfair circumstances (this is akin to corruption/graft in real life).

        In my opinion, this is not the same as people who use AI comment bots.

        Of course, other cheaters had other reasons, but the few I was friends with had similar motivations. (Actually, a few just created tools because they enjoyed creating tools, not so much actually using them.)

        - **account42** ([comment](https://news.ycombinator.com/item?id=49336573#49344138), 2026-08-18 11:30:16 UTC)
          Do you mean MMORPGs or single-player RPGs. Because modifying a game or game state to your likes with the goal of improving your personal enjoyment of the game is very different compared to cheating to get ahead of other people.

      - **rockinghigh** ([comment](https://news.ycombinator.com/item?id=49336573#49337529), 2026-08-17 20:57:44 UTC)
        Using tools to fix your writing style or grammar is not exactly cheating.

        - **brandon272** ([comment](https://news.ycombinator.com/item?id=49336573#49338460), 2026-08-17 22:20:57 UTC)
          This implies that writing styles are simply "correct" or "incorrect". I'd prefer to read someone's natural writing style, even if they do not consider themselves a good writer, because it comes from them genuinely. Much better than enduring text that has been fed into an LLM and homogenized.

        - **jackjeff** ([comment](https://news.ycombinator.com/item?id=49336573#49337807), 2026-08-17 21:20:22 UTC)
          There’s a world of difference between using AI as an editor vs letting it write a whole essay for you. AI;DR is about the latter.

          - **thatjoeoverthr** ([comment](https://news.ycombinator.com/item?id=49336573#49338033), 2026-08-17 21:39:28 UTC)
            I'll push back and say it's the former. Good business writing is all about the editing, and autoregressive LLMs are terrible editors. They roll dice on every word and put the same tics on every text. They meander.

            Suppose you check something with ChatGPT, get nine hundred words, edit that down to three or even one and send that. You won't get AI;DR for "I checked, we're good."

            - **johnnyanmac** ([comment](https://news.ycombinator.com/item?id=49336573#49342156), 2026-08-18 06:41:52 UTC)
              >Suppose you check something with ChatGPT, get nine hundred words, edit that down to three or even one and send that. You won't get AI;DR for "I checked, we're good."

              Maybe. The issue here is we know most people are simply posting 900 words wholesale, maybe editing down 20-30 words to try and sweep some dust under the rug (meanwhile the trash is still fully featured on top of the carpet).

              For your style: I'm not a writer but I question if it's even more efficient to edit 900 AI words down to 100. I can see some people finding it easier to change other's words than generate your own ideas, but I don't think it's a majority.  I certainly know it's more annoying to edit 900 lines of AI code into a succinct 100 line function/class.

          - **teo_zero** ([comment](https://news.ycombinator.com/item?id=49336573#49342039), 2026-08-18 06:25:05 UTC)
            > using AI as an editor vs letting it write a whole essay for you. AI;DR is about the latter

            I'm sure that's the intention, but the alarming trend, at least here on HN, is crying wolf at the first em-dash.

            - **account42** ([comment](https://news.ycombinator.com/item?id=49336573#49344144), 2026-08-18 11:32:14 UTC)
              Why is that alarming? Your immune system will also do some small amount of collateral damage to your own cells when its in a heightened state.

    - **strbean** ([comment](https://news.ycombinator.com/item?id=49336573#49337992), 2026-08-17 21:35:46 UTC)
      I've seen it used as a newer evolution of trolling on Reddit. A user hops in to a somewhat nuanced discussion and gives a very curt and rude contradiction, and then just uses an LLM to generate walls of argumentative text after you respond with "What are you talking about and why are you being such a dick?"

      Very low effort the ensnare someone and waste their time for a bit, even though it is pretty quickly obvious what they are doing.

    - **asadotzler** ([comment](https://news.ycombinator.com/item?id=49336573#49339355), 2026-08-17 23:57:53 UTC)
      Attention is all they need. It's ego-tripping, whoring for social status.

    - **tayo42** ([comment](https://news.ycombinator.com/item?id=49336573#49337924), 2026-08-17 21:31:12 UTC)
      Everyone can use the Internet. Some people are just crazy, neurodivergent or whatever.

  - **sobellian** ([comment](https://news.ycombinator.com/item?id=49336573#49337905), 2026-08-17 21:29:38 UTC)
    A few thoughts.

    - I'm open to seeing information from an AI (I'm fine with an LLM "teaching me") so long as it is high quality. That does require human inspection.

    - I've seen a related bit about AI-written emails where the commenter would rather see the prompt. I agree. As a software engineer, I like reproducibility. If an AI outputs an interesting result, show me the "source" (i.e. the model, effort, prompt, etc.). I wouldn't say no to an added one-liner summarizing a long response.

    - In the end this will be a difficult attitude to prosecute as it boils down to a Chinese-room-style preference. You want to hear from some being on the other end of a labyrinth of transmission lines and logic gates. As language models continue to develop, what goes on inside the room will be difficult to verify.

    - The day may come where, rather than people passing AI off as their own thought, they will pass off their own thought as AI. "If I wanted a human to teach me (thank you, no), I would ask a human." The coming generations may value AI's opinion much more highly, whether that's right or not. And people may want to usurp that credibility for themselves.

    - **dhorthy** ([comment](https://news.ycombinator.com/item?id=49336573#49340007), 2026-08-18 01:28:07 UTC)
      > AI-written emails where the commenter would rather see the prompt

      this a thousand times this

      LLMs are information transformers. if you're trying to take some rough idea and blow it out into something that "feels" substantive, you're just combining your high-signal idea / prompt with a bunch of meaningless bloat and noise from the model weights.

  - **freetime2** ([comment](https://news.ycombinator.com/item?id=49336573#49339365), 2026-08-17 23:59:30 UTC)
    What's astonishing to me is how quickly people at my workplace have adopted this habit. Six months ago my manager was vociferously complaining about his boss asking him to review a lengthy document that was clearly AI generated, saying that his boss wasn't even capable of understanding the document the LLM had created. Now the majority of technical communication I get from my manager is just a transcript exported directly from ChatGPT.

    Recently on a call with a junior coworker where they asked me to look at some changes they had made, they were completely unable to answer any questions that I asked on their own. The way the conversation went was: I ask a question, they type my question into a ChatGPT prompt, we read the output together and discuss whether it makes sense. This is a person I've had great discussions with in the past, and who has frequently had really good insights, but seems to have completely tapped out.

    To be fair, the outputs from ChatGPT tend to be quite good. It's the inputs people give it where problems most often arise - and people seem far too eager to charge ahead with a vibe coded solution built on invalid or incomplete inputs/assumptions. And it's shocking to see how quickly and willingly people have handed over control to LLMs.

    - **72deluxe** ([comment](https://news.ycombinator.com/item?id=49336573#49343233), 2026-08-18 09:11:57 UTC)
      This is very sad. I found it was interrupting coding when the editor would suggest new blocks of code without me actually thinking and I found I was just generally abandoning any thought processes.

      So I've disabled that and now I'm explicit if I want to solve a problem because then it means my brain's actually engaged.

      It seems to be like a shortcut to early onset dementia because the brain's never being actively involved in problem solving.

    - **Twirrim** ([comment](https://news.ycombinator.com/item?id=49336573#49339561), 2026-08-18 00:23:32 UTC)
      I've been wondering lately if this is about the end of the road for me for a career in tech (I've had a good long one, so.. maybe?).

      I'm so tired of AI Slopped architecture documents, code, messages in slack, emails etc.  I'm close to flat out rejecting any architecture doc I get that's written by an LLM, because I'm not sure the engineers even understand what they're proposing.  The code is often a nightmare under the hood, even if it works.  I've got smart coworkers who now just copy paste everything via an LLM giving themselves something approaching a lobotomy in the process.

      - **freetime2** ([comment](https://news.ycombinator.com/item?id=49336573#49339740), 2026-08-18 00:48:48 UTC)
        I've decided to leave my current company. It's mostly the result of burnout from working many years at an unsatisfying job, but the advent of AI has certainly exacerbated things. I no longer need the income (although it's certainly nice), and recently have begun to dread the start of every work day. It's time for a change.

        I may just get out of the tech industry altogether. But I'm also tempted to try my hand at an indie dev project that I have in mind. With AI, it seems like it would be easier than ever to get a new project off the ground. And I don't really mind AI-assisted development personally. It's mainly all the organizational and interpersonal disruption that is giving me a headache at the moment.

  - **Aramgutang** ([comment](https://news.ycombinator.com/item?id=49336573#49338887), 2026-08-17 23:02:47 UTC)
    There's an old meme tweet that goes like this:

    > the fact that i'm at risk of seeing a 14 year old's opinion at any point during my day is a human rights violation

    This always strongly resonated with me; if something was written by a 14-year-old, I don't want to read it, end of story. There is no way it can provide value to me. I shudder to think that I may have unknowingly argued with 14-year-olds on the Internet in the past.

    But if I had a child who was 14, I wouldn't object to interacting with them, obviously.

    It's the same with LLMs: the only time I want to be reading LLM output is when it's my model that I prompted myself.

  - **dspillett** ([comment](https://news.ycombinator.com/item?id=49336573#49337493), 2026-08-17 20:53:46 UTC)
    *> that it's not universally offensive and reviling to post an AI-generated response to another person*

    There has even been an advert extoling the behaviour (I forget which phone OS brand it was for, which is a shame as I might like to try avoid buying anything from them): "if a friend asks a question and your phone can answer directly, shouldn't it?", to which my gut reaction is "absolutely fucking not, it shouldn't". My more considered reaction is pretty much exactly the same.

    For a start I'd consider it rude and if I found out it was happening reduce my fucking my communication with that person, or call instead if messaging (unless it seems they have a fake them taking calls, no doubt that'll be a thing sooner rather than later). And quite frankly I will reply when I'm good and ready, thankyouverymuch, instant automated reactions plays far too much into the "always available" thing that I don't care for even without AI.

    I look forward to future news stories where people with such features turned on suffer PII exfoliation or other hacks when someone finds a prompt injection hole, or just uses the feature as designed because the user has been too open with what they have given it access to and who it should respond to (perhaps by inaction, because the defaults will likely be wide open for "convenience" until there is uproar).

    - **account42** ([comment](https://news.ycombinator.com/item?id=49336573#49344230), 2026-08-18 11:42:19 UTC)
      > I forget which phone OS brand it was for, which is a shame as I might like to try avoid buying anything from them

      That it is plausible to have come from any of the major ones just means that they all should be avoided. Which is of course not a very practical insight.

      > unless it seems they have a fake them taking calls, no doubt that'll be a thing sooner rather than later

      That would be the point where our friendship is over (or rather I acknowledge the fact that it was already over) and I delete & block the contact.

  - **tpoacher** ([comment](https://news.ycombinator.com/item?id=49336573#49337432), 2026-08-17 20:49:32 UTC)
    I completely agree in principle, but to play devil's advocate, if an "author's" prompting technique is better than mine such that they generate a more useful article than what my own AI session might produce on average, then *maybe* there's value in *some* generated articles.

    The above still implies some effort going into good prompting, however. I completely agree about the uselessness of "build me a castle; no bugs plz" style generated articles.

    - **mediaman** ([comment](https://news.ycombinator.com/item?id=49336573#49337848), 2026-08-17 21:24:30 UTC)
      It's possible, but I've experimented with different style guides and prompt methods and have never gotten it to output what I'd call "good" writing.

      It is almost always low information density. Sometimes I can get it to remove most of the extraordinarily cliche phrases it injects into everything, along with the tortured, gauche prose (especially Claude). But what remains is an expansion algorithm: it takes a simple idea and expands it like polyurethane foam to fill however much space it can take, the volume filled mainly by grammatical syntax and only traced with any actual semantic meaning.

      - **gowld** ([comment](https://news.ycombinator.com/item?id=49336573#49338528), 2026-08-17 22:26:24 UTC)
        "Good" is subjective, but I found this OOTB sufficiently information-dense and easy-to-customize:

        [https://claude.ai/share/ac747c6d-2a62-40b7-b33e-06a94cf34344](https://claude.ai/share/ac747c6d-2a62-40b7-b33e-06a94cf34344)

      - **elendilm** ([comment](https://news.ycombinator.com/item?id=49336573#49338129), 2026-08-17 21:46:44 UTC)
        One can give details of a product and ask the ai to generate the documentation.

  - **thih9** ([comment](https://news.ycombinator.com/item?id=49336573#49337718), 2026-08-17 21:12:41 UTC)
    > If you can't be bothered to put your time into writing it and teaching me what you think, why should I be bothered to read it?

    You are likely not the target audience anymore and they don't care if you're going to read it.

  - **giancarlostoro** ([comment](https://news.ycombinator.com/item?id=49336573#49337559), 2026-08-17 21:00:06 UTC)
    This is why even if I ask GPT or Claude or whatever to rewrite an email, I still rewrite it by hand with my own words, what I look for is, did the AI remove sentences where I repated myself or that were too wordy? Perfect, I'll ommit those details.

    - **jaredsohn** ([comment](https://news.ycombinator.com/item?id=49336573#49339549), 2026-08-18 00:21:34 UTC)
      Could probably ask the AI what changes they'd make to the email.

  - **noman-land** ([comment](https://news.ycombinator.com/item?id=49336573#49337487), 2026-08-17 20:53:08 UTC)
    You and I and everyone else need to make it clear to people who do this that we don't like them doing this and we think they are uncool.

    - **dspillett** ([comment](https://news.ycombinator.com/item?id=49336573#49337548), 2026-08-17 20:58:56 UTC)
      Me calling someone uncool would be rather hypocritical in afraid! I've done some interesting things, cool even, but that doesn't necessarily make conversation with me interesting/cool! I'll go with letting them know I find it dickish and perhaps even a tad offensive.

      - **sebastiennight** ([comment](https://news.ycombinator.com/item?id=49336573#49337665), 2026-08-17 21:08:45 UTC)
        Counterpoint: if you're uncool yourself, you might be uncool enough to call out uncoolness, from a "game recognizes game" point of view

        - **blitzar** ([comment](https://news.ycombinator.com/item?id=49336573#49338287), 2026-08-17 22:01:23 UTC)
          lame recognises lame

          - **dspillett** ([comment](https://news.ycombinator.com/item?id=49336573#49338354), 2026-08-17 22:10:34 UTC)
            That I shall have to purloin.

  - **ithkuil** ([comment](https://news.ycombinator.com/item?id=49336573#49338532), 2026-08-17 22:26:40 UTC)
    Don't get me wrong, I loathe the AI style as the next person.

    But I don't buy your argument: if a person used AI to produce a text it doesn't mean they haven't steered the I in the direction they wanted the conversation to go and (hopefully) review the output.

    That's an added value

    Yes, it would be nice if it was also pleasant to read

    - **LPisGood** ([comment](https://news.ycombinator.com/item?id=49336573#49339060), 2026-08-17 23:23:49 UTC)
      They don’t review the output. That’s the thing. No one is reading this stuff, not all of it at the least.

    - **oblio** ([comment](https://news.ycombinator.com/item?id=49336573#49339270), 2026-08-17 23:49:14 UTC)
      It's still a lower effort contribution and because the surface is plausible and the content is usually verbose, it's a bigger waste of time for the other party than a low effort 100% human contribution.

    - **gspr** ([comment](https://news.ycombinator.com/item?id=49336573#49341930), 2026-08-18 06:12:02 UTC)
      Steered it?! If I'm gonna *read* it, I want someone to have *written* it, not bloody "steered" it!

      "Why are you upset with this restaurant meal? Okay it wasn't actually cooked here per se, but the chef certainly reheated it and carefully monitored the microwave oven while doing so!"

      This crap just needs to end. "Steering" words at another human being is incredibly disrespectful.

      - **ithkuil** ([comment](https://news.ycombinator.com/item?id=49336573#49342914), 2026-08-18 08:20:45 UTC)
        big restaurants have many cooks that are trained and monitored by the chef, but the chef is certainly not necessarily prepairing your meal.

        The chef is however responsible for the outcome so you're absolutely right to complain if the meal sucks and most of this AI written crap definitely sucks to read.

        That said, it's not about the "principle" of having your meal cooked by the chef / the text written word by word by the human.

        It's about the outcome. People should learn to tame their AI tools/harnesses in such a way to produce quality output (code and prose) and it's absolutely despicable that so many people are so eager to lower our standards in quality just because everybody else seems to be doing it.

        - **account42** ([comment](https://news.ycombinator.com/item?id=49336573#49344325), 2026-08-18 11:51:51 UTC)
          If I go to a restaurant and find out I got a reheated meal I'm going to be upset no matter how much quality control the chef does of the reheating. That's just not something I would ever go to a restaurant for.

        - **gspr** ([comment](https://news.ycombinator.com/item?id=49336573#49344364), 2026-08-18 11:55:57 UTC)
          > That said, it's not about the "principle" of having your meal cooked by the chef / the text written word by word by the human. It's about the outcome.

          No. It very much isn't about outcome. It's about interpersonal relationships.

          > People should learn to tame their AI tools/harnesses in such a way to produce quality output (code and prose)

          The quality isn't the problem. The quality is that something that needs to be "tamed" is writing words that the "tamer" expects me to read.

  - **scarecrowbob** ([comment](https://news.ycombinator.com/item?id=49336573#49337563), 2026-08-17 21:00:24 UTC)
    Getting an AI response from folks has a very "let me google that for you" kind of feel.

    If you're not familiar with the concept... [https://letmegooglethat.com/?q=lmgtfy](https://letmegooglethat.com/?q=lmgtfy)

  - **jerezzprime** ([comment](https://news.ycombinator.com/item?id=49336573#49339838), 2026-08-18 01:02:22 UTC)
    To play devil's advocate here, it is possible for someone to simultaneously use AI to write and also not be a meat proxy. I'm not saying that is the norm, but I have written docs where the vast majority of the words come from AI, but I also spent multiple days on the substance and content.

    - **Ampersander** ([comment](https://news.ycombinator.com/item?id=49336573#49342730), 2026-08-18 07:53:23 UTC)
      Maybe if you only use the LLM to proof read or something? I don't know if LLMs are actually any good for this purpose, but it's something I came to think of when trying to answer your question.

      I do think that it is very difficult to not be a meat proxy when you utilize an LLM for writing tasks. These tools are computer programs that generate text, so what else would you do with it than have it write for you? This is being a meat proxy.

      Trying to avoid being a meat proxy can quickly eat the supposed productivity gains of using an LLM in the first place.

      Like say I need to write an article about some subject and it would take me the entire day to complete this task without an LLM. I can get some sort of article out of an LLM by simply asking, I don't need to think about the subject myself at all. The LLM productivity promise is also fulfilled, because I did an entire days work in a minute or so.

      Now if I also need to read and understand the work, and be able to defend it or explain it to others as if I produced it myself, then this will take a lot of time. If on top of this I need to edit the text to sound like me rather than an LLM, then I probably still need the whole day for this task and I have lost all the productivity increase that I sought from using the LLM.

      It's the thinking that takes time when you write, not typing. But you can't do the thinking and avoid doing it at the same time.

      The same idea applies to coding too. Doing code review and requiring the author and reviewer to read and understand the code basically eliminates all the productivity gains that using the LLM was supposed to provide. Throw out the reviewing, reading, and understanding and we can have each developer producing a thousand kloc per day, over 1000x productivity. If we don't throw those out, we are comparatively in the exact same spot as not using LLMs at all.

      - **account42** ([comment](https://news.ycombinator.com/item?id=49336573#49344367), 2026-08-18 11:56:24 UTC)
        Yes, it's like people have forgotten that junior contributors you can't trust yet often have net negative productivity due to the time you need to invest to review and guide them.

  - **fhe** ([comment](https://news.ycombinator.com/item?id=49336573#49339754), 2026-08-18 00:51:03 UTC)
    maybe it's not so absolute. if someone else has the talent or takes the effort to come up with a clever prompt that got an interesting response from an LLM, I'd want to read it too. Treating LLMs as a tool, this is not so different from someone else using Blender to create an interesting animation.

  - **m463** ([comment](https://news.ycombinator.com/item?id=49336573#49337077), 2026-08-17 20:23:26 UTC)
    AI;WR

  - **sailfast** ([comment](https://news.ycombinator.com/item?id=49336573#49339080), 2026-08-17 23:26:50 UTC)
    It is offensive and reviling. But people do it anyway. People are lazy. And often don’t care about you, the reader.

  - **scotty79** ([comment](https://news.ycombinator.com/item?id=49336573#49341321), 2026-08-18 04:38:05 UTC)
    I'd rather read something novel but AI generated, than the opinion I've seen few times already. Like yours.

  - **blitzar** ([comment](https://news.ycombinator.com/item?id=49336573#49338201), 2026-08-17 21:53:02 UTC)
    Is Ai really any more offensive than the templated influencer slop of the past few years?

    If your favourite creator is engaged in generating this style of content, then I think it says more about your tastes than their morals.

    Don't smash the like button, don't share and unsubscribe.

    - **crab_galaxy** ([comment](https://news.ycombinator.com/item?id=49336573#49338292), 2026-08-17 22:01:49 UTC)
      Everyone is fighting OP on this extremely reasonable take when some of us are dealing with coworkers that copy slack messages/JIRA ticket comments/PR feedback into Claude and respond with the pasted output *as is* back like that’s completely acceptable.

      Like I don’t need to be placated by someone else’s AI agent when I call out something in a PR, especially when they have such an aversion to conciseness and resolution

      - **blitzar** ([comment](https://news.ycombinator.com/item?id=49336573#49338350), 2026-08-17 22:09:59 UTC)
        Fair call, re-reading the original take ... paragraph 1: person to person interaction (your coworker example) - 100% agree

        Back in the 00's you would have been allowed to mock, abuse and bully people who did stuff like that in the workplace -- and the shame might have put an end to it. Maybe the loophole is you tell their Ai agent to f' off not them.

    - **edaemon** ([comment](https://news.ycombinator.com/item?id=49336573#49338243), 2026-08-17 21:56:09 UTC)
      Volume is the problem. There's so much more of it now. Many platforms I used to enjoy are just overwhelmed with valueless content.

      - **blitzar** ([comment](https://news.ycombinator.com/item?id=49336573#49338306), 2026-08-17 22:03:31 UTC)
        On platforms where you can not curate what you are fed, the healthiest option is to leave.

        - **account42** ([comment](https://news.ycombinator.com/item?id=49336573#49344467), 2026-08-18 12:05:37 UTC)
          The problem is unless it becomes socially unacceptable might run out of platforms. It's not just influencers doing this, it goes as far as "normal" posters in old-school forums.

        - **a96** ([comment](https://news.ycombinator.com/item?id=49336573#49343663), 2026-08-18 10:29:50 UTC)
          Yes. Volume is rarely the problem unless there's too little. Filter/search is the problem if desired material exists.

  - **cyanydeez** ([comment](https://news.ycombinator.com/item?id=49336573#49338823), 2026-08-17 22:55:27 UTC)
    ok, what part of the last decade led you to believe that communication decency has radically improved.?

  - **bdangubic** ([comment](https://news.ycombinator.com/item?id=49336573#49338215), 2026-08-17 21:53:45 UTC)
    while i might not have written it, i used my masters in prompt engineering to carefully guide its creation :)

    - **LPisGood** ([comment](https://news.ycombinator.com/item?id=49336573#49339237), 2026-08-17 23:44:45 UTC)
      If this is not sarcastic, which school gives such a masters

  - **xdennis** ([comment](https://news.ycombinator.com/item?id=49336573#49338978), 2026-08-17 23:13:32 UTC)
    > The part that astonishes me is that in the year of our common era two thousand twenty-six

    It astonishes me that in 2026 AD, people still like to pretend that our calendar is not based on Christ's supposed birth. Christians have no problem calling days after pagan gods (Wednesday = Woden's day, Thursday = Thor's day, etc), but for some reason we have to pretend like the calendar isn't based on the Christian god.

    - **tom_** ([comment](https://news.ycombinator.com/item?id=49336573#49339087), 2026-08-17 23:27:22 UTC)
      It's typically referred to as CE to indicate the speaker's personal lack of belief in the divinity of Jesus, that might be implied by using the term anno domini. Nobody is under any illusion about whose birth began this era.

  - **fragmede** ([comment](https://news.ycombinator.com/item?id=49336573#49338424), 2026-08-17 22:17:44 UTC)
    It takes energy to generate the LLM response. If you read the already generated response instead of generating your own, we burn less coal.

    - **account42** ([comment](https://news.ycombinator.com/item?id=49336573#49344400), 2026-08-18 12:00:23 UTC)
      Now add the energy needed by the human to read the response (not to mention his finite lifetime) to your calculation.

  - **godwinson__4-8** ([comment](https://news.ycombinator.com/item?id=49336573#49337627), 2026-08-17 21:05:42 UTC)
    Yes, we get it. Laziness has always abounded in human endeavors. Despite the common social norms against it, there is a clear reason. Obviously, if you can get the same reward with less work it is a greater ROI. The incentive is pretty straightforward. In a mechanized world the incentives are even more aligned towards a kind of laziness given the capacity for automation to scale.

    None of this is new. People who act like they were born yesterday at every instance in this parade of slop induced phenomena are more grating to me than the slop itself.

    Just take your response. Reads as incredibly lazy to me. I've read pretty much the exact same sentence so many times by now. At a certain point, what distinguishes a mob of humans repeating each other from an LLM? Original, high quality commentary is exceedingly rare. Surely you must already know this. Of all the words written on the internet, most must be garbage. It was not LLMs that tipped this balance. In my experience, the average LLM actually speaks as a superior interlocutor to the average person online. It comes with the benefit that if you get a lame response, you probably deserve it for asking such a lame question.

    Most humans are not worth reading. Sorry, but this should be obvious to anyone who has tried to research or investigate anything with significant rigor. People don't appreciate enough that many times when something comes up where the LLM is doing something "dumb" it is obviously because they are trained on a corpus authored by dumb humans. My favorite example of this is when people complained in a geopolitical simulation the LLM happily deployed a "tactical nuke" as if the phrase "tactical nuke" is not itself aptly described as a wholly human authored hallucination.

    People are using LLMs at work or w/e to get back time from their corporate bosses that don't care about them. Not everyone has the luxury of being able to act like an enlightenment era university student. Most words published have to be akin to "we'd like to reach out to your about your car's extended warranty" anyway. Many blogs are more or less cover for the same, or at the very least indirectly subsidized by such commercial interests. If that is not offensive, frankly it's not clear why it would be more offensive to have an AI author it. It's mostly all pablum anyway.

    No one who actually cares about a topic will use a LLM. The rest of them might as well, because it makes almost no difference. If you had a clearer model of this incentive structure you doubtlessly on the whole benefit from as a modern human typing on hackernews, instead of this knee-jerk reactive one ("universally offensive and reviling") you would learn to just move on and get over it. If you want more people to have the luxury of your enlightened discernment, you should probably celebrate LLMs automating away the majority of so-called "knowledge work" so that the economy, which has largely already solved for basic human needs, can achieve a state of hyper optimization, algorithmic foresight and UBI where none of us have to work and we can spend all our time in symposium with each other, given that is what you seem to desire for yourself and other humans. We will not get there if at every turn LLMs are demonized on these incessantly banal terms.

    - **otterley** ([comment](https://news.ycombinator.com/item?id=49336573#49338825), 2026-08-17 22:56:12 UTC)
      It's not controversial that if left alone, most people will tend towards minimizing laborious work, and that the use of technology to do that ought to be expected. Consider, however:

      1. This work was largely optional to begin with. Few people actually need to post on LinkedIn, write blogs, etc. It's arguably a mountain of content waste (which is why the term "slop" is so fitting). Not only does it waste the producer's time to produce it, but it also wastes the reader's time to try to consume it.

      2. It's not a substitute for actual work. If it becomes clear that you're using LLM to do work you are paid to do, eventually the person who pays you will notice, and replace you with the LLM. If your employer values you because of the work you do, it's in your best interest to do the job yourself.

      - **godwinson__4-8** ([comment](https://news.ycombinator.com/item?id=49336573#49338919), 2026-08-17 23:06:16 UTC)
        1. This doesn't make any sense. On this reading, most any work is "optional" in that you had the option to do something else. But few people have the option to not work at all. If creating slop generates a decent enough ROI, and *you have to work*, then why is it waste? It may be waste to *you*, but for them it is an income. Just like there are entire industries or products I might personally think are a waste and yet make tons of money. In the modern economy most work is optional then. So what point are you making?

        2. Yes, people get replaced at work all the time. And actually most employees who figure out who to maximize their own ROI (and thus their companies) get rewarded, not punished. If your slop code is "good enough" and you are moving the metrics the C suite cares about, your colleague taking far longer to create far less is obviously going to be punished.

        If some sea change happens that replaces a whole class of workers, that is beyond the scope of the individual worker to think about. The modern economy can be viewed as one long process of automation, where most workers have been subsidizing their own eventual replacement, given the privileged position of capital over labor. This is historically obvious. It does not mean it benefits the individual to go back into some state of nature, or not reap what benefits they may gain from the prevailing system while it is still the one at hand.

        - **otterley** ([comment](https://news.ycombinator.com/item?id=49336573#49341098), 2026-08-18 04:00:21 UTC)
          What I meant by "optional" work is that it's not being performed for a buyer; it's volunteer labor. Nobody's paying for individuals' awful LinkedIn posts. I suppose it could be framed as self-promotion aimed at a potential future payoff, but if it repels buyers, then it's pointless.

          Perhaps it's worth looking at this issue from the demand side instead. Who is the customer or buyer of the AI-generated work; and if there is one, how much do they value it? I contend that there are few actual buyers who are actually asking for the AI-generated output, and thus the value is low. These buyers are usually asking for some other outcome that flows downstream from the work, and AI slop is either being misperceived as the actual ask, or is a step in the middle somewhere.

          Next, I wasn't talking about slop code. I was talking about slop narrative work--the work preceding the coding phase that gets teams and goals aligned, and reports results to management. In a world in which code is increasingly machine-written, the focus turns to the planning and decision stages, and that's where communication skills are most important. If you're outsourcing that work to an LLM, you're providing little added value, and *that* makes you replaceable. Not by a machine, but someone better than you at writing.

          As for your last paragraph, I'm having trouble understanding whether you're in favor of AI-written content (not code, let's put that aside). That's the question I'm more interested in discussing than how economies evolve. I know how economic progress works ;-)

    - **Multicomp** ([comment](https://news.ycombinator.com/item?id=49336573#49338002), 2026-08-17 21:36:36 UTC)
      TL;DR: I want more effort posts/better SNR, so I guess I have to tolerate the human non-effort posts complaining about AI non-effort posts with the hope that it helps retard the rate of non-effort posts vs effort posts.

      While I'm hoping the AI bubble pops sooner than later, as I still hold out hope that knowledge work will continue to require knowledgeable humans at the helm, I wanted to add on that I think you make a good point.

      A lot of users online can't read[1], and between a lack of pure reading comprehension, poor media literacy habits draining one's brains and ability to focus, and finally the increase in AI-enabled content, I'm not surprised at how redditor-cultured netizens love to throw up their hands and say "AI;DR!", as if that makes them somehow morally superior.

      These users won't read dense texts or try to elucidate meaning out of human-written works, they ask for AI summaries or manual "TL;DR" entries as it is, now the AI is use is being used as an excuse to enable mental laziness and lack of attempts to read information.

      So while I get lost in wikipedia walks because I'm looking for written entertainment for 'learning', they are getting mind-melted by algorithms, therefore, an uncharitable part of me wants to let the meat-proxying continue.

      And then the other part of me that gets annoyed by having to sift through AI-slop-infested text to see what if any meat there may be in there decides that perhaps that's not as helpful of an attitude as I should take after all, because if everybody decides to meat-proxy the world away, I'll be unhappier than letting lazy functionally-illiterate-users complain aloud, even as the latter is boring reading as well.

      [1] in the [https://coding2learn.org/blog/2013/07/29/kids-cant-use-compu...](https://coding2learn.org/blog/2013/07/29/kids-cant-use-computers/) sense

      - **godwinson__4-8** ([comment](https://news.ycombinator.com/item?id=49336573#49338482), 2026-08-17 22:22:45 UTC)
        It's a good point, I just don't agree with the conclusion. I think if you examine the incentives/mechanics behind the phenomena, you would realize that a world in which there are more "meat proxies" for more tasks would be a more enlightened one. The precedents to me are obvious - go back and examine the most famous times of human flourishing. It was always connected to power and patronage - ie, commerce. Most people could not read for most of human history. Universities used to be institutions for a small number of elite who could afford not to labor because it was someone else's job. Compared to primeval man this is essentially using another human as a "meat-proxy". That's what the modern economy is. The CEO doesn't waste his time filling out the spreadsheet or w/e. It's the same concept. Why is a human meat-proxy necessarily better than a wholly mechanical one? Our social institutions have simply fallen behind our scale.

        I view LLMs optimistically as the catchup phase. After all, they aren't really "reinventing" anything, rather they are a tool to synthesize the vast human corpus and catch up to the scale. Yes, at the moment they are used for all sorts of things, most of which are trivial. But when the bubble pops it will not mean knowledge work has a renaissance, rather it will be the nail in the coffin. The bubble pop will mean it will be cheap, compute/LLMs become a utility. So let the AI fill out the spreadsheet. Allow UBI to flourish, implement a severe wealth tax. End pointless wars. Slim government, which is a lot of bloat and obfuscation around what should be automated, open and transparent disbursements. End private taxes on the economy (credit cards duopoly, etc) and essentially, everyone gets to act like an enlightenment era university student. On this view, the hope would be that the present times are the wars of religion, the storm before the calm. If we are able to make it through in a hyper-networked, nuclear age.

        LLMs are not going away, no matter how many Americans may want to go back to the proverbial land. Reactive movements have always existed, and always failed. I think you would simply be better served by advocating for the best case scenario, rather than aligning yourself with the AI skeptics who as you acknowledge, are also rather widely boring and intellectually lazy - that which you seek to remedy. The question of assuring UBI is not obvious. Imo there is far more rigor and interesting questions in the camp trying to create the optimistic future, than in those who resort to unexamined, parroted skepticism.

  - **ModernMech** ([comment](https://news.ycombinator.com/item?id=49336573#49337181), 2026-08-17 20:29:57 UTC)
    I went to a farm opening this weekend. A guy was there with fliers with about the barn renovation he completed, products they used, how the process went. 100% LLM output. How would you talk to your LLM about something like that? If he gave you that flier, would you scoff and trash it talking about how you can't be bothered to read it if he didn't write it? Or would you look it over?

    - **account42** ([comment](https://news.ycombinator.com/item?id=49336573#49344437), 2026-08-18 12:02:58 UTC)
      I would leave at the earliest convenience and avoid interacting with that person as much as possible.

    - **dspillett** ([comment](https://news.ycombinator.com/item?id=49336573#49337285), 2026-08-17 20:37:24 UTC)
      *> If he gave you that flier, would you scoff and trash it talking about how you can't be bothered to read it if he didn't write it? Or would you look it over?*

      Depends on his countenance and how good a mood I'm feeling in!

      In any case I might well ask how much time went into at least reviewing the output. Or I say (rather than a flat AI;WR) "I'll scan that and have an AI summerise it for me later".

    - **Calazon** ([comment](https://news.ycombinator.com/item?id=49336573#49340295), 2026-08-18 02:10:16 UTC)
      Is there something in particular I'm trying to glean from that information? If so I might look it over, or snap a photo and ask my own LLM about it.

      If not, I would politely keep my mouth shut, then pocket the flier to trash later, and on the way home I would complain about it to my wife.

      - **ModernMech** ([comment](https://news.ycombinator.com/item?id=49336573#49340734), 2026-08-18 03:00:48 UTC)
        > If so I might look it over, or snap a photo and ask my own LLM about it.

        Right, exactly, that's what you'd do whether he spend 10 hours on it or 10 minutes.

    - **quickthrowman** ([comment](https://news.ycombinator.com/item?id=49336573#49338636), 2026-08-17 22:39:24 UTC)
      > If he gave you that flier, would you scoff and trash it talking about how you can't be bothered to read it if he didn't write it? Or would you look it over?

      I would crumple up the flyer, throw it on the ground, and then ask for another one. Then I would crumple up that flyer, throw it on the ground, and ask for another one. I would repeat this until he refuses to give me another flyer.

  - **throwaway98797** ([comment](https://news.ycombinator.com/item?id=49336573#49338320), 2026-08-17 22:05:31 UTC)
    it’s not that it’s ai generated it’s that it’s bad.

  - **coderatlarge** ([comment](https://news.ycombinator.com/item?id=49336573#49337908), 2026-08-17 21:30:14 UTC)
    i wonder if you’re equally offended by a public figure hiring young people to ghost write for their social media accounts or their books etc

    - **otterley** ([comment](https://news.ycombinator.com/item?id=49336573#49338737), 2026-08-17 22:48:33 UTC)
      The benefit and promise of social media, at least early on, was that it was supposed to be authentic - that when someone posted, it was really coming from them. Engagement was truly personal, at least for a little while. It still is for most.

      In the book-publishing context, ghost writers have to be credited, even if the attribution is in small print.

- **cortesoft** ([comment](https://news.ycombinator.com/item?id=49336573#49337011), 2026-08-17 20:19:03 UTC)
  I really like the point I read somewhere the other day; instead of sending me the AI output, just send me the prompt you used to generate it. That is the only part that contains only the information you are trying to convey. The rest is just guesses flowery language added, and it confuses the actual message being sent.

  - **supermatt** ([comment](https://news.ycombinator.com/item?id=49336573#49337607), 2026-08-17 21:03:54 UTC)
    How is this? [https://claude.ai/share/99bfee0f-bab9-4593-aabb-377e71f1151d](https://claude.ai/share/99bfee0f-bab9-4593-aabb-377e71f1151d)

    - **stordoff** ([comment](https://news.ycombinator.com/item?id=49336573#49338214), 2026-08-17 21:53:44 UTC)
      FWIW, I tried to read the AI version first, and found myself bouncing back to the prompt multiple times. The AI version just reads as flat, impersonal, and as if it has had all the corners sanded off (both in style and content). The prompt conveys much more about what _you_ want to say, and is easier to read without zoning out and losing interest.

      If you must use AI in this way, I'd tell it to take a _much_ lighter touch. It cleans things up without washing away the personality of your writing. ChatGPT example:

      > adjust the following for spelling and grammar, making MINIMAL alterations to the original wording and content. do NOT rewrite, just clean up what is already there: [post]

      [https://chatgpt.com/share/6a8382b9-3620-83eb-b17e-4397aee5ad...](https://chatgpt.com/share/6a8382b9-3620-83eb-b17e-4397aee5ad61)

      - **badsectoracula** ([comment](https://news.ycombinator.com/item?id=49336573#49344219), 2026-08-18 11:41:11 UTC)
        I find amusing that both Claude and ChatGPT realized the "hackers" in "a lot of people on hackers that like to complain about stuff" was about "Hacker News" :-P

      - **supermatt** ([comment](https://news.ycombinator.com/item?id=49336573#49338409), 2026-08-17 22:16:23 UTC)
        Huh, thats really interesting... That sounds a lot better than I expected, and is readable enough for me to edit it.

        Thank you :)

    - **miyoji** ([comment](https://news.ycombinator.com/item?id=49336573#49337731), 2026-08-17 21:13:39 UTC)
      Yes, the original prompt is 10000% better than the AI output, because it shows me exactly how much the author (you?) cares about this topic and how much effort they're willing to put into communication, which is barely any at all.

      - **supermatt** ([comment](https://news.ycombinator.com/item?id=49336573#49337854), 2026-08-17 21:24:54 UTC)
        > which is barely any at all

        Clearly you either didn't read it, misunderstood it, disbelieved it, or just DGAF :)

        - **swatcoder** ([comment](https://news.ycombinator.com/item?id=49336573#49337968), 2026-08-17 21:33:42 UTC)
          What I read is that you're self-conscious about your writing style and that you find the LLM processed version of your own stream of thoughts to be helpful to you yourself.

          Which is fine for you, but doesn't change that many people can get more insight out of your original text than they can out of the generated adaptation, and can do so with more interest and less fatigue.

          And indeed, you don't have to care about that. But one would think that in publishing or sharing your writing at all, you do in fact have some investment in whether people receive those insights that you have. Otherwise, you could just keep the AI writings to yourself in the first place.

          - **shimman** ([comment](https://news.ycombinator.com/item?id=49336573#49338728), 2026-08-17 22:48:03 UTC)
            These people need therapy not chatgpt subs.

        - **minimaxir** ([comment](https://news.ycombinator.com/item?id=49336573#49338045), 2026-08-17 21:40:20 UTC)
          Many different people in this HN submission have given you similar feedback: given that, you should consider that your priors are not correct.

          - **qarl2** ([comment](https://news.ycombinator.com/item?id=49336573#49338284), 2026-08-17 22:01:15 UTC)
            It could also be that this site has created its own hive-mind environment.  Which is especially and bizzarely intolerant of AI at the moment.

            I don't want the prompt - I may not have access to an LLM to evaluate it.  The entire argument here is misguided, and deeply angry about AI.

            It's equivalent to answering a question with "google it".  Which is often times just plain rude.

            - **Alpha3031** ([comment](https://news.ycombinator.com/item?id=49336573#49338419), 2026-08-17 22:17:03 UTC)
              People having preferences different from you is not a hive mind.

              - **qarl2** ([comment](https://news.ycombinator.com/item?id=49336573#49338644), 2026-08-17 22:39:43 UTC)
                Of course not.  I didn't say anything like that.

                But I do see a consistent trend here regarding hostility to AI.  It seems to be a pattern, and a strange one.

                I've never had someone angry at me for posting a Google search, for example.

                - **Alpha3031** ([comment](https://news.ycombinator.com/item?id=49336573#49338765), 2026-08-17 22:50:25 UTC)
                  I've never seen anyone post a copy-and-paste of some pages of the Google search results while also excluding the search term, and I would find that bizzare. I would assume that you, like most people posting a Google search, would post the link to that search, which in the case of Google includes a copy of what would be equivalent to the prompt. In my experience, most people posting Google links would also include a short explanation of why they think it relevant were it not immediately obvious.

                  - **qarl2** ([comment](https://news.ycombinator.com/item?id=49336573#49338867), 2026-08-17 22:59:50 UTC)
                    >I've never seen anyone post a copy-and-paste of some pages

                    I have.

                    For example, I was looking for a bathmat.  My wife pasted me a list.  Just a week ago.

                    I don't think my wife is bizarre.  It's unfortunate that you do.

                    - **Alpha3031** ([comment](https://news.ycombinator.com/item?id=49336573#49338929), 2026-08-17 23:08:05 UTC)
                      I said I would find the *action* bizarre ("that", not "them"). Personally, I don't find it unfortunate to admit that some things still surprise me. If you choose to interpret that as judgement of your wife as a person, then that is up to you.

                      - **qarl2** ([comment](https://news.ycombinator.com/item?id=49336573#49338998), 2026-08-17 23:16:08 UTC)
                        She just wanted to show me what she wanted; I don't think she wanted to encourage me to choose a different color.

                        SO BIZZARE!

                        - **Alpha3031** ([comment](https://news.ycombinator.com/item?id=49336573#49339070), 2026-08-17 23:25:23 UTC)
                          Again, you are free to interpret my comments however you wish. My primary intent was to express my belief that people having different preferences to you regarding reading AI output does not constitute some bizzare hivemind, which you appear to have accepted. Your preferences regarding communications between yourself and your wife are none of my business. I recognise preferences may exist, and I am not one to kink-shame.

                          - **qarl2** ([comment](https://news.ycombinator.com/item?id=49336573#49339400), 2026-08-18 00:02:53 UTC)
                            My dearest dude -

                            You called my wife bizarre.  Then you said "TECHNICALLY, I didn't call your WIFE bizarre I called her ACTIONS bizarre."

                            I would ask you to stop talking to me, but it seems unlikely to work.

                            So.  You have a nice day, now.

                            - **wpietri** ([comment](https://news.ycombinator.com/item?id=49336573#49339947), 2026-08-18 01:19:42 UTC)
                              You're the one who decided to imagine that a reasonable discussion comment was an attack on your wife. You're also the one who started out calling things bizarre. As somebody not involved in this discussion, to me it looks like drama-seeking behavior.

                              - **qarl2** ([comment](https://news.ycombinator.com/item?id=49336573#49340256), 2026-08-18 02:04:32 UTC)
                                I do think that the anti-AI mentality around here is bizarre.

                                I do not think that forwarding a listing from Google is bizarre.

                                These seem like reasonable positions to me.

                                I am very sorry if my voicing these beliefs makes you uncomfortable.

            - **duskdozer** ([comment](https://news.ycombinator.com/item?id=49336573#49343698), 2026-08-18 10:35:20 UTC)
              >It could also be that this site has created its own hive-mind environment. Which is especially and bizzarely intolerant of AI at the moment.

              Really? I wonder where else you haunt because this is the most pro-AI place I'm around, both in fervor and number.

          - **supermatt** ([comment](https://news.ycombinator.com/item?id=49336573#49338942), 2026-08-17 23:09:12 UTC)
            There are also many others stating the same things - and they are getting flagged and downvoted for it.

            Just because those of you who disagree are more vocal, downvote and flag-happy doesn't make you right.

            - **qarl2** ([comment](https://news.ycombinator.com/item?id=49336573#49339121), 2026-08-17 23:30:23 UTC)
              HE WOULD NEVER FLAG SOMEONE JUST FOR DISAGREEING!

              He would make up an excuse that is entirely untrue and then flag them.

              Oh wait, I'm thinking of my last encounter with him.

              - **minimaxir** ([comment](https://news.ycombinator.com/item?id=49336573#49339220), 2026-08-17 23:42:34 UTC)
                If you're going to directly accuse me of malfeasance, link the threads so people can make their own opinions.

                [https://news.ycombinator.com/item?id=49233565](https://news.ycombinator.com/item?id=49233565)

                [https://news.ycombinator.com/item?id=49242231](https://news.ycombinator.com/item?id=49242231)

                - **qarl2** ([comment](https://news.ycombinator.com/item?id=49336573#49339307), 2026-08-17 23:53:36 UTC)
                  Sadly - most people on the site can't read them.  Only the power users, such as yourself.

                  But I am glad you've decided to engage.  Now will you answer my question?

        - **miyoji** ([comment](https://news.ycombinator.com/item?id=49336573#49338088), 2026-08-17 21:43:33 UTC)
          No, I did read it, and I think I understood it. My summary in my own words is that you find that LLMs can massage your writing and reduce the stress of communication. Did I believe it? Well...

          You have an account on HN dating back to 2013 with over 6000 comment karma, you clearly didn't have trouble communicating like a normal person for a decade on this website before the advent of LLMs. Your spelling and grammar in posts predating LLMs are also *far* better than what you've produced in this prompt, so I'm tempted to think that you're exaggerating your inability to communicate normally to make a point.

          But even so, the original wall of text communicates the point much more strongly and sincerely than the LLM trash.

          - **supermatt** ([comment](https://news.ycombinator.com/item?id=49336573#49338253), 2026-08-17 21:57:32 UTC)
            I haven't always struggled so much, but my ability to read has severely diminished over the past decade. I find it much easier to communicate in short form. It has always been disproportionately time-consuming for me to write though.

            It is the articulation of ideas that I struggle with and so I usually edit my comments multiple times. And to get rid of some of the more stupid stuff I say.

            To be fair, that word salad would read more like this comment if I gave it some time, but it would take many hours to produce a simple post with the same readability as the LLM.

        - **johnnyanmac** ([comment](https://news.ycombinator.com/item?id=49336573#49342408), 2026-08-18 07:13:10 UTC)
          Add some paragraphs and yes; your style is more "interesting than what an LLM generated. That's the only think truly hard to read compared to the output.

          Your style reveals the way you write sentences, the language and vocabulary you choose to employ, and even your emotion.

          Here's an obvious example:

          > I dont care ion people dont read my stuff. There are people that do and they find it useful. My ideas solidified have already started to bring dividends for me - and not from others reading beut from me being able to ficus my thoughts.

          which converts into

          >I don't particularly mind if people skip my stuff. Some people do read it and find it useful. And honestly, the biggest dividends haven't come from readers at all — they've come from the act of solidifying my own thoughts. That alone has been worth it.

          spelling aside, just look at the first sentence. You show a different kind of derision for your audience here compared to the LLM trying to sugar coat it and soften the blow. That's style, and a small part of why AI feels like it "slops" up any given style.

          "Brings dividends" isn't grammatically correct but reveals how your mind sees the idea. you see it as a result to manifest from your ideas. The Ai interpretation of "The biggest dividends..." grinds out the edges back to a more passive action happening more as a side goal.

          There's that much subtle changes in meaning from a 50 word passage being converted. Which AI should be "good" at. Now imagine how this breaks down slowly over the 600 word post you made if I broke down every little bit of it. That's what people are doing internally and quickly concluding "this all sounds the same". Which is about the worst thing you can be in an attention economy; boring and unoriginal.

          ----

          P.S. Yes. I don't want to come off as rude. But your prompt also does reveal how you approach writing as a whole. It's clear you a) value the presentation of the writing as much, if not more, than the contents of the writing and b) admire the writing "sounding smart and proper" but do not wish to impart effort to achieve those means yourself.

          I do believe there can be interesting prompts to read that is a back and forth correcting and managing the AI to give a more tailored writing as an end result. A conversation that reveals how you go past the basics spelling and grammar and tell the AI how to inject your style and taste into the generated results.  That would be true "AI-assisted writing".

          This was clearly not that. This was a single prompt: "make me an essay that sounds good and is formatted well". One and done. Not a conversation, but a demand trusting the standard of the average as output.

          I won't reject the idea of AI-driven writing one day making bespoke works. But I highly doubt it will be a one-and-done prompt that achieves this.

          - **supermatt** ([comment](https://news.ycombinator.com/item?id=49336573#49343534), 2026-08-18 10:09:17 UTC)
            My aim was to turn my ramblings into something more coherent. No more. No less.

            I have made longer notes using exactly the process you prescribe, but that wasn't necessary for me in this case as it wasn't the most complex of ideas - I just regenerated until it gave me a fair approximation of what I wanted.

            And to be fair - even if I had given it follow-up guidance it would still have the LLM "smell". It would receive EXACTLY the same treatment from the anti-llm crowd. Thats pretty much one of the core points of the post (judging the medium ahead of the content).

    - **ryankrage77** ([comment](https://news.ycombinator.com/item?id=49336573#49338969), 2026-08-17 23:12:39 UTC)
      The stream-of-consciousness in the prompt is much better than the LLMs response. Yes, it's messy and unpolished, maybe even a little hard to parse, but it's so much richer for it. The way it is written lets me follow your thought process, shows that you were getting the words out quickly without much or any editing, and how you were exploring the idea and making it more concrete by giving it written form.

      The LLM response has none of that character, it doesn't give me that little sliver of insight into the writer. It strips the idea from the author, making it generic and anonymous. The only thing I can gleam from text edited with an LLM like this (besides the literal meaning of the text), is that the author didn't care enough to express themselves.

      Sure, it's more polished, but doing the writing manually is half the point. You have an abstract idea, you refine into something that can be communicated, and in doing so, explore that idea and improve your understanding of it. I've re-written this paragraph a dozen times trying to do exactly that.

      - **supermatt** ([comment](https://news.ycombinator.com/item?id=49336573#49339050), 2026-08-17 23:22:47 UTC)
        Thanks for the feedback.

        It's getting those abstract ideas back out from the word-vomit I find very difficult. It is almost completely impenetrable to me to read that text - even though I wrote it!

        Someone in another comment ([https://news.ycombinator.com/item?id=49338214](https://news.ycombinator.com/item?id=49338214)) has shown a prompt to just break it up and fix the sentence structure rather than rewriting, which should hopefully help me to at least re-read what I have written.

      - **x-complexity** ([comment](https://news.ycombinator.com/item?id=49336573#49339889), 2026-08-18 01:11:07 UTC)
        > Yes, it's messy and unpolished, maybe even a little hard to parse, but it's so much richer for it.

        ...This part immediately made me link it to the hipster stereotype:

        "oh, it's sooooo much better on vinyl because you can hear the cracks & pops"

        Neither pieces in the chat log work for me: The prompt was a wall of ramblespeak. The output was a presentation that should've been an email.

        - **johnnyanmac** ([comment](https://news.ycombinator.com/item?id=49336573#49342562), 2026-08-18 07:31:17 UTC)
          "More interesting" =/= "good". Yes, at the end of the day it's a very derisive rant against people the writer feels is too hard on AI and a defense on how they personally wield it. With a slightly ill intent to create a messy, unstructured writing in the prompt to support his point of "see, people like pretty words!".

          Even the attempt of using Claude to be a fancy formatter failed when you look closely at the language employed in the final prompt. It's trying to convey the same ideas with better foratting, but still softens up the derision the author clearly has here. Which is the interesting part in my eyes.

          - **supermatt** ([comment](https://news.ycombinator.com/item?id=49336573#49343562), 2026-08-18 10:13:55 UTC)
            > a very derisive rant... the derision the author clearly has...

            You either do not know what derisive means or have worse reading comprehension than I do! /derision

            Seriously though - it's literally just talking about the use of an LLM as an accessibility aid and argues that the LLM-assisted writing can still contain human thought. What specifically did you consider contemptuous or mocking?

            FYI: [https://claude.ai/share/601e313e-905c-4e4a-bb6a-24a1315013e5](https://claude.ai/share/601e313e-905c-4e4a-bb6a-24a1315013e5)

            > slightly ill intent

            There was no ill intent. The content itself described the reason for the process. Even simple comments I write here end up with multiple edits over the hour-long edit window.

            If you read my entire comment history you will find I rarely make more than a single observation per comment. Anything more complex becomes too difficult to read and revise.

            Cognitive impairment is extremely difficult to understand until you have experienced it. I am particularly lucid this afternoon. That doesn't mean the difficulty is not real.

    - **an0malous** ([comment](https://news.ycombinator.com/item?id=49336573#49338438), 2026-08-17 22:19:01 UTC)
      I think you intentionally sandbagged your prompt by dragging on and being repetitive and it’s still a better read than the LLM output.

      There’s also a difference between “please edit my writing” and “please generate a blog post from these bullet points.”

    - **voxelghost** ([comment](https://news.ycombinator.com/item?id=49336573#49341422), 2026-08-18 04:53:07 UTC)
      I asked claude 4.5 :
      """
      Please, with an absolute minimum of content modification, edit this text with proper paragraph-formatting, spelling, punctuation and grammar. Do not alter vocabulary, language, or tone.
      """

      And then fed it your input.

      And the output was a very easily readable, enjoyable plain-ascii-text, with no Ai-ick, except for an em-dash or two.

      Tried pasting it here, but that removed paragraph formatting

      - **supermatt** ([comment](https://news.ycombinator.com/item?id=49336573#49341472), 2026-08-18 05:00:51 UTC)
        Thank you. Someone else posted similar with ChatGPT and it looks like that strategy could be a way for me to manually edit a lot more easily.

    - **flitzofolov** ([comment](https://news.ycombinator.com/item?id=49336573#49339855), 2026-08-18 01:05:22 UTC)
      This is actually a great representation of what is good and what is insidious about LLM assisted writing.

      The practice of writing can serve the purpose of conveying an idea or information to the readers, but it can also be an invaluable tool for the writer to process, digest, and internalize a message.

      The act of wordsmithing, and shaping the idea from its raw rambling form into a coherent narrative, is intellectual metabolism.

      A good writer will both distill the ideas, present them in such a way that will be pleasurable to their readers, and also bring the reader along the way so they can learn as well, and feel like an active participant.

      The LLM tend to produce prose that defeats the purpose for the writer, takes the joy out for the reader, and ultimately does nothing for anyone but take up space.

      It's not more words that make good stories, and it's not more code that makes good programs. It's what use is this to anyone, and only humans understand what other humans want and only humans can care.

      Seems like people in this thread agree that it's better to express oneself in a less skilled fashion but actually write something that represents your idea, than to present some polished turd and pass it off as your own writing.

      Same as a birthday card on some stock paper written in crayon will always be more valuable than a store bought card with generic sentiment.

    - **fireflash38** ([comment](https://news.ycombinator.com/item?id=49336573#49344268), 2026-08-18 11:45:54 UTC)
      I think it's hilarious how AI took something personal and the very first thing it spews out is a classic AI-ism.

      Do you read over what the AI spits out? Do you read over what you write?

      It takes time to do either, and both are the things that I think are actually useful.

    - **jcranmer** ([comment](https://news.ycombinator.com/item?id=49336573#49339472), 2026-08-18 00:12:31 UTC)
      The stream-of-consciousness is only hard to read because it lacks paragraph breaks, sometimes sentence breaks, and there's so many misspelled words. If you just tweak it to fix that stuff, it becomes fairly readable, like most internet comments or whatnot. (Which do you think this comment is, a polished essay, or lightly-formatted stream of consciousness?)

      Meanwhile, the LLM-generated essay is hard to read because it's essentially the high-school essay that's padding its paper to meet a minimum page count. I'm surprised that you find it easier to read than most human text, because I've invariably found that my first reaction to LLM-generated text is "where's the point?"--everything is just buried in so much *fluff*.

      So yeah, I find the prompt much better than the LLM output.

      - **supermatt** ([comment](https://news.ycombinator.com/item?id=49336573#49339728), 2026-08-18 00:46:27 UTC)
        Thanks. Im actually seeing that myself since someone helped me with formatting the word salad.

    - **swatcoder** ([comment](https://news.ycombinator.com/item?id=49336573#49337878), 2026-08-17 21:26:43 UTC)
      Sure enough, the prompt is infinitely more expressive and interesting.

      AI writing is like the voice anonymizer they'd use in TV interviews when they wanted to hide the identity of the person speaking. The output is more adherant to convention but likewise more impersonal and exhausting, and when it's used by too many people it's so indistint that it becomes noise.

      It might look good to you in isolation, because you're excited to see that it says what you meant to say without the features you feel self-conscious about, but to others it just reads like yet another sample of the same old AI slop. The message gets entirely lost behind that.

    - **jmilloy** ([comment](https://news.ycombinator.com/item?id=49336573#49340804), 2026-08-18 03:13:01 UTC)
      I read your entire jumbled stream joyfully and hated the llm article that was spit out.

    - **nunez** ([comment](https://news.ycombinator.com/item?id=49336573#49339762), 2026-08-18 00:52:25 UTC)
      definitely prefer the rambling; i can break it up into paragraphs sans LLM

    - **mrheosuper** ([comment](https://news.ycombinator.com/item?id=49336573#49340423), 2026-08-18 02:25:31 UTC)
      while both are difficult to read, i enjoy reading the prompt more, it feels more human (don't know exactly what).

  - **raincole** ([comment](https://news.ycombinator.com/item?id=49336573#49337790), 2026-08-17 21:19:01 UTC)
    The prompt is the whole chat history. It would be like 10~20 times longer than the final output if the author gave the slightest amount of shit.

    - **Alpha3031** ([comment](https://news.ycombinator.com/item?id=49336573#49338521), 2026-08-17 22:25:46 UTC)
      The author giving the slightest amount of shit seems like a big assumption to make, but ultimately even it that were the case I don't see why I would prefer what I read to be curated in that specific manner (having access only to what has been filtered past some black box). As opposed to being able to choose what to read from the whole chat history.

  - **CuriouslyC** ([comment](https://news.ycombinator.com/item?id=49336573#49340925), 2026-08-18 03:33:08 UTC)
    Would you prefer a 10k word discussion with an agent about a hypothesis with back and forth over data sources and such, analysis, etc, or a 2000 word AI essay condensate with the rough edges smoothed over manually?

  - **jampa** ([comment](https://news.ycombinator.com/item?id=49336573#49337761), 2026-08-17 21:16:39 UTC)
    I used to do that, but the person could be bad at prompting too (which is often why the LLM couldn't give a good answer in the first place).

    So the polite version I use now is: "Hey, just to get a bit more context, what was the original problem you were trying to solve?".

    That gets them to distill their own problem a bit further.

  - **coderatlarge** ([comment](https://news.ycombinator.com/item?id=49336573#49338134), 2026-08-17 21:46:56 UTC)
    i personally prompt to produce a baseline then re-prompt to tweak then re-re-prompt to re-order, then re-re-re-prompt to expand certain parts, then re-re-re-reprompt to properly cross reference internally , then re-re-re-re-reprompt to proof read and add missing references . so there is no single prompt that produced the document and if i were to start from scratch the path would likely be different.

  - **hinkley** ([comment](https://news.ycombinator.com/item?id=49336573#49339739), 2026-08-18 00:48:43 UTC)
    Somewhere in that wall of text is a single statement that might sink the entire project...

  - **snmx999** ([comment](https://news.ycombinator.com/item?id=49336573#49337252), 2026-08-17 20:34:35 UTC)
    Not all AI content was created with one prompt.

  - **m132** ([comment](https://news.ycombinator.com/item?id=49336573#49337583), 2026-08-17 21:02:05 UTC)
    I like how some people take offence at that

    - **fallingbananna** ([comment](https://news.ycombinator.com/item?id=49336573#49343527), 2026-08-18 10:08:08 UTC)
      I don't like it. I don't take any offence. It just triggers the same AI;DR for me.

      If I think the task requires a human to think about it. And the person is the human paid to think about it. Whether I get a wall of AI text, prompt, or an entire AI conversation... there is no human insight in it.

      If that person took the time to think about the problem, had a chat with the AI, and understood the output, surely they can take the final step and tell me the short result/summary themselves, right?

      ---

      However, if I had to choose lesser evil, I would of course prefer to have a link to the AI conversation over having a wall of text directly in the conversation.

  - **globular-toast** ([comment](https://news.ycombinator.com/item?id=49336573#49342794), 2026-08-18 08:02:48 UTC)
    Yeah, my post is more than a year old at this point: [https://blog.gpkb.org/posts/just-send-me-the-prompt/](https://blog.gpkb.org/posts/just-send-me-the-prompt/)

    A lot of people replying seem to be misunderstanding, though. The only point of human-to-human communication is to transmit thoughts from one brain to another. If you simply send me stuff from AI then *I don't need you*. I want to hear *your* thoughts. If you don't have any, then I don't need or want to hear from you. Your thoughts are entirely contained within your prompts. Just send me those.

  - **paulpauper** ([comment](https://news.ycombinator.com/item?id=49336573#49337052), 2026-08-17 20:21:39 UTC)
    Many people use many prompts and revisions or prompts or combinations or human and AI writing. Its not a simple as just making a single prompt and copying the output as the blog post.

    - **pelotron** ([comment](https://news.ycombinator.com/item?id=49336573#49337668), 2026-08-17 21:08:49 UTC)
      They could prompt the AI to scroll up and copy their previous prompts for them.

    - **rsalus** ([comment](https://news.ycombinator.com/item?id=49336573#49337260), 2026-08-17 20:35:11 UTC)
      Yeah, by the time my thought is fully formed I've gone through an entire conversation.

  - **onion2k** ([comment](https://news.ycombinator.com/item?id=49336573#49337294), 2026-08-17 20:37:59 UTC)
    That implies you think the output of an LLM is *only* a rewording of the prompt, and that it doesn't add anything from it's corpus of training data. That's obviously untrue.

    - **andriamanitra** ([comment](https://news.ycombinator.com/item?id=49336573#49338971), 2026-08-17 23:12:41 UTC)
      Even when LLMs add something it's a better idea to let the *readers* use LLMs to augment content. They have the best knowledge of their own background and what they're looking for.

      Sharing information that is already in the corpus is simply not that valuable in a world where everyone has access to their own LLMs.

    - **Alpha3031** ([comment](https://news.ycombinator.com/item?id=49336573#49338696), 2026-08-17 22:44:58 UTC)
      I'm in the "post both and let your readers figure out which, if any, they prefer" camp but even if you didn't (and unless you were using one of those super special models that can't be released according to the companies) I would hope that any literate adult that thought it valuable would be capable of consulting something with comparable knowledge and experience.

      Of course, given that posting one is not mutually exclusive with posting the other, I would still think that posting both is the easiest way to satisfy both people who prefer to read the prompt and those who prefer the read the output.

- **neilv** ([comment](https://news.ycombinator.com/item?id=49336573#49337044), 2026-08-17 20:21:09 UTC)
  > *Look, I get it. It’s Q3 2026, and we should expect that everyone is utilizing AI at SOME point in their process (sourcing ideas, creating outlines, refining prose, etc.).*

  Sounds like this isn't everyone, but rather, it's people who have nothing to say, and -- even after they've "sourced ideas" -- they don't know how to reason about it, nor how to communicate it.

  This isn't everyone.  This is people engaged in generating noise, for the sake of noise.

- **bawana** ([comment](https://news.ycombinator.com/item?id=49336573#49344191), 2026-08-18 11:37:56 UTC)
  Verbosity and ‘helpfulness’ is by design to increase token use. ‘The elements of style’ by strunk and white is part of my system prompt

- **jannyfer** ([comment](https://news.ycombinator.com/item?id=49336573#49336883), 2026-08-17 20:11:10 UTC)
  [https://hn.algolia.com/?dateRange=all&page=2&prefix=false&qu...](https://hn.algolia.com/?dateRange=all&page=2&prefix=false&query=%22ai%3BDR%22&sort=byDate&type=comment)

  [https://news.ycombinator.com/item?id=46991394](https://news.ycombinator.com/item?id=46991394)

  - **Fantosism** ([comment](https://news.ycombinator.com/item?id=49336573#49336942), 2026-08-17 20:15:10 UTC)
    Thank you. Felt like I was stuck in a time loop.

- **sega_sai** ([comment](https://news.ycombinator.com/item?id=49336573#49336762), 2026-08-17 20:03:21 UTC)
  If some text is AI written as a response to a much shorter prompt, then the prompt and/or sources used to make the text should be published instead (or at the very least together with the text).

  - **al_borland** ([comment](https://news.ycombinator.com/item?id=49336573#49337084), 2026-08-17 20:24:07 UTC)
    I had to do this with my boss. He sent an email saying he asked AI about an assignment he gave us, then sent us the reply from the LLM. It was verbose and lacked any and all awareness of the constraints we have within the company. The assignment was poorly defined from the outset, and I asked for the prompt he used, because I thought that would be far more useful to understand what *he* was looking for rather than what AI decided to spit back.

    It turned out his prompt was equally uninspired... 1 or 2 sentences. That was the thought he put into it, which then had us spending hours trying to figure out the AI reply. He could have saved the whole team a full day by just sending the prompt... or nothing at all.

    - **Gigachad** ([comment](https://news.ycombinator.com/item?id=49336573#49338750), 2026-08-17 22:49:29 UTC)
      Having this problem a lot at work currently. Every single jira ticket is a novel worth of useless text you have to skip over to find the human written parts. Occasionally important details get lost in the noise because they are sandwiched between slop.

  - **bessbd** ([comment](https://news.ycombinator.com/item?id=49336573#49337088), 2026-08-17 20:24:24 UTC)
    I wish I could do a "right-click -> view page source"-like "right click -> view prompt" or like the dark mode toggle (prompt <-> ai slop (expanded)), depending on my mood (although almost everything is in constant dark mode, so I believe I'd look mostly at the prompts)

  - **beloch** ([comment](https://news.ycombinator.com/item?id=49336573#49337157), 2026-08-17 20:28:08 UTC)
    The infinite monkey theorem[1] can be applied to show that AI is not incapable of producing quality output.  However, expecting your audience to sort through the output from a very large quantity of monkeys is not respectful.  I think the best approach would be:

    "Here is the prompt and model I used, here is the *portion of the output* that stuck out to me as relevant and useful, and here, in my own words, is why I think that is so."

    i.e. Highlight the good part of the output for me and, preferably, explain why you think it's good.  Otherwise it's the same thing as posting slop, only with extra steps.  You thought it was worth posting and I thought that made it worth looking at, but now I'm sorting through a bunch of monkey garbage looking for what made you think that.  Being a different person, I may not find that hidden gem and I may become quite frustrated with you.

    ________________

    [1][https://en.wikipedia.org/wiki/Infinite_monkey_theorem](https://en.wikipedia.org/wiki/Infinite_monkey_theorem)

  - **zirkonit** ([comment](https://news.ycombinator.com/item?id=49336573#49337174), 2026-08-17 20:29:35 UTC)
    Funnily enough, for me AI writing is usually the summarizer rather than expander. I would usually give Claude 2-3x the amount of data in notes, context, braindump etc; when doing person-to-person communication, using AI to _expand_ the context rather than shrink it is doing everyone a disservice.

    - **JimTheMan** ([comment](https://news.ycombinator.com/item?id=49336573#49339642), 2026-08-18 00:35:09 UTC)
      The problems with AI text is mostly a 'skill issue' or 'taste issue'.

      It's a tool like any other. It assists the intelligent, but makes the lazy - lazi-er.

  - **add-sub-mul-div** ([comment](https://news.ycombinator.com/item?id=49336573#49336812), 2026-08-17 20:06:20 UTC)
    I think of a prompt more like a tweet. The medium does matter. If someone was only willing or able to put an abbreviated amount of thought and effort into something, it's not worth a disproportionate amount my time or attention.

    - **JoshTriplett** ([comment](https://news.ycombinator.com/item?id=49336573#49336844), 2026-08-17 20:08:32 UTC)
      Exactly. And I think the information theory matters here: it's worth putting in information proportional to the human-supplied input, not proportional to the AI-expanded output.

    - **paulpauper** ([comment](https://news.ycombinator.com/item?id=49336573#49337132), 2026-08-17 20:26:32 UTC)
      It's like  "inverse twitter "

  - **perching_aix** ([comment](https://news.ycombinator.com/item?id=49336573#49336946), 2026-08-17 20:15:16 UTC)
    "please walk our observability stacks, our IaC code and config, our cloud account, and our application codebases to gather an RCA for for any errored out request responses we've been producing this week. include a tabulated breakdown."

    ~actual prompt i sent in to claude last week. doing what you propose would be basically impossible / nonsensical, and further undo the entire exercise, sending all the money spent on the tokens down the toilet.

    put differently, if you use agents in any actually useful manner, the principle you describe erases whatever value they did end up providing. though since the whole underlying premise is that ai never provides any value, maybe that's the intended result and is as expected. in which case, i'd argue such a desire is more than a bit demagogue.

- **CyberMacGyver** ([comment](https://news.ycombinator.com/item?id=49336573#49336890), 2026-08-17 20:11:40 UTC)
  Don’t be a meat proxy [0] is another one I like

  [0] [https://news.ycombinator.com/item?id=49151933](https://news.ycombinator.com/item?id=49151933)

- **slybot** ([comment](https://news.ycombinator.com/item?id=49336573#49337001), 2026-08-17 20:18:20 UTC)
  3 years ago; [https://news.ycombinator.com/item?id=35638229](https://news.ycombinator.com/item?id=35638229)

- **hatthew** ([comment](https://news.ycombinator.com/item?id=49336573#49337545), 2026-08-17 20:58:38 UTC)
  One of the ways I think about this is to treat AI as if it were another person. If I want to give information to Bob but I think Alice might do a better job of writing something, I'm not going to ask Alice and then copy-paste her response to Bob. I'd either tell Bob to ask Alice, or loop Alice into the conversation. Me being the middleman between Alice and Bob can cause several issues including delayed communication, miscommunication, and obscured provenance.

  Alice being AI or a real person doesn't change those factors much.

  - **CuriouslyC** ([comment](https://news.ycombinator.com/item?id=49336573#49340984), 2026-08-18 03:40:56 UTC)
    I think this is a reasonable position, I prefer when people separate their words from their agent's words clearly, but I don't have a problem with reading stuff other people's agents wrote if the input to the writing was really good. I don't need to see the prompt, not having your agent Cyrano me is enough.

- **pavon** ([comment](https://news.ycombinator.com/item?id=49336573#49336748), 2026-08-17 20:02:18 UTC)
  AI—DR

  - **phito** ([comment](https://news.ycombinator.com/item?id=49336573#49343141), 2026-08-18 08:58:48 UTC)
    It's late and you've already done what most people aren't doing — go rest.

  - **orc00** ([comment](https://news.ycombinator.com/item?id=49336573#49337766), 2026-08-17 21:16:57 UTC)
    You've addressed a load-bearing seam.

    - **krat0sprakhar** ([comment](https://news.ycombinator.com/item?id=49336573#49337994), 2026-08-17 21:35:55 UTC)
      Haha, this is my favorite one so far. Well done sir

  - **GPerson** ([comment](https://news.ycombinator.com/item?id=49336573#49337500), 2026-08-17 20:54:10 UTC)
    You’ve hit your session limit

  - **armanj** ([comment](https://news.ycombinator.com/item?id=49336573#49337104), 2026-08-17 20:24:57 UTC)
    You're absolutely right

  - **hamdingers** ([comment](https://news.ycombinator.com/item?id=49336573#49337133), 2026-08-17 20:26:36 UTC)
    Now I have the full picture

  - **sethops1** ([comment](https://news.ycombinator.com/item?id=49336573#49338675), 2026-08-17 22:42:48 UTC)
    Google Gemini is experiencing high load at the moment.

  - **attheballot** ([comment](https://news.ycombinator.com/item?id=49336573#49342750), 2026-08-18 07:56:45 UTC)
    This bit in particular

    > Look, I get it. It’s Q3 2026, and we should expect that everyone is utilizing AI at SOME point in their process (sourcing ideas, creating outlines, refining prose, etc.).

    I stopped reading there.

    - **r_lee** ([comment](https://news.ycombinator.com/item?id=49336573#49343016), 2026-08-18 08:37:08 UTC)
      I really don't understand the "refining prose"

      it's more like, "refining prose so that nobody sane will bother reading it". like wow it's so useful to claudefy your thoughts, wow look at how amazing your blog post looks now with how much more slop you produced from your prompt, amazing.

      I really wonder like, do those authors not think from the perspective of the reader?

  - **marton78** ([comment](https://news.ycombinator.com/item?id=49336573#49337492), 2026-08-17 20:53:45 UTC)
    this is based on actual measurements, not just guesswork

  - **hidelooktropic** ([comment](https://news.ycombinator.com/item?id=49336573#49336756), 2026-08-17 20:02:59 UTC)
    I get this reference

  - **Gecko4072** ([comment](https://news.ycombinator.com/item?id=49336573#49337170), 2026-08-17 20:29:27 UTC)
    You hit the nail on the head.

  - **DamnInteresting** ([comment](https://news.ycombinator.com/item?id=49336573#49337505), 2026-08-17 20:54:35 UTC)
    I appreciate the pushback!

  - **cobolexpert** ([comment](https://news.ycombinator.com/item?id=49336573#49336971), 2026-08-17 20:16:34 UTC)
    You closed the gap

  - **incognito124** ([comment](https://news.ycombinator.com/item?id=49336573#49337096), 2026-08-17 20:24:36 UTC)
    genuinely amazing

  - **Applejinx** ([comment](https://news.ycombinator.com/item?id=49336573#49337353), 2026-08-17 20:43:09 UTC)
    Love the em-dash. Chef's-kiss.

  - **mock-possum** ([comment](https://news.ycombinator.com/item?id=49336573#49337045), 2026-08-17 20:21:11 UTC)
    That’s the shape of it

  - **bratr** ([comment](https://news.ycombinator.com/item?id=49336573#49336959), 2026-08-17 20:15:56 UTC)
    here's a honest take

  - **r_lee** ([comment](https://news.ycombinator.com/item?id=49336573#49336821), 2026-08-17 20:06:49 UTC)
    that's load-bearing

  - **mukize** ([comment](https://news.ycombinator.com/item?id=49336573#49337405), 2026-08-17 20:47:09 UTC)
    and honestly—that's the seam right there.

- **Lerc** ([comment](https://news.ycombinator.com/item?id=49336573#49339292), 2026-08-17 23:52:07 UTC)
  For me the bar is still quality.  Sure it bothers me if I search for something and find a crappy AI written tutorial that answers none of my questions,  but if I found a high quality well written, insightful, and informative tutorial, I would not care if it were AI written.

  I guess the same thing goes for articles written by humans.   I don't really read the articles that are "Shower thoughts that I think are profound" or "The way I do things is the way everyone should do things"

  There is a fairly common wisdom that the way you get good at writing is by writing a lot, I'm prepared to cut people a lot of leeway at people putting all of the stuff out there before they are good at writing.  It's just the path you have to take.  That's OK, because I don't have to read it.

  And I'm fine with people making crappy AI generated tutorials while they figure out how to make better AI generated tutorials.  I am not fond of people who are creating bulk content by volume without any regard to quality or improvement.  Some may be doing this to make money,  and maybe that works, I suspect for the most part it doesn't.  I don't appreciate it though, whether it be AI or human produced bulk content.

  I'd spare a thought for those who feel that they are producing high quality content when they are not.  Everyone has a poor perspective on something sometimes.  Usually the harshest punishment they will face is the feelings their future selves experience when they look upon their work with a more balanced perspective.

- **mikhmha** ([comment](https://news.ycombinator.com/item?id=49336573#49339633), 2026-08-18 00:33:31 UTC)
  Recently I've gotten lots of DM's from boutique marketing firms offering to promote the game i'm working on. I'm pretty sure they all find leads via scraping the Steam API. Many of these small firms are people in developing countries.

  It's frustrating dealing with them since they all use AI in communications. Everything is written so flowery and with so much extra words. Any feedback I give is met with overwhelming praise about "how right I am". Its exhausting.

  I understand many of them are in developing countries and aren't confident in their English skills. But I always tell them I'd rather they write in broken English to communicate their own ideas. I want to hear what they have to say, directly from their brain. I don't have issues with parsing bad english. Usually its straight and to the point.

  They always end up defaulting back to AI messaging. Even when I tell them to be genuine. I'd love to give one of these firms a chance, but they fail this basic step. I think they think everyone in the developed world likes AI or something.

- **devrob** ([comment](https://news.ycombinator.com/item?id=49336573#49339429), 2026-08-18 00:06:23 UTC)
  I used to have a rolling product satire I called "Claude Handshake" which basically explained how cold-email is dead today as people feed email contents into Claude and Claude responds with a draft, that usually comes from another person doing the same thing.

  The idea was to just avoid sending email altogether and just simulate the interaction entirely using Claude.

- **nektro** ([comment](https://news.ycombinator.com/item?id=49336573#49341638), 2026-08-18 05:33:57 UTC)
  > Yes, there are certain situations in which we should expect 100% AI-generated copy. Customer support would be a perfect example.

  hard disagree on this

- **ronbenton** ([comment](https://news.ycombinator.com/item?id=49336573#49337390), 2026-08-17 20:45:53 UTC)
  Anyone else have coworkers responding to your human PR review comments with AI? I feel like I'm taking crazy pills, how can anyone find this socially acceptable?

- **Alephinitesimal** ([comment](https://news.ycombinator.com/item?id=49336573#49341892), 2026-08-18 06:07:03 UTC)
  I once spent two days on a pr and got an obviously AI generated review that contradicted what we agreed one before. So I had AI respond to it.
  The next day he asked if I'd used AI. I used the same justification he'd used for his review.
  Fight magic with magic. He never reviewed my pr that way again.

- **firefoxd** ([comment](https://news.ycombinator.com/item?id=49336573#49338230), 2026-08-17 21:54:54 UTC)
  I've asked questions to people who wrote interesting articles where I didn't know it was AI generated. But then, they couldn't really answer me because most examples in the article wasn't something they experienced themselves. So basically, we were both reading the article for the first time, with made up scenarios.

- **atleastoptimal** ([comment](https://news.ycombinator.com/item?id=49336573#49337900), 2026-08-17 21:29:11 UTC)
  The problem is that in most domains we reward effort sometimes even more than results, especially in fields where results are hard to verify. A wall of text is the classic way to signal effort and delay feedback, a signal which was costly pre-AI, but now is not costly. However norms have not shifted.

- **meerita** ([comment](https://news.ycombinator.com/item?id=49336573#49343204), 2026-08-18 09:07:34 UTC)
  I am writing excellent documentation with AI. The key success is to have rules to write documentation, PRs, commits, etc. I use ASD-STE100 and some constraints on what to write, how, and what it matters to my projects.

  - **dominicq** ([comment](https://news.ycombinator.com/item?id=49336573#49343899), 2026-08-18 11:03:11 UTC)
    doubt

- **Sha1rholder** ([comment](https://news.ycombinator.com/item?id=49336573#49337417), 2026-08-17 20:48:08 UTC)
  I personally don't care whether a piece of writing was AI-generated as long as it's useful or insightful.

  However there's only 10% of AI-generated writing that is worth reading. If some articles convince me that there's somebody behind it contributing valuable understanding, I'm willing to overlook the telltale AI mannerisms. It's understandable that some domain experts aren't very proficient in English.

  That said, statistically speaking 90% AI-generated pieces are a waste of readers' time. It's a good strategy to simply skip them.

  I know this looks like a bot comment. It's not. It's a much older style of writing known as *Chinglish*. That's why as a non-native English speaker, I can totally understand why someone would want to use AI to help with their writing.

- **ProCodeSoftware** ([comment](https://news.ycombinator.com/item?id=49336573#49337497), 2026-08-17 20:54:01 UTC)
  I have been feeling the same way for the past few months. I just want to say I will never read a paragraph that has signs of AI, because most of the time, the people didn't put much effort in it. I don't care if it is factually correct or not.

- **dbspin** ([comment](https://news.ycombinator.com/item?id=49336573#49337019), 2026-08-17 20:19:30 UTC)
  "Look, I get it. It’s Q3 2026, and we should expect that everyone is utilizing AI at SOME point in their process (sourcing ideas, creating outlines, refining prose, etc.)."

  Hell no. Sourcing ideas? From AI? Are you kidding? Essentially guaranteeing they won't be original? Refining prose? Making it much more likely it'll be generic as hell. Call me old fashioned, but while I can certainly understand asking LLMs concrete questions - how do I fix this, where can I unsubscribe from that - using AI to help communicate seems bass-ackwards. LLMs have no idea what you're talking about - they're free associating probabilistic sentences! What on earth value could that have in communicating. They self contradict, hallucinate, speak most frequently in a weird smug corporatese. How is this an attractive use case of the technology?

  - **yoz-y** ([comment](https://news.ycombinator.com/item?id=49336573#49341903), 2026-08-18 06:08:59 UTC)
    Sourcing ideas just seems so weird… if you don’t have an idea about what to make, then just don’t ?

- **TRiG_Ireland** ([comment](https://news.ycombinator.com/item?id=49336573#49344305), 2026-08-18 11:49:52 UTC)
  "It’s Q3 2026, and we should expect that everyone is utilizing AI at SOME point in their process."

  No. Very much no.

- **teo_zero** ([comment](https://news.ycombinator.com/item?id=49336573#49342493), 2026-08-18 07:25:01 UTC)
  Whenever I'm tempted to base my judgment on *how* something's been created rather than *what* the end result is, I think about the scene where Sheldon throws away the french toast Penny made for him, despite smelling good, just because "Monday is oatmeal day."

  - **gavinsyancey** ([comment](https://news.ycombinator.com/item?id=49336573#49342633), 2026-08-18 07:39:50 UTC)
    Before LLMs came around, it took quite a bit more effort to write something than to read it. So the fact that someone had taken the time to create something was a signal that they thought it was worth that effort, and so it might be worth my (lesser) effort to read it. And even with that filter there was a lot of human-created crap out there.

    I value my time. With a LLM, it takes very little effort to create a vast mountain of crap that will take a lot of time and effort to read through. True, it is also possible to use LLMs as a tool while creating things that are not worthless. But the fact that someone has not taken the time to make their thing not sound obviously AI-generated is a strong signal that it will not be worth my time.

- **runtime_lens** ([comment](https://news.ycombinator.com/item?id=49336573#49343164), 2026-08-18 09:02:17 UTC)
  AI comments are becoming a second documentation system nobody asked for. If the code is self-explanatory, “why this is good” is usually just noise.

- **brunoborges** ([comment](https://news.ycombinator.com/item?id=49336573#49337074), 2026-08-17 20:23:12 UTC)
  If a coworker sends me an AI generated report to help on my task, I am more likely to ask them to just send me the prompt and model they used. Let me own the session and steer it however I want.

  - **paulpauper** ([comment](https://news.ycombinator.com/item?id=49336573#49337105), 2026-08-17 20:24:58 UTC)
    Then put the report in AI and have it read it . that is the only appropriate response

    - **brunoborges** ([comment](https://news.ycombinator.com/item?id=49336573#49337673), 2026-08-17 21:09:14 UTC)
      I believe I have better context data in my session than someone simply prompting based on hearsay of what they think they know about the task I have at hand.

      Also, I may have already started looking into it, but now this other person just wasted money.

- **jumploops** ([comment](https://news.ycombinator.com/item?id=49336573#49337898), 2026-08-17 21:28:44 UTC)
  > I’m SUPER jealous that I didn’t think of this first...

  Not to toot my own horn, but...[0]

  On a more serious note, we're planning a trip with family, and my mother-in-law asked if I'd read "the planning doc" yet.

  It was a shared ChatGPT thread. Thankfully I read enough LLM output to skim it easily and avoid offending her (:

  [0][https://x.com/jumploops/status/2031936768023638069](https://x.com/jumploops/status/2031936768023638069)

- **keithnz** ([comment](https://news.ycombinator.com/item?id=49336573#49340768), 2026-08-18 03:06:33 UTC)
  Not sure how others are using AI, but for us, an AI dump is actually much better than some human editing/writing it.   What we've found is that people become gatekeepers of context due to their role in the company they have privileged access to certain context, so when some question is asked, the person who's AI has the right context can look at it and generate a response making sure not to leak anything important and making sure the question is not nefarious.  Also important that your AI doesn't generate a wall of text but is super concise.  This works incredibly well for us.

- **dktoao** ([comment](https://news.ycombinator.com/item?id=49336573#49340414), 2026-08-18 02:24:43 UTC)
  There is a sort of symmetry here with there also being things that everyone writes that no one reads.

  * Cover Letters

  * Most test reports

  * Lots of docs required by the government

  * I'm sure there are more you can think of

  So now we can have stuff written that no-one ever writes and no-one ever reads? Hmm...

  - **teo_zero** ([comment](https://news.ycombinator.com/item?id=49336573#49342116), 2026-08-18 06:35:29 UTC)
    Even worse: cover letters, presentation letters, even CVs themselves are routinely read by AI, at least in the screening phase.

- **Gepsens** ([comment](https://news.ycombinator.com/item?id=49336573#49342515), 2026-08-18 07:27:21 UTC)
  We could put comments in separate files with an annotation format. For example:
  ion.cpp.cmt
  And autoremove all comments from source files. Then use plug-ins to toggle comment files within the text editor.

- **ramdump** ([comment](https://news.ycombinator.com/item?id=49336573#49337068), 2026-08-17 20:22:47 UTC)
  The fear I have is that I accuse of AI without being 100% certain. I've not found a good way around this except to talk to the person.

  - **LPisGood** ([comment](https://news.ycombinator.com/item?id=49336573#49337161), 2026-08-17 20:28:23 UTC)
    I left a comment on some of my interns, clearly AI generated code and response asking for him to please not respond with AI generated output — the response was talking about things I had known he was unfamiliar with because I had worked with him. The response itself had some particular formatting/content decisions that were generally a very odd way for anyone to write, but certainly not an intern. He responded that he did write this himself and that he was upset I would accuse him, etc.

    I, of course, had no choice but to apologize. I hope I was right, but clearly there is some chance I was wrong.

  - **Alien1Being** ([comment](https://news.ycombinator.com/item?id=49336573#49337582), 2026-08-17 21:01:50 UTC)
    Pangram does a decent job of AI detection.

- **darrelld** ([comment](https://news.ycombinator.com/item?id=49336573#49337135), 2026-08-17 20:26:39 UTC)
  We have a junior research student who does this on slack.

  Before I think he was using AI and other tools to translate his messages since english isn't his first language. His own words, then AI translated it. Sounded kinda clunky, but I could sense the human behind the words and I gave grace since I can only imagine how hard it is to properly communicate your ideas when English isn't your first language.

  But now it's gotten to a point where I can tell he's not using it for just translation. I'm gonna need to chat with him.

  Redacted example below

  ```Hey @PERSON_WHO_ASKED_QUESTION Both good, and the retrieval one isn't written down anywhere. In order.

  One corpus or four. My lean is one. Same chunks and embeddings tables, source_type column to tell them apart.

  Values I'd propose, flat rather than nested: paper, dataset_description, dataset_readme, dataset_contributors, dataset_records, dataset_files. Description and readme split because their units already differ, one row versus one row per paragraph. A discriminator that can't separate those isn't doing much. The existing 440 rows would need backfilling to paper.

  Chunk id in the same spirit: dataset doi, source type, ord. So EXAMPLE_DOI.

  Worth checking before any of this matters: does chunks.doi carry a foreign key to papers.doi in 0001_init.sql? If it does, a metadata chunk with a dataset doi can't go in that table at all, and separate storage stops being a choice. Ten second read, I haven't done it. Shout if you get there first.

  Retrieval is the one that's bigger than it looks. Search once across everything and nothing guarantees a paper chunk and a metadata chunk both land in the top k. The facts we want relate the two, and the generator can only write those if it sees both sides in the same window. So if one type systematically wins the ranking, that class of fact doesn't get worse. It becomes impossible.

  Which way it goes I don't know. Two mechanisms pull opposite ways. Metadata chunks are short, tens of tokens against roughly 450 for a paper chunk, so they may just lose. But we embed context header plus text, and on a short chunk the header is most of the vector. The header is the dataset name, which is also most of the query. That points the other way.

  Cheaper to measure than argue. Load one dataset's metadata, run a normal dataset level query, record the rank of the first chunk of each source type. Runnable as soon as any one of our four subtasks lands.

  After that it's one pool, per source with quotas, or one pool with a floor per source type. I'd rather not pick before there's a measurement.
  ```

- **hinkley** ([comment](https://news.ycombinator.com/item?id=49336573#49339702), 2026-08-18 00:42:35 UTC)
  This has really started to hit my radar because people are filing PRs with AI generated commit messages that read like a bill being presented to congress. Holy shit, give me a summary.

  I don't know if the contributors are writing any of the code they're submitting or just using AI to hop on every 'help wanted' tagged ticket in every product database but if it looks mostly like a smart human wrote it, which usually takes two rounds of reviews, then it can probably go in.

  But if you make me work for it more than you did I'm just going to close the PR and do it myself.

- **bicepjai** ([comment](https://news.ycombinator.com/item?id=49336573#49339035), 2026-08-17 23:20:50 UTC)
  Totally agree with the core argument.
  I understand there must be some etiquette in the space of llm-writing where writers must respect the readers enough to edit and review. Also, pages and pages of LLM content is not something anyone should be proud about sharing. But we are in this world where condensing an argument is so easy that in the busy lives we live, sometimes some arguments are made with LLMs online. If those arguments are pages, I understand the backlash, but if it’s a terse argument, then I would urge others to address the argument made rather than categorizing them under AI;DR, it’s like ad-llminem in my view.

- **illusive4080** ([comment](https://news.ycombinator.com/item?id=49336573#49340146), 2026-08-18 01:47:51 UTC)
  What do you think of AI generated infographics? Someone at my job is creating them on the daily and sending them around to leadership. I find it lazy and too busy.

- **jedberg** ([comment](https://news.ycombinator.com/item?id=49336573#49338665), 2026-08-17 22:41:43 UTC)
  Every time this comes up I have to ask, how do you know it is AI?  Sure, sometimes there are strong tells, like if they forget to take off the "Do you want me to change anything" at the end.

  But AI was trained on good writing.  Good writing looks like AI.  I've had to reduce my use of em dashes for example because they are an "AI tell".  I used to like using the term "load bearing".

  And the list gets longer every day.  Eventually every mark of a good writer will be an AI tell.

  I don't know how to resolve this.  But I've been accused multiple times of copy/pasting AI when I did no such thing, and it's getting equally frustrating.

  - **bastawhiz** ([comment](https://news.ycombinator.com/item?id=49336573#49338751), 2026-08-17 22:49:29 UTC)
    Can you read something and tell when an author you like wrote it without seeing the attribution? I can. I think most of us could, because people use certain phrases or have a particular style. That doesn't make it bad.

    AI writing isn't actually all that bad. But it has a very specific style, and there are MANY tells. I use Claude every single day, and it's immediately obvious to me when I'm reading something Claude wrote. "It's not X, it's Y" "That's the reframe" "The gap is" I could go on.

    I too like using em dashes, and have been since I learned the keyboard shortcut over a decade ago. I've never been accused of posting ai-written text because of it.

    AI is indeed trained on good writing, but it's also trained on bad writing. And it's post trained on specific things that are writing that aren't good or bad for reasons unrelated to style. What you're left with is a one-size-fits-all writing style. Doing math? Doing medicine? Doing anime waifu role play? It all starts from the same generic milquetoast style until you tell it not to. And to me (and apparently many other people) that's super easy to pick out.

  - **Gigachad** ([comment](https://news.ycombinator.com/item?id=49336573#49338722), 2026-08-17 22:47:10 UTC)
    I know it's AI because the laziest coworker you know just posted 400 paragraphs of text on a minor topic.

    - **jedberg** ([comment](https://news.ycombinator.com/item?id=49336573#49338757), 2026-08-17 22:49:53 UTC)
      Sure, that's one of those obvious tells.  But when I sit and spend 10 minutes making a well thought out and researched comment, and then properly format it in markdown, and then the first response is "this is AI", it's really frustrating.

      - **asadotzler** ([comment](https://news.ycombinator.com/item?id=49336573#49339558), 2026-08-18 00:22:48 UTC)
        If you read more literature you will get better at writing and your writing should stop being as similar to the banal mess that AI spits out. This is on you to differentiate.

        - **jedberg** ([comment](https://news.ycombinator.com/item?id=49336573#49339683), 2026-08-18 00:40:13 UTC)
          I’ve read plenty of literature. So has the AI training. That won’t help. In fact, it will make it worse.

          I even studied writing in college. I’ve written published books and articles. I can write well. But thanks for the tip!

  - **nunez** ([comment](https://news.ycombinator.com/item?id=49336573#49339783), 2026-08-18 00:55:06 UTC)
    It has that feel to it. Hard to describe. It has a very consistent way of writing that gives it away, even if it's rephrase from text that was previously written by a human.

    Beyond that, most AI content is WAY WAY WAY WAY WAY longer than it needs to be to get its point across and is oversaturated with unneeded "mic drop" phrases

  - **twoodfin** ([comment](https://news.ycombinator.com/item?id=49336573#49339253), 2026-08-17 23:46:03 UTC)
    The problem with AI writing isn’t the tics and the tells. The problem with AI writing is that it’s *bad*.

    The typical highly voted HN AI-written post has an annoying clickbait title, then jumps into a meandering chain of “so there I was” scene-setting, assertions of dubious reliability & relevance, and supposed supporting examples. All punctuated by short, unhelpfully dramatic sentences that would interrupt the high-level narrative, if only there were one.

    I’m really curious what “good AI writing” you had in mind. My personal intuition is that for almost any topic, the HN LLM-generated post *du jour* has a far superior cousin sitting in the archive pre-2021.

- **whstl** ([comment](https://news.ycombinator.com/item?id=49336573#49336930), 2026-08-17 20:14:15 UTC)
  There is a light at the end of the tunnel for all the minds burned out by AI slop.

  I already saw someone getting fired for only producing AI text as part of their entire output, after being unable to explain what they “wrote” in multiple situations.

  And recently my company enacted a mandate that text made for humans should not be AI generated.

  Sooner or later every company will start realizing that this is just people too lazy to actually work and coasting on a paycheck, at the expense of every other worker.

  - **LPisGood** ([comment](https://news.ycombinator.com/item?id=49336573#49337192), 2026-08-17 20:30:38 UTC)
    This makes me happy to hear that someone got fired for that, but I just cannot picture that happening at my organization. Perhaps standards are too low. What sort of thing did they get fired for? Was there some warning etc?

    - **whstl** ([comment](https://news.ycombinator.com/item?id=49336573#49337340), 2026-08-17 20:42:20 UTC)
      Product Manager using Jira AI to hallucinate tickets, epics, metrics and roadmap. Even the numbers were completely made up.

      There were too many incidents of “this doesn’t look right” in the same week, so when their boss did a thorough check a couple days after, it was all fake, everything. Eventually they admitted and got canned.

      - **LPisGood** ([comment](https://news.ycombinator.com/item?id=49336573#49338019), 2026-08-17 21:38:45 UTC)
        I don’t understand the level of incompetence that would lead someone to that state.

  - **rfff2** ([comment](https://news.ycombinator.com/item?id=49336573#49336952), 2026-08-17 20:15:40 UTC)
    Yup sooner or later the new heuristic will be quality of comms measured by how short a thing is rather than how long.

    Much how like essay's have a word limit - and people think you should max it out.

    We will go in the opposite direction - which I'll be glad about!

  - **ModernMech** ([comment](https://news.ycombinator.com/item?id=49336573#49337118), 2026-08-17 20:25:36 UTC)
    But they got fired for not being able to explain it, not for using it.

    - **whstl** ([comment](https://news.ycombinator.com/item?id=49336573#49337284), 2026-08-17 20:37:20 UTC)
      It’s not as if he was advertising to the world that he wasn’t really working.

- **Gecko4072** ([comment](https://news.ycombinator.com/item?id=49336573#49336811), 2026-08-17 20:06:08 UTC)
  I thought this was: I summarized with AI; didn't read.

  - **adroitboss** ([comment](https://news.ycombinator.com/item?id=49336573#49336854), 2026-08-17 20:08:56 UTC)
    I thought the exact same. There is also a growing problem with people using AI to summarize everything instead of reading the actual text. I thought this addressed that issue by having a section for the AI to help summarize or something similar.

- **anotherevan** ([comment](https://news.ycombinator.com/item?id=49336573#49339315), 2026-08-17 23:54:33 UTC)
  While I don't always agree with everything Drew writes, the title of his blog post[1], "Please stop externalising your costs directly into my face," really resonated with me.

  At the end of the day I don't care how much of what you're presenting is your own words vs AI generated, as long as I can see evidence that you have reviewed and understood what you've passed to me. My resentment and ire is raised when the onus is pushed on me to be the first real human reviewer, having to do all the weighing of merit, practicality and in some cases plausibility that the quote un-quote author should have done before ever hitting send. It's passing the buck and an abdication of responsibility. It is lazy and makes more work for those you foist it upon when your role should be making the effort in your communications to make it easier for the recipient. Not wasting their time having to spend orders of magnitude more effort refuting bullshit you shouldn't have put out there in the first place.

  It is something that has always pissed me off, however AI has made it fair easier for lazy people to think they sound smart and externalise their costs into my face.

  [1] [https://drewdevault.com/blog/Stop-externalizing-your-costs-o...](https://drewdevault.com/blog/Stop-externalizing-your-costs-on-me/)

- **ilaksh** ([comment](https://news.ycombinator.com/item?id=49336573#49338916), 2026-08-17 23:05:50 UTC)
  Valid and fair especially in the 95% of cases where the AI added a lot of unnecessary detail.

  On the other hand, I suspect that we are pretty quickly going to get to the point within a few years where we realize that the best AIs are not just being overly verbose. But rather their communication is just more compressed and thorough.

  So even though we still see a lot of jaggedness and weird failures in some places，in other ways I think this is actually an aspect of intelligence where AI has surpassed humans. Just in terms of being able to deal with a certain density of information.

- **agnishom** ([comment](https://news.ycombinator.com/item?id=49336573#49341403), 2026-08-18 04:50:04 UTC)
  Related:

  Don't Be a Meat Proxy: [https://gruhn.me/blog/2026-08-03/](https://gruhn.me/blog/2026-08-03/)

  No Meat Proxy: [https://nomeatproxy.com/](https://nomeatproxy.com/)

  How to Passive-Aggressively Shame People Who Use LLMs Selfishly: [https://joshmoody.org/blog/selfish-ai/](https://joshmoody.org/blog/selfish-ai/)

- **m12k** ([comment](https://news.ycombinator.com/item?id=49336573#49341500), 2026-08-18 05:06:36 UTC)
  Throwing unread AI output at others is the new version of “sitting on your phone, oblivious to those spending time with you”. Every new consumer technology comes with a new way of being rude.

- **montroser** ([comment](https://news.ycombinator.com/item?id=49336573#49336944), 2026-08-17 20:15:15 UTC)
  I am pro AI, and also deeply share this sentiment.

  I think sometimes people have a big long thread with Claude where they feel enthusiastic about the back and forth being very productive -- and then they genuinely want to share the summary of the conversation with their colleagues so that they can feel it too.  It's not just typing a short prompt and copy/pasting the response.

  But, Claude, especially Opus is *so* unnecessarily flowery, and smug -- and it's *so* identifiably characteristic.

  It somehow rubs salt in the wound: "I didn't take the time to write this out in my own words, so now you get to listen to this petulant asshole mansplain it to you".

  If it would get to the point, and with some humility, it would be a much different proposition.

  - **matheusmoreira** ([comment](https://news.ycombinator.com/item?id=49336573#49339012), 2026-08-17 23:18:19 UTC)
    Only after switching to Sol did I notice how verbose and smug Claude was. Now I wonder if Claude's at least partly responsible for the AI hate.

- **nunez** ([comment](https://news.ycombinator.com/item?id=49336573#49339375), 2026-08-18 00:00:39 UTC)
  > Customer support would be a perfect example. We’re not looking for artisanal “did you make sure to reset your phone” style dialogue.

  Yeah...I'm probably dropping whatever services do this. If the company can't invest the capital to hire humans that help humans, then what does that say about their products?

- **mercurialsolo** ([comment](https://news.ycombinator.com/item?id=49336573#49340514), 2026-08-18 02:34:28 UTC)
  We just need better specialized models for these. Writing is as much a process of thinking as of communicating the idea. Current generation of outputs eliminate the process of thinking

- **heurist** ([comment](https://news.ycombinator.com/item?id=49336573#49341032), 2026-08-18 03:47:46 UTC)
  I find after 4 or 5 rounds of targeted feedback and requests to tighten the text AI can produce exceptionally readable documentation.

- **rphv** ([comment](https://news.ycombinator.com/item?id=49336573#49341128), 2026-08-18 04:06:23 UTC)
  > ...then I’m afraid I received a different message than you intended

  Are you sure about that?

- **pixelesque** ([comment](https://news.ycombinator.com/item?id=49336573#49336783), 2026-08-17 20:04:30 UTC)
  Too sloppy, didn't read.

  - **nik282000** ([comment](https://news.ycombinator.com/item?id=49336573#49337596), 2026-08-17 21:03:05 UTC)
    Big fan of "slop-jockies" as a collective term for AI spammers.

- **uygar** ([comment](https://news.ycombinator.com/item?id=49336573#49337283), 2026-08-17 20:37:06 UTC)
  I'm not particularly interested in who wrote the first draft. What matters is whether someone took responsibility for the final version.

- **protocolture** ([comment](https://news.ycombinator.com/item?id=49336573#49340027), 2026-08-18 01:30:22 UTC)
  Engagement Bait; Didnt Read.

- **keeda** ([comment](https://news.ycombinator.com/item?id=49336573#49341355), 2026-08-18 04:42:00 UTC)
  I dunno, not a huge fan of TL;DR (even though it definitely has its place for long-winded walls of text) -- I feel like TL;DR is a cause or a symptom or both of our dwindling attention spans. I think this inability to read anything longer than a tweet, and the resulting loss of nuance, has been pretty bad for discourse, online or off.

  AI-writing is definitely very annoying to read, but I don't know if it's ideal to start dismissing interesting content before we even get to its substance just because we don't like its form.

  - **0x69420** ([comment](https://news.ycombinator.com/item?id=49336573#49341377), 2026-08-18 04:46:00 UTC)
    but our dwindling attention spans are caused by a deluge of material sapping our energy before we can devote it to something worthwhile. developing a fast and frugal mental filter for insubstantial walls of slop is a new prerequisite for not being so exhausted that you default to saying tl;dr to the real, good stuff.

- **therepanic** ([comment](https://news.ycombinator.com/item?id=49336573#49337240), 2026-08-17 20:33:57 UTC)
  You don't have to preface every criticism by saying you're a huge AI proponent. EVERYONE overdoes this.

- **deathanatos** ([comment](https://news.ycombinator.com/item?id=49336573#49340070), 2026-08-18 01:36:11 UTC)
  The problem is merely determining to "AI; DR" itself is not free. Reading an article takes effort, effort that one hopes will result in something intellectually stimulating. By the time you sample enough of the content to make the determination that the article is AI, you've already invested effort, and now found out the rug has been pulled.

  Sure, before, there was always the possibility that the article wouldn't deliver. Sturgeon's Law. But now it's like 10× more, and the amount of slop out there means its even harder to find that (human-written) gem amongst all the chaff. This last month especially, I've started to wonder "what even is the point of HN?" as more and more of the frontpage ends up dominated by slop. *The* thing that made HN worth it in the beginning is that it had a high gem:chaff ratio — at least compared to other corners of the Internet at the time I joined.

- **krona** ([comment](https://news.ycombinator.com/item?id=49336573#49336902), 2026-08-17 20:12:30 UTC)
  A similar metaphor (I think I came up with but can't remember) is the slop sandwich. You can deliver slop to me but only when wrapped in a thick layer of human intervention (which usually also means removing 50% of the slop)

- **blobbers** ([comment](https://news.ycombinator.com/item?id=49336573#49338682), 2026-08-17 22:43:18 UTC)
  (such as giant automated meeting summaries we all get after an hour long slog).

- **seanmcdirmid** ([comment](https://news.ycombinator.com/item?id=49336573#49341381), 2026-08-18 04:46:19 UTC)
  What I dislike is people who say they don’t know something when it’s easy to just Google it, with Gemini looking up fairly trivial factoids and comparisons is especially easy now. I know this was a stronger meme a few years ago, “just Google it dammit!” But now it’s even more so. People who don’t know these things at this point just don’t want to know, and they still get offended when someone throws an AI answer at them, not understanding that they already offended other people first by being willfully ignorant.

- **redrix** ([comment](https://news.ycombinator.com/item?id=49336573#49337779), 2026-08-17 21:18:02 UTC)
  If you didn’t take the time to write it, why should anyone take the time to read it?

  - **CuriouslyC** ([comment](https://news.ycombinator.com/item?id=49336573#49340999), 2026-08-18 03:43:01 UTC)
    I hope you posted this ironically.

- **dkersten** ([comment](https://news.ycombinator.com/item?id=49336573#49338553), 2026-08-17 22:29:38 UTC)
  If you can’t be bothered to write it, then I can’t be bothered reading it.

- **waynecochran** ([comment](https://news.ycombinator.com/item?id=49336573#49339126), 2026-08-17 23:31:07 UTC)
  Fight fire w fire. Have AI read it and decide what to do w it.

- **dfee** ([comment](https://news.ycombinator.com/item?id=49336573#49339386), 2026-08-18 00:01:29 UTC)
  that's fine. doesn't absolve you from responsibilities of recipientship - as you'll inevitably find out (if you haven't already).

- **Alien1Being** ([comment](https://news.ycombinator.com/item?id=49336573#49337589), 2026-08-17 21:02:33 UTC)
  AI generated text should be treated as spam and automatically filtered out.

- **stevenhubertron** ([comment](https://news.ycombinator.com/item?id=49336573#49338474), 2026-08-17 22:21:56 UTC)
  Seem's reasonable and what I hold myself and my team to.

- **friarpuck** ([comment](https://news.ycombinator.com/item?id=49336573#49338415), 2026-08-17 22:16:42 UTC)
  Overall, I agree.  My only problem with the idea is that I'm seeing more and more people just use "AI;DR" to deride an opinion that they don't agree with.  It's becoming the new "paid shill".

- **techpression** ([comment](https://news.ycombinator.com/item?id=49336573#49337071), 2026-08-17 20:22:53 UTC)
  This hurts particularly much when it comes to software changelogs/release notes, most recently for me was the solidjs 2 beta, reading the announcement post was painful, even the headers are LLM:isms.

- **LogicFailsMe** ([comment](https://news.ycombinator.com/item?id=49336573#49339298), 2026-08-17 23:52:34 UTC)
  I suspect the free market of information content will ultimately sort this all out. I feel similarly about AI art, but to get to that point I had to go to my city's art museum and experience artwork in person. There's just no comparison between being in the same room with a Michelangelo sculpture and peering at a Stable Diffusion/Midjourney/Whatever image on one's screen, there just isn't. What AI can do though is create endless content and too many are content with that, see linkedin.

  TLDR: Content != Art

- **tim-projects** ([comment](https://news.ycombinator.com/item?id=49336573#49340662), 2026-08-18 02:52:52 UTC)
  NP;DR

  (Newsletter popup,. Didn't read)

- **runjake** ([comment](https://news.ycombinator.com/item?id=49336573#49337566), 2026-08-17 21:00:53 UTC)
  I guess I'm in the minority. I don't mind an AI response if it's informative, concise and well-crafted.

  The problem is that those kinds of responses are rare in the tech world. But when you have someone competent at the helm, it's much better than reading human slop.

- **boogieknite** ([comment](https://news.ycombinator.com/item?id=49336573#49337200), 2026-08-17 20:31:12 UTC)
  > But if you’re my colleague and we’re in a Slack discussion and you post a wall of Claude output, then I’m afraid I received a different message than you intended.

  i have what ill call a "condition" where i fear assuming someone did something stupid is insulting. i try not to patronize people because i also assume that would be insulting. this leads to issues where sometimes people really want to be lead to water rather than make an implied connection themselves

  this is a roundabout way of saying, is there a genuinely polite way to tell colleagues posting ai copypasta makes them seem ignorant? i dont think ai:dr is workplace appropriate. id like to tell people gently and avoid patronizing if possible

- **purplethreads** ([comment](https://news.ycombinator.com/item?id=49336573#49337561), 2026-08-17 21:00:15 UTC)
  Impossible to know unless you did read.

  TL;DR works because I can see the length at a glance

  And you *cannot* tell all AI. Only mainstream crap like ChatGPT and Gemini which is full of cached tropes and boilerplate formats so it all sounds the same.

  My custom invoicing software automates notes based on years of my previous notes and tasks I did - looks nothing like AI.

  Use a real library and local model, mess with settings, there is a lot more to this than the mainstream consumer apps.

  - **trelbutate** ([comment](https://news.ycombinator.com/item?id=49336573#49338186), 2026-08-17 21:51:46 UTC)
    So? This is about ovious stuff where you notice the typical annoying AI style directly in the first paragraph. After all, 99% of "regular" people use the mainstream models, and anyone who uses a local model probably knows enough about AI that they don't dump raw output on you.

- **chasing** ([comment](https://news.ycombinator.com/item?id=49336573#49338209), 2026-08-17 21:53:24 UTC)
  So what you're saying is: You no longer visit LinkedIn.

- **VCFundedGenYer** ([comment](https://news.ycombinator.com/item?id=49336573#49337562), 2026-08-17 21:00:23 UTC)
  The irony of making such a bold progressive statement while still being on X and not Mastodon....

- **themgt** ([comment](https://news.ycombinator.com/item?id=49336573#49337235), 2026-08-17 20:33:19 UTC)
  *But if you’re my colleague and we’re in a Slack discussion and you post a wall of Claude output*

  Claude, post that wall of output to Slack yourself. Make no mistakes.

- **thm** ([comment](https://news.ycombinator.com/item?id=49336573#49337003), 2026-08-17 20:18:32 UTC)
  Eternal September already?

  - **nik282000** ([comment](https://news.ycombinator.com/item?id=49336573#49337777), 2026-08-17 21:17:49 UTC)
    There's been a few. The last one was 2007 when the iPhone changed the internet from a place you went because you wanted to be there and had a reason to engage, into an app meant to entertain you for 5min at a time between text messages and flushing.

- **classictraffic** ([comment](https://news.ycombinator.com/item?id=49336573#49336990), 2026-08-17 20:17:49 UTC)
  This blog post also feels AI written (I can tell it’s human written, just sloppy)

- **sportsracersss** ([comment](https://news.ycombinator.com/item?id=49336573#49339836), 2026-08-18 01:02:09 UTC)
  I love the notion, but I'm too conflict-averse to assert it.

  Really hate it when I send a tricky spec out for review and people respond a couple minutes later with a Claude summary. Way to add value bro.

- **quantum_state** ([comment](https://news.ycombinator.com/item?id=49336573#49337128), 2026-08-17 20:26:22 UTC)
  Very good shorthand

- **frogperson** ([comment](https://news.ycombinator.com/item?id=49336573#49338283), 2026-08-17 22:01:04 UTC)
  I don't think AI is ever fully going away, but I can't wait for the bubble to pop and customers are forced to pay the actual cost of tokens.  i think that's the only way we see a meaningful reduction in slop.

  - **CuriouslyC** ([comment](https://news.ycombinator.com/item?id=49336573#49341011), 2026-08-18 03:44:49 UTC)
    DeepSeek v4 flash blew the doors off that fantasy. Even if we switched to tokenomics, models are getting good enough and cheap enough that there's no stopping this train.

- **foobar1962** ([comment](https://news.ycombinator.com/item?id=49336573#49338414), 2026-08-17 22:16:42 UTC)
  "I would have written a shorter letter, but I did not have the time."

- **jr3592** ([comment](https://news.ycombinator.com/item?id=49336573#49337058), 2026-08-17 20:22:11 UTC)
  The irony here is that his very own post reads (to me) as AI slop.  Take this line:

  > I’ve been thinking about it ever since. Why? Because there is growing grumbling among everyone about AI writing. And it’s not just others; it’s me!

  Classic AI "its not just, its..."

- **Razengan** ([comment](https://news.ycombinator.com/item?id=49336573#49337506), 2026-08-17 20:54:38 UTC)
  By the way, just want to say, AI can be good for some bedtime stories while trying to fall asleep lol

  After you've exhausted your favorite audiobooks, I mean

  Like, I love The Wind in the Willows, but I wish the part where Toad and the gang go on the road in the cart lasted for longer. I asked ChatGPT to invent some fill-in chapters matching the same style and speak it out loud, and it kinda did OK actually.

- **kmeisthax** ([comment](https://news.ycombinator.com/item?id=49336573#49337473), 2026-08-17 20:51:57 UTC)
  > Yes, there are certain situations in which we should expect 100% AI-generated copy. Customer support would be a perfect example. We’re not looking for artisanal “did you make sure to reset your phone” style dialogue.

  No, no, no, no - the whole point of customer support is that I am having a problem that requires attention from a representative of the business I am dealing with. Businesses really don't like doing this; they call it a cost center to have to talk to their own customers, so they staff their call centers with increasingly useless script-readers designed specifically to shield the people with knowledge of the matter you're facing against customers like you. This is a great solution for dealing with technically illiterate people who don't do basic troubleshooting and terrible for literally anyone else who actually tries to be a good customer.

- **hankbond** ([comment](https://news.ycombinator.com/item?id=49336573#49337016), 2026-08-17 20:19:23 UTC)
  Whenever I see a massive project README all I can think is if you didn't write it, ME won't READ it.

- **7e** ([comment](https://news.ycombinator.com/item?id=49336573#49343052), 2026-08-18 08:44:14 UTC)
  The new modern workflow is to take a succinct idea and expand it into pages and pages of slop using AI. Nobody reads this slop, they ask another AI to summarize it back down to the original succinct core.

- **river_otter** ([comment](https://news.ycombinator.com/item?id=49336573#49337086), 2026-08-17 20:24:16 UTC)
  It's now faster to write than to read. A first in human history

- **gnarlouse** ([comment](https://news.ycombinator.com/item?id=49336573#49337861), 2026-08-17 21:25:35 UTC)
  YO (AIDR)IAN!

- **Terr_** ([comment](https://news.ycombinator.com/item?id=49336573#49336774), 2026-08-17 20:03:57 UTC)
  > TL;DR (too long; didn’t read) was the solution for social media.

  > AI;DR (AI; didn’t read) is the solution for AI slop.

  Maybe I'm the odd one out here and didn't plumb the worse-depths of social media, but I feel I need to defend good old TLDR as a slightly different, and less-hostile animal.

  It *can* be a moral condemnation of the poster, where they're disrespecting everyone else's time by posting something big and vague... But it usually isn't. At least half the time TLDR is someone providing a summary because they think it'd be useful (even of it's sometimes a hostile interpretation.)

  - **Jare** ([comment](https://news.ycombinator.com/item?id=49336573#49337139), 2026-08-17 20:27:00 UTC)
    tl;dr as the sole reply to someone IS a condemnation of what they wrote. tl;dr at the front of your message with a short summary, is an admission that the long version may not be for everyone and there's a core point for quick consumption.

    I'd say that sounds about the same for ai;dr. I could see myself posting a prompt like that in front of the generated report.

  - **mrtesthah** ([comment](https://news.ycombinator.com/item?id=49336573#49340830), 2026-08-18 03:18:25 UTC)
    I agree, likening it to "TL;DR" is much too charitable. At least when someone wrote a wall of text it was apparent they cared enough about the subject to think about and pay attention to it.

- **layer8** ([comment](https://news.ycombinator.com/item?id=49336573#49337242), 2026-08-17 20:34:07 UTC)
  Not to be confused with Aider.

- **scotty79** ([comment](https://news.ycombinator.com/item?id=49336573#49341268), 2026-08-18 04:29:51 UTC)
  Another use of this might be labeling yourself of the stuff you just pasted from your AI without reading so that the readers are aware where did the text come from.

- **verdverm** ([comment](https://news.ycombinator.com/item?id=49336573#49339821), 2026-08-18 01:00:27 UTC)
  Not the first time this has been used, despite what author wants to claim, not the first time any of this has been said or commented about on HN

  [https://hn.algolia.com/?q=ai%3Bdr](https://hn.algolia.com/?q=ai%3Bdr)

  This piece is still slop, human or ai created

  fwiw, I'm partial to ns;nt ([https://blog.kinglycrow.com/no-skill-no-taste/](https://blog.kinglycrow.com/no-skill-no-taste/)), but it is different in nuance

- **elendilm** ([comment](https://news.ycombinator.com/item?id=49336573#49338185), 2026-08-17 21:51:45 UTC)
  Its a bit lame in 2026, to attack the messenger instead of the content of the message.

  Its awfully similiar to bitching about reading mails on a computer and attacking the sender.

  The virtue signaling is beyond me.
  I dont care about AI;DR or TL;DR.

  Give me good content. And I will read it.

- **arm32** ([comment](https://news.ycombinator.com/item?id=49336573#49336728), 2026-08-17 20:00:44 UTC)
  This is HW;DR: human-written, did read

  - **sermah** ([comment](https://news.ycombinator.com/item?id=49336573#49336775), 2026-08-17 20:03:57 UTC)
    TA;DU: Too ambiguous, didn’t understand

    - **em-bee** ([comment](https://news.ycombinator.com/item?id=49336573#49336800), 2026-08-17 20:05:49 UTC)
      yeah, how about HW;WR? human written, worth reading.

    - **hinkley** ([comment](https://news.ycombinator.com/item?id=49336573#49336786), 2026-08-17 20:04:43 UTC)
      did understand?

  - **spudlyo** ([comment](https://news.ycombinator.com/item?id=49336573#49336885), 2026-08-17 20:11:16 UTC)
    This is LE;DU: low-effort, didn't upvote.

- **ademup** ([comment](https://news.ycombinator.com/item?id=49336573#49336895), 2026-08-17 20:11:53 UTC)
  I'll probably be downvoted to the bottom of the ocean, but I feel this needs to be said:

  - Why does it matter who or what wrote a thing? And how would you know if the /content/ is worthwhile, unless you read it...

  - The ability to "detect AI" is imperfect at best. 90% AI written? 5%? How would you know, unless you read it....

  - If you didn't read it, then why brag about it with an "AI;DR"?

  - If you are wrong, and you announce it to the world, how would it feel to someone who spent a lot of time and energy writing?

  - **otterley** ([comment](https://news.ycombinator.com/item?id=49336573#49337445), 2026-08-17 20:49:58 UTC)
    > Why does it matter who or what wrote a thing?

    Two reasons:

    1. I can't effectively engage in follow-up conversation with the "author." I can't do it with the human (principal) because they didn't write it and can't explain it--and, in fact, they may not even personally agree with all if it!

    2. It shifts the cognitive burden from writer to reader. What makes writing hard, and valuable, is the effort put into translating one's raw, unfiltered thoughts into writing that is easy to comprehend, and the writer's own unique personality that is expressed in it. As ambient prose, AI-generated writing is often not only more difficult to read than human-drafted prose, but it also has this "sameness" quality that makes every "author" have the same personality.

  - **Planktonne** ([comment](https://news.ycombinator.com/item?id=49336573#49337205), 2026-08-17 20:31:34 UTC)
    > Why does it matter who or what wrote a thing

    The purpose of writing is to communicate. The person communicating is an important part of the message.

    Consider the sentence "I'm waiting for you at home." It really matters if it's said by your loving wife or an evil clown. You can extrapolate from this.

  - **its-summertime** ([comment](https://news.ycombinator.com/item?id=49336573#49336997), 2026-08-17 20:18:07 UTC)
    Imagine a future where 99% of text is written by 1 unpassionate person. Reading the same patterns, the same tropes, the same flow across paragraphs, over and over, would be unpleasant. It already is unpleasant.

  - **supermatt** ([comment](https://news.ycombinator.com/item?id=49336573#49337366), 2026-08-17 20:44:03 UTC)
    The problem is that some people think all AI-assisted writing is prompting "write me a post about X", so they see LLM prose and assume there has been no thought or effort put into it.

  - **jastanton** ([comment](https://news.ycombinator.com/item?id=49336573#49336987), 2026-08-17 20:17:39 UTC)
    Because my time is valuable and if the person who sent me something didn't care enough to write it, then I don't care enough to read it.

    Bragging about it is weird, but I will use it like I use 'RTFM'.

    And detectability - My AI-DAR (radar), is fairly fined tuned but not perfect, so if I make a mistake, oh well, the point is I'm protecting my time.

    - **ModernMech** ([comment](https://news.ycombinator.com/item?id=49336573#49337031), 2026-08-17 20:20:08 UTC)
      So how much time do you deem a minimum amount for someone to spend on some unit of work before you're willing to read it? And what technologies are allowed -- are word processors allowed or does it have to be done with a writing instrument like a pencil? What about spell check? Do you care if they had done their research with a Wikipedia or do you prefer card catalog for the really important work?

      - **robrtsql** ([comment](https://news.ycombinator.com/item?id=49336573#49337756), 2026-08-17 21:16:06 UTC)
        I'm not sure. Another way to think about it: how _little_ time is someone able to spend on something where you will still be interested in reading it? If someone tells their unattended LLM agent to create a blog, write whatever content will maximize banner ad revenue, and then share each post on Hacker News, would you read it? What if the content is actually interesting in your opinion?

        - **ModernMech** ([comment](https://news.ycombinator.com/item?id=49336573#49339163), 2026-08-17 23:35:06 UTC)
          For me, the amount of time could be very minimal. A person can splash some paint on a canvas, tape a banana to a wall, press a shutter, or write 14 syllables and if it's well considered then that can be enough. Time spent just doesn't play into it for me, unless that's actually part of the point.

          > If someone tells their unattended LLM agent to create a blog, write whatever content will maximize banner ad revenue, and then share each post on Hacker News, would you read it? What if the content is actually interesting in your opinion?

          Yes, I think if one of that content had a headline that interested me I would definitely click on it, because that's already happened!

  - **krelas** ([comment](https://news.ycombinator.com/item?id=49336573#49337129), 2026-08-17 20:26:23 UTC)
    The shape of Claude’s writing style is horrible to read and easy to spot, and that’s a ground truth.

    - **rfgplk** ([comment](https://news.ycombinator.com/item?id=49336573#49337407), 2026-08-17 20:47:18 UTC)
      A belt-and-braces approach.

  - **layman51** ([comment](https://news.ycombinator.com/item?id=49336573#49337051), 2026-08-17 20:21:32 UTC)
    In one case, I could tell because the tone of the piece sounded exactly like the kind of stuff I would read after prompting an LLM and I had never heard of the author before, but I knew that they were like an intern or a new college grad and for some reason their piece was trying to persuade employees in a certain field about how they had to use AI itself. It just rubbed me the wrong way because if they did use AI, then they didn't even bother to rewrite the repetitive instances of "it's not X; it's y", and also "This isn't X".

  - **VeninVidiaVicii** ([comment](https://news.ycombinator.com/item?id=49336573#49336927), 2026-08-17 20:14:10 UTC)
    Maybe you haven’t seen enough coworkers send you pages and pages of slop.

  - **xboxnolifes** ([comment](https://news.ycombinator.com/item?id=49336573#49337328), 2026-08-17 20:41:11 UTC)
    > If you didn't read it, then why brag about it with an "AI;DR"?

    It's a reference to TL;DR. If you can understand that, you can understand AI;DR.

  - **bigstrat2003** ([comment](https://news.ycombinator.com/item?id=49336573#49337844), 2026-08-17 21:23:42 UTC)
    > Why does it matter who or what wrote a thing?

    Because what the clanker produces is almost always bad output compared to what a capable human would produce. Furthermore, even an incapable human is better than a clanker, because at least humans have intrinsic value that they bring to the table. Finally, it's just plain disrespectful to refuse to take some time to answer a question and hand it off to the clanker.

- **supermatt** ([comment](https://news.ycombinator.com/item?id=49336573#49336970), 2026-08-17 20:16:30 UTC)
  I submit pretty much the opposite of this, but it didn't gain any traction: [https://news.ycombinator.com/item?id=49332291](https://news.ycombinator.com/item?id=49332291)

  - **Planktonne** ([comment](https://news.ycombinator.com/item?id=49336573#49337154), 2026-08-17 20:27:46 UTC)
    You submitted thoughtless pap; of course it didn't get any traction.

    Why would you think it would?

    - **supermatt** ([comment](https://news.ycombinator.com/item?id=49336573#49337164), 2026-08-17 20:28:56 UTC)
      [comment text unavailable]

      - **Planktonne** ([comment](https://news.ycombinator.com/item?id=49336573#49337218), 2026-08-17 20:32:14 UTC)
        > What was thoughtless about it?

        You didn't put any meaningful thought into it.

        - **supermatt** ([comment](https://news.ycombinator.com/item?id=49336573#49337224), 2026-08-17 20:32:46 UTC)
          Yes, I did. That was the whole point of the post.

          - **Planktonne** ([comment](https://news.ycombinator.com/item?id=49336573#49337388), 2026-08-17 20:45:45 UTC)
            I believe you believe you did, but the post makes more of a point through its conception than it does through its prose.

            - **supermatt** ([comment](https://news.ycombinator.com/item?id=49336573#49337480), 2026-08-17 20:52:45 UTC)
              > I believe you believe you did

              Wow, peak ableism. It is a post about how I use an LLM as an accessibility aid for reading and writing. We're not all out here faking creative writing you know...

              - **Planktonne** ([comment](https://news.ycombinator.com/item?id=49336573#49338082), 2026-08-17 21:42:52 UTC)
                I would a thousand times rather read your stream of consciousness, even though I disagree with it, than the bland pulp of the LLM output. In every way that matters, it's stronger and communicating far more.

                I don't agree that it's ableism to believe that you are far more worth talking to than a machine regurgitating attenuated averages.

                - **CuriouslyC** ([comment](https://news.ycombinator.com/item?id=49336573#49341052), 2026-08-18 03:50:54 UTC)
                  You say this, but it's likely a lie. Maybe not for you, but for every N people like you that say it, a high percentage of them are lying. There's research on people's preference for AI generated content over human content when the provenance of the content is blind, which flips on its head when provenance is not blind.  The truth is the actual "art" never mattered, most people are living in Plato's cave and they're scraping and clawing for some shred of identity and sense of belonging, and being part of the anti-AI clique gives them that. That's how we get things like Jackson Pollock and bananas duct-taped to cardboard being held up as some kind of achievement.

                  - **Planktonne** ([comment](https://news.ycombinator.com/item?id=49336573#49342912), 2026-08-18 08:20:24 UTC)
                    > people's preference for AI generated content over human content when the provenance of the content is blind, which flips on its head when provenance is not blind

                    I don't think this shows what you think it shows. AI output (in short clumps) looks like human output; it's designed to do that. Naturally people will sometimes prefer it to other stuff that looks like human output, but crucially this shifts when they realise they're not actually being communicated with.

                    - **supermatt** ([comment](https://news.ycombinator.com/item?id=49336573#49343142), 2026-08-18 08:58:58 UTC)
                      > this shifts when they realise

                      I think this is pretty much is what they were saying about the provenance being blind. If you are able to deduce the LLM usage through the long-form text then that removes the blindness and objectivity.

                      I wonder if you view adversarially humanised LLM-generated content in the same light as that which hasn't been obfuscated. I recall seeing some paper with examples posted here a few months ago, where I (and the participants in the study) literally couldn't tell the difference between them and human writing. I have considered using humanisation myself but there is both less control over the output and it (obviously) loses the LLM-like structure that I find so easy to read - and is therefore antithesis to my own objectives.

                - **supermatt** ([comment](https://news.ycombinator.com/item?id=49336573#49338689), 2026-08-17 22:44:12 UTC)
                  > I don't agree that it's ableism to believe that you are far more worth talking to than a machine regurgitating attenuated averages.

                  Straw man. That literally wasn't what you said. You dismissed what I wrote as thoughtless. It wasn't about disagreement it was purely invalidation.

                  - **Planktonne** ([comment](https://news.ycombinator.com/item?id=49336573#49339083), 2026-08-17 23:27:00 UTC)
                    I think you're conflating a couple of different things here.

                    1. I do disagree with your position in both the prompt and the output; I don't think you're correct. That doesn't mean I don't think you're worth talking to.

                    2. I do think the output was thoughtless; there is thought evident in the prompt, but then you passed it through a blandifying filter that took it out. You made your contribution less valuable and less valid, removing intention. That's thoughtless.

                    You do not need a filter; it does not make your writing better, it makes it more pallid.

                    - **supermatt** ([comment](https://news.ycombinator.com/item?id=49336573#49339339), 2026-08-17 23:56:16 UTC)
                      I had 3 main positions - are you disagreeing with them all? You have not directly engaged with any of them.

                      ```text
                        1) Content shouldn't be judged solely on the use of an LLM.
                        2) There is a distinction between slop and assisted authorship.
                        3) LLMs can be valuable accessibility tools.

                      ```

                      You are now saying that the OUTPUT was thoughtless, whereas before you said that "I" had not put meaningful thought into it. Those are different claims.

                      As for the output, I regenerated it until I was happy that it communicated my position effectively. That in itself requires both thought and intention.

                      You may prefer my unedited prose, but your preference doesn't make either my input or my editorial choices thoughtless.

                      - **Planktonne** ([comment](https://news.ycombinator.com/item?id=49336573#49339529), 2026-08-18 00:19:26 UTC)
                        > are you disagreeing with them all

                        Yes. I think an LLM can be useful for trivial or functional tasks, but for expressing complex positions, it's worse than useless. It's absolutely valid to dismiss LLM-generated prose, and people who who think they're doing 'assisted authorship' tend to be mistaken.

                        I'm not saying you are incapable of thought; I'm saying that you've abdicated that by transmitting through an LLM.

                        - **supermatt** ([comment](https://news.ycombinator.com/item?id=49336573#49339718), 2026-08-18 00:44:57 UTC)
                          > Yes

                          Well you are of course entitled to disagree.

                          > I'm not saying you are incapable of thought; I'm saying that you've abdicated that by transmitting through an LLM.

                          What you actually said was that I "didn't put any meaningful thought into it". Thats the INPUT, not OUTPUT. Anyway. I think we're as far as we are going to get with this "discussion". Have a good evening!

                          - **simoncion** ([comment](https://news.ycombinator.com/item?id=49336573#49340180), 2026-08-18 01:53:13 UTC)
                            > What you actually said was that I "didn't put any meaningful thought into it".

                            What he literally said was [0][1]

                            ```text
                              You submitted thoughtless pap; of course it didn't get any traction.
                              ...
                              > What was thoughtless about it?

                              You didn't put any meaningful thought into it.

                            ```

                            > Thats the INPUT, not OUTPUT.

                            You didn't submit the input, you submitted the output. In actual fact, Planktonne asserted that the input that you did not publish would have been *much* more strongly preferred to the output that you did publish: [2]

                            ```text
                              I would a thousand times rather read your stream of consciousness, even though I disagree with it, than the bland pulp of the LLM output. In every way that matters, it's stronger and communicating far more.

                            ```

                            [0] <[https://news.ycombinator.com/item?id=49337154](https://news.ycombinator.com/item?id=49337154)>

                            [1] <[https://news.ycombinator.com/item?id=49337218](https://news.ycombinator.com/item?id=49337218)>

                            [2] <[https://news.ycombinator.com/item?id=49338082](https://news.ycombinator.com/item?id=49338082)>

                            - **supermatt** ([comment](https://news.ycombinator.com/item?id=49336573#49341247), 2026-08-18 04:27:01 UTC)
                              > You didn't submit the input, you submitted the output

                              I submit BOTH the input AND the output - that was the ENTIRE point of the post.

                              Honestly, I beat myself up for years over having a reading disability - whereas it’s evident some of you don’t even make the effort to read yet still feel they have something to say.

  - **danielodievich** ([comment](https://news.ycombinator.com/item?id=49336573#49339538), 2026-08-18 00:20:32 UTC)
    Fascinating seeing you get irate with people who are giving you feedback that your own thoughts are far superior to the regurgitated "cleaned up" version which is absolute garbage indeed.

    You have some solid ideas there but they are very poorly organized. I think you would benefit from a class in writing. I had a month-long technical writing workshop back a couple of decades ago that my company sponsored and it helped me tremendously with starting with wall of consciousness, progressing to writing plan, outline and then editing. It had a very positive impact on my career in professional services where clear communication via documents is an essential part of value prop.

    - **supermatt** ([comment](https://news.ycombinator.com/item?id=49336573#49341315), 2026-08-18 04:37:02 UTC)
      > Fascinating seeing you get irate with people who are giving you feedback that your own thoughts are far superior to the regurgitated "cleaned up" version which is absolute garbage indeed.

      That is not the part I take issue with at all! In fact many (if not all) of my comments to those people are thanking them.

      I think you need to go and  double check exactly what I have replied! Feel free to link to anywhere you think I have been irate in response to someone stating their preference! I think you will find my only grievance is where people have called the INPUT thoughtless or zero effort.

      I’m finding it fascinating how people are commenting on what they think they have read rather than what they have actually read - both in relation to the post and in my replies.

      I do appreciate your advice on following a writing course. I did exactly that to great effect in the early 2000s. Unfortunately it is of little help these days

  - **meindnoch** ([comment](https://news.ycombinator.com/item?id=49336573#49336991), 2026-08-17 20:17:52 UTC)
    Yeah, I wonder why! /s

    - **supermatt** ([comment](https://news.ycombinator.com/item?id=49336573#49337007), 2026-08-17 20:18:46 UTC)
      Because some people are just ignorant and downvote anything they either aren't willing or able to understand :)

- **a2ff6eeb0** ([comment](https://news.ycombinator.com/item?id=49336573#49336996), 2026-08-17 20:18:06 UTC)
  Eventually, AI will be a far better writer than a human is, and then nobody will want to read the human generated subpar writing.

  AI writing is rapidly improving. Human writing, on average not so much.

  - **platevoltage** ([comment](https://news.ycombinator.com/item?id=49336573#49337591), 2026-08-17 21:02:53 UTC)
    I'll take "subpar" human writing, music, art, or whatever any day of the week.

    - **a2ff6eeb0** ([comment](https://news.ycombinator.com/item?id=49336573#49339244), 2026-08-17 23:45:13 UTC)
      People say this, but AI artists keep getting listens on music platforms, doing at least as well as human artists if the listener is making a blind choice.

      [https://www.promarket.org/2026/05/04/consumers-prefer-ai-mus...](https://www.promarket.org/2026/05/04/consumers-prefer-ai-music-until-theyre-told-its-ai/)

      - **platevoltage** ([comment](https://news.ycombinator.com/item?id=49336573#49340043), 2026-08-18 01:31:57 UTC)
        Sure. Kid Rock also sold more records than the Pixies.

- **eddieroger** ([comment](https://news.ycombinator.com/item?id=49336573#49336842), 2026-08-17 20:08:18 UTC)
  >However, I have a new policy.

  >If you’re not bothered enough to review and edit it...

  >...then I’m not going to bother reading it.

  Just playing Devil's Advocate here, but we've had copywriters and editors for generations now. Not reading something because AI did the post-writing work feels kinda weak. Skip stuff started from AI, fine, but this is just because it's AI, not because the author didn't do the task. And I do get the point is that if an AI did /most/ of the work, ok to that, too, but not post-write processing alone.

  - **afr0ck** ([comment](https://news.ycombinator.com/item?id=49336573#49337271), 2026-08-17 20:36:16 UTC)
    I think the main reason many people (including me), very often, lack the motivation to read content that is likely generated by AI is the suspicion that it comes from a place of intellectual laziness. Another reason, based on personal experience, is that AI content may suffer from too much verbosity, too much jargon and over-confidence, which makes the reading experience feel fake and border-line irritating. In many cases the content may have very little to no nuance, which is ultimately a waste of time.

    As an anecdote, someone posted a blogpost on Linkedin on using agents to implement a driver to access PCIe devices over TCP/IP. I was intrigued because that's not an easy task for several reasons, like handling PCIe interrupts and DMA. For exmaple, how does the remote machine map the device's PCIe BARs? And when it issues I/O to the devices registers, how are these reads and writes transferred to the remote device. In the end, this is just some virtual memory. In a local machine, this is either directly mapped to the PCIe physical addresses or some IOMMU virtual address space which is then translated by the hardware upon CPU/device/VM access.

    After reading the long verbose promising article, in the end, the guy (with the help of the agent) only managed to implement access to the PCIe config space so that lspci on the remote machine works and shows the remote PCIe device, but that's all. It never addressed the issues above nor even mentioned them. The code was AI generated. The article was AI-written. The article never made a reference to DMA, interrupts, MSIX-X, IOMMU, IOTLB, virtual memory, etc, but it made big claims on next-gen datacenter disaggregated architecture, boosting GPU utilization, reducing large scale inference costs, etc.

    Anyway, you get my point: big long beautiful words, but zero nuance.

  - **nancyminusone** ([comment](https://news.ycombinator.com/item?id=49336573#49336963), 2026-08-17 20:16:11 UTC)
    >But if you’re my colleague and we’re in a Slack discussion and you post a wall of Claude output

    did you formerly hire copywriters for this task?

  - **jere** ([comment](https://news.ycombinator.com/item?id=49336573#49336956), 2026-08-17 20:15:46 UTC)
    And how could you possibly distinguish those scenarios without wasting all your time?

  - **AnimalMuppet** ([comment](https://news.ycombinator.com/item?id=49336573#49337037), 2026-08-17 20:20:43 UTC)
    The problem with copywriters is that they wrote "copy" - which turns out to be *writing that I don't want to read*.  And the problem with AI is that much of what it trained on is copy, so it trained to write stuff that I don't want to read.

    So in the end, I don't care if a human wrote it or an AI, I don't want to read it either way.

    What's wrong with copyrighters?  They write like corporations, not like humans (see the Cluetrain Manifesto for more on this).  They sound like nobody - literally inhuman.  I don't want to read that.  I want to hear a human voice.  If I can't hear that in your writing, I don't need to read it.

  - **het25** ([comment](https://news.ycombinator.com/item?id=49336573#49336954), 2026-08-17 20:15:43 UTC)
    that is load bearing information, and i won't tiptoe around it.

- **rfgplk** ([comment](https://news.ycombinator.com/item?id=49336573#49337245), 2026-08-17 20:34:17 UTC)
  It's an ego issue for most people. For one, part of it comes from genuine intimidation or fear, the notion that a machine can be smarter than you, or at least produce answers that are more knowledgeable than you could. But I think the more striking issue is what LLMs do to the perceived value of expertise. Especially in engineering there's this weird pecking order hierarchy, where someone should be listened to just "because they have the YOE/Experience/Other meaningless metrics" under their belt. Now all of a sudden, someone with relatively little (or no) background in a given subject is capable of just entering a prompt and within seconds obtaining an answer that is expert or near expert level. (You can see the results of this with engineers just hopping between different fields with ease)

  The implication is that expertise is being devalued in real time, and in a sense it really is, but I think that most people really do need to face the reality of their emotions and where it comes from. For myself personally, I have no qualms about reading or even engaging with AI content, as long as the content itself is of quality and truthful.

  - **thatjoeoverthr** ([comment](https://news.ycombinator.com/item?id=49336573#49337433), 2026-08-17 20:49:34 UTC)
    Example from work.

    I described a problem to a new hire. Symptoms, how to reproduce, etc. and asked him to go investigate it, pin down the problem and solve it. It was a non-trivial and hard to reproduce bug.

    Instead of doing any of that, he sent back very quickly a wall of text. Generic advice. Nothing relevant. Along with this he sent a PR that would have broken prod.

    It was useless, and basically amounted to throwing the assignment back in my face. Since I, like literally everyone else, already have Claude Code, having an expensive person use it for me (slowly and badly) is worthless. In fact, it's negative value, and a huge waste of time. ChatGPT would have given me the same wall of text for pennies.

    In the end I got rid of him.

    I'm sure he thought I was "intimidated", and had "ego" issues. But he's actually just redundant.

  - **jeremyjh** ([comment](https://news.ycombinator.com/item?id=49336573#49337312), 2026-08-17 20:40:00 UTC)
    No, that’s not it. Its easy as competent engineers for us to forget how terrible most people are at prompting AI, or reviewing and correcting AI output. Raw output from typical prompts is garbage. If I start reading something that no one even bothered to edit well enough to tone down the AI speak, odds are its garbage and I don't need to spend more time engaging with it than the author did.

    - **rfgplk** ([comment](https://news.ycombinator.com/item?id=49336573#49337452), 2026-08-17 20:50:34 UTC)
      But the point is that it's garbage because of the low quality of the information, and not necessarily because an LLM made it. I do agree that most people don't know how to prompt.

      - **jeremyjh** ([comment](https://news.ycombinator.com/item?id=49336573#49337574), 2026-08-17 21:01:15 UTC)
        Right, and I’m not going to spend the time trying to gauge the information quality when I already know the person who sent it didn’t think it was important enough to edit - or isn’t capable of it.

  - **spelk** ([comment](https://news.ycombinator.com/item?id=49336573#49337515), 2026-08-17 20:55:35 UTC)
    Admittedly a controversial take, but I think *some* of the AI skepticism I see is driven by status anxiety, alongside the perfectly legitimate complaints about verbosity, low-effort output, lack of a human voice, etc.

    The bar for what counts as expertise is shifting. If someone with relatively little background can use an LLM to get to a reasonably informed answer much faster than before, then experience and credentials alone carry a bit less signalling power than they used to. That obviously doesn't mean the inexperienced person suddenly has the judgement, context or intuition of an actual expert, but I do think some of the hostility toward AI comes from discomfort with that change.

    AI is still wrong, goes in weird circular loops, and doesn't solve the fundamental human problems around judgement, organization, learning curves, accountability, etc. But it does seem to be raising the baseline expectation for what a competent knowledge worker *should* produce, and I feel that shift is genuinely uncomfortable for a lot of people who based their identities around being rigorous abstract problem solvers.

    - **AloysB** ([comment](https://news.ycombinator.com/item?id=49336573#49340878), 2026-08-18 03:26:00 UTC)
      Ironically, some of the AI 'trustism'[1] is very much driven by anxiety the fear of being left behind if one does not jump on the train.

      I agree that it shifts the notion of what is expertise, but for the worst. It's very hard to tell who is actually an expert, and who is mimicking the expert.

      The consequences vary from annoyance to downright catastrophe.
      e.g.: a confidently wrong medical advice

      On the other side, sometimes the expertise is not a requirement for the user: "If it works and does what it says on the box, that's all I care".

      I like the fact that you use the word "some", awesome to see some nuance. It's a tricky situation.

      ---

      [1] I am being an idiot on purpose, I think the word skepticism was completely derailed from its origin and meaning.

      A minimum amount of skepticism is very healthy, especially for software engineering.
      Most software engineers, and science-based professions for that matter, are skeptics at heart. And it's a good thing.

      Skepticism is the base of science; science thrived when we admitted ignorance and became skeptic towards our own knowledge.

  - **hatthew** ([comment](https://news.ycombinator.com/item?id=49336573#49337456), 2026-08-17 20:50:57 UTC)
    Reading a copy-pasted AI response feel the same to me as reading a massive wall of text with no punctuation. It *may* contain valuable information, but it's harder to extract the signal out from among all the noise, and the writing style is *correlated* with a lack of valuable information, so I generally give up and decide to spend my time reading something else.

    Is that an ego issue? Doesn't seem like it to me.

  - **intended** ([comment](https://news.ycombinator.com/item?id=49336573#49337696), 2026-08-17 21:11:04 UTC)
    Nah its just bad writing.

    Plus I’ve been seeing where AI productivity is highest and it’s been when leveraged by an expert.
