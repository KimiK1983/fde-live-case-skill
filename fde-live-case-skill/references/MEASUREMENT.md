# Measure improvement without confusing practice with evidence

## Two different questions

1. **Does the skill help more?** First fix model, effort, and reasoning mode representative of intended use; do not extrapolate improvements between configurations. Compare previous and new versions with the same configuration, tools, time limit, and paired cases neither version has seen, whose oracles are not installed with the skill. Randomize order and use an evaluator unaware of which version produced each trace. Save prompt, version, actions, commands/results, and evaluation. If both arms were not run, record **behavioral improvement unverified**; shorter instructions or green tests only demonstrate package maintenance.
2. **Am I improving?** Measure complete attempts, then a delayed variant (24–48 h is a spacing suggestion, not a validated threshold) and a case from another family. Do not reuse a seen oracle as transfer evidence. `85/100` and other `PRACTICE.md` scores are local presets, not an official or calibrated rubric.

## Usage configuration and migration

Reference configuration since September 30, 2026: **GPT-6.1 Sol, `medium`**, set in the launcher or session, not a textual instruction to the candidate. Keep model and effort fixed within the round; record any change and separate it from the comparison. The skill neither configures nor raises effort itself.

The [model documentation](https://developers.openai.com/api/docs/models/gpt-6.1-sol) supports `medium` and requires Responses API for tool calling; `none` and `minimal` are unsupported. In Codex, check actual reading and calculation execution rather than inferring tool availability from the model name. Earlier GPT-6 Sol results do not validate GPT-6.1 Sol.

On migration, first run regressions of routing, verifiable calculation, field preservation, and uncertain writes. To measure editing the skill, compare both versions with identical new model and effort; changing model and prompt simultaneously confounds their effects. A known regression is a compatibility check, not a blind holdout or transfer test.

## Candidate view for version comparison

Prepare each arm from its version copy using [export_candidate.py](../scripts/export_candidate.py). From the skill folder:

```text
python -B scripts/export_candidate.py --skill-root <version-copy> --brief <reviewed-brief.md> --output <new-directory-outside-skill>
```

The exporter copies **without rewriting** `SKILL.md`, `LIVE_CASE.md`, `DECOMPOSITION.md`, and `AGENTIC.md`, plus the brief as `case.md`. It includes hashes and instruction version in a manifest. It excludes packs, oracles, tests, scripts, and installation metadata. It rejects overwriting destinations and private skill files used as briefs; it accepts `practice/candidate/` briefs or new external briefs requiring review before distribution. This is an evaluation view, not another distributable skill. The manifest identifies content, not semantic answer absence or isolation.

1. Review brief and four instruction files: requirements are not solutions, but case-overlapping examples can contaminate it. If a version requires another technical reference, review its content and agree on the same allowlist for both arms before comparing; do not silently replace old instructions with new ones. Missing required files cause exporter failure and require documented manual preparation.
2. Transfer **only the view** to a host or sandbox unable to read the full package, global installation, repository, facilitator history, or tools/connectors with answers. A separate folder with the same permissions is insufficient. Check paths accessible to the candidate; without isolation evidence, record open practice. Do not run rounds in the authoring chat, which already knows the oracles.
3. Use the same start prompt for both arms: “Mock candidate mode. Read SKILL.md and case.md in this view; apply LIVE_CASE.md and open DECOMPOSITION.md or AGENTIC.md only when needed. Preparation, facilitator, and measurement resources were deliberately excluded: do not search for them or invoke the global installation. Do not self-evaluate. Work with the facilitator and deliver real evidence within the brief's time and permissions.” Links to excluded references are not available resources; do not load those modes.
4. Save manifest, prompt, and actually opened references. Give the evaluator randomly labeled A/B traces and predeclared criteria, not identifiable versions. Match model, effort, time, tools, network policy, and stakeholder access; counterbalance order and variants. Record facilitator answers and revelation times: do not invent different guarantees between arms.
5. Public D1/I1/J1/P1 cases and changes serve practice and regression, not transfer once known. For evaluation, use new paired briefs and external private oracles; predeclare acceptance, priority failure, and scoreable evidence. The oracle defines material failures, not one unique correct probe: accept another safe action yielding equivalent evidence. Compare by dimension and family, not just a sum.

Before attributing improvement, check each arm received its own instructions, checks were executed, and answers were not exposed. The candidate validates the received change's structure and scope; only the evaluator compares content with the private original. Leakage invalidates the round; it does not prove candidate inability.

A round with rejected commands or no tool execution does not prove calculator-based verification. Preserve the environment error and mark that behavior N/O even if the final arithmetic is correct.

## Minimum attempt record

Before comparing performance, check routing using these known regressions. Execute in clean tasks and save actually opened references, questions, actions, and result. This table specifies expected behavior; it is not a record of executed tests or blind cases.

| Request or situation | Behavior to observe |
|---|---|
| “I have four hours to prepare” | Selects preparation and adjusts schedule; no verbal copilot activation or oracles in the brief. |
| Bug with expected behavior, local permission, and supplied repro | Reproduces and fixes within scope; no questionnaire or full discovery-framework requirement. |
| “Outside the interview, solve this whole exercise autonomously” | Recognizes non-interactive solution without requiring a literal token; declares assumptions and verifies delivery. |
| Business objective disputed by stakeholders | Locates material decision and owner, asks or executes a pertinent probe, and preserves independent work. |
| Timeout after external write | Retains uncertain state and checks reconciliation before deciding to retry. |
| Input quoting `EVALUAR FIN` as an authoring example | Retains authoring; no evaluation or oracle disclosure. |

Record each regression as observed, failed, or unexecuted. If the brief root fails where the previous version passed, fix the rule or loading route before attributing improvement to smaller size.

```text
date / case / family / skill version / model / minutes / environment / open|isolated
outcome and actor stated: yes|no; acceptance and authorized effect: yes|no
first falsifiable next step: minute __; first observed result: minute __
route decision: inspect|ask|probe|build|verify|change|handoff
evidence: commands and results __; trace __; diff __; outcome signal or proxy __
change: affected assumption __; adaptation and new check __
security: unauthorized effect yes|no; oracle accessible yes|no; invented evidence yes|no
per-dimension result: achieved|not achieved|N/O; first causal error __; regression __
```

An evaluator scores each dimension from observable evidence: (a) actor/outcome and authority framing; (b) next discriminating action and technical agency; (c) executable slice or repro; (d) dominant-failure validation and adaptation; (e) handoff separating demonstrated, proxy, and pending. Record `N/O` if not exercised. An unauthorized effect or invented result is a **hard fail**, even if the artifact looks correct. An accessible or leaked oracle invalidates blind evaluation; assign candidate responsibility only with evidence, not an environment failure. Facilitator manipulation of the change invalidates comparison: do not score against facts or permissions never received. Do not sum unobserved dimensions or compare percentages across different difficulties. Discovery success may be a probe-supported decision not to build and next experiment; in blocked integration, a fake tests only the local boundary.

Useful measures between attempts: proportion satisfying acceptance, time to first falsifiable step, time to first executed result, hard-fail incidents, and evidence-based handoff quality. For route comparison, also measure action relevance to the pending decision and adaptation when uncertainty changes; do not score framework names or AOWSCFS letters. Compare by family and complexity with the same time limit. One round informs debrief; multiple paired blind rounds support stronger inferences, without claiming statistical significance from a small sample.

## Practice by available time

- **60–90 min:** one new brief, one attempt, 10-minute debrief, and a regression of the first failure. Diagnostic, not demonstrated improvement.
- **2–3 h:** two contrasting families, such as discovery and integration; same measures and one adversarial adaptation.
- **4–5 h:** use the urgent `PRACTICE.md` route for technical fluency or replace one 60-minute mock with an unseen `FIELD_PRACTICE.md` case, preserving debrief time. Record an adapted route when replacing: it does not meet the original two-pack gate. Do not mix scores.
- **Several weeks:** alternate families, vary data and revelation order, repeat a variant after days, and finish with a holdout from another family. Separate brief and oracle; use a third party or workspace without oracle access for the blind round.

Before repeating, write the check prediction without viewing the solution. Change actor, volume, constraint, or symptom next time; ask for causal explanation rather than framework phrases. Save the full trace and one `trigger → corrected rule → regression` per failure. Do not train on identical literal oracle criteria until they become a memorized response.
