from builder.core.version import major_minor

from builder.parser.emoji_parser import extract_emoji_map

from builder.writer.meta_writer import write_meta_json
from builder.writer.row_writer import write_category_text
from builder.writer.default_writer import write_current_json


def generate() -> None:
    """
    Generates emoji_zwj.json, its metadata (.meta.json), and plain character list (.txt).
    Includes all fully-qualified emojis using ZWJ or composed of multiple codepoints.
    Source: emoji-test.txt from Unicode Consortium
    """
    version = major_minor()

    data = extract_emoji_map(mode="emoji_zwj")

    write_current_json("emoji", "emoji_zwj", data)

    write_meta_json(
        name="emoji_zwj",
        source_url=f"https://unicode.org/Public/emoji/{version}/emoji-test.txt",
        target_rel_path="emoji/emoji_zwj.json",
        entry_count=len(data),
    )

    write_category_text("emoji_zwj", data)
