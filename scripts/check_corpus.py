#!/usr/bin/env python3
"""Check that the corpus is intact.

1. Immutability: every file listed in PROVENANCE.json exists with the recorded
   SHA-256, and no unlisted file has appeared under weft/.
2. Structure (moved from weft/runtime/core/selftest.py): fenced code blocks are
   balanced, chat-export artifacts are absent, every ```python block parses,
   and the five exported widgets are present.

Run: python3 scripts/check_corpus.py
"""
from __future__ import annotations

import ast
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CORPUS = ROOT / "weft"


def check_provenance() -> list[str]:
    manifest = json.loads((ROOT / "PROVENANCE.json").read_text())
    errors = []
    listed = set()
    for entry in manifest["files"]:
        path = ROOT / entry["path"]
        listed.add(entry["path"])
        if not path.is_file():
            errors.append(f"missing: {entry['path']}")
            continue
        data = path.read_bytes()
        if hashlib.sha256(data).hexdigest() != entry["sha256"] or len(data) != entry["bytes"]:
            errors.append(f"modified: {entry['path']} (the corpus is verbatim; put corrections in Moissanite-Labs/weft)")
    for path in sorted(CORPUS.rglob("*")):
        rel = path.relative_to(ROOT).as_posix()
        if path.is_file() and rel not in listed:
            errors.append(f"unlisted file: {rel} (add it to PROVENANCE.json with its source)")
    return errors


def check_structure() -> tuple[dict, list[str]]:
    errors = []
    md_files = sorted(CORPUS.rglob("*.md"))
    fenced = py_blocks = 0
    for md in md_files:
        rel = md.relative_to(ROOT).as_posix()
        text = md.read_text(encoding="utf-8")
        fences = len(re.findall(r"^```", text, re.M))
        fenced += fences // 2
        if fences % 2:
            errors.append(f"unbalanced code fences: {rel} ({fences})")
        if "Use code with caution." in text:
            errors.append(f"chat-export artifact 'Use code with caution.': {rel}")
        if "<FollowUp>" in text or "</FollowUp>" in text:
            errors.append(f"chat-export artifact <FollowUp>: {rel}")
        for i, m in enumerate(re.finditer(r"```python\n(.*?)```", text, re.S)):
            py_blocks += 1
            try:
                ast.parse(m.group(1))
            except SyntaxError as e:
                errors.append(f"python block {i} does not parse: {rel}:{e.lineno}: {e.msg}")
    widgets = sorted((CORPUS / "browser-sources" / "widgets").glob("*.html"))
    if len(widgets) != 5:
        errors.append(f"expected 5 exported widgets, found {len(widgets)}")
    stats = {"markdown_files": len(md_files), "fenced_blocks": fenced, "python_blocks_parsed": py_blocks, "widgets": len(widgets)}
    return stats, errors


def main() -> int:
    errors = check_provenance()
    stats, structural = check_structure()
    errors += structural
    for e in errors:
        print(f"FAIL {e}", file=sys.stderr)
    print(json.dumps({"status": "FAIL" if errors else "PASS", **stats}))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
