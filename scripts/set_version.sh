#!/bin/bash

# Update the Unicode version in VERSION.txt

if [ -z "$1" ]; then
  echo "❌ Please provide a version number, e.g.: ./scripts/set_version.sh 15.1.0"
  exit 1
fi

printf "%s" "$1" > VERSION.txt
echo "✅ Version updated to: $1"
