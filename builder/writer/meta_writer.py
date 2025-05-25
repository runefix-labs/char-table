import json
import hashlib
from datetime import datetime, timezone

from builder.core.version import read_version
from builder.core.path_utils import resolve_current_path, resolve_meta_path


def write_meta_json(name: str, source_url: str, target_rel_path: str, entry_count: int) -> None:
    """
    Write a corresponding metadata file for a given dataset,
    saving it under char_table/meta/.

    Args:
        name (str): Table name, e.g. "emoji_base"
        source_url (str): Source URL used to generate this dataset
        target_rel_path (str): Relative path of the output file, e.g. "emoji/emoji_base.json"
        entry_count (int): Number of entries in the generated dataset
    """
    # Locate the target data file
    data_path = resolve_current_path(target_rel_path)
    with open(data_path, "rb") as f:
        file_bytes = f.read()

    # Calculate SHA-256 hash of the output file
    file_hash = hashlib.sha256(file_bytes).hexdigest()

    # Get current UTC time (ISO 8601 format with trailing Z)
    now = datetime.utcnow().replace(tzinfo=timezone.utc)
    iso_time = now.isoformat(timespec="seconds").replace("+00:00", "Z")

    # Read global version from VERSION.txt
    version = read_version()

    # Compose metadata object
    meta = {
        "name": name,
        "source": source_url,
        "last_fetched": iso_time,
        "entry_count": entry_count,
        "hash": file_hash,
        "version": version
    }

    # Write to char_table/meta/{name}.meta.json
    meta_path = resolve_meta_path(name)
    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)

    print(f"📝 Meta written: {meta_path}")
