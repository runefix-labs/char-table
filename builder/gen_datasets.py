import sys

from builder.generators.emoji_base import generate as gen_emoji_base
from builder.generators.emoji_zwj import generate as gen_emoji_zwj
from builder.generators.cjk_unified import generate as gen_cjk_unified
from builder.generators.japanese_kana import generate as gen_japanese_kana
from builder.generators.korean_syllables import generate as gen_korean_syllables
from builder.generators.variants import generate as gen_variants


def print_usage() -> None:
    """
    Print usage instructions for available dataset generation commands.
    """
    print("Usage:")
    print("  python gen_datasets.py all                # Generate all datasets")
    print("  python gen_datasets.py emoji_base         # Only generate emoji_base.json")
    print("  python gen_datasets.py emoji_zwj          # Only generate emoji_zwj.json")
    print("  python gen_datasets.py cjk_unified        # Only generate CJK unified table")
    print("  python gen_datasets.py japanese_kana      # Only generate Japanese kana table")
    print("  python gen_datasets.py korean_syllables   # Only generate Korean syllables table")
    print("  python gen_datasets.py variants           # Only generate fullwidth variant table")


def dispatch(command: str) -> None:
    """
    Dispatch the given command string to the appropriate generator function.

    Args:
        command (str): The command name passed from CLI.
    """
    match command:
        case "emoji_base":
            gen_emoji_base()
        case "emoji_zwj":
            gen_emoji_zwj()
        case "cjk_unified":
            gen_cjk_unified()
        case "japanese_kana":
            gen_japanese_kana()
        case "korean_syllables":
            gen_korean_syllables()
        case "variants":
            gen_variants()
        case "all":
            print("✨ Generating all datasets...")
            gen_emoji_base()
            gen_emoji_zwj()
            gen_cjk_unified()
            gen_japanese_kana()
            gen_korean_syllables()
            gen_variants()
        case _:
            print(f"❌ Unknown command: {command}")
            print_usage()


if __name__ == "__main__":
    # Entry point: parse CLI args and dispatch command
    if len(sys.argv) != 2:
        print_usage()
        sys.exit(1)

    dispatch(sys.argv[1])
