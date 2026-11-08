# Contributing to the Weft corpus

This repository is a verbatim archive. Please read this before opening a pull request.

## What is accepted

- **Recovered material.** Turns or files from the original sessions that are missing here. Say where they came from
  and how they were captured, add them under `weft/`, and add each file to `PROVENANCE.json` with its SHA-256 and size.
- **Tooling.** Improvements to `scripts/check_corpus.py` and CI.

## What goes elsewhere

- Fixing an error in a document, analysing a claim, or repairing code from a listing: open an issue or PR in
  [Moissanite-Labs/weft](https://github.com/Moissanite-Labs/weft). Cite the corpus by path and line, for example
  `weft/mac.md:50-100`.
- Design-language work: [Moissanite-Labs/weft-eido](https://github.com/Moissanite-Labs/weft-eido).

Existing files are never edited, reformatted or renamed. CI fails if a hash changes.

## Sign-off

Every commit needs a [Developer Certificate of Origin](https://developercertificate.org/) sign-off (`git commit -s`).
Contributions are accepted under the licenses in [NOTICE](NOTICE). Please follow the
[Code of Conduct](CODE_OF_CONDUCT.md). Security reports go through
[Moissanite-Labs/weft's security policy](https://github.com/Moissanite-Labs/weft/blob/main/SECURITY.md).
