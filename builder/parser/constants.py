from typing import Literal

# LanguageMode defines all supported character extraction modes related to CJK scripts.
# Used by language_parser.py to distinguish between CJK unified ideographs, Japanese kana, and Hangul syllables.
LanguageMode = Literal["cjk_unified", "japanese_kana", "korean_syllables"]

# SymbolMode defines symbolic character extraction modes.
# Used by symbol_parser.py to differentiate between fullwidth Unicode variants and manually curated wide punctuations.
SymbolMode = Literal["fullwidth_variants", "fullwidth_punctuations"]

# EmojiMode defines emoji parsing strategies for emoji-test.txt.
# Used by emoji_parser.py to extract either base (single-codepoint) or ZWJ (multi-codepoint) emoji.
EmojiMode = Literal["emoji_base", "emoji_zwj"]
