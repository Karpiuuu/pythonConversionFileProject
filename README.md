# Data Converter  

## Opis projektu  
Data Converter to aplikacja umożliwiająca konwersję danych pomiędzy różnymi formatami plików: JSON, YAML i XML. Projekt zawiera zarówno interfejs graficzny (GUI) oparty na bibliotece PyQt5, jak i wersję konsolową, która pozwala na konwersję plików za pomocą poleceń w terminalu.  

## Funkcjonalności  
- Obsługa formatów JSON, YAML i XML.  
- Konwersja danych pomiędzy różnymi formatami.  
- Interfejs graficzny ułatwiający wybór plików i formatów.  
- Wersja konsolowa dla użytkowników preferujących pracę w terminalu.  
- Automatyczne tworzenie pliku wynikowego z odpowiednim rozszerzeniem.  

## Wymagania  
- Python 3.10 lub nowszy.  
- Zainstalowane zależności:  
    - PyQt5  
    - PyYAML  
    - xmltodict  
    - pyinstaller  

## Instalacja  
1. Sklonuj repozytorium:  
     ```bash  
     git clone <adres_repozytorium>  
     ```  
2. Zainstaluj wymagane zależności:  
     ```bash  
     python -m pip install --upgrade pip  
     ./requirements/installResources.ps1  
     ```  

## Uruchomienie  
### Interfejs graficzny  
Uruchom aplikację GUI:  
```bash  
python app_ui.py  
```  

### Wersja konsolowa  
Uruchom aplikację w terminalu, podając ścieżki do pliku wejściowego i wyjściowego:  
```bash  
python main.py <plik_wejściowy> <plik_wyjściowy>  
```  
Przykład:  
```bash  
python main.py examples/example.json examples/output.xml  
```  

## Budowanie pliku wykonywalnego  
Aby zbudować plik wykonywalny (.exe), użyj GitHub Actions lub lokalnie:  
```bash  
pyinstaller --onefile --noconsole app_ui.py  
```  

## Przykłady  
### Plik JSON  
```json  
{  
        "osoba": {  
                "name": "Anna",  
                "age": 30,  
                "hobbies": ["reading", "cycling", "chess"]  
        }  
}  
```  

### Plik YAML  
```yaml  
product:  
    name: Laptop  
    price: 4999.99  
    available: true  
    features:  
        - SSD  
        - 16GB RAM  
        - Intel i7  
```  

### Plik XML  
```xml  
<person>  
    <firstName>John</firstName>  
    <lastName>Doe</lastName>  
    <contact>  
        <email>john@example.com</email>  
        <phone>123-456-789</phone>  
    </contact>  
</person>  
```  

## Autorzy  
Projekt został stworzony przez Michała Karpińskiego nr indeksu: 56021