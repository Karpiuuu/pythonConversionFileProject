import sys
import os

SUPPORTED_EXTENSIONS = [".json", ".yaml", ".yml", ".xml"]

def get_file_extension(file_path: str) -> str:
    return os.path.splitext(file_path)[1].lower()

def is_supported_file(file_path: str) -> bool:
    return get_file_extension(file_path) in SUPPORTED_EXTENSIONS

def main():
    if len(sys.argv) != 3:
        print("Błąd: Podaj dokładnie 2 argumenty: <plik_wejściowy> <plik_wyjściowy>")
        print("Przykład: program.exe input.json output.xml")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.exists(input_file):
        print(f"Błąd: Plik wejściowy nie istnieje: {input_file}")
        sys.exit(1)

    input_ext = get_file_extension(input_file)
    output_ext = get_file_extension(output_file)

    if input_ext not in SUPPORTED_EXTENSIONS:
        print(f"Błąd: Nieobsługiwane rozszerzenie pliku wejściowego: {input_ext}")
        sys.exit(1)

    if output_ext not in SUPPORTED_EXTENSIONS:
        print(f"Błąd: Nieobsługiwane rozszerzenie pliku wyjściowego: {output_ext}")
        sys.exit(1)

    print(f"Rozpoczynam konwersję z {input_ext} do {output_ext}...")

if __name__ == "__main__":
    main()
