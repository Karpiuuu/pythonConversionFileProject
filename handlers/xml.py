import xmltodict
import sys

def load_xml_file(path: str):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = xmltodict.parse(f.read())
        return data
    except Exception as e:
        print(f"Błąd podczas wczytywania pliku XML: {e}")
        sys.exit(1)


def save_xml_file(path: str, data):
    try:
        xml_str = xmltodict.unparse(data, pretty=True)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(xml_str)
    except Exception as e:
        print(f"Błąd podczas zapisu do pliku XML: {e}")
        sys.exit(1)
