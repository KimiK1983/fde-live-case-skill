# P1 · Latency in a multi-client platform

**Time:** 60 minutes. **Your role:** FDE with a client reporting a slow support agent. No production access; analyze traces, request discriminating data, and propose a read-only probe or local repro. No real timeout, scaling, or configuration changes are authorized.

The client says “AI became slow after traffic increased.” Four sample traces, in seconds:

| Trace | Concurrent requests | Queue/orchestrator | Model | External tool | Total |
|---|---:|---:|---:|---:|---:|
| a | 2 | 0.2 | 1.3 | 0.8 | 2.3 |
| b | 3 | 0.3 | 1.4 | 0.9 | 2.6 |
| c | 20 | 3.1 | 1.5 | 0.9 | 5.5 |
| d | 24 | 4.0 | 1.4 | 1.0 | 6.4 |

Bound what you know versus suspect; choose a next probe separating hypotheses. Explain how you decide between client mitigation and a shared platform correction, what evidence is needed before claiming success, and how to hand off. Adapt if a second affected client appears.
