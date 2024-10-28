from gif_manager import GIFManager
from gif_info_editor import GIFInfoEditor


def main():
    # Procesa y guardar la información de los GIFs
    directory = input("Ingrese la ruta de la carpeta con archivos GIF: ")
    output_file = "GIF_info.txt"

    gif_manager = GIFManager(directory)
    gif_manager.search_gif_files()

    if gif_manager.gif_files:
        print(f"Se encontraron {len(gif_manager.gif_files)} archivos GIF.")
        gif_manager.process_gif_files(output_file)
        print(f"Información de los archivos GIF guardada en {output_file}.")
    else:
        print("No se encontraron archivos GIF.")
        return

    # Carga la información y lista los GIFs para editarlos
    editor = GIFInfoEditor(output_file)
    editor.load_info()

    while True:
        editar = input("¿Desea editar la información en el archivo .txt? (s/n): ").strip().lower()
        if editar == 's':
            # Mostrar la lista de GIFs disponibles para editar
            print("\nGIFs disponibles para editar:")
            gifs = list(editor.gif_data.keys())
            for idx, gif_name in enumerate(gifs, 1):
                print(f"{idx}. {gif_name}")

            # Seleccionar GIF por número
            try:
                choice = int(input("Seleccione el número del GIF que desea modificar: ")) - 1
                if choice < 0 or choice >= len(gifs):
                    print("Número inválido, intenta de nuevo.")
                    continue
                gif_name = gifs[choice]
            except ValueError:
                print("Entrada inválida, ingrese un número.")
                continue

            # Seleccionar atributo y nuevo valor
            attribute = input("Ingrese el atributo que desea modificar (por ejemplo, 'Cantidad de colores'): ")
            new_value = input(f"Ingrese el nuevo valor para '{attribute}': ")

            # Realizar la modificación y guardar los cambios
            editor.edit_info(gif_name, attribute, new_value)
            editor.save_changes()
            print("Los cambios se han guardado en el archivo .txt.")

        elif editar == 'n':
            print("No se realizaron cambios en el archivo .txt.")
            break
        else:
            print("Opción no válida. Ingrese 's' para sí o 'n' para no.")


if __name__ == "__main__":
    main()
