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
#print(cantidad_apariciones("Prueba.txt","Hola"))

#Ejercicio2
def clonar_sin_comentarios(nombre_archivo:str):
    archivo = open(nombre_archivo,"r")
    archivo_sin_comen = open("clonadoSinComentarios.py","w")
    lineas = archivo.readlines()
    for linea in lineas:
        if not linea.strip()[0] == "#":
            archivo_sin_comen.write(linea)
    archivo.close()
    archivo_sin_comen.close()
#clonar_sin_comentarios("ejemploComentario.py")

#Ejercicio3
def reverso(nombre_archivo:str):
    archivo = open(nombre_archivo,"r")
    reverso = open ("reverso.txt","w")
    lineas = archivo.readlines()
    for linea in lineas:
        reverso.insert(0,linea)
    archivo.close()
    reverso.close()
#reverso("Prueba.txt") 

#Ejercicio8
from queue import LifoQueue as Pila
p = Pila ()
p . put (1) # apilar
elemento = p . get () # desapilar
p . empty () # vacia ?
def generar_nros_al_azar(cantidad:int,desde:int,hasta:int) -> Pila:
    resultado: Pila = Pila()
    while cantidad < 0:
        numero = random.randint(desde,hasta)
        resultado.put(numero)
        cantindad - 1
    return resultado

print(generar_nros_al_azar(10,0,10))