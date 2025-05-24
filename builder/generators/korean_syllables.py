import json
from builder.utils.meta_writer import write_meta
from builder.utils.version import read_version_txt
from builder.utils.path_utils import resolve_current_path


def is_korean_syllable(cp: int) -> bool:
    """
    Check whether the given code point is a Hangul Syllable (Korean).

    Unicode range: U+AC00 to U+D7AF — precomposed modern Hangul syllables (11,172 total).
    Reference: https://www.unicode.org/charts/PDF/UAC00.pdf

    Args:
        cp (int): Unicode code point

    Returns:
        bool: True if the character is a Korean syllable
    """
    return 0xAC00 <= cp <= 0xD7AF


def generate() -> None:
    """
    Main generator function. Extracts all Hangul syllables and writes to korean_syllables.json.
    A corresponding .meta.json file is also created.
    """
    syllable_map = {}

    for cp in range(0xAC00, 0xD7B0):  # Inclusive range: AC00 to D7AF
        syllable_map[chr(cp)] = 2

    current_path = resolve_current_path("cjk/korean_syllables.json")
    with open(current_path, "w", encoding="utf-8") as f:
        json.dump(syllable_map, f, ensure_ascii=False, indent=2)

    print(f"✅ Done: {current_path} ({len(syllable_map)} entries)")

    version = read_version_txt()
    write_meta(
        name="korean_syllables",
        source_url=f"https://unicode.org/Public/{version}/ucd/Blocks.txt",
        target_rel_path="cjk/korean_syllables.json",
        entry_count=len(syllable_map)
    )
