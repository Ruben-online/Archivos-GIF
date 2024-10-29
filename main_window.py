import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog, \
    QListWidget, QLineEdit, QHBoxLayout, QMessageBox
from gif_manager import GIFManager
from gif_info_editor import GIFInfoEditor


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana principal
        self.setWindowTitle("Editor de Información de GIFs")
        self.setGeometry(200, 200, 600, 400)

        # Configuración de layout principal
        main_layout = QVBoxLayout()

        # Widgets
        self.folder_label = QLabel("Carpeta seleccionada: Ninguna")
        self.select_folder_btn = QPushButton("Seleccionar carpeta de GIFs")
        self.process_gifs_btn = QPushButton("Procesar GIFs y guardar información")
        self.gif_list = QListWidget()
        self.attribute_input = QLineEdit()
        self.new_value_input = QLineEdit()
        self.save_changes_btn = QPushButton("Guardar Cambios en Atributo")

        # Conectar señales a slots
        self.select_folder_btn.clicked.connect(self.select_folder)
        self.process_gifs_btn.clicked.connect(self.process_gifs)
        self.gif_list.itemSelectionChanged.connect(self.load_gif_attributes)
        self.save_changes_btn.clicked.connect(self.save_changes)

        # Agregar widgets al layout
        main_layout.addWidget(self.folder_label)
        main_layout.addWidget(self.select_folder_btn)
        main_layout.addWidget(self.process_gifs_btn)
        main_layout.addWidget(QLabel("GIFs procesados:"))
        main_layout.addWidget(self.gif_list)

        # Edición de atributos
        attribute_layout = QHBoxLayout()
        attribute_layout.addWidget(QLabel("Atributo a editar:"))
        attribute_layout.addWidget(self.attribute_input)
        main_layout.addLayout(attribute_layout)

        new_value_layout = QHBoxLayout()
        new_value_layout.addWidget(QLabel("Nuevo valor:"))
        new_value_layout.addWidget(self.new_value_input)
        main_layout.addLayout(new_value_layout)

        main_layout.addWidget(self.save_changes_btn)

        # Configuración de contenedor y layout
        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        # Variables internas
        self.directory = None
        self.editor = None

    def select_folder(self):
        # Seleccionar carpeta de GIFs
        self.directory = QFileDialog.getExistingDirectory(self, "Seleccione la carpeta con archivos GIF")
        if self.directory:
            self.folder_label.setText(f"Carpeta seleccionada: {self.directory}")

    def process_gifs(self):
        # Procesar los GIFs en la carpeta seleccionada
        if not self.directory:
            QMessageBox.warning(self, "Advertencia", "Seleccione una carpeta primero.")
            return

        output_file = "GIF_info.txt"
        gif_manager = GIFManager(self.directory)
        gif_manager.search_gif_files()

        if gif_manager.gif_files:
            gif_manager.process_gif_files(output_file)
            QMessageBox.information(self, "Éxito", f"Información guardada en {output_file}.")
            self.load_gif_list()
        else:
            QMessageBox.warning(self, "Advertencia", "No se encontraron archivos GIF en la carpeta seleccionada.")

    def load_gif_list(self):
        # Cargar los nombres de los GIFs en la lista
        self.editor = GIFInfoEditor("GIF_info.txt")
        self.editor.load_info()
        self.gif_list.clear()
        for gif_name in self.editor.gif_data.keys():
            self.gif_list.addItem(gif_name)

    def load_gif_attributes(self):
        # Cargar los atributos del GIF seleccionado
        selected_gif = self.gif_list.currentItem().text()
        if selected_gif:
            attributes = "\n".join([f"{k}: {v}" for k, v in self.editor.gif_data[selected_gif].items()])
            QMessageBox.information(self, "Atributos del GIF", f"Atributos de {selected_gif}:\n\n{attributes}")

    def save_changes(self):
        # Guardar los cambios en un atributo de un GIF seleccionado
        selected_gif = self.gif_list.currentItem()
        if not selected_gif:
            QMessageBox.warning(self, "Advertencia", "Seleccione un GIF de la lista.")
            return

        gif_name = selected_gif.text()
        attribute = self.attribute_input.text().strip()
        new_value = self.new_value_input.text().strip()

        if attribute and new_value:
            self.editor.edit_info(gif_name, attribute, new_value)
            self.editor.save_changes()
            QMessageBox.information(self, "Éxito", "Los cambios se han guardado en el archivo .txt.")
            self.attribute_input.clear()
            self.new_value_input.clear()
        else:
            QMessageBox.warning(self, "Advertencia", "Debe ingresar un atributo y un nuevo valor.")


# Ejecución de la aplicación
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()