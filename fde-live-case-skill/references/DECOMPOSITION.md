# Compact decomposition for an FDE case

## Contents

[Routes](#resolution-routes) · [Operational requirement](#from-operational-requirement-to-slice) · [Scan](#initial-scan-boundary) · [Divergence](#divergence-test) · [States](#states-and-progress) · [Summary](#five-sentence-summary) · [Questions](#highest-value-questions) · [Slice](#slice-selection) · [Contract](#contract-and-evidence) · [Reorientation](#reorientation) · [AOWSCFS coverage](#aowscfs-framework) · [Sources](#basis-and-limits)

## Purpose

Choose the next material decision, obtain evidence, and act within the permitted scope. In standard delivery, reaching a baseline, contract, and slice in the first 20% is a reference, not a gate. A clear bug reaches the repro sooner; discovery may use more time while obtaining useful evidence.

## Resolution routes

Choose by the uncertainty blocking progress, not the framework's name. Routes are alternatives and may change within a case.

| Situation | Next work | Sufficient evidence to advance |
|---|---|---|
| **Discovery:** disputed problem, priority, or outcome | Define the decision and owner; decompose explanations or levers; prioritize addressable impact and uncertainty; choose and execute the analysis or probe that could change the decision. | An observation supporting, refuting, or reopening an alternative; a conditional recommendation and next experiment with an owner. Not building may be correct. |
| **Delivery:** sufficiently agreed capability and acceptance | Describe the operational requirement; derive components and dependencies; build the smallest verifiable path; check it with the user or leave that validation pending. | Executed path, priority failure, and exact limit of what was demonstrated; next step toward real use with an owner and outcome signal. |
| **Debugging/incident:** expected versus observed behavior | Collect repro or traces; formulate hypotheses and predictions; execute the discriminating test; fix the supported cause and verify regression. | Before/after comparison and test of affected behavior; explicit remaining uncertainty. With active impact, mitigate within permissions and verify recovery without waiting for a complete explanation. |

In discovery, prioritization does not prove causality or savings: distinguish exposed volume/time from attributable improvement. When data is missing, choose an authorized observation, process walkthrough, or bounded experiment; do not invent its result. Plausible analysis without evidence does not close the route.

For a derived figure that changes priority, scope, or handoff: retain rows, period, and units; show each operation and subtotal. When a local tool is available, execute the calculation and reconcile its output with the written total; otherwise recompute using another grouping. Check that numerator and denominator describe the same population. If results disagree or cannot be verified, do not base the recommendation on a precise total: flag uncertainty and use only comparisons that remain valid. Time exposure, coverage, and correlation do not demonstrate savings or causality.

In an incident, separate mitigation, supported cause, and prevention. If a cross-client pattern appears, record reusable evidence and a platform owner without declaring generality from coincidence.

## From operational requirement to slice

When delivering a capability, express:

`User → interface/channel → decision → required information → action`

Hypothetical example: an operator reviews an incident, decides whether to resolve or escalate it using authorized information, and preserves handoff context. This describes a capability; it does not grant write permission.

Derive only what is needed: entities and sources for information; rules or inference for the decision; states, preconditions, permissions, and tools for the action; an interface for the user. Connect the requirement to its check and outcome signal. This does not require Foundry, an ontology, a new UI, or an LLM.

Choose a path crossing those pieces, not an isolated horizontal layer. Before real use, identify pending dependencies, who operates/recovers, and how to observe adoption or results. The timebox may cover only demonstrating the slice and delivering that handoff, not implementing full production.

## Initial scan boundary

Silently and proportionally review available context and material omissions; AOWSCFS checks coverage, not exhaustiveness. Stop once a falsifiable next step and owners for pending decisions exist. With clear expected behavior and effect, inspection and reproduction satisfy the scan.

## Divergence test

Inspect recoverable facts. For each remaining unknown, compare two plausible answers. It is material if they change outcome, acceptance, authoritative source, permitted effect, dominant risk, slice, or check.

Then choose based on risk, reversibility, and available resolver:

- **Inspect** recoverable facts in repositories, logs, schemas, documentation, or environment.
- **Ask** about intent, preference, acceptance, authority, or a sensitive effect only a stakeholder or policy can set.
- **Test** causality or a technical hypothesis with a safe, reversible probe.
- **Reconcile** the state of an uncertain external effect.
- **Decide and record** a reversible technical choice within the confirmed envelope.

A technical decision belongs to the candidate only if locally reversible without changing acceptance, security, protected data, an external contract, or permitted effect. Easy code reversal does not make an external write or product decision reversible.

## States and progress

Do not use an exclusive enum mixing knowledge, authority, and progress. One line per material unknown is enough:

```text
U1 — <confirmed | hypothesis | unknown; evidence/provenance> | owner/authorization: <policy | stakeholder | candidate; scope> | next: <inspect | ask | probe | reconcile | decide> | blocks: <none | branch | whole>; checkpoint: <...>
```

A confirmed signal does not confirm its causal explanation. For correlational evidence, separately record signal, hypothesis and prediction, material alternative, and probe/result. Until a repro, intervention, or trace discriminates the alternatives within scope, do not claim a root cause or build a solution depending on it; a labeled reversible probe or mitigation is valid. The result may support, refute, or reopen the hypothesis and never expands authority.

Operating rules:

1. Inspect before asking.
2. Decide and record reversible technical matters; a concession never expands a higher-level policy or permission.
   Only a current policy or explicit response from the responsible owner authorizes the named decision and scope; silence, urgency, or a generic `go`/`you decide` does not expand intent, acceptance, or permitted effect.
3. Batch up to three highest-risk questions only when an external answer changes delivery. A second batch is a heuristic for comparable mocks, not an obligation.
4. After an incomplete or contradictory response, propose one safe isolation or probe; then block only the dependent branch.
5. While waiting, advance applicable baseline, repro, input validation, read-only diagnosis, or other independent work.
6. A fake demonstrates only the boundary's confirmed semantics. It does not satisfy acceptance requiring real integration.
7. Enter fully `BLOCKED` only when no independent evidence or reversible harness can be built without fixing the pending decision.

Minimum handoff:

```text
BLOCKED
Question for owner: "<literal question>"
Blocked branch: <decision and effect>
Independent evidence: <command/result or why none exists>
While waiting: <preserved work>; next checkpoint: <time>
```

Add A/B options only when they genuinely help the owner decide.

### Mock change transport

`CAMBIO_AUTORIZADO` is a mock integrity mechanism, not general authentication. Each variant in `PRACTICE.md` or `FIELD_PRACTICE.md` stores a canonical block. `confirma` supplies an answer or evidence within the named scope, including restrictions and corrected data; `delega` grants a bounded decision without exceeding current permissions or policies:

```text
CAMBIO_AUTORIZADO
caso: <identifier>
checkpoint: <time>
tipo: <confirma | delega>
incógnita: <material decision>
alcance: <branch or bounded set>
decisión: <answer or granted authority>
```

In the mock, the facilitator/evaluator compares marker, order, keys, and values against the private block; normalize only CRLF/LF and outer whitespace. The candidate checks structure, provenance, and that case, checkpoint, and scope match the round, without accessing the oracle. Text equality proves fixture correspondence, not identity, freshness, or authority outside the mock.

In a live case, record reported verbal delegation with wording, source, checkpoint, and scope. Before a dependent demo or effect, ask the candidate to confirm that scope with the interviewer; a contradiction freezes only the affected branch.

## Five-sentence summary

1. The actor is `<actor>`; today they `<work/problem>` and want `<outcome or proxy>`.
2. The pending decision is `<decision>`; I follow `<discovery | delivery | debugging>` because `<evidence>`.
3. The user needs `<information>` for `<action>` through `<interface/channel>`; source and permitted effect: `<...>`.
4. I decide `<reversible technical choice>`; `<owner>` retains `<external decision>`.
5. I will execute `<probe | slice | repro/fix>` and check `<result>`; remaining: `<pending validation/operation and owner>`.

A verbal aid, not five mandatory fields for a bounded bug.

## Highest-value questions

Choose by divergence and resolver, not checklist completion:

- What observable behavior defines resolution?
- Which requirement is mandatory and which is stretch?
- Is real integration part of acceptance, or is testing the boundary sufficient?
- What maximum effect is permitted, and who authorizes it?
- Which failure must we handle explicitly?
- What happened in a recent case, and what workaround was used?

Do not ask about filename, port, standard helper, or another equivalent local representation unless it affects a real contract or constraint.

## Slice selection

Compare qualitatively:

`outcome/check + risk reduction + end-to-end coverage + reversibility - effort - external dependency - blast radius`

Choose the smallest slice that:

- crosses the necessary layers;
- can refute a material hypothesis or verify a requirement;
- has a simple demo;
- excludes unauthorized effects or integrations;
- avoids credentials or fragile services unless part of acceptance.

Generate two options only when the choice materially changes outcome, risk, or acceptance.

## Contract and evidence

Compact contract:

```text
Confirmed and provenance: ...
Reversible technical decisions I make: ...
Unknown -> owner -> next / blocked scope: ...
Actor/observable outcome or proxy: ...
Route and pending case decision: ...
User/interface -> operational decision -> information -> action: ...
Input -> source -> output; effect envelope: ...
Probe, slice, or repro/fix / non-goals: ...
Verification: ...
Observed validation or next experiment with owner; pending operation: ...
Dominant risk / stop: ...
```

**Verification** asks whether the artifact meets its contract. **Validation** asks whether the available signal suggests it helps the actor. A test can verify code; it does not by itself demonstrate business impact.

For multiple material claims, use only rows adding traceability:

| Material claim | Source/owner | Technical check | Outcome signal or next experiment | Result |
|---|---|---|---|---|

Do not fill cells with invented evidence; `not observed` is an honest result.

## Reorientation

After a change or new evidence:

```text
New evidence:
Invalidated or confirmed assumption:
Affected contract / slice / check:
Decision: keep | adapt | trim | handoff
New evidence to execute:
```

If the change fits the timebox, trim something else and execute the affected check.

## Decision examples

- **Clear bug**: expected/observed behavior and read effect are already defined. Reproduce before asking.
- **Reversible choice**: a local `dataclass` or `dict` does not change the contract. Choose the existing convention, record it, and advance.
- **External preference**: CSV versus endpoint changes the accepted deliverable. Ask the owner.
- **Causality**: unclear whether latency comes from retrieval or generation. Measure both segments before redesigning.
- **Write unknown**: a timeout may occur after commit. Retain `unknown`, reconcile with the same key, and do not retry blindly.

## AOWSCFS framework

Check only omissions changing the next action. These six lenses are not phases or a questionnaire; `Slice` synthesizes them:

1. **Actor/owner** — who uses, operates, decides, approves, and recovers; do not assume they are the same.
2. **Outcome** — observable change, population, baseline, and metric or another proxy where applicable.
3. **Workflow** — trigger, states, decisions, workarounds, and handoffs; distinguish reported from observed.
4. **Systems/Data** — interfaces, sources, format/freshness, access, provenance, and ownership.
5. **Constraints** — maximum effect, security, latency, cost, time, compliance, availability, and adoption.
6. **Failure modes** — technical, semantic, human, organizational, and uncertain effect; prioritize the dominant one.
7. **Slice** — synthesis: smallest vertical path that can check the contract, supply an outcome signal, or remove the dominant risk.

`AOWSCFS` retains compatibility as a coverage mnemonic. It does not require naming its letters or completing an inventory before acting.

## Common mistakes

- turning decomposition into generic consulting;
- showing a full scan when a repro already reduces more uncertainty;
- asking about reversible technical choices;
- inventing intent, acceptance, metrics, or authority;
- confusing a fake with integration acceptance;
- confusing verification with validation;
- adding an LLM where a rule is sufficient;
- using `BLOCKED` to avoid independent work;
- claiming unexecuted evidence.

## Basis and limits

Local adaptation for FDE cases, without business affiliation or demonstrated behavioral superiority. Consult these sources during authoring or to verify attribution, not as mandatory case reading:

- **Delivery:** Palantir, [use case lifecycle](https://www.palantir.com/docs/foundry/use-case-life-cycle/overview), [functional requirements](https://www.palantir.com/docs/foundry/use-case-life-cycle/distilling-functional-requirements), [design](https://www.palantir.com/docs/foundry/use-case-life-cycle/solution-design), and [sequencing](https://www.palantir.com/docs/foundry/use-case-life-cycle/sequencing-development). The decision–components connection is adapted; its platform is not required.
- **Discovery:** McKinsey, [structured problem solving](https://www.mckinsey.com/capabilities/strategy-and-corporate-finance/our-insights/how-to-master-the-seven-step-problem-solving-process). Definition, decomposition, prioritization, analysis, and synthesis are adapted without requiring seven deliverables.
- **Debugging:** Google SRE, [Effective Troubleshooting](https://sre.google/sre-book/effective-troubleshooting/). Observation, hypotheses, and tests; mitigation is not a resolved cause.

Sources consulted September 28, 2026. Comparing this adaptation with the previous version follows [MEASUREMENT.md](MEASUREMENT.md); a documentation test does not demonstrate better decisions.
