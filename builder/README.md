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

| Directory / File                | Description                                                                |
|---------------------------------| -------------------------------------------------------------------------- |
| `gen_datasets.py`               | Unified entry point for dataset generation and command dispatching         |
| `generators/`                   | Character data extractors for different categories                         |
| ├── `emoji_base.py`             | Extract basic single-codepoint `emoji`                                     |
| ├── `emoji_zwj.py`              | Extract `emoji` formed by `ZWJ` sequences (multi-codepoint)                |
| ├── `cjk_unified.py`            | Extract unified `CJK` ideographs                                           |
| ├── `japanese_kana.py`          | Extract Japanese kana blocks                                               |
| ├── `korean_syllables.py`       | Extract Korean syllable blocks                                             |
| ├── `fullwidth_variants.py`     | Extract fullwidth variants in FF01–FF60 / FFE0–FFE6                        |
| └── `fullwidth_punctuations.py` | Manually curated list of punctuation and symbols treated as fullwidth      |
| `utils/`                        | Common utility functions and helpers                                       |
| ├── `emoji_source.py`           | Fetches `emoji-test.txt` from Unicode (URL is auto-generated from version) |
| ├── `meta_writer.py`            | Writes `.meta.json` files (includes `hash`, `entry_count`, UTC timestamp)  |
| ├── `path_utils.py`             | Resolves paths for both `current` and `meta` outputs                       |
| └── `version.py`                | Reads `VERSION.txt` to provide global version control                      |

## 🧱 Output Conventions

- All generated datasets are saved under `char_table/current/`.

- Each data file is paired with a corresponding `.meta.json` file written to `char_table/meta/`.

- All Unicode versioning is controlled centrally via `VERSION.txt` in the project root (e.g., `"15.1.0"`).

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
