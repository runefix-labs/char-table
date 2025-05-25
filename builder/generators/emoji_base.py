from builder.core.version import major_minor

from builder.parser.emoji_parser import extract_emoji_map

from builder.writer.meta_writer import write_meta_json
from builder.writer.row_writer import write_category_text
from builder.writer.default_writer import write_current_json


def generate() -> None:
    """
    Generates emoji_base.json, its metadata (.meta.json), and plain character list (.txt).
    Includes only single-codepoint fully-qualified emojis.
    Source: emoji-test.txt from Unicode Consortium
    """
    version = major_minor()

    data = extract_emoji_map(mode="emoji_base")

    write_current_json("emoji", "emoji_base", data)

    write_meta_json(
        name="emoji_base",
        source_url=f"https://unicode.org/Public/emoji/{version}/emoji-test.txt",
        target_rel_path="emoji/emoji_base.json",
        entry_count=len(data)
    )

    write_category_text("emoji_base", data)
