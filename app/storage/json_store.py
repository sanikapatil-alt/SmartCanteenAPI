
import json
from pathlib import Path


# Find the project data folder
BASE_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = BASE_DIR / "data"


def read_json(filename):
    file_path = DATA_DIR / filename

    DATA_DIR.mkdir(parents=True, exist_ok=True)

    # Create an empty JSON list if file doesn't exist
    if not file_path.exists():
        write_json(filename, [])
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    except json.JSONDecodeError:
        raise ValueError(f"{filename} contains invalid JSON")


def write_json(filename, data):
    file_path = DATA_DIR / filename
    temp_path = DATA_DIR / f"{filename}.tmp"

    DATA_DIR.mkdir(parents=True, exist_ok=True)

    try:
        with open(temp_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        temp_path.replace(file_path)

    except OSError:
        if temp_path.exists():
            temp_path.unlink()
        raise
