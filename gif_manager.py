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
                    self.gif_files.append(os.path.join(root, file))

    def process_gif_files(self):
        for gif_file in self.gif_files:
            extractor = GIFExtractor(gif_file)
            extractor.get_info()
            extractor.show_info()
