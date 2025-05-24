import json
from typing import List, Dict
from builder.utils.meta_writer import write_meta
from builder.utils.version import read_version_txt
from builder.utils.path_utils import resolve_current_path
from builder.utils.emoji_source import fetch_emoji_test_txt


def parse_emoji_base(raw_lines: List[str]) -> Dict[str, int]:
    """
    Parse emoji-test.txt lines and extract all fully-qualified single-codepoint emojis.

    Args:
        raw_lines (List[str]): Raw lines from emoji-test.txt

    Returns:
        Dict[str, int]: A dictionary mapping each single-character emoji to width 2
    """
    emoji_map: Dict[str, int] = {}

    for line in raw_lines:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        if "; fully-qualified" not in line:
            continue

        codepoints_str, comment = line.split(';')[0], line.split('#')[1].strip()
        emoji_char = comment.split(' ')[0]

        # Skip multi-codepoint (composite) emojis, only keep single characters
        if ' ' in codepoints_str.strip():
            continue

        emoji_map[emoji_char] = 2

    return emoji_map


def generate() -> None:
    """
    Main entry point. Downloads emoji-test.txt, extracts single-character emojis,
    writes to emoji_base.json, and generates the corresponding metadata.
    """
    lines = fetch_emoji_test_txt()
    emoji_data = parse_emoji_base(lines)

    current_path = resolve_current_path("emoji/emoji_base.json")
    with open(current_path, "w", encoding="utf-8") as f:
        json.dump(emoji_data, f, ensure_ascii=False, indent=2)

    print(f"✅ Done: {current_path} ({len(emoji_data)} entries)")

    # Write corresponding .meta.json
    version = read_version_txt()
    emoji_version = ".".join(version.split(".")[:2])
    write_meta(
        name="emoji_base",
        source_url=f"https://unicode.org/Public/emoji/{emoji_version}/emoji-test.txt",
        target_rel_path="emoji/emoji_base.json",
        entry_count=len(emoji_data)
    )
