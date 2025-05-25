from builder.core.version import read_version

from builder.parser.language_parser import extract_lang_map

from builder.writer.meta_writer import write_meta_json
from builder.writer.row_writer import write_category_text
from builder.writer.default_writer import write_current_json


def generate() -> None:
    """
    Generates cjk_unified.json, its metadata (.meta.json), and plain character list (.txt).
    Includes Basic + Extension A–G + Compatibility Ideographs from the Unicode CJK blocks.
    Source: Unicode UCD Blocks.txt
    """
    version = read_version()

    data = extract_lang_map("cjk_unified")

    write_current_json("cjk", "cjk_unified", data)

    write_meta_json(
        name="cjk_unified",
        source_url=f"https://unicode.org/Public/{version}/ucd/Blocks.txt",
        target_rel_path="cjk/cjk_unified.json",
        entry_count=len(data)
    )

    write_category_text("cjk_unified", data)
