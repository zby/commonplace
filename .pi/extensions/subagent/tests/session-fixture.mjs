import fs from "node:fs";
import path from "node:path";
import { randomUUID } from "node:crypto";

// Protocol fixture only. The normal Pi storage rules are tested separately.
export function sessionFixture(args, cwd, directory) {
  const index = args.indexOf("--session");
  let file = index < 0 ? undefined : args[index + 1];
  if (!file) {
    fs.mkdirSync(directory, { recursive: true });
    file = path.join(directory, `${randomUUID()}.jsonl`);
    fs.writeFileSync(file, JSON.stringify({ type: "session", version: 3,
      id: randomUUID(), timestamp: new Date().toISOString(), cwd }) + "\n");
  }
  const header = JSON.parse(fs.readFileSync(file, "utf8").split("\n")[0]);
  return "\nPI_SUBAGENT_SESSION " + JSON.stringify({ type: "subagent_session", sessionId: header.id, sessionFile: file, cwd, pid: 12345 }) + "\n";
}
