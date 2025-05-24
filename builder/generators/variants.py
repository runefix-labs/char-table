import json
from builder.utils.meta_writer import write_meta
from builder.utils.version import read_version_txt
from builder.utils.path_utils import resolve_current_path


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
    return 0xFF01 <= cp <= 0xFF60 or 0xFFE0 <= cp <= 0xFFE6


def generate() -> None:
    """
    Generate the fullwidth variants table (fullwidth_variants.json),
    which maps common fullwidth characters to width 2 for display alignment purposes.
    """
    variant_map = {}

    for cp in range(0x110000):
        if is_fullwidth_variant(cp):
            variant_map[chr(cp)] = 2

    output_path = resolve_current_path("variants/fullwidth_variants.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(variant_map, f, ensure_ascii=False, indent=2)

    print(f"✅ Done: {output_path} ({len(variant_map)} entries)")

    version = read_version_txt()
    write_meta(
        name="fullwidth_variants",
        source_url=f"https://unicode.org/Public/{version}/ucd/Blocks.txt",
        target_rel_path="variants/fullwidth_variants.json",
        entry_count=len(variant_map)
    )
