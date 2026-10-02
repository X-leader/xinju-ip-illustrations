#!/usr/bin/env python3
"""Verify that a release copy contains only the default Xinju identity."""

from __future__ import annotations

import hashlib
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "xinju-ip-illustrations"
ACTIVE_IMAGE = SKILL / "assets" / "ip" / "active-ip-four-view.png"
DEFAULT_IMAGE = SKILL / "assets" / "ip" / "xinju-ip-four-view.png"
ACTIVE_PROFILE = SKILL / "references" / "character-ip.md"
DEFAULT_PROFILE = SKILL / "references" / "character-ip-xinju-default.md"
REQUIRED = (
    SKILL / "SKILL.md",
    SKILL / "agents" / "openai.yaml",
    ACTIVE_IMAGE,
    DEFAULT_IMAGE,
    ACTIVE_PROFILE,
    DEFAULT_PROFILE,
)
PRIVATE_MARKERS = (
    "/Users/",
    "\\Users\\",
    "codex-clipboard-",
    "generated_images/",
    "/Desktop/",
)
TEXT_SUFFIXES = {".md", ".yaml", ".yml", ".py", ".txt"}


def digest(path: Path) -> str:
    hasher = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    for path in REQUIRED:
        if not path.is_file():
            fail(f"missing required file: {path.relative_to(ROOT)}")

    if digest(ACTIVE_IMAGE) != digest(DEFAULT_IMAGE):
        fail("active character image is not the built-in Xinju default")

    if ACTIVE_PROFILE.read_bytes() != DEFAULT_PROFILE.read_bytes():
        fail("active character profile is not the built-in Xinju default")

    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        if path.stat().st_size > 20 * 1024 * 1024:
            fail(f"file exceeds 20 MiB: {path.relative_to(ROOT)}")
        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        content = path.read_text(encoding="utf-8", errors="ignore")
        for marker in PRIVATE_MARKERS:
            if marker in content and path != Path(__file__).resolve():
                fail(f"private path marker {marker!r} in {path.relative_to(ROOT)}")

    print("Release verification passed: default Xinju active, required files present, no private path markers found.")


if __name__ == "__main__":
    main()
