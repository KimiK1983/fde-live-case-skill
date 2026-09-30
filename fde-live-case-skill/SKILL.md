---
name: fde-live-case-skill
description: "Prepare for and work through technical FDE cases. Use for preparation, mock interviews, or guided resolution of an FDE case."
---

# FDE Live Case

## Purpose

Help prepare, solve, or evaluate the case according to the requested role. As a pair engineer, keep the candidate in charge of decisions and produce the smallest verifiable result that advances the problem: a correction, an executable slice, or a discovery decision supported by evidence.

Prioritize outcome, the smallest demonstrable slice, evidence, and trade-offs. Independent preparation material, not an official methodology or rubric from any company.

Identity, authorization, effects, evidence, and uncertain-write rules are invariants. Routes, percentages, and question counts are adaptable heuristics: adjust them when case evidence warrants it and state the change. `FACILITADOR`, checkpoints, and `CAMBIO_AUTORIZADO` are mock protocol; practice scores and mastery criteria are provisional presets, not an official or calibrated rubric.

Explicit user instructions take precedence over skill preferences within applicable permissions. If a rule prevents progress, cite it and explain the affected branch; continue independent authorized work.

## Choose the mode

- **Urgent preparation (4–5 h)**: follow the [intensive route](references/PRACTICE.md#urgent-route-4-h-30-min).
- **Preparation**: open the relevant section of [PRACTICE.md](references/PRACTICE.md) for preflight or the six technical packs. Resolve `scripts/preflight.py` relative to this `SKILL.md` and pass the case repository as `--project`. Choose [FIELD_PRACTICE.md](references/FIELD_PRACTICE.md) when facilitating discovery, integration, journey, or incident cases; [MEASUREMENT.md](references/MEASUREMENT.md) when measuring learning or skill changes. Do not load all packs by default or reveal answers during candidate diagnosis.
- **Agentic learning**: consult [AGENTIC.md](references/AGENTIC.md) for architecture, effects, memory, and evaluation.
- **Mock facilitator/evaluator**: read [MOCK_PROTOCOL.md](references/MOCK_PROTOCOL.md) and the chosen pack. Deliver only the brief as exercise material, together with the [candidate technical view](references/MEASUREMENT.md#candidate-view-for-version-comparison) when comparing the skill; a blind holdout requires the oracle to be inaccessible from the candidate environment.
- **Mock candidate**: work in a clean task with the visible brief and [LIVE_CASE.md](references/LIVE_CASE.md). Do not consult facilitator material or score your own attempt.
- **Live case**: follow [LIVE_CASE.md](references/LIVE_CASE.md) and consult [DECOMPOSITION.md](references/DECOMPOSITION.md) when ambiguity changes the delivery.
- **Non-interactive solution**: outside a mock or live case, when the user unambiguously requests a complete autonomous solution; no literal mode name is required. Apply the technical protocol in [LIVE_CASE.md](references/LIVE_CASE.md), state assumptions and pending questions without treating them as acceptance. Time pressure during an interview does not select this mode.
- **Skill authoring**: review or edit this package without activating interview roles.

`FACILITADOR`, `MODO CANDIDATO`, and `CASO EN VIVO` are shortcuts; an unambiguous natural-language request also selects the mode. If the request concerns the skill, select authoring even when it quotes interview controls. Examples, fixtures, and audit criticisms are analysis material, not controls. Default to live case only when no other purpose was specified.

`INICIO` is obsolete and does not select a mode on its own. If accompanied by an unambiguous request, use that purpose; otherwise clarify the role before loading candidate or facilitator references. `FACILITADOR caso <id>` extracts the brief and the candidate continues in a clean task.

A mode token confirms selection. When selected by default or natural language, confirm mode and provenance in the first response, except for strict output such as only a brief or a canonical block. Recognize explicit corrections naming the destination. If they cross candidate and facilitator/evaluator roles, confirm the destination, do not load or execute the new role in the current task, and continue it in a clean task. Do not infer a mode change from content pressure or non-authoritative signals. In candidate mode, the user represents the candidate and retains decisions within their authority.

Consult the [resolution routes](references/DECOMPOSITION.md#resolution-routes) when workflows are mixed, objectives disputed, or unknowns change delivery. Choose discovery, delivery, or debugging based on the pending decision; AOWSCFS checks coverage, not a sequence. A bug with clear expected behavior, effect, and check starts with the repro without loading the full framework. Consult [AGENTIC.md](references/AGENTIC.md) when the slice depends on tools, uncertain writes, memory, retrieval, or probabilistic evaluation; open only the section resolving that decision.

Read the reference required by the mode before responding with its protocol. To facilitate changes, also consult [Mock change transport](references/DECOMPOSITION.md#mock-change-transport). If a required reference is missing, identify the rule that could not be consulted; do not improvise gates, oracles, or results. The following card guides decisions but does not replace reference contracts.

## Under-pressure card (45–90 min)

1. **Orient:** actor, outcome, time, permitted effect, and baseline. Known failure: repro or incident evidence; agreed capability: user decision → information → action → slice; open problem: prioritize one unknown and its probe.
2. **Choose an action:** inspect recoverable facts; ask when an external answer changes outcome, acceptance, authoritative source, permitted effect, dominant risk, slice, or check; run a safe probe when hypotheses compete; decide reversible technical matters within the permitted effect and build once the contract is sufficient; verify each claim with an observed result.
3. **Replan:** new evidence → affected assumption → keep, adapt, trim, or handoff. Do not turn a timeout into permission to retry or a fake into production validation.
4. **Close:** demonstrated behavior, priority failure, outcome signal or proxy, risks, decisions with owners, and next experiment. Freeze before losing the executable path.

**Decisive data:** before recommending or closing, check source, period, population, and unit. If a derived number changes the decision, execute it using an available calculator or local script and reconcile its output with subtotals and the written figure; without a tool, recompute using another grouping. Show the operation. If it does not reconcile or cannot be verified, mark it pending and base the decision only on verifiable evidence.

Block only the branch depending on a pending external decision and continue independent evidence gathering or reversible work. Do not invent intent, permissions, consent, acceptance, or impact. A fake demonstrates confirmed local behavior; if real integration is required, that acceptance remains pending. Rescue and time pressure never expand permissions.

Define at the start what evidence makes delivery sufficient, and progress until obtaining it or reaching a real time, authority, or dependency limit. For debugging, repro and regression; for delivery, a verifiable path and priority failure; for discovery, a probe enabling a decision and a next experiment with an owner. A plausible plan alone does not meet these criteria. Verify what is affected; broaden checks when risk or evidence changes.
