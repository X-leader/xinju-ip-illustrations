#!/usr/bin/env python3
"""Replace the single active character or restore the built-in Xinju default."""

from __future__ import annotations

import argparse
import shutil
import tempfile
from pathlib import Path


SKILL_DIR = Path(__file__).resolve().parents[1]
ACTIVE_IMAGE = SKILL_DIR / "assets" / "ip" / "active-ip-four-view.png"
ACTIVE_PROFILE = SKILL_DIR / "references" / "character-ip.md"
DEFAULT_IMAGE = SKILL_DIR / "assets" / "ip" / "xinju-ip-four-view.png"
DEFAULT_PROFILE = SKILL_DIR / "references" / "character-ip-xinju-default.md"
SUPPORTED_IMAGES = {".png"}
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
REQUIRED_PROFILE_SECTIONS = (
    "# 活动人物 IP",
    "## 参考状态",
    "## 固定身份锚点",
    "## 跨风格与动作锁",
)


def existing_file(value: str) -> Path:
    path = Path(value).expanduser().resolve()
    if not path.is_file():
        raise argparse.ArgumentTypeError(f"file not found: {path}")
    return path


def replace_active(image: Path, profile: Path) -> None:
    validate_image(image)
    validate_profile(profile)
    ACTIVE_IMAGE.parent.mkdir(parents=True, exist_ok=True)
    ACTIVE_PROFILE.parent.mkdir(parents=True, exist_ok=True)
    staged_image = stage_copy(image, ACTIVE_IMAGE.parent, ".png")
    staged_profile = stage_copy(profile, ACTIVE_PROFILE.parent, ".md")
    commit_pair(staged_image, staged_profile)


def reset_xinju() -> None:
    if not DEFAULT_IMAGE.is_file() or not DEFAULT_PROFILE.is_file():
        raise FileNotFoundError("built-in Xinju default is incomplete")
    validate_image(DEFAULT_IMAGE)
    validate_profile(DEFAULT_PROFILE)
    staged_image = stage_copy(DEFAULT_IMAGE, ACTIVE_IMAGE.parent, ".png")
    staged_profile = stage_copy(DEFAULT_PROFILE, ACTIVE_PROFILE.parent, ".md")
    commit_pair(staged_image, staged_profile)


def validate_image(image: Path) -> None:
    if image.suffix.lower() not in SUPPORTED_IMAGES:
        raise ValueError("active character sheet must be a PNG file")
    if image.read_bytes()[:8] != PNG_SIGNATURE:
        raise ValueError("active character sheet has a .png name but is not PNG data")


def validate_profile(profile: Path) -> None:
    if profile.suffix.lower() != ".md":
        raise ValueError("profile must be a Markdown file")
    content = profile.read_text(encoding="utf-8")
    missing = [section for section in REQUIRED_PROFILE_SECTIONS if section not in content]
    if missing:
        raise ValueError(f"profile is missing required sections: {', '.join(missing)}")


def commit_pair(staged_image: Path, staged_profile: Path) -> None:
    """Replace image and profile as one recoverable operation."""
    backup_image = stage_copy(ACTIVE_IMAGE, ACTIVE_IMAGE.parent, ".bak") if ACTIVE_IMAGE.exists() else None
    backup_profile = stage_copy(ACTIVE_PROFILE, ACTIVE_PROFILE.parent, ".bak") if ACTIVE_PROFILE.exists() else None
    try:
        staged_image.replace(ACTIVE_IMAGE)
        staged_profile.replace(ACTIVE_PROFILE)
    except Exception:
        if backup_image is not None:
            backup_image.replace(ACTIVE_IMAGE)
        else:
            ACTIVE_IMAGE.unlink(missing_ok=True)
        if backup_profile is not None:
            backup_profile.replace(ACTIVE_PROFILE)
        else:
            ACTIVE_PROFILE.unlink(missing_ok=True)
        raise
    finally:
        staged_image.unlink(missing_ok=True)
        staged_profile.unlink(missing_ok=True)
        if backup_image is not None:
            backup_image.unlink(missing_ok=True)
        if backup_profile is not None:
            backup_profile.unlink(missing_ok=True)


def stage_copy(source: Path, directory: Path, suffix: str) -> Path:
    """Copy to the destination filesystem before replacing the active file."""
    directory.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(dir=directory, suffix=suffix, delete=False) as handle:
        staged = Path(handle.name)
    try:
        shutil.copy2(source, staged)
    except Exception:
        staged.unlink(missing_ok=True)
        raise
    return staged


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--reset-xinju", action="store_true")
    mode.add_argument("--image", type=existing_file)
    parser.add_argument("--profile", type=existing_file)
    args = parser.parse_args()

    if args.reset_xinju:
        if args.profile is not None:
            parser.error("--profile cannot be used with --reset-xinju")
        reset_xinju()
        print("Active character reset to Xinju.")
        return

    if args.profile is None:
        parser.error("--profile is required with --image")
    replace_active(args.image, args.profile)
    print("Active character replaced.")


if __name__ == "__main__":
    main()
