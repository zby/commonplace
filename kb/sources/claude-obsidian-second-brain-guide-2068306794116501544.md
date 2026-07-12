---
source: https://x.com/undefinedKi/status/2068306794116501544
captured: 2026-06-30T04:45:33.865959+00:00
capture: xdk
genre: practitioner-report
type: kb/sources/types/snapshot.md
status_id: 2068306794116501544
conversation_id: 2068306794116501544
post_count: 1
---

# How to Build an AI Second Brain With Claude and Obsidian That Gets Smarter Every Day (Full Guide)

Author: @undefinedKi
Post: https://x.com/undefinedKi/status/2068306794116501544
Created: 2026-06-20T12:15:41.000Z

Your best ideas are scattered across a dozen places right now. Notes apps. Browser tabs. Old chats with Claude that you closed and will never find again. Every time you sit down to work, you rebuild context from memory, and you forget most of it.
A second brain fixes that. It is one place that holds everything you know, with Claude sitting on top of it, reading it, connecting it, and growing it for you. You stop re-explaining yourself every session, because the system already remembers. Ask it anything you have ever written down and it answers from the whole thing.
This is the idea Andrej Karpathy popularized in April 2026 with his LLM Wiki pattern. The setup takes an evening, and unlike a chat history that rots, this one gets sharper every single day you use it.
Below is the full walkthrough, written so you can follow it even if you have never opened Claude Code or Obsidian before. Every step spells out exactly what to click and what to type.
 
What you are actually building
Two tools, two jobs.
Obsidian is the storage. A free notes app that keeps everything as plain text files on your own computer. Notes link to each other, and over time those links form a graph, a visible map of how your ideas connect. It lives on your machine, not in a company's cloud, and the files are yours forever.
Claude is the brain on top. It reads the entire vault, files new information where it belongs, links it to what is already there, and answers questions across all of it.
The whole thing is just text files. That means it is not locked to any one AI. Point a different model at it next year and it still works, because you own the brain, not the tool.
Step 1: Install Claude Desktop
Go to claude.com/download in your browser and download the desktop app for your system (Windows or Mac). Run the installer and open the app.
Sign in with your Claude account. You need a paid plan (Pro is $20/month), the free tier will not work for this.
At the top of the app you will see tabs: Chat, Cowork, and Code. Click the Code tab. This is Claude Code, the version that can actually read and write files on your computer. If it asks you to upgrade, your plan needs to be paid first.
Step 2: Install Obsidian and make your vault
Go to obsidian.md and download Obsidian. It is free. Install it and open it.
On the welcome screen, click Create new vault. Give it a name like "brain," pick a folder on your computer to store it, and click Create. That folder is now your second brain. Everything Claude writes will land here as text files.
Make one note so you have seen how it works: click the new-note icon, type a sentence, then type two square brackets and a word like [[goals]]. That bracketed word becomes a link. That is the core mechanic, notes pointing at notes. Claude will do this linking for you automatically later.
Step 3: Turn on the connection inside Obsidian
Claude needs a door into your vault. Obsidian opens one with a plugin.
In Obsidian, click the Settings gear (bottom left). In the menu, click Community plugins, then Turn on community plugins. Click Browse, search for Local REST API, click it, then Install, then Enable.
Now click on Local REST API in your installed plugins list to open its settings. You will see an API Key, a long string of letters and numbers. Copy it and keep it somewhere for the next step. Leave Obsidian open, the connection only works while the app is running.
Step 4: Connect Claude to the vault
Now you tell Claude how to reach that door. In the Claude Code tab, you have a place to type commands. Paste this in, but first replace PASTE-YOUR-KEY-HERE with the key you copied:
claude mcp add-json obsidian-vault '{ "type": "stdio", "command": "uvx", "args": ["mcp-obsidian"], "env": { "OBSIDIAN_API_KEY": "PASTE-YOUR-KEY-HERE", "OBSIDIAN_HOST": "127.0.0.1", "OBSIDIAN_PORT": "27124" } }'
Obsidian shows the key with the word "Bearer" in front of it. Do not include that word. Paste only the string of letters and numbers after it, nothing else.
This wires Claude to your vault through MCP, the standard way Claude talks to other apps. After it runs, type this to test it: "list every file in my Obsidian vault." If Claude reads your notes back to you, the connection works. If it cannot, make sure Obsidian is still open and the plugin is enabled.
Step 5: Load yourself into the brain
Right now Claude can read your vault but knows nothing about you. An empty brain is useless. Fix that first, and don't type it all out by hand. Make Claude interview you.
In the Claude panel inside Obsidian, paste this:
You are setting up my second brain. Interview me ONE question at a time to build my profile. Ask about: who I am and what I do, my goals for this year, how I want you to talk to me, my strengths and weaknesses, and my current projects. Wait for each answer before the next question. When finished, write everything into a file called CLAUDE.md at the vault root, structured with headers, so you load it automatically every session.
Answer like you're briefing a new co-founder. The more real your answers, the more the brain knows you. When it finishes, open CLAUDE.md in your vault, your whole context is now saved. You never re-explain yourself again.
Step 6: Create a project with the right structure
Your CLAUDE.md is the strategy layer. Projects are where work happens. Each one is its own folder so Claude focuses on a single job instead of your whole life at once. Have Claude build it. Paste:
Create a project folder in my vault called youtube-channel. Inside it, create four folders: Inputs, Process, Outputs, Feedback. Then write a CLAUDE.md inside that project folder describing what this project is, its one goal, and your specific role in helping me hit it. Interview me if you need details.
Swap youtube-channel for whatever you're building. You now have a clean pipeline: ideas land in Inputs, Claude works in Process, finished work goes to Outputs, results and metrics go to Feedback. Repeat this for every area, content, finances, clients.
Step 7: Open a single project to work in it
This is the move that keeps it sharp. Don't work from the giant vault. Open just the project so Claude sees only that job.
In Obsidian, click the vault name at the bottom left, then:
Manage vaults  →  Open folder as a vault  →  pick your project folder  →  Trust
Claude now reads only that project's CLAUDE.md. It knows exactly what it's helping with and ignores everything else. The big vault plans. A single project ships.
Step 8: Build a skill so you never repeat yourself
A skill is a saved workflow Claude runs on command. Anything you do more than once becomes one. Inside a project, paste:
I want to turn this into a reusable skill. Here is how I do [the task], with an example: [paste your example or steps]. Save this as a markdown skill file inside this project's skills folder, with a clear name and a description of when to trigger it.
Next time, you just say run the [name] skill and it executes your way, instantly. Build one per repeated task: writing client emails, prepping a video, categorizing bank statements.
Step 9: Wire in live data (calendar, email)
Static notes are half the brain. Connect what changes in real time. To add Google Calendar, run this in the Claude Code terminal:
 
