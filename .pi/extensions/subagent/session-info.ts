/** Report the session selected by Pi itself; do not duplicate its storage rules. */
import type { ExtensionAPI } from "@earendil-works/pi-coding-agent";

export default function (pi: ExtensionAPI) {
	pi.on("session_start", (_event, ctx) => {
		process.stderr.write("\nPI_SUBAGENT_SESSION " + JSON.stringify({
			type: "subagent_session", sessionId: ctx.sessionManager.getSessionId(),
			sessionFile: ctx.sessionManager.getSessionFile(), cwd: ctx.cwd, pid: process.pid,
		}) + "\n");
	});
}
