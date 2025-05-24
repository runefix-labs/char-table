import json
from builder.utils.meta_writer import write_meta
from builder.utils.version import read_version_txt
from builder.utils.path_utils import resolve_current_path


def is_japanese_kana(codepoint: int) -> bool:
    """
    Check whether the given Unicode code point is a Japanese Kana character.

    Covered Unicode blocks:
    - 3040..309F: Hiragana
    - 30A0..30FF: Katakana
    - 31F0..31FF: Katakana Phonetic Extensions
    - 1B000..1B0FF: Kana Supplement
    - 1B100..1B12F: Kana Extended-A
    - 1B130..1B16F: Kana Extended-B

    Args:
        codepoint (int): Unicode code point

    Returns:
        bool: True if the character is in any of the Kana blocks
    """
    return (
        0x3040 <= codepoint <= 0x309F or  # Hiragana
        0x30A0 <= codepoint <= 0x30FF or  # Katakana
        0x31F0 <= codepoint <= 0x31FF or  # Katakana Phonetic Extensions
        0x1B000 <= codepoint <= 0x1B0FF or  # Kana Supplement
        0x1B100 <= codepoint <= 0x1B12F or  # Kana Extended-A
        0x1B130 <= codepoint <= 0x1B16F    # Kana Extended-B
    )


def generate() -> None:
    """
    Main generator function. Iterates over all Unicode code points and extracts Japanese Kana characters.
    The results are saved to japanese_kana.json, along with its metadata file.
    """
    kana_map = {}

    for cp in range(0x110000):
        if is_japanese_kana(cp):
            kana_map[chr(cp)] = 2

    current_path = resolve_current_path("cjk/japanese_kana.json")

    with open(current_path, "w", encoding="utf-8") as f:
        json.dump(kana_map, f, ensure_ascii=False, indent=2)

    print(f"✅ Done: {current_path} ({len(kana_map)} entries)")

    version = read_version_txt()
    write_meta(
        name="japanese_kana",
        source_url=f"https://unicode.org/Public/{version}/ucd/Blocks.txt",
        target_rel_path="cjk/japanese_kana.json",
        entry_count=len(kana_map)
    )
