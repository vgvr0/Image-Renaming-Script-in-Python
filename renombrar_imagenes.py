import os

def renombrar_imagenes(directorio):
    contador = 1
    for nombre_archivo in os.listdir(directorio):
        if nombre_archivo.endswith(".jpg") or nombre_archivo.endswith(".png"):  # Filtrar por tipos de archivo deseados
            extension = nombre_archivo.split(".")[-1]
            nuevo_nombre = f"imagen_{contador}.{extension}"
            ruta_actual = os.path.join(directorio, nombre_archivo)
            ruta_nueva = os.path.join(directorio, nuevo_nombre)
            os.rename(ruta_actual, ruta_nueva)
            contador += 1

# Ejemplo de uso
directorio = "/ruta/al/directorio"  # Ruta al directorio donde se encuentran las imágenes
renombrar_imagenes(directorio)
