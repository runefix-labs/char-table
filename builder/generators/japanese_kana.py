from builder.core.version import read_version

from builder.parser.language_parser import extract_lang_map

from builder.writer.meta_writer import write_meta_json
from builder.writer.row_writer import write_category_text
from builder.writer.default_writer import write_current_json


def generate() -> None:
    """
    Generates japanese_kana.json, its metadata (.meta.json), and plain character list (.txt).
    Includes Hiragana, Katakana, and all extended kana blocks.
    Source: Unicode UCD Blocks.txt
    """
    version = read_version()

    data = extract_lang_map("japanese_kana")

    write_current_json("cjk", "japanese_kana", data)

    write_meta_json(
        name="japanese_kana",
        source_url=f"https://unicode.org/Public/{version}/ucd/Blocks.txt",
        target_rel_path="cjk/japanese_kana.json",
        entry_count=len(data)
    )

    write_category_text("japanese_kana", data)
