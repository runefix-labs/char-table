import os


def resolve_current_path(rel_path: str) -> str:
    """
    Constructs the output path for dataset JSON files under char_table/current/.

    Args:
        rel_path (str): Relative subpath under current/, e.g. "emoji/emoji_base.json"

    Returns:
        str: Absolute path to char_table/current/<rel_path>, with directories created if needed
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.abspath(os.path.join(base_dir, "..", "..", "char_table", "current", rel_path))
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    return full_path


def resolve_meta_path(name: str) -> str:
    """
    Constructs the output path for metadata files under char_table/meta/.

    Args:
        name (str): Dataset name without file extension, e.g. "emoji_base"

    Returns:
        str: Absolute path to char_table/meta/<name>.meta.json, with directories created if needed
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.abspath(os.path.join(base_dir, "..", "..", "char_table", "meta", f"{name}.meta.json"))
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    return full_path


def resolve_category_path(name: str) -> str:
    """
    Constructs the output path for plain character lists under char_table/categories/.

    Args:
        name (str): Dataset name without file extension, e.g. "emoji_base"

    Returns:
        str: Absolute path to char_table/categories/<name>.txt, with directories created if needed
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.abspath(os.path.join(base_dir, "..", "..", "char_table", "categories", f"{name}.txt"))
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    return full_path
