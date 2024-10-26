from gif_manager import GIFManager


def main():
    directory = input("Ingrese la ruta de la carpeta con archivos GIF: ")
    output_file = "GIF's.txt"

    gif_manager = GIFManager(directory)
    gif_manager.search_gif_files()

    if gif_manager.gif_files:
        print(f"Se encontraron {len(gif_manager.gif_files)} archivos GIF.")
        gif_manager.process_gif_files(output_file)
        print(f"Información de los archivos GIF guardada en {output_file}.")
    else:
        print("No se encontraron archivos GIF.")


if __name__ == "__main__":
    main()
