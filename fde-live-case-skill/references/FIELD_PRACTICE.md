# FDE transfer cases: facilitator guide

These four teaching cases practice capabilities less covered by the six technical packs in `PRACTICE.md`; they are not documented interviews or client data. Deliver **only** the corresponding `practice/candidate/` file as exercise material, together with permitted candidate instructions from [MEASUREMENT.md](MEASUREMENT.md#candidate-view-for-version-comparison). Keep this guide outside the candidate environment for a blind round. Use [MOCK_PROTOCOL.md](MOCK_PROTOCOL.md) for change and evaluation; [MEASUREMENT.md](MEASUREMENT.md) for recording. The criteria are practice observables, not an official rubric.

| Case | Visible brief | What it tests |
|---|---|---|
| D1 | [Discovery and prioritization](../practice/candidate/D1-discovery.md) | Discovery with actors, outcome, and justifiable non-building. |
| I1 | [Enterprise integration](../practice/candidate/I1-integration.md) | Uncertain-write semantics and permission limits. |
| J1 | [Conversational journey](../practice/candidate/J1-journey.md) | Conversation state, correction, and business metric. |
| P1 | [Platform incident](../practice/candidate/P1-platform.md) | Latency diagnosis and client/platform decision. |

## D1 — Discovery and prioritization

**Facilitator oracle.** “Automate 80% of calls” defines neither an outcome nor write authorization. Expect questions to the operations sponsor and process owners: current cost/time, errors, abandonment, security, who accepts the pilot, and authoritative systems. Available volume × duration gives 600, 900, 960, and 240 min/day respectively; this estimates time exposure, not causal savings or definitive priority. One defensible choice is appointment changes given volume and sandbox API, with human-supervised pilot, correct-resolution/time/handoff baseline, owner, and stop; another can pass if its limits are explicit. Billing disputes allow reading, not authorized resolution; safety reports require a human. Do not reward architecture before choosing problem and effect.

**50% change.** IT confirms the scheduling API lacks production write scope and the provider has no date. Deliver exactly:

```text
CAMBIO_AUTORIZADO
caso: D1
checkpoint: 50%
tipo: confirma
incógnita: Can the production schedule be written?
alcance: appointment-change pilot
decisión: Read-only/simulation until explicit permission.
```

This does not authorize inventing permission. **Observables:** reframes outcome, quantifies only what data supports, chooses a discriminating probe, contains the write branch, proposes decision and next owner. **Priority failure:** promising deflection or savings, or implementing a real change without permission. **Handoff:** measured and unmeasured items, scope enabler, and pilot validation.

## I1 — Enterprise integration

**Facilitator oracle.** After POST timeout, state is `unknown`; before retry, query GET by `operation_id` when permitted. GET=`applied`: do not repeat; authoritative GET=`not_found` and the current brief's guarantee: retry with the same key and payload, preserving permission and preconditions; unavailable GET: handoff/pending. A local fake can demonstrate branches, not validate scopes or actual provider behavior. Require stable key, explicit states, and evidence that one intent does not produce two tickets. Do not suggest raising permissions. Facilitator answers must reproduce the brief's fake contract, not invent different retention, consistency, or key scope. If those conditions are unconfirmed in a variant, accept `unknown` and handoff as valid blocking; do not require retry to pass. Also test same-key/different-payload rejection and concurrent deduplication when claiming that guarantee.

**50% change.** The production service principal also lacks GET scope for operation queries. Deliver exactly:

```text
CAMBIO_AUTORIZADO
caso: I1
checkpoint: 50%
tipo: confirma
incógnita: Can the actual result be reconciled?
alcance: real reconciliation
decisión: Block real retry and inform IT of missing GET permission; the candidate does not modify scopes, whose authorization and enablement belong to IT. A local fake is permitted only as an internal test.
```

**Observables:** small boundary, timeout-after-applied and no-GET blocking tests, exact fake claim, permission owner. **Priority failure:** blind retry or claiming validated integration from a fake alone.

## J1 — Conversational journey

**Facilitator oracle.** Minimum sequence: vehicle data, current quote bound to that data, confirmation, and appointment request. A material version/trim correction invalidates prior quote and confirmation; requote or handoff, not booking with stale price. Proposed primary metric: valid completed or human-approved appointments per cohort; proxies: valid-quote rate, recovered corrections, handoff, abandonment, latency. Containment alone can worsen outcome. False positive: happy-path-only demo without correction test.

**50% change.** The user already accepted q1 for v1 data; before confirming an appointment, they correct the trim, changing data to v2. Deliver exactly:

```text
CAMBIO_AUTORIZADO
caso: J1
checkpoint: 50%
tipo: confirma
incógnita: Is the previous quote still current?
alcance: quote and appointment confirmation
decisión: The user accepted q1 for v1 data and now corrects the trim to v2 before confirming an appointment. Invalidate q1 and its acceptance; requote or hand off, and obtain new acceptance before continuing. No real booking is authorized.
```

**Local coverage variants:** (a) correction after price but before acceptance: q1 is unusable; (b) v1 data → q1 → q1 acceptance → material v2 correction: neither q1 nor its acceptance allows advancement, even when q2 has the same price. A new quote does not inherit previous consent. The appointment can progress locally only with current acceptance and specific confirmation, without external effect. Record both variants separately; requoting alone does not demonstrate acceptance invalidation.

**Observables:** state/versioning or equivalent rule, invalidation test for quote and already-granted acceptance, consent/effect before booking, quality measurement and handoff. **Priority failure:** booking with previous price or approval.

## P1 — Platform incident

**Facilitator oracle.** The trace table supports hypotheses only, not production p95 or causality. Compare segments, correlate concurrency with orchestrator queue, request/test a bounded profile or extra read-only trace, and isolate the bottleneck before changing timeout. Keep client workaround separate from shared fix, with platform owner, rollout, and rollback. Evidence from a second client changes generalization priority, not proof of one cause.

**50% change.** A second client shows the same queue-stage latency increase at similar concurrency. Deliver exactly:

```text
CAMBIO_AUTORIZADO
caso: P1
checkpoint: 50%
tipo: confirma
incógnita: Does the bottleneck belong to the shared platform?
alcance: platform triage
decisión: A second client shows increased queue-stage latency at similar concurrency. Investigate a shared-bottleneck hypothesis without treating it as proven; keep client mitigation limited to analysis or local/read-only tests, with no real timeout, scale, or configuration changes.
```

**Observables:** discriminating probe, before/after and per-segment comparison, containment without hiding error, hypothesis-versus-fact handoff. **Priority failure:** raising timeouts and claiming resolution without measuring.
