# 🛠 builder/

This directory contains the **character table build system**, including all scripts and utility modules.  
Its main role is to extract structured data such as `Emoji`, `CJK`, and fullwidth variant symbols from official `Unicode` sources,  
then generate standardized `JSON` files along with metadata (`.meta.json`) for downstream usage.

---

## 🚀 Quick Commands

We recommend using module-based execution to invoke the generators:

```bash
# Generate all datasets (recommended)
python -m builder.gen_datasets all

# Generate a specific dataset only
python -m builder.gen_datasets emoji_base
python -m builder.gen_datasets emoji_zwj
python -m builder.gen_datasets cjk_unified
python -m builder.gen_datasets japanese_kana
python -m builder.gen_datasets korean_syllables
python -m builder.gen_datasets fullwidth_variants
python -m builder.gen_datasets fullwidth_punctuations
```

## 📁 Submodule Structure

### Top-Level

| Path              | Description                                     |
| ----------------- | ----------------------------------------------- |
| `gen_datasets.py` | Main CLI entry point for all dataset generation |
| `VERSION.txt`     | Controls the Unicode version for all builds     |

### generators/

Each file contains a `generate()` function that extracts and writes one dataset.

| File                        | Dataset Description                                             |
| --------------------------- | --------------------------------------------------------------- |
| `emoji_base.py`             | Single-codepoint fully-qualified emoji                          |
| `emoji_zwj.py`              | ZWJ / multi-codepoint emoji sequences                           |
| `cjk_unified.py`            | CJK Unified Ideographs (Basic + A–G + Compatibility)            |
| `japanese_kana.py`          | All Hiragana, Katakana, and extended kana ranges                |
| `korean_syllables.py`       | 11,172 modern Hangul syllables (U+AC00–U+D7AF)                  |
| `fullwidth_variants.py`     | Fullwidth Latin / symbol variants (FF01–FF60, FFE0–FFE6)        |
| `fullwidth_punctuations.py` | Manually curated wide punctuation used in East Asian typography |

### core/

Low-level utilities shared across parsers and writers.

| File              | Purpose                                        |
| ----------------- | ---------------------------------------------- |
| `emoji_source.py` | Fetches `emoji-test.txt` from Unicode.org      |
| `path_utils.py`   | Resolves output paths for JSON and metadata    |
| `version.py`      | Parses Unicode version info from `VERSION.txt` |

### parser/

Encapsulates all Unicode classification and extraction logic.

| File                 | Purpose                                                             |
| -------------------- | ------------------------------------------------------------------- |
| `emoji_parser.py`    | Parses emoji data by mode: `base` or `zwj`                          |
| `language_parser.py` | Handles extraction for `cjk_unified`, `kana`, `hangul`              |
| `symbol_parser.py`   | Handles fullwidth symbol detection and curated punctuation mappings |
| `constants.py`       | Centralizes mode enums for emoji/language/symbol parsing            |

### writer/

Responsible for writing various output formats.

| File                | Purpose                                                        |
|---------------------| -------------------------------------------------------------- |
| `default_writer.py` | Writes main `.json` dataset files under `char_table/current/`  |
| `meta_writer.py`    | Writes `.meta.json` files with hash, source, and timestamps    |
| `row_writer.py`     | Writes plain `.txt` file listing each character (one per line) |

## 🧱 Output Conventions

- All generated `.json` files are saved under `char_table/current/`. 
- Corresponding `.meta.json` metadata goes under `char_table/meta/`. 
- Plain `.txt` character lists (one char per line) accompany each dataset. 
- Unicode versioning is managed globally by `VERSION.txt`.

## 🔒 Metadata Format

Each generated table comes with a metadata file with the following structure:

```json
{
  "name": "emoji_base",
  "source": "https://unicode.org/Public/emoji/15.1/emoji-test.txt",
  "last_fetched": "2025-05-24T12:34:56Z",
  "entry_count": 1170,
  "hash": "75f9e35b...a150",
  "version": "15.1.0"
}
```

---

For a full overview of the project structure and background, see the main `README.md` at the root directory.
