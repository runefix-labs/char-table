from builder.core.version import read_version

from builder.parser.symbol_parser import extract_symbol_map

from builder.writer.meta_writer import write_meta_json
from builder.writer.row_writer import write_category_text
from builder.writer.default_writer import write_current_json


def generate() -> None:
    """
    Generates fullwidth_variants.json, its metadata (.meta.json), and plain character list (.txt).
    Covers fullwidth Latin, digits, symbols in FFXX/FFE0–FFE6 blocks.
    Source: Unicode UCD Blocks.txt
    """
    version = read_version()

    data = extract_symbol_map("fullwidth_variants")

    write_current_json("variants", "fullwidth_variants", data)

    write_meta_json(
        name="fullwidth_variants",
        source_url=f"https://unicode.org/Public/{version}/ucd/Blocks.txt",
        target_rel_path="variants/fullwidth_variants.json",
        entry_count=len(data)
    )

    write_category_text("fullwidth_variants", data)
