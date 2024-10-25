import os
from gif_extractor import GIFExtractor


class GIFManager:
    def __init__(self, directory_path):
        self.directory_path = directory_path
        self.gif_files = []

    def search_gif_files(self):
        for root, dirs, files in os.walk(self.directory_path):
            for file in files:
                if file.lower().endswith('.gif'):
                    gif_path = os.path.join(root, file)
                    self.gif_files.append(gif_path)
                    print(f"Archivo encontrado: {gif_path}")  # Confirmación de archivo

    def process_gif_files(self):
        if not self.gif_files:
            print("No se encontraron archivos GIF para procesar.")
            return

        for gif_file in self.gif_files:
            print(f"Procesando archivo GIF: {gif_file}")  # Confirmación de procesamiento
            extractor = GIFExtractor(gif_file)
            extractor.get_info()
            extractor.show_info()
