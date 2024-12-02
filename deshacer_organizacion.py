import os
from shutil import move

def deshacer_organizacion(ruta):
    subcarpetas = [os.path.join(ruta, carpeta) for carpeta in os.listdir(ruta) if os.path.isdir(os.path.join(ruta, carpeta))]
    for subcarpeta in subcarpetas:
        archivos = os.listdir(subcarpeta)
        for archivo in archivos:
            ruta_archivo = os.path.join(subcarpeta, archivo)
            ruta_destino = os.path.join(ruta, archivo)
            try:
                move(ruta_archivo, ruta_destino)
                print(f"Archivo {archivo} movido de {subcarpeta} a {ruta}")
            except Exception as e:
                print(f"No se pudo mover {archivo}: {e}")

        # Eliminar subcarpeta vacía
        try:
            os.rmdir(subcarpeta)
            print(f"Subcarpeta {subcarpeta} eliminada")
        except Exception as e:
            print(f"No se pudo eliminar la carpeta {subcarpeta}: {e}")

if __name__ == "__main__":
    ruta_principal = input("Introduce la ruta de la carpeta principal donde organizaron los archivos: ").strip()
    if os.path.exists(ruta_principal):
        deshacer_organizacion(ruta_principal)
    else:
        print("La ruta especificada no existe.")
