import os
import datetime


class GIFExtractor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.version = None
        self.image_size = None
        self.color_count = None
        # Tipo de compresión
        self.compression_type = "LZW"
        # Tipo de formato
        self.numeric_format = "little-endian"
        self.background_color = None
        self.image_count = 0
        self.creation_date = None
        self.modification_date = None
        self.comments = None

    # Método para obtener la información del GIF (recorrido de bits)
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

                # Cuenta la cantidad de imágenes en el GIF
                file.seek(10)
                while True:
                    block = file.read(1)
                    # Identificador de imagen
                    if block == b'\x2C':
                        self.image_count += 1
                    # Fin del archivo GIF
                    elif block == b'\x3B':
                        break
                    else:
                        file.seek(-1, 1)

                # Obtener las fechas de creación y modificación del archivo desde el sistema
                self.creation_date = datetime.datetime.fromtimestamp(os.path.getctime(self.file_path))
                self.modification_date = datetime.datetime.fromtimestamp(os.path.getmtime(self.file_path))

                # Si la versión es GIF89a, extraer comentarios
                if self.version == "GIF89a":
                    self.comments = self._extract_comments(file)

        except Exception as e:
            print(f"Error al leer el arhivo {self.file_path}: {e}")

    def _extract_comments(self, file):
        comments = []
        file.seek(10)
        while True:
            block_id = file.read(1)
            if block_id == b'\x21':
                extension_label = file.read(1)
                # Comentario
                if extension_label == b'\xFE':
                    comment_data = b""
                    while True:
                        sub_block_size = file.read(1)[0]
                        if sub_block_size == 0:
                            break
                        comment_data += file.read(sub_block_size)
                    comments.append(comment_data.decode('ascii', errors='ignore'))
                else:
                    file.seek(1, 1)
            # Fin del GIF
            elif block_id == b'\x3B':
                break
        return "\n".join(comments)

    def show_info(self):
        print(f"\nArchivo: {self.file_path}")
        print(f"Versión: {self.version}")
        print(f"Tamaño de imagen: {self.image_size}")
        print(f"Cantidad de colores: {self.color_count}")
        print(f"Color de fondo: {self.background_color}")
        print(f"Tipo de compresión: {self.compression_type}")
        print(f"Formato numérico: {self.numeric_format}")
        print(f"Cantidad de imágenes: {self.image_count}")
        print(f"Fecha de creación: {self.creation_date}")
        print(f"Fecha de modificación: {self.modification_date}")
        print(f"Comentarios: {self.comments if self.comments else 'N/A'}")
