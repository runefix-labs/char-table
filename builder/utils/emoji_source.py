import requests
from typing import List
from builder.utils.version import read_version_txt


def fetch_emoji_test_txt() -> List[str]:
    """
    Automatically reads the Unicode version from VERSION.txt at the project root,
    and fetches the corresponding emoji-test.txt from the official Unicode website.

    Returns:
        List[str]: A list of lines from the fetched emoji-test.txt file.
    """
    unicode_version = read_version_txt()
    emoji_version = ".".join(unicode_version.split(".")[:2])  # e.g. "15.1.0" -> "15.1"

    url = f"https://unicode.org/Public/emoji/{emoji_version}/emoji-test.txt"
    print(f"🌐 Fetching emoji-test.txt from {url} ...")

    response = requests.get(url)
    response.raise_for_status()
    return response.text.splitlines()
