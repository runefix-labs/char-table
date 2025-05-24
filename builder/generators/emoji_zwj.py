import json
from typing import List, Dict
from builder.utils.meta_writer import write_meta
from builder.utils.version import read_version_txt
from builder.utils.path_utils import resolve_current_path
from builder.utils.emoji_source import fetch_emoji_test_txt


def parse_emoji_zwj(raw_lines: List[str]) -> Dict[str, int]:
    """
    Parse emoji-test.txt and extract all fully-qualified emojis that:
    - contain ZWJ (Zero Width Joiner), or
    - consist of multiple code points.

    Args:
        raw_lines (List[str]): Raw lines from emoji-test.txt

    Returns:
        Dict[str, int]: A dictionary mapping multi-codepoint (ZWJ) emoji strings to width 2
    """
    emoji_map: Dict[str, int] = {}

    for line in raw_lines:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        if "; fully-qualified" not in line:
            continue

        codepoints_str, comment = line.split(';')[0], line.split('#')[1].strip()
        emoji_str = comment.split(' ')[0]

        # Keep only emojis that contain ZWJ or consist of multiple code points
        if '\u200D' in emoji_str or ' ' in codepoints_str.strip():
            emoji_map[emoji_str] = 2

    return emoji_map


def generate():
    """
    Main entry point.
    Downloads emoji-test.txt → extracts ZWJ/multi-codepoint emojis →
    writes to emoji_zwj.json → generates metadata file.
    """
    lines = fetch_emoji_test_txt()
    emoji_data = parse_emoji_zwj(lines)

    current_path = resolve_current_path("emoji/emoji_zwj.json")

    with open(current_path, "w", encoding="utf-8") as f:
        json.dump(emoji_data, f, ensure_ascii=False, indent=2)

    print(f"✅ Done: {current_path} ({len(emoji_data)} entries)")

    # Write .meta.json
    version = read_version_txt()
    emoji_version = ".".join(version.split(".")[:2])
    write_meta(
        name="emoji_zwj",
        source_url=f"https://unicode.org/Public/emoji/{emoji_version}/emoji-test.txt",
        target_rel_path="emoji/emoji_zwj.json",
        entry_count=len(emoji_data)
    )
