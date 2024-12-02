import os
from shutil import move, Error
from argparse import ArgumentParser
try:
    from colorama import init
except ModuleNotFoundError:
    from os import system
    print("[!] Instalando colorama...")
    system("pip install colorama")
    from colorama import init

init()  # Inicia colorama para los colores en consola


class COLOR:
    def __init__(self):
        self.GREEN = "\033[32m"
        self.BLUE = "\033[34m"
        self.RED = "\033[31m"
        self.WHITE = "\033[37m"
        self.RESET = "\033[39m"

    def POINTGREEN(self, text1="", text2=""):
        return self.GREEN + "[" + self.BLUE + "*" + self.GREEN + "] " + self.WHITE + text1 + text2 + self.WHITE

    def POINTRED(self, text=""):
        return self.RED + "[!] " + text + self.RESET


def crear_carpetas_si_no_existe(carpetas, ruta):
    """Crea las carpetas necesarias si no existen"""
    for carpeta in carpetas:
        ruta_carpeta = os.path.join(ruta, carpeta)
        if not os.path.exists(ruta_carpeta):
            os.mkdir(ruta_carpeta)


def mover_archivos(ruta_origen, ruta_destino):
    """Mueve un archivo de una ruta a otra"""
    try:
        move(ruta_origen, ruta_destino)
        print(f"Archivo movido: {os.path.basename(ruta_origen)} → {ruta_destino}")
    except Error as e:
        print(COLOR().POINTRED(f"No se pudo mover el archivo: {ruta_origen}"))


def organizar_archivos(ruta):
    print(COLOR().POINTGREEN("Organizando archivos en la carpeta: ", ruta))

    # Definición de carpetas
    carpetas = [
        "Clases curso/",
        "Notebooks/",
        "Python/",
        "Data/",
        "Documentos/",
        "Imagenes/",
        "Videos/",
        "Musica/",
        "Comprimidos/",
        "Programas/",
        "Otros/"
    ]
    crear_carpetas_si_no_existe(carpetas, ruta)

    # Archivos en la carpeta
    archivos = [arch for arch in os.listdir(ruta) if os.path.isfile(os.path.join(ruta, arch))]
    for archivo in archivos:
        ruta_archivo = os.path.join(ruta, archivo)
        extension = archivo.split(".")[-1].lower()

        # Archivos que contienen "clase" en el nombre
        if "clase" in archivo.lower():
            mover_archivos(ruta_archivo, os.path.join(ruta, "Clases curso/", archivo))

        # Notebooks de Jupyter
        elif extension == "ipynb":
            mover_archivos(ruta_archivo, os.path.join(ruta, "Notebooks/", archivo))

        # Archivos de Python
        elif extension == "py":
            mover_archivos(ruta_archivo, os.path.join(ruta, "Python/", archivo))

        # Archivos relacionados con datos o valores
        elif extension in ["xlsx", "xls", "csv", "json"] or "valores" in archivo.lower() or "data" in archivo.lower():
            mover_archivos(ruta_archivo, os.path.join(ruta, "Data/", archivo))

        # Documentos generales
        elif extension in ["txt", "doc", "docx", "pdf"]:
            mover_archivos(ruta_archivo, os.path.join(ruta, "Documentos/", archivo))

        # Imágenes
        elif extension in ["png", "jpg", "jpeg", "gif", "bmp"]:
            mover_archivos(ruta_archivo, os.path.join(ruta, "Imagenes/", archivo))

        # Videos
        elif extension in ["mp4", "avi", "mkv", "mov", "flv"]:
            mover_archivos(ruta_archivo, os.path.join(ruta, "Videos/", archivo))

        # Música
        elif extension in ["mp3", "wav", "flac"]:
            mover_archivos(ruta_archivo, os.path.join(ruta, "Musica/", archivo))

        # Archivos comprimidos
        elif extension in ["zip", "rar", "7z"]:
            mover_archivos(ruta_archivo, os.path.join(ruta, "Comprimidos/", archivo))

        # Programas
        elif extension in ["exe", "msi"]:
            mover_archivos(ruta_archivo, os.path.join(ruta, "Programas/", archivo))

        # Otros archivos
        else:
            mover_archivos(ruta_archivo, os.path.join(ruta, "Otros/", archivo))

    print(COLOR().POINTGREEN("Archivos organizados correctamente."))


def main():
    parser = ArgumentParser(description="Organizar archivos en carpetas según su extensión.")
    parser.add_argument("-r", "--ruta", type=str, help="Ruta de la carpeta a organizar.")
    args = parser.parse_args()

    if args.ruta:
        ruta = os.path.abspath(args.ruta)
        organizar_archivos(ruta)
    else:
        print(COLOR().POINTRED("Debe especificar la ruta de la carpeta a organizar."))


if __name__ == "__main__":
    main()
