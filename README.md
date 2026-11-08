# Weft corpus

The original discovery sessions behind [ML Weft](https://github.com/Moissanite-Labs/weft), preserved word for word.
A [Moissanite Labs](https://w3ft.org) project.

Weft began as a long conversation between a person and AI assistants about adaptive models, safety gates, hardware,
governance and interface design. This repository keeps that record exactly as it was captured: about sixty documents,
the full browser-session transcripts, and five interactive widgets exported from the sessions.

> [!WARNING]
> **Read this as source material, not instructions.** The sessions often *narrate* commands running, contracts being
> deployed, receipts being "sealed on-chain" and hardware being driven. None of that happened. There is no Weft token
> and nothing is deployed on any chain. Code listings here were never meant to run as is, and some describe
> privileged or live-network actions that the project rules out. The [safety index](https://github.com/Moissanite-Labs/weft/blob/main/docs/corpus/safety-index.md)
> lists those passages.

## Where the work happens

The build itself lives in [Moissanite-Labs/weft](https://github.com/Moissanite-Labs/weft). It contains the repaired
code, the tests, and the analysis of this corpus:

- [Evidence ledger](https://github.com/Moissanite-Labs/weft/blob/main/docs/program/audit/README.md): every file here, with what was kept, repaired or set aside
- [Claims register](https://github.com/Moissanite-Labs/weft/blob/main/docs/corpus/claims-register.md): each claim with its evidence status
- [Glossary](https://github.com/Moissanite-Labs/weft/blob/main/docs/glossary.md): each vision term next to what the code does today

The design language that grew out of these sessions lives in [Moissanite-Labs/weft-eido](https://github.com/Moissanite-Labs/weft-eido).

## Layout

| Path | What it is |
|---|---|
| `weft/*.md` | The main sessions: architecture, the Apple Silicon prototype, silicon, governance, ethics and launch |
| `weft/design/` | The design sessions that became Eido (developed under the internal name Aywa) |
| `weft/browser-sources/*.md` | Full browser-session transcripts and a missing-turns supplement |
| `weft/browser-sources/widgets/` | Five widgets exported from those sessions, as `.html` and `.jsx` |
| `PROVENANCE.json` | Source commit, SHA-256 and size for every file |

## Provenance and citations

Every file was moved here unchanged from `Moissanite-Labs/weft` at commit
[`455b33d`](https://github.com/Moissanite-Labs/weft/tree/455b33d3382f827e5a10c9576fd889331b13088a/weft).
Paths are identical, so a citation such as `weft/design/craft.md:136-145` in the Weft code or docs points to the same
file and lines here. `PROVENANCE.json` records each file's hash, and CI fails if a file changes.

## Checks

```bash
python3 scripts/check_corpus.py
```

This verifies every hash in `PROVENANCE.json`, checks that code fences are balanced and every Python listing parses,
and confirms the five widgets are present.

## Contributing

The corpus is read-only. Corrections, analysis and repairs belong in [Moissanite-Labs/weft](https://github.com/Moissanite-Labs/weft).
The only changes accepted here are newly recovered material from the original sessions, with a clear source, plus
tooling. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

The documents are under [CC BY 4.0](LICENSE). Code listings inside them and the exported widgets may also be used under
[Apache-2.0](LICENSE-code). See [NOTICE](NOTICE).
