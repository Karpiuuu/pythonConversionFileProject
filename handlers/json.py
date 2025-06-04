import json
import sys

def load_json_file(path: str):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except json.JSONDecodeError as e:
        print(f"Błąd składni JSON: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Błąd podczas wczytywania pliku JSON: {e}")
        sys.exit(1)
