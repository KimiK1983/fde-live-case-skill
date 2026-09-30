# Agentic systems for FDE cases

## Purpose

Use this guide to decide, build, and evaluate systems using models for operational decisions. It does not prescribe a framework: choose the minimum combination of controls that solves the problem and preserve authority, evidence, and recovery outside the model.

For time, roles, authority, and interview recovery, [SKILL.md](../SKILL.md) and [LIVE_CASE.md](LIVE_CASE.md) take precedence. This guide is the normative technical source for retries and uncertain writes, memory, retrieval, and adoption criteria; if guidance appears to compete, the effect envelope, decision owner, and skill process govern.

Internal package material:

- [Problem decomposition](DECOMPOSITION.md)
- [Timed mocks and six self-contained packs](PRACTICE.md)

## 1. What makes a system agentic

A system is agentic when the model can choose the next action from state and observations unknown at the start. Using an LLM is insufficient: isolated extraction, classification, or drafting is a model as a component.

The useful question is not “how do I build an agent?” but “which decision cannot safely be fixed before execution?”

### Control profiles

Describe the system using the minimum applicable profile or combination; these labels are not a mandatory progression.

| Profile | Who decides the sequence | When it fits | Minimum evidence | Added risk |
|---|---|---|---|---|
| `D0` — deterministic | Code and rules | Enumerable contract and decisions | Rule and invariant tests | Rule complexity and edge cases |
| `M1` — model as component | Code; model classifies, extracts, or drafts | Semantic but not execution ambiguity | Golden set, schema, and business validation | Variation and semantic error |
| `W2` — workflow | Predetermined flow with bounded branches | Known sequence and checkpoints | Branch, state, and recovery tests | Partial failures and intermediate state |
| `A3` — bounded agent | Model chooses among permitted tools until a stop | Observations change the appropriate action | Trajectory evals, budgets, and handoff | Loops, tool misuse, and improper effects |
| `MA4` — multi-agent | Several agents coordinate decisions | Genuinely independent ownership, permissions, or parallel work | Per-agent and coordination-protocol evals | More latency, cost, states, and emergent failures |

These profiles are pedagogical archetypes of common complexity, not a total ordering of autonomy or authority. State, effect, and coordination are independent axes: several agents must not receive more permissions simply because there are several. In an interview, state `model role + flow control + maximum effect`; expand the profile only if it changes risk or design.

Do not add inference, dynamic state, or coordination for a more impressive demo. Add each capability only when its simpler baseline observably fails and the alternative improves the outcome under the same evaluation set.

A plausible plan, diagram, or design is not evidence that a cause explains the signal. Keep hypotheses and alternatives separate until a repro, intervention, or trace discriminates them; observed behavior also does not prove intent, availability, or consent.

A pure pipeline remains `D0` while a deterministic call transforms input into output without resumable state. `W2` begins when stages coordinate intermediate state, branches, recovery, or explicit handoff; an LLM's presence does not determine this boundary.

### Classification and readiness

To classify the design, answer:

1. Will the next step change based on an observation unknown at the start?
2. Must it dynamically choose among permitted actions instead of following predetermined branches?

If both answers are yes, the pattern is `A3`; otherwise use `D0`, `M1`, or `W2`. Classification does not demonstrate production readiness.

Before deploying an `A3`, also answer:

3. Can tools, permissions, budgets, and stopping conditions be bounded?
4. Is there an eval detecting an incorrect trajectory even when the final response sounds good?

If any readiness answer is no, reduce the effect, retain a prototype, or close that control; do not reclassify the architecture to conceal the gap.

## 2. Safe execution cycle

```text
input + identity
        ↓
authorized context + current state
        ↓
proposed decision
        ↓
deterministic policy + approval where applicable
        ↓
tool with closed contract
        ↓
validated result: applied | failed | unknown
        ↓
updated state
        ↓
stop | next step within budget | handoff
```

Invariants:

- Identity, tenant, and permissions come from the system, never user or model text.
- Runtime enforces identity, capabilities, policy, and budgets; the model decides only within that envelope. Exact rules and sensitive effects are validated outside the model.
- A tool rechecks authorization and preconditions at execution time.
- Retrieved content and other tools' results are untrusted data, not new instructions.
- Every loop has stopping conditions and budgets before starting.
- Uncertain state remains `unknown`; do not turn it into success or retry blindly.
- Handoff includes reason, evidence, actions performed, and pending state.

