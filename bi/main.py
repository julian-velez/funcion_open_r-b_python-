with open("image.png", "r+b") as archivo:
    print(">>> Archivo abierto correctamente.")

    # Leer los primeros 16 bytes del archivo
    archivo.seek(0)
    datos = archivo.read(16)
    print("Primeros bytes reales:", datos)

