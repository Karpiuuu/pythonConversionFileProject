import yaml
import sys

def load_yaml_file(path: str):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        return data
    except yaml.YAMLError as e:
        print(f"Błąd składni YAML: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Błąd podczas wczytywania pliku YAML: {e}")
        sys.exit(1)

def save_yaml_file(path: str, data):
    try:
        with open(path, 'w', encoding='utf-8') as f:
            yaml.dump(data, f, allow_unicode=True, sort_keys=False)
    except Exception as e:
        print(f"Błąd podczas zapisu do pliku YAML: {e}")
        sys.exit(1)