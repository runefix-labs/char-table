# 📐 char-table

**char-table** is a Unicode-based dataset generator for East Asian wide-character support, extracting `emoji`, `CJK`, `kana`, `Hangul`, and fullwidth variant characters into structured JSON datasets — with reproducible `meta` information.

---

## 📦 Output Structure

```text
char_table/
├── archive/      # Optional: timestamped snapshots (.tar.gz)
├── categories/   # Raw character lists (plain .txt), no width values
├── current/      # Default output: JSON maps with width info (e.g. {"🌍": 2})
└── meta/         # Auto-generated metadata (.meta.json) for each dataset
```

## 📜 Supported Tables

- `emoji_base`: Single-codepoint emoji
- `emoji_zwj`: ZWJ-composed emoji
- `cjk_unified`: CJK Unified Ideographs (Basic + Extension A–G)
- `japanese_kana`: Hiragana & Katakana blocks
- `korean_syllables`: Hangul Syllables block
- `fullwidth_variants`: Fullwidth symbols and ASCII-like variants (FF01–FF60, FFE0–FFE6)
- `fullwidth_punctuations`: Manually curated fullwidth punctuations and symbols used in CJK typography

## 🚀 Usage

```bash
# Generate all datasets (emoji, CJK, kana, etc.)
make

# Archive the current dataset snapshot (current + meta)
make archive

# Display the current Unicode version
make version

# Set Unicode version (updates VERSION.txt)
make set-version VERSION=15.1.0
```

## 🧾 Unicode Version

The current Unicode version is defined in [`VERSION.txt`](./VERSION.txt),  
strictly aligned with the official releases from the [Unicode Consortium](https://home.unicode.org/) releases. \
For historical version details, refer to: \
[Unicode Version History](https://www.unicode.org/versions/enumeratedversions.html)

## 📌 CHANGELOG

See [CHANGELOG.md](./CHANGELOG.md) for version history.

## 🪪 LICENSE

MIT © 2025 Pokeya Z. Chen / Runefix Labs
