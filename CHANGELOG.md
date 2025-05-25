# CHANGELOG

## [15.1.0] - 2025-05-25
- Major refactor of the build system with clearer modular separation (`core`, `parser`, `writer`)
- Added new output directory: `char_table/categories/` for storing raw character lists
- All generators now support category `.txt` output (for manual width assignment)

## [15.1.0] - 2025-05-24
- Updated to [Unicode 15.1.0](https://unicode.org/Public/15.1.0/).
- Regenerated all tables using new source.
- Added new table: `fullwidth_punctuations`
  - Manually curated set of punctuation and symbols commonly rendered as width=2 in East Asian typography.
  - Includes book title marks, corner brackets, Japanese middle dot, ellipsis, reference marks, arrows, ASCII decorations, and more.

## [15.0.0] - 2025-05-24
- Initial public release.
- Supports:
  - emoji_base / emoji_zwj
  - cjk_unified
  - japanese_kana
  - korean_syllables
  - fullwidth_variants
