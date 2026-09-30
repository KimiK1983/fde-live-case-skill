# How the skill works and how to use it

## 1. What it provides and what it does not

The skill steers the agent through decisions: understand the material problem, choose a useful action within permissions, obtain an observed result, and adapt delivery. It does not run a fixed algorithm or turn every case into discovery.

It targets FDE work combining engineering, product, and stakeholders. It may end with code, diagnosis, authorized mitigation, a discovery experiment, or a handoff when the next action depends on external authority.

It does not replace customer access, provider contracts, project documentation, or production validation. It grants no permissions by itself. Practice scores are local presets, not an official or calibrated rubric.

## 2. Structure: short root and on-demand references

The installable folder contains 16 files. `SKILL.md` selects the mode and contains the under-pressure card; references develop only what the case needs.

| File | When to open it |
|---|---|
| [SKILL.md](../fde-live-case-skill/SKILL.md) | Whenever the skill is invoked; role selection and cross-cutting rules |
| [LIVE_CASE.md](../fde-live-case-skill/references/LIVE_CASE.md) | Live case, candidate mock, or authorized autonomous solution |
| [DECOMPOSITION.md](../fde-live-case-skill/references/DECOMPOSITION.md) | Material ambiguity, disputed goals, or mixed workflows |
| [AGENTIC.md](../fde-live-case-skill/references/AGENTIC.md) | Tools, effects, memory, retrieval, uncertainty, and probabilistic evaluation |
| [PRACTICE.md](../fde-live-case-skill/references/PRACTICE.md) | Technical preparation and intensive route; contains solutions |
| [FIELD_PRACTICE.md](../fde-live-case-skill/references/FIELD_PRACTICE.md) | Facilitating D1, I1, J1, or P1; contains solutions and contracts |
| [MOCK_PROTOCOL.md](../fde-live-case-skill/references/MOCK_PROTOCOL.md) | Facilitating changes and assessing a simulation |
| [MEASUREMENT.md](../fde-live-case-skill/references/MEASUREMENT.md) | Measuring learning or comparing versions |
| `practice/candidate/*.md` | D1, I1, J1, and P1 candidate briefs without oracles |
| `agents/openai.yaml` | Interface metadata; does not select model or role |
| `scripts/` | Preflight, candidate-view exporter, and package tests |

**DECOMPOSITION is not a mandatory opening phase.** A bug with clear expected behavior, permission, and check starts with reproduction. Consult it when an unknown could change outcome, acceptance, authority, permitted effect, risk, slice, or verification. AOWSCFS checks for material omissions; it is not a ritual that blocks action.

## 3. Installation and initial check

