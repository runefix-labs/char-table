# Makefile for char-table dataset generation

.DEFAULT_GOAL := all

.PHONY: all emoji cjk kana hangul variants archive version set-version

## Default: generate all datasets
all:
	python -m builder.gen_datasets all

## Only generate emoji_base + emoji_zwj
emoji:
	python -m builder.gen_datasets emoji_base
	python -m builder.gen_datasets emoji_zwj

## Only generate CJK unified
cjk:
	python -m builder.gen_datasets cjk_unified

## Only generate Japanese kana
kana:
	python -m builder.gen_datasets japanese_kana

## Only generate Korean syllables
hangul:
	python -m builder.gen_datasets korean_syllables

## Only generate fullwidth variants (includes symbols + punctuations)
variants:
	python -m builder.gen_datasets fullwidth_variants
	python -m builder.gen_datasets fullwidth_punctuations

## Archive current dataset into timestamped tar.gz
archive:
	bash scripts/archive.sh

## Show current Unicode version
version:
	@echo "📦 Unicode version: $$(cat VERSION.txt)"

## Set Unicode version via VERSION.txt
set-version:
	bash scripts/set_version.sh $(VERSION)
