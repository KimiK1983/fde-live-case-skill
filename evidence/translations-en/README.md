# English reading translations

These files translate the Spanish briefs, startup prompt, and final responses from the September 30, 2026 regression run. They are **not new model outputs** and do not establish English behavioral equivalence.

Original records, logs, manifests, results, and hashes remain in [gpt61-medium-2026-09-30](../gpt61-medium-2026-09-30). Original instruction content is pinned in [v0.1.0](https://github.com/KimiK1983/fde-live-case-skill/tree/v0.1.0). Translated response tables retain observed numbers; decimal and thousands separators follow English conventions.

| Case | Translated brief | Translated final response |
|---|---|---|
| Arithmetic | [case.md](arithmetic/case.md) | [stage1.md](arithmetic/stage1.md) |
| Field preservation | [case.md](input-loss/case.md) | [stage1.md](input-loss/stage1.md) |
| Uncertain write | [case.md](uncertain-write/case.md) | [stage1.md](uncertain-write/stage1.md) |
| Authoring | [case.md](authoring/case.md) | [stage1.md](authoring/stage1.md) |

The current runner uses these English **input** translations and current English instructions. Its future outputs must be evaluated separately. [criteria.json](criteria.json) is copied verbatim because the original criteria were already English; [prompt.txt](prompt.txt) is translated. Protocol identifiers remain literal.
