import json

from builder.core.path_utils import resolve_current_path


def write_current_json(category: str, name: str, data: dict[str, int]) -> str:
    """
    Writes a character-width mapping JSON file to char_table/current/{category}/{name}.json.

    Args:
        category (str): Subdirectory under current/, e.g. "emoji", "cjk"
        name (str): File name without extension, e.g. "emoji_base"
        data (dict[str, int]): Character width mapping

    Returns:
        str: The full absolute path of the written JSON file
    """
    rel_path = f"{category}/{name}.json"
    output_path = resolve_current_path(rel_path)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ JSON written: {output_path} ({len(data)} entries)")
    return output_path
