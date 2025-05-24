# 📐 char-table

**char-table** is a Unicode-based dataset generator for East Asian wide-character support, extracting `emoji`, `CJK`, `kana`, `Hangul`, and fullwidth variant characters into structured JSON datasets — with reproducible `meta` information.

---

## 📦 Output Structure

```text
char_table/
├── current/   # All up-to-date dataset files
├── archive/   # Optional: historical snapshots
└── meta/      # Metadata for each dataset
```

## 📜 Supported Tables

- `emoji_base`: Single-codepoint emoji
- `emoji_zwj`: ZWJ-composed emoji
- `cjk_unified`: CJK Unified Ideographs (Basic + Extension A–G)
- `japanese_kana`: Hiragana & Katakana blocks
- `korean_syllables`: Hangul Syllables block
- `fullwidth_variants`: Fullwidth punctuation, Latin & symbols

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

The current version is defined in [`VERSION.txt`](./VERSION.txt),  
and aligned with the official [Unicode Consortium](https://home.unicode.org/) releases.

## 📌 CHANGELOG

See [CHANGELOG.md](./CHANGELOG.md) for version history.

## 🪪 LICENSE

MIT © 2025 Pokeya Z. Chen / Runefix Labs