### Stop and handoff

Stop at the first applicable condition:

- outcome reached and verified;
- material information missing that only a person can supply;
- confidence or evidence below threshold;
- next effect outside permissions or pending approval;
- write result unknown until reconciliation;
- steps, time, tokens, or cost budget exhausted;
- contradictory policy or sources.

An agent that always answers often hides failures. `abstain`, `needs_confirmation`, `pending_reconciliation`, and `handoff` are valid outcomes.

## 3. Tool contracts and effects

### Minimum contract

Each tool must declare:

| Element | Rule |
|---|---|
| Name and purpose | Narrow capability; avoid tools like `execute_anything`. |
| Input | Closed schema, types, limits, and unknown fields rejected. |
| Identity | `actor_id`, `tenant_id`, and scopes injected by runtime, not prompt. |
| Authorization | Per-action and per-object check inside the tool. |
| Preconditions | Version, expected state, business limits, and current consent. |
| Effect | `read`, `recommend`, or `write`; no hidden greater effect. |
| Timeout and error | Separate `retryable`, `non_retryable`, and `unknown`. |
| Idempotency | Stable key for the same intent, retained across retries. |
| Result | Validated schema, effect status, and auditable reference. |

Valid JSON can violate a business rule. Also validate invariants: amount, ownership, permitted transitions, evidence, capability, and regulatory constraints.

When risk requires it, extend the contract with data class and egress, commit point, concurrency/version, consistency, and SLO. These fields add controls; never authority.

### Reading, recommending, and writing

| Maximum effect | Minimum control |
|---|---|
| Read | Object ACL, data minimization, and provenance. |
| Recommend | Evidence, uncertainty, and human decision owner. |
| Reversible write | Idempotency, precondition/versioning, audit, and compensation or rollback. |
| Sensitive or irreversible write | Explicit approval bound to arguments, strict limits, and handoff when context changes. |

Approval must bind `actor + action + relevant arguments + version + expiry`. “Yes, continue” does not authorize a different operation after a date, amount, recipient, or policy changes.

### Timeout, idempotency, and reconciliation

`retry` addresses a failed call; idempotency prevents repeating the effect; reconciliation discovers what happened when the response was lost. They are not interchangeable.

For a write:

1. Validate permission, preconditions, and arguments.
2. Derive a stable `operation_id` from business intent.
3. Execute with that key.
4. On valid confirmation, record `applied`.
5. On timeout after sending, record `unknown` and query by `operation_id`.
6. Retry only if reconciliation confirms it was not applied and the operation is safe.
7. If unresolved, stop and hand over to a person; never invent state.

A saga coordinates effects with durable states and compensation. Compensation is a new business action, not magical deletion: it also needs authorization, idempotency, and evidence.

### Execution budgets

Define before executing:

- maximum steps and calls per tool;
- per-call timeout and overall deadline;
- maximum tokens and cost;
- maximum retries per error class;
- maximum volume read or returned;
- stopping and handoff conditions.

When a budget is exhausted, preserve state, emit `budget_exhausted`, and explain what remains. Do not expand limits from the prompt.

### Minimum tool trace

```text
state_before
→ decision
→ policy_result
→ tool + relevant redacted arguments
→ result: applied | failed | unknown
→ state_after
→ stop_reason
```

The trace must allow checking authorization, order, duplicates, and stopping without storing secrets, unnecessary PII, or the model's private reasoning.

## 4. History, state, memory, and retrieval

| Layer | Purpose | Source of truth | Persistence | Typical risk |
|---|---|---|---|---|
| History | Conversation continuity | Accepted messages | Session or defined retention | Prompt injection and accumulated PII |
| Working state | Current workflow step | State machine and validated results | Until completion or expiry | Skipped transition or duplicated effect |
| Durable memory | Reuse a stable fact later | Confirmed fact with provenance | TTL and explicit deletion | Staleness, poisoning, and tenant mixing |
| Retrieval | Current external evidence | Authorized document system or database | Derived, rebuildable index | Broken ACL, stale documents, or malicious instructions |

