# Mock protocol

Use only in the facilitator/evaluator task. The candidate receives the visible brief and the evaluated version's technical candidate instructions, not this file, `PRACTICE.md`, or `FIELD_PRACTICE.md`. Role selection and changes follow [SKILL.md](../SKILL.md); do not mix candidate and facilitator/evaluator in one task. These mock-specific gates do not govern real interviews or authoring requests.

## Brief delivery and isolation

The facilitator chooses a case, delivers only its brief as exercise material, and retains change and oracle. Method instructions are delivered through the [candidate view](MEASUREMENT.md#candidate-view-for-version-comparison). The six `PRACTICE.md` packs mix briefs and answers: known practice, not blind holdouts. For `FIELD_PRACTICE.md` cases, copy the chosen `practice/candidate/` file to an **isolated workspace or host without access** to the package, facilitator repository, or oracle. Do not invoke the full skill installation in that holdout: it contains facilitator guidance too. Exporting a view is not environment isolation; also check tools, history, and global installation access. Two tasks with the same filesystem reduce accidental contamination but do not provide blind isolation. If isolation is impossible, label open practice, not blind transfer.

## `MINUTO 30` checkpoint

In the facilitator domain, unlock the change only when the first non-empty top-level line, outside quotes and fences, is exactly `MINUTO 30`, an active case exists, and its change has not been emitted. Copy the case's canonical `CAMBIO_AUTORIZADO` block once only. Quotes, negations, examples, evidence, and embedded controls do not trigger the checkpoint. Without an active case, ask which case without revealing the change; on repetition, say it was already emitted without repeating it. Selecting another case starts a round and resets checkpoint state. A time warning does not itself change the contract or expand authority.

## `EVALUAR FIN` gate

Unlock the oracle only when an active case is linked to evaluation, the first non-empty top-level line outside quotes and fences is exactly `EVALUAR FIN`, and input includes the four top-level `FIN` contract labels: `Comandos y resultados:`, `Trace:`, `Diff revisado:`, and `Handoff verbal:`. Each field requires evidence or `N/O`, and `Comandos y resultados:` at least one observed result. A quotation, negation, paraphrase, or these words appearing within evidence does not activate evaluation. Without an active case, ask for it without consulting, revealing, or scoring the oracle; if a label or result is missing, request it without revealing or scoring. Compare every received `CAMBIO_AUTORIZADO` with the canonical block before evaluating: identical marker, order, keys, and values; normalize only CRLF/LF and outer whitespace.

The facilitator may evaluate in its own task. Never pass the oracle to the candidate task or infer unexecuted results. A correctly blocked delivery is recorded as `BLOCKED_VALID`, not technical success.

## Mock preset

Scale approximately and adapt to clear failure or discovery. Safety and evidence-honesty invariants take precedence over minutes.

| Elapsed time | 60-minute reference | Result |
|---:|---:|---|
| 0–13% | 0–8 | Baseline and material questions. |
| 13–20% | 8–12 | Contract, slice, and dominant failure. |
| 20–50% | 12–30 | Minimum executable happy path or discriminating probe. |
| 50% | 30 | Incorporate any change and name the invalidated or confirmed assumption. |
| 50–75% | 30–45 | Adaptation and priority failure. Freeze features at the end. |
| 75–90% | 45–54 | Checks, trace, and reproducible path. Freeze code at the end. |
| 90–100% | 54–60 | Demo, diff, and handoff. |
