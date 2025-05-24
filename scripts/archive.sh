#!/bin/bash
set -e

VERSION=$(cat VERSION.txt)
TIMESTAMP=$(date -u +"%Y-%m-%d_%H-%M-%S")
ARCHIVE_DIR="char_table/archive"
FILENAME="char_table_${TIMESTAMP}_v${VERSION}.tar.gz"
TAR_OPTS="--owner=char --group=table"

mkdir -p "$ARCHIVE_DIR"

tar $TAR_OPTS -czf "$ARCHIVE_DIR/$FILENAME" \
    char_table/current \
    char_table/meta

echo "✅ Archive created: $ARCHIVE_DIR/$FILENAME"
