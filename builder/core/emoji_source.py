import requests

from builder.core.version import major_minor


def emoji_fetchers() -> list[str]:
    """
    Automatically reads the Unicode version from VERSION.txt at the project root,
    and fetches the corresponding emoji-test.txt from the official Unicode website.

    Returns:
        list[str]: A list of lines from the fetched emoji-test.txt file.
    """
    version = major_minor()

    url = f"https://unicode.org/Public/emoji/{version}/emoji-test.txt"
    print(f"🌐 Fetching emoji-test.txt from {url} ...")

    response = requests.get(url)
    response.raise_for_status()
    return response.text.splitlines()
