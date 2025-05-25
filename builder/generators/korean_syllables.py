from builder.core.version import read_version

from builder.parser.language_parser import extract_lang_map

from builder.writer.meta_writer import write_meta_json
from builder.writer.row_writer import write_category_text
from builder.writer.default_writer import write_current_json


def generate() -> None:
    """
    Generates korean_syllables.json, its metadata (.meta.json), and plain character list (.txt).
    Includes all 11,172 precomposed modern Hangul syllables (U+AC00–U+D7AF).
    Source: Unicode UCD Blocks.txt
    """
    version = read_version()

    data = extract_lang_map("korean_syllables")

    write_current_json("cjk", "korean_syllables", data)

    write_meta_json(
        name="korean_syllables",
        source_url=f"https://unicode.org/Public/{version}/ucd/Blocks.txt",
        target_rel_path="cjk/korean_syllables.json",
        entry_count=len(data),
    )

    write_category_text("korean_syllables", data)
