import os
import sys
from shutil import move, Error
from argparse import ArgumentParser
try:
    from colorama import init
except ModuleNotFoundError:
    """
    Si el modulo colorama no esta instalado, se instalara a continuacion:
    """
    from os import system
    print("[!] Al parecer usted no tiene colorama instalado, ahora se lo instalaremos")
    print("[!] Mediante un \"pip install colorama\"")
    system("pip install colorama")
    from colorama import init


init()  # iniciamos colorama


class COLOR:
    def __init__(self):
        self.BLACK = "\033[30m"
        self.RED = "\033[31m"
        self.GREEN = "\033[32m"
        self.YELLOW = "\033[33m"
        self.BLUE = "\033[34m"
        self.MAGENTA = "\033[35m"
        self.CYAN = "\033[36m"
        self.WHITE = "\033[37m"
        self.RESET = "\033[39m"

        self.LIGHTBLACK_EX = "\033[90m"
        self.LIGHTRED_EX = "\033[91m"
        self.LIGHTGREEN_EX = "\033[92m"
        self.LIGHTYELLOW_EX = "\033[93m"
        self.LIGHTBLUE_EX = "\033[94m"
        self.LIGHTMAGENTA_EX = "\033[95m"
        self.LIGHTCYAN_EX = "\033[96m"
        self.LIGHTWHITE_EX = "\033[97m"

    def UP(self, n=1):
        return '\033[' + str(n) + 'A'

    def DOWN(self, n=1):
        return '\033[' + str(n) + 'B'

    def FORWARD(self, n=1):
        return '\033[' + str(n) + 'C'

    def BACK(self, n=1):
        return '\033[' + str(n) + 'D'

    def POS(self, x=1, y=1):
        return '\033[' + str(y) + ';' + str(x) + 'H'

    def SET_TITLE(self, text):
        return "\033]2;{}\007".format(text)

    def CLEAR(self):
        return "\033[3J\033[H\033[2J"

    def POINTGREEN(self, text1="", text2=""):
        return self.LIGHTGREEN_EX + "[" + self.BLUE + "*" + self.LIGHTGREEN_EX + "] " + self.LIGHTWHITE_EX + text1 + text2 + self.LIGHTWHITE_EX

    def POINTRED(self, text=""):
        return self.LIGHTYELLOW_EX + "[" + self.RED + "*" + self.LIGHTYELLOW_EX + "] " + self.LIGHTMAGENTA_EX + text + "\n" + self.LIGHTWHITE_EX


def crear_carpetas_si_no_existe(carpetas, ruta):
    for carpeta in carpetas:
        ruta_carpeta = os.path.join(ruta, carpeta)
        if not os.path.exists(ruta_carpeta):
            os.mkdir(ruta_carpeta)


def mover_archivos(ruta_origen, ruta_destino):
    try:
        move(ruta_origen, ruta_destino)
    except Error as e:
        print(COLOR().POINTRED("No se pudo mover el archivo: " + ruta_origen))


def organizar_archivos(ruta):
    print(COLOR().POINTGREEN("Organizando archivos en la carpeta: ", ruta))
    carpetas = ["Documentos/", "Imagenes/", "Videos/", "Musica/", "Comprimidos/", "Programas/", "Archivos3D/", "Otros/"]
    crear_carpetas_si_no_existe(carpetas, ruta)

    archivos = [arch for arch in os.listdir(ruta) if os.path.isfile(os.path.join(ruta, arch))]
    for archivo in archivos:
        extension = archivo.split(".")[-1].lower()
        if extension in ["txt", "doc", "docx", "pdf", "xlsx"]:
            mover_archivos(os.path.join(ruta, archivo), os.path.join(ruta, carpetas[0], archivo))
        elif extension in ["png", "jpg", "jpeg", "gif", "bmp"]:
            mover_archivos(os.path.join(ruta, archivo), os.path.join(ruta, carpetas[1], archivo))
        elif extension in ["mp4", "avi", "mkv", "mov", "flv"]:
            mover_archivos(os.path.join(ruta, archivo), os.path.join(ruta, carpetas[2], archivo))
        elif extension in ["mp3", "wav", "flac"]:
            mover_archivos(os.path.join(ruta, archivo), os.path.join(ruta, carpetas[3], archivo))
        elif extension in ["zip", "rar", "7z"]:
            mover_archivos(os.path.join(ruta, archivo), os.path.join(ruta, carpetas[4], archivo))
        elif extension in ["exe", "msi"]:
            mover_archivos(os.path.join(ruta, archivo), os.path.join(ruta, carpetas[5], archivo))
        elif extension in ["stl", "obj", "fbx", "prusaslicer", "svg", "gcode", "3mf", "amf", "3ds", "blend", "dae", "dxf", "ifc", "lwo", "lws", "lxo", "ma", "md2", "md3", "md5anim", "md5camera", "md5mesh", "mmd", "ms3d", "ply", "x", "x3d", "xgl", "xml", "ogex", "fbx", "glb", "gltf", "3d", "3ds", "3mf", "ac", "ac3d", "acc", "amf", "ase", "ask", "b3d", "blend", "bvh", "cob", "csm", "dae", "dxf", "enff", "fbx", "glb", "gltf", "hmp", "ifc", "ifczip", "irr", "irrmesh", "lwo", "lws", "lxo", "md2", "md3", "md5anim", "md5camera", "md5mesh", "mdc", "mdl", "mesh", "mesh.xml", "mot", "ms3d", "ndo", "nff", "obj", "off", "ogex", "pk3", "ply", "pmx", "prj", "q3o", "q3s", "raw", "scn", "sib", "smd", "stl", "stp", "ter", "uc", "vta", "x", "x3d", "xgl", "xml", "zgl"]:
            mover_archivos(os.path.join(ruta, archivo), os.path.join(ruta, carpetas[6], archivo))
        else:
            mover_archivos(os.path.join(ruta, archivo), os.path.join(ruta, carpetas[7], archivo))
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
