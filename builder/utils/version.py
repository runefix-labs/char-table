import os


def read_version_txt() -> str:
    """
    Reads the VERSION.txt file from the project root and returns the Unicode version number.

    Returns:
        str: The version string, e.g. "15.1.0"
    """
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    version_file = os.path.join(base_dir, "VERSION.txt")

    with open(version_file, "r", encoding="utf-8") as f:
        return f.read().strip()