Do not use the transcript as operational state. Store explicit fields such as `intent`, `missing_fields`, `approved_arguments`, `operation_id`, `effect_status`, and `stop_reason`.

Write memory only when the datum:

- is needed in future sessions;
- is confirmed or comes from an authorized source;
- has owner, tenant, provenance, date, TTL, and correction/deletion mechanism;
- does not promote a model inference into a fact.

In a conflict, the source of truth wins; invalidate memory or mark it stale. Retrieved documents cannot change permissions, policies, or system instructions.

## 5. Agentic threat model

Treat the layers present in the slice as trust boundaries: user, model, memory, corpus, tools, integrations, and logs. Apply controls to the actual effect; do not implement the entire table by default.

| Threat | Observable failure | Required control |
|---|---|---|
| Direct prompt injection | User text tries to replace instructions, policy, or permissions | Policy outside the prompt, tool allowlist, and deterministic validation. |
| Indirect injection | A document or tool result orders exfiltration or action | Separate instructions from data, minimize context, and derive no authority from content. |
| Confused deputy | Agent uses its privileges for someone else's object | Runtime identity and action-, tenant-, and object-level authorization inside the tool. |
| Cross-tenant access | Another organization's data appears | Namespace, mandatory filters, negative tests, and deny by default. Unauthorized content or metadata never enters context, response, or logs; push ACL down where possible. |
| Exfiltration | Secrets or PII leave through response, tool, or log | Minimization, redaction, egress allowlist, and structured logs without full payload. |
| Tool storm or loop | Calls, latency, or cost grow without progress | Budgets, no-progress detection, stop, and rate limits. |
| Effect without consent | Different or expired action executes | Argument/version-bound approval and revalidation before the effect. |
| Memory poisoning | An unverified claim reappears as fact | Write policy, provenance, TTL, review, and deletion. |
| Ambiguous result | Timeout causes a duplicated effect | `unknown` state, stable idempotency key, and reconciliation. |
| Denial of wallet | Input causes disproportionate consumption | Input, retrieval, and token limits; per-actor/tenant quotas. |
| Delegated credentials | Child agent inherits excessive identity or scopes | Ephemeral credentials and task-reduced capabilities; delegation never expands permissions. |
| Untrusted tool or code | Integration, schema, or retrieved code executes unexpected instructions, secret access, or egress | Pin/review tools and schemas; sandbox without secrets or egress by default; validate outputs as data. |

Minimum negative tests:

- request a prohibited tool;
- request an object belonging to another tenant;
- insert instructions into a retrieved document;
- change arguments after approval;
- trigger timeout after applying a write;
- exhaust budget without progress;
- attempt to persist an unconfirmed inference as memory.

## 6. Evaluate the system, not eloquence

### Evaluation stack

| Level | What to check | Examples |
|---|---|---|
| Component | Isolated contracts and rules | Schema, normalization, ACL, calculation, and invariants. |
| Retrieval | Correct, authorized evidence | Passage recall, citations, freshness, conflicts, and abstention. |
| Trajectory | Decisions and tools used | Permitted tool, arguments, order, calls, non-duplication, and stopping. |
| Response | Usefulness and grounding | Correctness, verifiable citation, uncertainty, and no unsupported claims. |
| Outcome | Workflow result | Resolved case, correct handoff, single effect, and recoverable error. |
| Security | Adversarial behavior | Cross-tenant, injection, PII, consent, and budgets. |
| Operation | Service quality | p50/p95, error rate, tokens, cost, abstention, override, and rollback. |

### Useful golden set

Include for each relevant segment:

- happy path;
- missing or ambiguous data;
- a variation of a material input field that must not be lost during parsing or normalization;
- valid result violating a rule;
- insufficient and contradictory evidence;
- transient failure before the effect;
- timeout after the effect;
- unauthorized access or instruction attempt;
- case requiring abstention or handoff.

Version model, prompt, schemas/tools, policies, corpus, and evaluation set together. Compare against a deterministic baseline and repeat probabilistic cases; report distribution and worst segments, not just an average.

