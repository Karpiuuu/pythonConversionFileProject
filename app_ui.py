import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QFileDialog, QComboBox, QVBoxLayout, QMessageBox
)
import os
from handlers import json, yaml, xml

class ConverterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Data Converter")
        self.setGeometry(200, 200, 400, 200)

        self.input_path = ""
        self.output_path = ""

        self.label = QLabel("Wybierz plik wejściowy:")
        self.button_input = QPushButton("Wybierz plik")
        self.combo_format = QComboBox()
        self.combo_format.addItems(["json", "yaml", "xml"])
        self.button_convert = QPushButton("Konwertuj")

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button_input)
        layout.addWidget(QLabel("Wybierz format wyjściowy:"))
        layout.addWidget(self.combo_format)
        layout.addWidget(self.button_convert)

        self.setLayout(layout)

        self.button_input.clicked.connect(self.select_input_file)
        self.button_convert.clicked.connect(self.convert_file)

    def select_input_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Wybierz plik", "", "All Files (*.*)")
        if file_path:
            self.input_path = file_path
            self.label.setText(f"Wybrano: {os.path.basename(file_path)}")

    def convert_file(self):
        if not self.input_path:
            QMessageBox.warning(self, "Błąd", "Nie wybrano pliku wejściowego.")
            return

        input_ext = os.path.splitext(self.input_path)[1].lower()
        output_ext = self.combo_format.currentText().lower()
        output_ext = ".yaml" if output_ext == "yaml" else f".{output_ext}"
        self.output_path = self.input_path.replace(input_ext, f"_converted{output_ext}")

        # Wczytywanie
        try:
            if input_ext == ".json":
                data = json.load_json_file(self.input_path)
            elif input_ext in [".yaml", ".yml"]:
                data = yaml.load_yaml_file(self.input_path)
            elif input_ext == ".xml":
                data = xml.load_xml_file(self.input_path)
            else:
                QMessageBox.warning(self, "Błąd", f"Nieobsługiwane rozszerzenie: {input_ext}")
                return
        except Exception as e:
            QMessageBox.critical(self, "Błąd", f"Nie udało się wczytać pliku: {e}")
            return

        # Zapis
        try:
            if output_ext == ".json":
                json.save_json_file(self.output_path, data)
            elif output_ext in [".yaml", ".yml"]:
                yaml.save_yaml_file(self.output_path, data)
            elif output_ext == ".xml":
                xml.save_xml_file(self.output_path, data)
        except Exception as e:
            QMessageBox.critical(self, "Błąd", f"Nie udało się zapisać pliku: {e}")
            return

        QMessageBox.information(self, "Sukces", f"Zapisano plik: {self.output_path}")

def main():
    app = QApplication(sys.argv)
    window = ConverterApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
