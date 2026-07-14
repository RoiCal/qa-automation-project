import json
from pathlib import Path # provide a generic path
from typing import Any # for flexabilty but is not type safe


PROJECT_ROOT = Path(__file__).resolve().parent.parent


def load_json_test_data(relative_path: str) -> list[dict[str, Any]]:
    """Load test data from a JSON file relative to the project root."""
    file_path = PROJECT_ROOT / relative_path

    with file_path.open(encoding="utf-8") as file:
        return json.load(file)