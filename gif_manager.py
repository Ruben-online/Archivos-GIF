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

    def process_gif_files(self, output_file="GIF_info.txt"):
        # Limpiar el archivo antes de escribir nueva información
        open(output_file, 'w').close()

        for gif_file in self.gif_files:
            print(f"\n--- Procesando archivo GIF: {gif_file} ---")
            extractor = GIFExtractor(gif_file)
            extractor.get_info()  # Extrae la información
            extractor.show_info()  # Muestra en consola
            extractor.save_to_file(output_file)  # Guarda en el archivo de texto
            print(f"--- Información guardada en {output_file} ---\n")
