import os


def resolve_current_path(rel_path: str) -> str:
    """
    Converts a relative path (e.g. "emoji/emoji_base.json") into an absolute path
    under the char_table/current directory, and ensures the target directory exists.

    Args:
        rel_path (str): A relative path, such as "emoji/emoji_base.json"

    Returns:
        str: The constructed absolute path with intermediate directories created
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.abspath(os.path.join(base_dir, "..", "..", "char_table", "current", rel_path))
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    return full_path


def resolve_meta_path(name: str) -> str:
    """
    Constructs the output path for metadata files under char_table/meta/.

    Args:
        name (str): The table name without file extension, such as "emoji_base"

    Returns:
        str: The full path, e.g. char_table/meta/emoji_base.meta.json
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.abspath(os.path.join(base_dir, "..", "..", "char_table", "meta", f"{name}.meta.json"))
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    return full_path
