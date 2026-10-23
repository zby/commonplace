# Hand-launch prompt for one recurring task

Substitute the task name, then pass the text below as the prompt of a
headless harness session started in the repository root. Phase 1 launches
this by hand; the heartbeat will later build the same prompt from the due
set.

---

You are running the recurring task `<task>` unattended. Nobody will answer
questions; if you cannot complete the run, write nothing and stop.

1. Read `kb/tasks/recurring/<task>.md`. It is the runbook. Follow its
   `Run Procedure`, `Batch` (if present) and `Output` sections exactly.
2. Read the log named in its `Output` section before doing anything else.
   Earlier sections tell you what previous runs did; use them as the runbook
   says.
3. Write only inside the paths named in the runbook's `Write scope`. Read
   whatever you need, but do not create, edit or delete any other file.
4. When the log is appended, stage only the write-scope file with
   `git add <path>` and commit with the subject given in `Write scope` and
   the trailer `Model: <your model id>`. Never use `git add -A`, `git add .`
   or `git commit -a`; the checkout may hold other sessions' uncommitted work.
5. Stop after the commit. Do not push.
