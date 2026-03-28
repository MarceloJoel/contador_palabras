# Programa para contar en un archivo de texto

#! Pedir al usuario la ruta de un archivo de texto
ruta = input("Ingrese la ruta del archivo de texto: ")

#Leer el contenido del archivo
with open(ruta, 'r') as archivo:
    contenido = archivo.read()

# Separar en palabras
palabras = contenido.split()
print(f"El archivo tiene {len(palabras)} palabras")

# Contar número total de palabras
total_palabras = len(palabras)
print(f"El archivo tiene {total_palabras} palabras")

