import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QFileDialog, QComboBox, QVBoxLayout, QMessageBox
)
from PyQt5.QtCore import QThread, pyqtSignal, QObject

from handlers import json, yaml, xml


class Worker(QObject):
    finished = pyqtSignal(str)
    error = pyqtSignal(str)

    def __init__(self, input_path, output_path, input_ext, output_ext):
        super().__init__()
        self.input_path = input_path
        self.output_path = output_path
        self.input_ext = input_ext
        self.output_ext = output_ext

    def run(self):
        try:
            if self.input_ext == ".json":
                data = json.load_json_file(self.input_path)
            elif self.input_ext in [".yaml", ".yml"]:
                data = yaml.load_yaml_file(self.input_path)
            elif self.input_ext == ".xml":
                data = xml.load_xml_file(self.input_path)
            else:
                self.error.emit(f"Nieobsługiwane rozszerzenie: {self.input_ext}")
                return

            if self.output_ext == ".json":
                json.save_json_file(self.output_path, data)
            elif self.output_ext in [".yaml", ".yml"]:
                yaml.save_yaml_file(self.output_path, data)
            elif self.output_ext == ".xml":
                xml.save_xml_file(self.output_path, data)

            self.finished.emit(self.output_path)

        except Exception as e:
            self.error.emit(str(e))


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

        self.thread = QThread()
        self.worker = Worker(self.input_path, self.output_path, input_ext, output_ext)
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.on_conversion_success)
        self.worker.error.connect(self.on_conversion_error)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        self.thread.start()

    def on_conversion_success(self, path):
        QMessageBox.information(self, "Sukces", f"Zapisano plik: {path}")

    def on_conversion_error(self, error_message):
        QMessageBox.critical(self, "Błąd", error_message)


def main():
    app = QApplication(sys.argv)
    window = ConverterApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
