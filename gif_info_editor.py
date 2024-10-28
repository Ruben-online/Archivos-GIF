class GIFInfoEditor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.gif_data = {}  # Almacenará la información de cada GIF

    # Cargar la información del archivo .txt
    def load_info(self):
        with open(self.file_path, 'r') as file:
            current_gif = None
            for line in file:
                line = line.strip()
                if line.startswith("--- Información del archivo:"):
                    current_gif = line.split(": ")[1]
                    self.gif_data[current_gif] = {}
                elif current_gif and ": " in line:
                    key, value = line.split(": ", 1)
                    self.gif_data[current_gif][key] = value

    # Editar un atributo de un GIF específico
    def edit_info(self, gif_name, attribute, new_value):
        if gif_name in self.gif_data:
            if attribute in self.gif_data[gif_name]:
                print(f"Modificando {attribute} de {gif_name}: '{self.gif_data[gif_name][attribute]}' a '{new_value}'")
                self.gif_data[gif_name][attribute] = new_value
            else:
                print(f"Atributo '{attribute}' no encontrado en {gif_name}.")
        else:
            print(f"GIF '{gif_name}' no encontrado en los datos cargados.")

    # Guardar cambios en el archivo .txt
    def save_changes(self):
        with open(self.file_path, 'w') as file:
            for gif_name, attributes in self.gif_data.items():
                file.write(f"--- Información del archivo: {gif_name} ---\n")
                for key, value in attributes.items():
                    file.write(f"{key}: {value}\n")
                file.write("\n------------------------------------------\n")
