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
