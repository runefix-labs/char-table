import json
from builder.utils.meta_writer import write_meta
from builder.utils.path_utils import resolve_current_path


def generate() -> None:
    """
    Generates a curated list of punctuation and symbols that are commonly treated as fullwidth (width = 2)
    in East Asian environments (CJK terminals and typography).
    """

    # Manually curated based on real-world rendering behavior and Unicode East Asian Width annotations
    punct_map = {
        # Title marks / brackets (commonly used in CJK)
        "《": 2, "》": 2,  # Book title marks
        "「": 2, "」": 2,  # Corner brackets
        "『": 2, "』": 2,  # Double corner brackets
        "【": 2, "】": 2,  # Bold brackets
        "（": 2, "）": 2,  # Fullwidth parentheses
        "［": 2, "］": 2,  # Fullwidth square brackets
        "｛": 2, "｝": 2,  # Fullwidth curly braces
        "〈": 2, "〉": 2,  # Angle brackets
        "﹃": 2, "﹄": 2,  # Quotation corner marks
        "︻": 2, "︼": 2,  # Ornate brackets (used in ASCII art)

        # Quotation marks
        "“": 2, "”": 2,  # Double quotes
        "‘": 2, "’": 2,  # Single quotes

        # Sentence punctuation (used in Chinese / Japanese)
        "。": 2, "、": 2,  # Period, comma
        "，": 2, "．": 2,  # Fullwidth comma/period
        "：": 2, "；": 2,  # Colon, semicolon
        "？": 2, "！": 2,  # Question mark, exclamation mark

        # Tilde / prolonged sound / middle dot
        "〜": 2, "～": 2,  # Wave dash / fullwidth tilde
        "・": 2,          # Japanese middle dot

        # Dashes / ellipses / continuation marks
        "—": 2, "――": 2,  # Em dash / double dash
        "…": 2, "‥": 2,    # Ellipsis / double dot
        "︰": 2, "﹏": 2,  # Vertical ellipsis / underline filler

        # Reference / symbolic marks
        "※": 2,           # Reference mark
        "†": 2, "‡": 2,    # Dagger / double dagger
        "￣": 2,           # Macron (commonly used in manga)
        "　": 2,           # Fullwidth space (U+3000)

        # Circled numbers
        "①": 2, "②": 2, "③": 2, "④": 2, "⑤": 2,
        "⑥": 2, "⑦": 2, "⑧": 2, "⑨": 2, "⑩": 2,

        # Common graphical symbols (black/white circles, squares, stars)
        "●": 2, "○": 2,
        "◆": 2, "◇": 2,
        "■": 2, "□": 2,
        "★": 2, "☆": 2,

        # Arrows
        "→": 2, "←": 2, "↑": 2, "↓": 2,
        "↔": 2, "⇔": 2,

        # Unit symbols
        "℃": 2, "℉": 2,

        # Box-drawing / ASCII art elements
        "╭": 2, "╮": 2, "╯": 2, "╰": 2,
        "━": 2, "┃": 2, "┏": 2, "┓": 2, "┗": 2, "┛": 2,
    }

    output_path = resolve_current_path("variants/fullwidth_punctuations.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(punct_map, f, ensure_ascii=False, indent=2)

    print(f"✅ Done: {output_path} ({len(punct_map)} entries)")

    write_meta(
        name="fullwidth_punctuations",
        source_url="manually_curated (CJK typography conventions)",
        target_rel_path="variants/fullwidth_punctuations.json",
        entry_count=len(punct_map),
    )