Follow the Google sign-in (OAuth) it opens, and grant read access. Now you can say:
Read my calendar for today, log what I committed to in each meeting into my tasks project, and flag anything without a clear next step.
Add Gmail, Slack, or Notion the same way. Always grant read-only where you can, the brain should read your data, not delete it.
Step 10: Put it on autopilot
Once your skills work, schedule them so the brain maintains itself. In Claude Desktop, open the Schedule tab in the sidebar, click + New task, and fill in:
 
Or just tell Claude in any session: set up a daily task at 7am that organizes my vault and summarizes what changed. You wake up to a brain that filed itself overnight.
One rule you never break: keys, not prompts. Telling an agent "don't delete this" is a suggestion, not a safety setting. If it technically can delete a file or send an email, assume one day it will. Control access at the permission level, read-only and scoped keys, not with words.
Bonus: skip the setup with a ready-made repo
If you would rather not wire it from scratch, the open-source community already packaged the whole thing. Search these on GitHub:
claude-obsidian by AgriciDaniel. A self-organizing second brain built on the Karpathy wiki pattern. It scaffolds the vault, sets up the connection for you, and ships presets for different roles, executive, builder, creator, researcher, so the structure matches how you work.
obsidian-second-brain by eugeniughelbur. Comes with 43 ready commands like /obsidian-save, /obsidian-daily, and /obsidian-find. Works across Claude, Codex, and Gemini, so you are never locked to one tool.
second-brain-starter by coleam00. It interviews you, generates a plan for a proactive assistant, then builds it from plain text files, Python, and an Obsidian vault.
All of them are just text files and scripts. Clone one, then reshape it into your own private version.
What you have after these steps
Before this, Claude forgets you the moment you close the tab. Every session starts cold. You are the one holding all the context, and you lose most of it.
After this, Claude has a memory of your entire life and work. A vault that holds everything, a model that picks up exactly where it left off, a graph that grows itself while you sleep. All plain text. All yours. All running on whatever model you point at it.
Same subscription. Completely different machine.
You are not building a Claude setup. You are building your own memory, and it gets smarter every day you feed it.
Almost nobody does this. Most people will read all nine steps and build nothing.
The ones who start today will open their graph in a month and freeze, because it knows things they had forgotten they knew. And they will never go back to a blank chat box again.
If this was useful, head to my profile and follow. I write about AI, Claude, and systems that actually run.
Ciao,
@undefinedKi
