#Ejercicio1.1
def contar_lineas(nombre_archivo : str) -> int:
    archivo = open(nombre_archivo, "r")
    lineas = archivo.readlines()
    archivo.close()
    return len(lineas)

#print(contar_lineas("Prueba.txt"))

#Ejercicio1.2
def existe_palabra(palabra: str, nombre_archivo: str) -> bool:
    archivo = open(nombre_archivo, "r")
    texto = archivo.read()
    archivo.close()
    return palabra in texto
        
#print(existe_palabra("Hola","Prueba.txt"))

#Ejercicio1.3
def cantidad_apariciones(nombre_archivo:str,palabra:str) -> int:
    archivo = open(nombre_archivo,"r")
    contenido = archivo.read()
    contador = contenido.count(palabra)
    archivo.close()
    return contador
print(cantidad_apariciones("Prueba.txt","Hola"))