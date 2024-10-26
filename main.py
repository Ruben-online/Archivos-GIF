from gif_manager import GIFManager


def main():
    directory = input("Ingrese la ruta de la carpeta con archivos GIF: ")

    gif_manager = GIFManager(directory)
    gif_manager.search_gif_files()

    if gif_manager.gif_files:
        print(f"\nSe encontró {len(gif_manager.gif_files)} archivos GIF")
        gif_manager.process_gif_files()
    else:
        print("No se encontró nigun archivo .gif")


if __name__ == "__main__":
    main()
