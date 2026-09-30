# Evidence of operation and limits on effectiveness

Evidence cutoff: **September 30, 2026**. These are local authoring tests, not independent evaluation or commercial outcomes.

## What the tests support

**Fact:** the English distribution passes 46 structural/script tests. The Spanish instructions published in [v0.1.0](https://github.com/KimiK1983/fde-live-case-skill/tree/v0.1.0) met four known behavioral regression criteria with GPT-6.1 Sol `medium`.

**Limited inference:** the historical observations support usability and the model's ability to apply those Spanish instructions in the four tested situations. Structural checks support the English package's integrity, not equivalent model behavior.

**Not demonstrated:** English behavioral equivalence, superiority over another version, general FDE effectiveness, interview performance, business impact, absence of future errors, or transfer to unseen cases. Four passes in this battery are not a product success rate.

## 1. Package integrity

Command executed from this distribution's root:

```text
python -X utf8 -B fde-live-case-skill/scripts/test_preflight.py -v
```

English result: **46/46, OK**. See the [English validation log](../evidence/english-package-tests.txt); the [original log](../evidence/package-tests.txt) is preserved. Authoring requires Python 3.12+ and PyYAML. Everyday Markdown instruction use requires neither these checks nor this dependency.

Checks cover the 16-file manifest, local links/anchors, interface YAML, canonical transports, preflight, and candidate export. They do not themselves check semantic answer leakage or agent reasoning.

Additional local `skill-creator` validation returned `Skill is valid!`. That script belongs to the local Codex authoring environment and is not a repository dependency.

## 2. Four regressions with GPT-6.1 Sol

**Design:** one execution per case; criteria set before running; same model, `medium` effort, startup prompt, and local tools; two concurrent processes. Technical candidate view exported without packs/oracles. Manual response/trace assessment. No control arm, version randomization, or independent evaluator.

Published records include [configuration](../evidence/gpt61-medium-2026-09-30/environment.json), [original prompt](../evidence/gpt61-medium-2026-09-30/prompt.txt), and [original preregistered criteria](../evidence/gpt61-medium-2026-09-30/criteria.json). The evaluated Spanish instruction hash was `817f6d2a1934ed2bed2b942add1baf6690855bc4e6255d4d1850b91c8c9fcf87`. Case manifests can be checked against **v0.1.0**, not the translated current skill.

| Case | Targeted failure | Observed result | Original evidence |
|---|---|---|---|
| Arithmetic | Accept a supplied incorrect total and attribute unmeasured savings | Executes 540 + 720 + 800 = **2,060 min**, 260 calls; rejects 2,360 and distinguishes exposure from savings | [Brief](../evidence/gpt61-medium-2026-09-30/arithmetic/case.md), [response](../evidence/gpt61-medium-2026-09-30/arithmetic/stage1.md), [trace](../evidence/gpt61-medium-2026-09-30/arithmetic/stage1.jsonl) |
| Field preservation | Ignore an unknown country and return unrequested countries | Reproduces `pe`/`CA` broadening results; preserves both filters and executes five local checks | [Brief](../evidence/gpt61-medium-2026-09-30/input-loss/case.md), [response](../evidence/gpt61-medium-2026-09-30/input-loss/stage1.md), [trace](../evidence/gpt61-medium-2026-09-30/input-loss/stage1.jsonl) |
| Uncertain write | Retry POST with a new key after timeout and inaccessible GET | Retains `unknown`, identity, and key without another write; proposes reconciliation or handoff | [Brief](../evidence/gpt61-medium-2026-09-30/uncertain-write/case.md), [response](../evidence/gpt61-medium-2026-09-30/uncertain-write/stage1.md), [trace](../evidence/gpt61-medium-2026-09-30/uncertain-write/stage1.jsonl) |
| Mode selection | Activate assessment from `EVALUAR FIN` quoted during authoring | Stays in authoring; activates neither assessment nor oracle | [Brief](../evidence/gpt61-medium-2026-09-30/authoring/case.md), [response](../evidence/gpt61-medium-2026-09-30/authoring/stage1.md), [trace](../evidence/gpt61-medium-2026-09-30/authoring/stage1.jsonl) |

All four met their criteria. Traces contain **12 commands completed with exit code 0**: four for arithmetic, four for field preservation, and two for each remaining case. No file-change events appear. This does not prove technical host isolation or absence of every possible unrecorded effect.

The country fix retains exact comparison: `pe` returns empty rather than silently normalizing to `PE`. Normalization/clarification remain contract decisions. The test detects and corrects improper broadening; it does not validate a general search engine.

[Labeled English translations](../evidence/translations-en/README.md) provide readable briefs, responses, prompt, and criteria. They are translations, not new model outputs. Original records, manifests, results, and provenance hashes remain unchanged.

### Environment incident

The first attempt with Codex 0.155.0 returned HTTP 400: `The 'gpt-6.1-sol' model is not supported when using Codex with a ChatGPT account.` There was no model response: **N/O due to environment**, not four reasoning failures. Published rounds used already-installed Codex 0.159.2 successfully. No global configuration changed and no component was installed.

### Trace publication

Machine-specific paths and session IDs were replaced with placeholders. Commands, results, and responses were preserved except for those literal substitutions. [provenance.json](../evidence/gpt61-medium-2026-09-30/provenance.json) records original/published hashes per entry. No credentials, caches, medical-directory data, or private conversations were included.

## 3. Contradictory evidence and prior attempts

**Earlier implementation test, GPT-6 Sol `medium`:** a candidate in a new task built a medical-directory CLI. Its six tests passed, but an additional evaluator check found that a query with a mistranscribed first and last name lost the second token and searched the first as a surname. Six passing tests therefore did not ensure transcription-failure resolution. This version preceded the general field-preservation check. It was one uncontrolled round on the same host, without full technical isolation. Only this historical summary is public, not the private data or artifact.

**Later review-versus-control pilot, GPT-6 Sol `medium`:** both versions detected the discarded field when explicitly asked for an adversarial check. This was a tie, not demonstrated improvement. Reviewing a parser was narrower than building a complete solution under pressure. Concurrent timing also prevents attributing causal gains. The short rule remains because it expresses a verifiable check, not because the pilot proves superiority.

These observations prevent calling the new model's four regressions a definitive solution to the original problem. Model, case, and context also changed; the difference cannot be attributed solely to the skill.

## 4. Relationship to MEASUREMENT.md

| Condition | Historical battery |
|---|---|
| Model and effort recorded | Yes: GPT-6.1 Sol `medium` |
| Identifiable instructions and criteria | Yes: hashes, briefs, prompt, and criteria |
| Tools actually executed | Yes: completed events and outputs |
| Brief and oracle separated in prompt | No oracles provided; known regressions |
| Oracle technically inaccessible | Not verified; shared host |
| Paired unseen cases | No |
| Both arms with same model/effort | No |
| Randomized order and blind assessment | No |
| Complete 45–90-minute case | No |

Correct classification: **open behavioral compatibility regression; behavioral improvement unverified**. Follow all [MEASUREMENT.md](../fde-live-case-skill/references/MEASUREMENT.md) requirements for an effectiveness comparison. The English translation has not yet undergone a model rerun.

## 5. Replay

First run package tests. Replaying the four regressions requires an authenticated Codex CLI supporting the model. The runner uses reading/calculation tools and account quota. It does not modify the skill and refuses to overwrite the destination:

```text
python -X utf8 -B benchmarks/run_regressions.py --output eval-runs/my-round
```

If several executables exist, select the effective one:

```text
python -X utf8 -B benchmarks/run_regressions.py --codex <codex-path> --output eval-runs/my-round-2
```

The runner fixes `gpt-6.1-sol` and `medium`. Its `status=ok` means a response was received, **not** that behavioral criteria were met. Inspect commands, outputs, response, and limitations against the published criteria. New results can vary; verbatim reproduction is not guaranteed.

The current portable runner uses the English translated cases, prompt, and criteria with the current English instructions, while preserving model/execution arguments. Thus it is an **English adaptation**, not an exact replay of the original Spanish prompts. It replaces the original Windows-specific executable selection with `--codex`. It is not an isolated sandbox, automatic evaluator, or blind-comparison reproduction. For the original instruction/prompt content, consult v0.1.0.

Runner transport checks were also executed:

```text
python -X utf8 -B benchmarks/test_run_regressions.py -v
```

Result: **3/3, OK**. They verify that client rejection is not recorded as a valid response, storing a response does not imply scoring, and timeout preserves a partial trace. These are runner tests with a simulated client, not three additional model tests.

## 6. What would establish improvement

Compare baseline and revision with identical GPT-6.1 Sol `medium`, new paired cases, equal tools/time, inaccessible oracles, randomized order, and assessment without version names. Measure acceptance by family, time to first probe and observed result, adaptation, hard fails, and handoff. Preserve ties and failures; do not select only successful examples.

Until that design runs, the defensible description is: **documented skill, structurally checked, with positive and negative local-use evidence; behavioral superiority pending**.
