import os


def read_version() -> str:
    """
    Reads the VERSION.txt file from the project root and returns the Unicode version number.

    Returns:
        str: The version string, e.g. "15.1.0"
    """
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    version_file = os.path.join(base_dir, "VERSION.txt")

    with open(version_file, "r", encoding="utf-8") as f:
        return f.read().strip()


def read_major_minor_version() -> str:
    """
    Reads the Unicode version from VERSION.txt and returns only the major.minor part.

    Returns:
        str: The major.minor version string, e.g. "15.1"
    """
    version = read_version()
    return ".".join(version.split(".")[:2])


def major_minor() -> str:
    """
    Shortcut alias for read_major_minor_version().
    """
    return read_major_minor_version()
