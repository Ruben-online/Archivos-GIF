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
                print(f"--- Leyendo archivo: {self.file_path} ---")

                # Leer los primeros 6 bytes para obtener la versión
                header = file.read(6)
                self.version = header.decode('ascii')

                # Tamaño de la imagen
                width = int.from_bytes(file.read(2), 'little')
                height = int.from_bytes(file.read(2), 'little')
                self.image_size = (width, height)

                # Color de fondo y cantidad de colores
                packed_byte = file.read(1)[0]
                self.color_count = 2 ** ((packed_byte & 0b00000111) + 1)
                self.background_color = file.read(1)[0]

                # Contar imágenes (frames) en el archivo GIF
                while True:
                    block = file.read(1)
                    if not block:  # Verificar fin del archivo
                        break
                    elif block == b'\x2C':  # Identificador de imagen (frame)
                        self.image_count += 1

                        # Saltar al siguiente bloque de datos (tamaño desconocido)
                        file.seek(9, 1)  # Saltar datos del frame por ejemplo

                    elif block == b'\x3B':  # Fin del archivo GIF
                        break
                    else:
                        # Bloque irrelevante - leer el tamaño y saltarlo
                        block_size = file.read(1)[0]
                        file.seek(block_size, 1)

                # Obtener fechas de creación y modificación del archivo desde el sistema
                self.creation_date = datetime.datetime.fromtimestamp(os.path.getctime(self.file_path))
                self.modification_date = datetime.datetime.fromtimestamp(os.path.getmtime(self.file_path))

                # Extraer comentarios si es GIF89a
                if self.version == "GIF89a":
                    self.comments = self._extract_comments(file)

        except Exception as e:
            print(f"Error al leer el archivo {self.file_path}: {e}")

    def _extract_comments(self, file):
        comments = []
        file.seek(10)
        while True:
            block_id = file.read(1)
            if block_id == b'\x21':  # Extension introducer
                extension_label = file.read(1)
                if extension_label == b'\xFE':  # Comment Label
                    comment_data = b""
                    while True:
                        sub_block_size = file.read(1)[0]
                        if sub_block_size == 0:
                            break
                        comment_data += file.read(sub_block_size)
                    comments.append(comment_data.decode('ascii', errors='ignore'))
                else:
                    # Saltar a la siguiente sección si no es un bloque de comentario
                    file.seek(1, 1)
            elif block_id == b'\x3B':  # Fin del archivo GIF
                break
        return "\n".join(comments) if comments else "Sin comentarios"

    def show_info(self):
        print(f"\nVersión: {self.version}")
        print(f"Tamaño de imagen: {self.image_size}")
        print(f"Cantidad de colores: {self.color_count}")
        print(f"Color de fondo: {self.background_color}")
        print(f"Tipo de compresión: {self.compression_type}")
        print(f"Formato numérico: {self.numeric_format}")
        print(f"Cantidad de imágenes: {self.image_count}")
        print(f"Fecha de creación: {self.creation_date}")
        print(f"Fecha de modificación: {self.modification_date}")
        print(f"Comentarios: {self.comments if self.comments else 'N/A'}")

        # Guardar la información en un archivo .txt
    def save_to_file(self, output_file):
        with open(output_file, 'a') as file:
            file.write(f"\n--- Información del archivo: {self.file_path} ---\n")
            file.write(f"Versión: {self.version}\n")
            file.write(f"Tamaño de imagen: {self.image_size}\n")
            file.write(f"Cantidad de colores: {self.color_count}\n")
            file.write(f"Color de fondo: {self.background_color}\n")
            file.write(f"Tipo de compresión: {self.compression_type}\n")
            file.write(f"Formato numérico: {self.numeric_format}\n")
            file.write(f"Cantidad de imágenes: {self.image_count}\n")
            file.write(f"Fecha de creación: {self.creation_date}\n")
            file.write(f"Fecha de modificación: {self.modification_date}\n")
            file.write(f"Comentarios: {self.comments if self.comments else 'N/A'}\n")
            file.write("\n------------------------------------------\n")
