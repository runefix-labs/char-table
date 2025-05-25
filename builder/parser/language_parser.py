from builder.parser.constants import LanguageMode


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


def is_japanese_kana(codepoint: int) -> bool:
    """
    Determine whether a Unicode code point belongs to any Japanese Kana block.

    Covered ranges:
    - 3040..309F: Hiragana
    - 30A0..30FF: Katakana
    - 31F0..31FF: Katakana Phonetic Extensions
    - 1B000..1B0FF: Kana Supplement
    - 1B100..1B12F: Kana Extended-A
    - 1B130..1B16F: Kana Extended-B

    Args:
        codepoint (int): Unicode code point

    Returns:
        bool: True if the code point is a Japanese kana character
    """
    return (
        0x3040 <= codepoint <= 0x309F or
        0x30A0 <= codepoint <= 0x30FF or
        0x31F0 <= codepoint <= 0x31FF or
        0x1B000 <= codepoint <= 0x1B0FF or
        0x1B100 <= codepoint <= 0x1B12F or
        0x1B130 <= codepoint <= 0x1B16F
    )


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


def extract_cjk_char_map() -> dict[str, int]:
    """
    Extracts all CJK Unified Ideographs from the full Unicode range
    and returns a character → width mapping (all width = 2).

    Returns:
        dict[str, int]: Mapping from character to width 2
    """
    result: dict[str, int] = {}
    for cp in range(0x110000):
        if is_cjk_unified(cp):
            result[chr(cp)] = 2
    return result


def extract_kana_char_map() -> dict[str, int]:
    """
    Extracts all Japanese kana characters from the full Unicode range
    and returns a character → width mapping (all width = 2).

    Returns:
        dict[str, int]: Mapping from character to width 2
    """
    result: dict[str, int] = {}
    for cp in range(0x110000):
        if is_japanese_kana(cp):
            result[chr(cp)] = 2
    return result


def extract_korean_syllable_map() -> dict[str, int]:
    """
    Extracts all precomposed Korean syllables from Unicode
    and returns a character → width mapping (all width = 2).

    Returns:
        dict[str, int]: Mapping of Hangul syllables to width 2
    """
    return {chr(cp): 2 for cp in range(0xAC00, 0xD7B0)}


def extract_lang_map(mode: LanguageMode) -> dict[str, int]:
    """
    Extract CJK character maps by category.

    Supported modes:
    - "cjk_unified"      : Extracts all CJK Unified Ideographs
    - "japanese_kana"    : Extracts Japanese kana blocks (Hiragana, Katakana, etc.)
    - "korean_syllables" : Extracts modern Hangul syllables (Korean)

    Args:
        mode (LanguageMode): Extraction category. Must be one of:
            - "cjk_unified"
            - "japanese_kana"
            - "korean_syllables"

    Returns:
        dict[str, int]: Mapping from character to width 2
    """
    if mode == "cjk_unified":
        return extract_cjk_char_map()
    elif mode == "japanese_kana":
        return extract_kana_char_map()
    elif mode == "korean_syllables":
        return extract_korean_syllable_map()

    return {}