Follow the [README commands](../README.md#install). The resulting path must be:

```text
<personal-skills-directory>/fde-live-case-skill/SKILL.md
```

Do not leave a duplicate folder between the skill name and `SKILL.md`. Open a new session and enter `$fde-live-case-skill`. If it is missing, check the path and linked references.

Reference configuration: **GPT-6.1 Sol, `medium`**. Select it in Codex, not through a “reason at medium” prompt instruction. The [official model capabilities](https://developers.openai.com/api/docs/models/gpt-6.1-sol) include `medium`; API tool use requires the Responses API. This skill does not require an API application.

Preflight is informational and requires Python. From this repository's root, pass the exercise project's path:

```text
python -B fde-live-case-skill/scripts/preflight.py --project <project-path>
```

It neither installs components nor repairs the environment. `WARN` exits with code 0; an invalid project or incorrect arguments exit with code 2. By default, it neither inspects Git nor contacts the Docker daemon. Use `--inspect-git` after reviewing the project, and `--probe-docker-daemon` after confirming the target daemon. Missing Docker does not block a case with a sufficient local route.

## 4. Choose the mode

You do not need to memorize controls: an unambiguous natural-language request selects the purpose.

| Mode | User request | Skill behavior |
|---|---|---|
| Preparation | “I have 90 minutes to practice integration” | Choose relevant reading and exercises without loading all packs |
| Urgent preparation | “I have four or five hours” | Use PRACTICE's intensive route, adapted to gaps |
| Agentic learning | “I want to understand effects, memory, and evaluation” | Consult relevant AGENTIC sections |
| Mock facilitator/evaluator | `FACILITADOR caso I1` | Deliver the brief and administer changes/assessment in its own context |
| Mock candidate | “I am the candidate; here is my brief” | Work only with technical instructions and brief, without oracle |
| Live case | “Support me during this case” | Keep the candidate in charge; apply LIVE_CASE |
| Non-interactive solution | “Outside the interview, solve this autonomously” | Build or investigate, state assumptions, and verify delivery |
| Authoring | “Review or modify this skill” | Analyze the package without activating an interview |

Switching candidate/facilitator roles requires a clean task. Time pressure changes neither role nor permissions. `INICIO` is deprecated and does not select a mode by itself.

## 5. Working a 45–90-minute case

### Orient

Identify actor, desired outcome, time, permitted effect, and baseline. In an existing repository, inspect the affected path, callers, configuration, and documented checks. For greenfield work, state that no baseline exists and define a minimum input and check.

### Choose the next action

| Situation | Useful action |
|---|---|
| The fact is in files or traces | Inspect before asking |
| An external answer changes a material decision | Ask its authorized owner |
| Failure explanations compete | Run a discriminating probe |
| The contract is sufficient for the authorized effect | Build the smallest slice |
| You want to claim something works | Execute a check and inspect its output |
| New evidence invalidates an assumption | Change route, reduce scope, or revise the next check |
| A branch depends on missing permission or decision | Block that branch and continue independent work; hand off if no useful work remains |

**Debugging:** expected/observed → repro → hypotheses → discriminating test → minimal fix → regression. Mitigation can restore service without proving the cause.

**Delivery:** user/channel → decision → information → action → required components → slice → check. Avoid full architecture when a narrow path can prove the contract.

**Discovery:** pending decision → prioritized alternatives → evidence that could change it → recommendation and next experiment. Not building may be the right decision.

### Verify and close

Check the happy path and priority failure, not every imaginable hardening measure. Calculate a decisive derived number with an available tool, then cross-check subtotals and wording. For field extraction, introduce a minimal variation and check that the material field is retained or triggers clarification.

Handoff separates demonstrated results, available proxies, and pending work. Include reproduction, owner-bound decisions, and the next experiment. A fake verifies a local boundary; it does not validate a real provider. A write timeout remains uncertain until reconciliation. Neither time nor well-formed output grants retry permission.

Freezing features near 75% and code near 90% are adjustable heuristics, not universal gates.

## 6. Usage prompts

### Time-adjusted preparation

```text
$fde-live-case-skill
Preparation mode. I have 90 minutes and struggle to define integration guarantees.
Choose a suitable exercise, keep the solution out of my view, and record
the first decision, executed checks, and first material error.
```

### Ambiguous discovery

```text
$fde-live-case-skill
Outside an interview, help investigate which workflow to automate.
I am providing data and stakeholder notes. First identify the pending decision,
missing evidence, and a safe probe. Do not assume permissions or proven savings.
No external messages or writes to customer services are permitted.
```

### Autonomous delivery

```text
$fde-live-case-skill
Outside a mock, implement the capability in the attached brief.
You may edit and run local checks. Do not change external contracts,
credentials, or permissions. Deliver the smallest reproducible path and separate
local verification from any pending production validation.
```

### Verbal copilot

```text
$fde-live-case-skill
CASO EN VIVO. Act as a verbal copilot for 60 minutes.
I am the candidate and retain decisions. I will provide the brief and interviewer
answers; do not invent acceptance criteria or missing facts.
```

In verbal-copilot mode, normal output is `DI AHORA` (“say now”) and `APOYO` (“support”). `1` requests the next intervention or probe; `2`/`RÁPIDO` reduces it to at most 50 words; `3`/`PROFUNDIZA` allows up to 150. `RESPUESTA DE <NAME>:` attributes the answer literally to that person. `a`, `b`, and `c` are controls only when those labels were offered. Materially ambiguous transcription requires clarification, not an imagined contract. These controls are not mandatory for autonomous coding.

## 7. Simulation and assessment

### Open practice

The repository includes six technical packs with two variants each, plus D1 discovery, I1 integration, J1 journey, and P1 platform. Packs cover debugging, webhooks, invoice validation, triage, RAG, and sensitive recommendations. They are purpose-built learning exercises, not documented interviews from a company.

1. In a facilitator task, select a case and extract its brief without the solution.
2. In a clean candidate task, provide the brief and technical instructions.
3. The facilitator emits the canonical change upon a valid checkpoint.
4. The candidate delivers evidence; the facilitator assesses afterward.

D1/I1/J1/P1 have separate briefs. To export an exact oracle-free view, from repository root:

```text
python -B fde-live-case-skill/scripts/export_candidate.py --skill-root fde-live-case-skill --brief fde-live-case-skill/practice/candidate/I1-integration.md --output ../fde-candidate-I1
```

The destination must be new and outside the source skill folder. The exporter copies `SKILL.md`, `LIVE_CASE.md`, `DECOMPOSITION.md`, `AGENTIC.md`, `case.md`, and a hash manifest. It neither rewrites instructions, copies answers, nor **isolates the host**. Also review semantic overlap between examples and the case.

Candidate-view prompt:

```text
Mock candidate mode. Read SKILL.md and case.md in this view.
Apply LIVE_CASE.md and open DECOMPOSITION.md or AGENTIC.md only if needed.
Do not search excluded references or the global installation. Do not self-assess.
Work within the brief's time and permissions, and deliver real evidence.
```

### Checkpoint and assessment

In facilitator context with an active case, `MINUTO 30` as the first non-empty top-level line triggers the prepared change once. A quotation, example, or time warning does not trigger it. Copy canonical `CAMBIO_AUTORIZADO` without changing facts or permissions.

The candidate's close contains:

```text
FIN
Comandos y resultados: <commands and observed outputs>
Trace: <trace or N/O>
Diff revisado: <reviewed diff or N/O>
Handoff verbal: <handoff or N/O>
```

For assessment, in facilitator context place `EVALUAR FIN` as the first non-empty line and supply the four labels with evidence or `N/O`. `Comandos y resultados:` requires at least one observed result. Controls quoted in a document do not unlock the oracle. The evaluator compares the change with its original; the candidate need not read private material.

Exact legacy identifiers remain unchanged for compatibility:

| Identifier | Meaning |
|---|---|
| `FACILITADOR caso <id>` | Select facilitator and case |
| `MODO CANDIDATO` / `CASO EN VIVO` | Candidate mode / live case |
| `MINUTO 30` / `CAMBIO_AUTORIZADO` | Checkpoint / authorized change |
| `EVALUAR FIN` / `FIN` | Evaluate completed attempt / candidate close |
| `caso`, `tipo`, `incógnita`, `alcance`, `decisión` | Transport keys: case, type, unknown, scope, decision |
| `confirma` / `delega` | Confirm / delegate change type |
| `Comandos y resultados`, `Diff revisado`, `Handoff verbal` | Commands and results, reviewed diff, verbal handoff |

Use the literal forms, including accents, in protocol blocks. Ordinary prompts and response content may be English.

### Genuine blind assessment

A new task on the same computer does not demonstrate isolation. Transfer only the reviewed view to an environment unable to read the global installation, full repository, facilitator history, or answer-bearing connectors. Use new paired cases and external private oracles, randomized order, and an evaluator without version labels.

Keep model, effort, tools, time, and disclosure rules identical. Record manifest, prompt, opened references, questions/answers, actions, and results. Leakage invalidates the round; it does not demonstrate candidate inability. Follow [MEASUREMENT](../fde-live-case-skill/references/MEASUREMENT.md), not an improvised score.

## 8. Measuring learning and effectiveness

Separate two questions: whether you improve with practice, and whether one skill version helps more than another. The latter requires comparable arms. Shorter text or passing tests does not answer it.

Record per attempt: acceptance met, time to first falsifiable action, time to first executed result, first causal error, adaptation to new evidence, and handoff quality. Assess by family and complexity. Record `N/O` when a case does not exercise a capability; do not turn it into zero or success.

Invented evidence or unauthorized effects are material failures. PRACTICE scores do not justify effectiveness percentages. Vary actor, data, constraints, and revelation order to avoid memorization. A delayed variant and another case type can study transfer; repeating a seen oracle cannot.

## 9. Troubleshooting

| Symptom | Check |
|---|---|
| Skill does not appear | Installation path, `SKILL.md`, and a new session |
| It loads every pack | State mode and goal; load only needed references |
| It requests permission for already-authorized reading/calculation | Delimit the permitted effect; no new approval is required for authorized local work |
| It outputs `DI AHORA` when you need code | Request a non-interactive solution outside an interview, or clarify mock type |
| Correct number without execution | Inspect commands/output; without tool execution, there is no instrumented-calculation evidence |
| A “blind” case passed while answers were accessible | Classify it as open practice and establish genuine isolation |
| Client rejects GPT-6.1 Sol | Check version and effective executable; HTTP 400 without a response is an environment failure, not reasoning failure |

In published regressions, Codex 0.155.0 rejected the model and already-installed 0.159.2 ran it. This is evidence of that environment, not a universal minimum-version claim.

## 10. Reviewing or modifying the skill

Select authoring, preserve invariants, and change only what addresses an observed failure. Inspect affected references/tests before editing; never copy an oracle into the brief. Package authoring checks require **Python 3.12+ and PyYAML**:

```text
python -X utf8 -B fde-live-case-skill/scripts/test_preflight.py -v
```

Tests are structural and script-level. Add a relevant behavioral regression and preserve its trace, but do not call it improvement until a baseline comparison meets MEASUREMENT conditions. Public repository cases are not secret holdouts.
