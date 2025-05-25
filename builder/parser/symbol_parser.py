from builder.parser.constants import SymbolMode


def extract_fullwidth_punctuations_map() -> dict[str, int]:
    """
    Returns a manually curated map of punctuation and symbolic characters
    commonly rendered as fullwidth (width = 2) in CJK typography environments.

    Returns:
        dict[str, int]: Character → width mapping
    """
    return {
        # Title marks / brackets (commonly used in CJK)
        "《": 2, "》": 2, "「": 2, "」": 2, "『": 2, "』": 2,
        "【": 2, "】": 2, "（": 2, "）": 2, "［": 2, "］": 2,
        "｛": 2, "｝": 2, "〈": 2, "〉": 2, "﹃": 2, "﹄": 2,
        "︻": 2, "︼": 2,

        # Quotation marks
        "“": 2, "”": 2, "‘": 2, "’": 2,

        # Sentence punctuation
        "。": 2, "、": 2, "，": 2, "．": 2,
        "：": 2, "；": 2, "？": 2, "！": 2,

        # Tilde / middle dots / continuation marks
        "〜": 2, "～": 2, "・": 2,
        "—": 2, "――": 2, "…": 2, "‥": 2,
        "︰": 2, "﹏": 2,

        # Reference / symbolic marks
        "※": 2, "†": 2, "‡": 2, "￣": 2, "　": 2,

        # Circled numbers
        "①": 2, "②": 2, "③": 2, "④": 2, "⑤": 2,
        "⑥": 2, "⑦": 2, "⑧": 2, "⑨": 2, "⑩": 2,

        # Common graphic symbols
        "●": 2, "○": 2, "◆": 2, "◇": 2,
        "■": 2, "□": 2, "★": 2, "☆": 2,

        # Arrows
        "→": 2, "←": 2, "↑": 2, "↓": 2,
        "↔": 2, "⇔": 2,

        # Units
        "℃": 2, "℉": 2,

        # Box drawing
        "╭": 2, "╮": 2, "╯": 2, "╰": 2,
        "━": 2, "┃": 2, "┏": 2, "┓": 2, "┗": 2, "┛": 2,
    }


def is_fullwidth_variant(cp: int) -> bool:
    """
    Determines whether a given Unicode code point is a fullwidth variant character.

    Fullwidth range:
      - U+FF01 to U+FF60 (common fullwidth symbols, digits, Latin letters)
      - U+FFE0 to U+FFE6 (additional fullwidth symbols)

    Args:
        cp (int): Unicode code point

    Returns:
        bool: True if the code point is considered a fullwidth variant
    """
    return (0xFF01 <= cp <= 0xFF60) or (0xFFE0 <= cp <= 0xFFE6)


def extract_fullwidth_variant_map() -> dict[str, int]:
    """
    Extracts all fullwidth variant characters from Unicode range
    and returns a character → width mapping (width = 2).

    Returns:
        dict[str, int]: Mapping from fullwidth variant character to width 2
    """
    return {chr(cp): 2 for cp in range(0xFF01, 0xFF61)} | {chr(cp): 2 for cp in range(0xFFE0, 0xFFE7)}


def extract_symbol_map(mode: SymbolMode) -> dict[str, int]:
    """
    Unified extractor for symbolic character width mappings.

    Args:
        mode (Literal["variant", "punctuations"]):
            - "fullwidth_variants": Extract characters from fullwidth Unicode ranges (FFXX)
            - "fullwidth_punctuations": Extract manually curated punctuation/symbols (not in FFXX but wide)

    Returns:
        dict[str, int]: Character → width mapping
    """
    if mode == "fullwidth_variants":
        return extract_fullwidth_variant_map()
    elif mode == "fullwidth_punctuations":
        return extract_fullwidth_punctuations_map()

    return {}
