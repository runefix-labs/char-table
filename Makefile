# Makefile for char-table dataset generation and utilities
# --------------------------------------------------------
# Provides convenient aliases for running dataset generators,
# managing Unicode versioning, and archiving output files.

# Default goal when running `make`
.DEFAULT_GOAL := all

# Declare all targets as phony (non-file-based)
.PHONY: all emoji language symbols archive version set-version

## Generate all datasets (emoji, CJK, symbols)
all:
	python -m builder.gen_datasets all

## Generate emoji-related datasets only (base, zwj)
emoji:
	python -m builder.gen_datasets emoji_base
	python -m builder.gen_datasets emoji_zwj

## Generate all language blocks (CJK, kana, hangul)
language:
	python -m builder.gen_datasets cjk_unified
	python -m builder.gen_datasets japanese_kana
	python -m builder.gen_datasets korean_syllables

## Generate symbol-related datasets only (variants, punctuations)
symbols:
	python -m builder.gen_datasets fullwidth_variants
	python -m builder.gen_datasets fullwidth_punctuations

## Archive current dataset into timestamped tar.gz
archive:
	bash scripts/archive.sh

## Show current Unicode version
version:
	@echo "📦 Unicode version: $$(cat VERSION.txt)"

## Set Unicode version manually
set-version:
	bash scripts/set_version.sh $(VERSION)
