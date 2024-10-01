class GIFExtractor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.version = None
        self.image_size = None
        self.color_count = None
        self.compression_type = None
        self.background_color = None
        self.image_count = None
        self.created_on = None

    def get_info(self):
        try:
            with open(self.file_path, 'rb') as file:
                # Primeros 6 bytes, obtiene la versión del GIF
                header = file.read(6)
                self.version = header.decode('ascii')

                # Obtiene el tamaño de la imagen
                width = int.from_bytes(file.read(2), 'little')
                height = int.from_bytes(file.read(2), 'little')
                self.image_size = (width, height)

                # Obtiene color de fondo y cantidad de colores
                packed_byte = file.read(1)[0]
                self.color_count = 2 ** ((packed_byte & 0b00000111) + 1)
                self.background_color = file.read(1)[0]

        except Exception as e:
            print(f"Error al leer el arhivo {self.file_path}: {e}")

    def show_info(self):
        print(f"Archivo: {self.file_path}")
        print(f"Versión: {self.version}")
        print(f"Tamaño de imagen: {self.image_size}")
        print(f"Cantidad de colores: {self.color_count}")
        print(f"Color de fondo: {self.background_color}")