import os

from builder.core.path_utils import resolve_category_path


def write_category_text(name: str, char_map: dict[str, int]) -> None:
    """
    Writes a plain-text character list file under char_table/categories/,
    with one character per line, for category-based lookup.

    Args:
        name (str): Dataset name (e.g., "emoji_base", "cjk_unified")
        char_map (dict[str, int]): Mapping of characters to display width (typically 2)
    """
    # Sort for deterministic output
    sorted_chars = sorted(char_map)

    # Resolve absolute path
    output_path = resolve_category_path(name)

    # Ensure parent directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Write each character to a new line
    with open(output_path, "w", encoding="utf-8") as f:
        for ch in sorted_chars:
            f.write(ch + "\n")

    print(f"📝 Category TXT written: {output_path} ({len(sorted_chars)} chars)")
