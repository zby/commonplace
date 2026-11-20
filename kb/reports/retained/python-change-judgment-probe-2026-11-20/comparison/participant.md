A team distributes a CPython build for Linux services. It is deciding whether to change the build it ships by default. The following figures describe a fictional deployment.

The current default omits frame pointers. The proposed default preserves them in the interpreter and the bundled native extensions. Frame pointers let a sampling profiler trace the chain of native function calls while a service is running. A third-party library built without them can interrupt that chain. Both builds remain available. Switching a running service to the other build requires a redeployment.

In a replay of the team's usual traffic, the proposed build used 1% more CPU time for the same requests. In four of the last ten performance investigations, the existing profiler could not identify the caller at a point the investigators cared about. In a replay of those four incidents using the proposed build, the caller was visible in three. The team has no estimate of the investigation time that information would have saved.

Should the team change its default build? Give your judgment and explain how you reached it. Use the case as given. Work independently without tools or outside research. Answer in at most 250 words.
