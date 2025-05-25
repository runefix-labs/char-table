from builder.parser.constants import EmojiMode
from builder.core.emoji_source import emoji_fetchers


def parser_emoji(lines: list[str], mode: EmojiMode) -> dict[str, int]:
    """
    Extract fully-qualified emoji from emoji-test.txt lines.

    Args:
        lines (list[str]): Raw content of emoji-test.txt
        mode (Literal["emoji_base", "emoji_zwj"]): Extraction mode:
            - "emoji_base": only single-codepoint emoji
            - "emoji_zwj" : only ZWJ or multi-codepoint sequences

    Returns:
        dict[str, int]: Mapping of emoji string → width 2
    """
    result: dict[str, int] = {}

    for line in lines:
        line = line.strip()
        if not line or line.startswith("#") or "; fully-qualified" not in line:
            continue

        codepoints_str, comment = line.split(";")[0], line.split("#")[1].strip()
        emoji_str = comment.split(" ")[0]

        if mode == "emoji_base":
            # Exclude multi-codepoint
            if " " not in codepoints_str.strip():
                result[emoji_str] = 2
        elif mode == "emoji_zwj":
            # Include if ZWJ or multiple codepoints
            if "\u200D" in emoji_str or " " in codepoints_str.strip():
                result[emoji_str] = 2

    return result


def extract_emoji_map(mode: EmojiMode) -> dict[str, int]:
    """
    Fetches emoji-test.txt from Unicode and extracts emojis based on the specified mode.

    This function handles fetching the source file and delegates the parsing to `parser_emoji()`.

    Args:
        mode (Literal["base", "zwj"]): Extraction mode:
            - "emoji_base": only single-codepoint emoji
            - "emoji_zwj" : only multi-codepoint or ZWJ-based emoji

    Returns:
        dict[str, int]: Mapping of extracted emoji to width=2
    """
    lines = emoji_fetchers()
    result = parser_emoji(lines, mode)
    return result
