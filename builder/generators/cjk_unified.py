import json
from builder.utils.meta_writer import write_meta
from builder.utils.version import read_version_txt
from builder.utils.path_utils import resolve_current_path


def is_cjk_unified(codepoint: int) -> bool:
    """
    Determine whether a Unicode code point belongs to the CJK Unified Ideographs blocks.

    Covered ranges:
    - 4E00..9FFF    : Basic CJK Ideographs (commonly used characters)
    - 3400..4DBF    : Extension A
    - 20000..2A6DF  : Extension B
    - 2A700..2B73F  : Extension C
    - 2B740..2B81F  : Extension D
    - 2B820..2CEAF  : Extension E
    - 2CEB0..2EBEF  : Extension F
    - 30000..3134F  : Extension G
    - F900..FAFF    : Compatibility Ideographs

    Args:
        codepoint (int): Unicode code point

    Returns:
        bool: True if the code point is a CJK Unified Ideograph
    """
    return (
        0x4E00 <= codepoint <= 0x9FFF or
        0x3400 <= codepoint <= 0x4DBF or
        0x20000 <= codepoint <= 0x2A6DF or
        0x2A700 <= codepoint <= 0x2B73F or
        0x2B740 <= codepoint <= 0x2B81F or
        0x2B820 <= codepoint <= 0x2CEAF or
        0x2CEB0 <= codepoint <= 0x2EBEF or
        0x30000 <= codepoint <= 0x3134F or
        0xF900 <= codepoint <= 0xFAFF
    )


def generate() -> None:
    """
    Main generation function.
    Scans the entire Unicode range to extract all CJK Unified Ideographs,
    writes them to cjk_unified.json, and generates the corresponding metadata.
    """
    cjk_map = {}

    for cp in range(0x110000):
        if is_cjk_unified(cp):
            cjk_map[chr(cp)] = 2

    current_path = resolve_current_path("cjk/cjk_unified.json")
    with open(current_path, "w", encoding="utf-8") as f:
        json.dump(cjk_map, f, ensure_ascii=False, indent=2)

    print(f"✅ Done: {current_path} ({len(cjk_map)} entries)")

    version = read_version_txt()
    write_meta(
        name="cjk_unified",
        source_url=f"https://unicode.org/Public/{version}/ucd/Blocks.txt",
        target_rel_path="cjk/cjk_unified.json",
        entry_count=len(cjk_map)
    )
