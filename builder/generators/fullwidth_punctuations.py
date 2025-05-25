from builder.parser.symbol_parser import extract_symbol_map

from builder.writer.meta_writer import write_meta_json
from builder.writer.row_writer import write_category_text
from builder.writer.default_writer import write_current_json


def generate() -> None:
    """
    Generates fullwidth_punctuations.json, its metadata (.meta.json), and plain character list (.txt).
    Manually curated set of wide punctuation and symbols commonly rendered as width=2 in CJK environments.
    Source: manually curated (CJK typography conventions)
    """
    data = extract_symbol_map("fullwidth_punctuations")

    write_current_json("variants", "fullwidth_punctuations", data)

    write_meta_json(
        name="fullwidth_punctuations",
        source_url="manually_curated (CJK typography conventions)",
        target_rel_path="variants/fullwidth_punctuations.json",
        entry_count=len(data),
    )

    write_category_text("fullwidth_punctuations", data)