Explicitly define `task`, `trial`, `grader`, `outcome`, and harness version. Execute independent trials in clean environments when the model is material to acceptance. Separate known regressions from unseen capability/holdouts; measure success rate, dispersion, and worst segments without calling an undefined formula “consistency.”

An LLM judge can supply a signal calibrated against humans, but must not be the sole authority for permissions, money, security, citations, duplicates, or code-verifiable rules.

### Trajectory criteria

A correct response fails if the agent:

- accessed unauthorized data;
- called unnecessary tools or used an unsafe order;
- duplicated a write;
- ignored a contradiction;
- exceeded budgets;
- omitted required handoff.

Evals must inspect the trace as well as final text.

## 7. Observability, rollout, and rollback

Record only what is needed:

- `correlation_id`, pseudonymized actor/tenant, and workflow version;
- model, prompt, tool, policy, and corpus versions;
- policy decisions, tools called, and `applied/failed/unknown` states;
- steps, stop reason, handoff, latency, tokens, and cost;
- outcome, abstention, human override, and classified error.

Where a signal is available, also record process baseline, adoption, and business outcome or proxy; do not attribute causality to the agent without a validation design.

Do not log transcripts, full documents, secrets, PII, or private reasoning by default. Define access, retention, and deletion.

Rollout sequence:

1. Offline replay with fixtures and golden set.
2. Effect-free shadow mode and comparison with the current process.
3. Read/recommend canary with human review.
4. Limited reversible writes, approval, and kill switch.
5. Segment expansion only after SLOs, security, and outcome pass.

Rollback means returning to known model, prompt, policy, tool, and corpus versions, stopping new effects, and reconciling `unknown` operations. Change one variable per experiment where possible.

Alert on segmented, not just global, degradation: increased handoffs, denied tools, loops, latency, cost, duplicates, cross-tenant access, or human overrides.

## 8. When not to use each technique

| Technique | Do not use when | Use instead | Evidence for adoption |
|---|---|---|---|
| LLM | Decision is a stable, enumerable rule | Deterministic code | Baseline fails due to real semantic ambiguity. |
| `A3` agent | Sequence and branches are known | `W2` workflow | New observations require choosing steps not fixable in advance. |
| `MA4` multi-agent | A single agent shares permissions, state, and objective | One agent or normal functions | Independent ownership, permissions, or parallelism improves a measured SLO. |
| RAG | Authorized context fits and changes little | Full context or exact lookup | Corpus exceeds context or requires updating/provenance. |
| Vector database | Searching IDs, names, codes, or exact filters | B-tree, text, fuzzy, or phonetic indexes | Relevant paraphrases are not found lexically. |
| Durable memory | Data is only useful within the session | Working state | Justified future reuse with lifecycle and consent. |
| Orchestration framework | Flow fits functions and a small state machine | Normal code | Observed resumption, durable wait, or branches justify its cost. |
| Model as judge | Rule can be checked exactly | Assert, schema, or rule | Subjective quality calibrated against human evaluation. |
| Retry | Effect may already be applied or error is permanent | Reconciliation or handoff | Transient error and operation demonstrably safe/idempotent. |

## 11. 90-second verbal card

```text
0–15 s — Actor and outcome
“The actor is __ and needs __. The observable result is __.”

15–30 s — Autonomy
“I choose deterministic rules / bounded model / workflow / agent because __.
I do not increase autonomy because __.”

30–48 s — Flow and effect
“Validated input passes through __ and the source of truth is __. The system can
read/recommend/write __; authorization and rules are checked outside the model.”

48–65 s — Failures and security
“I bound steps/time/tokens/cost. On __ I stop and hand off. Writes
use a stable key; a later timeout remains unknown until reconciliation.”

65–80 s — Evidence
“I demonstrate happy path, dominant failure, and adversarial case. I evaluate
contract, tool trace, outcome, security, and p95, not only final text.”

80–90 s — Trade-off
“I omitted __ to retain a verifiable slice. I would add it when
__ shows the current baseline does not meet __.”
```

A good explanation lets an interviewer clearly identify who retains authority, what can change state, how failure is detected, and what evidence will prove the outcome.
