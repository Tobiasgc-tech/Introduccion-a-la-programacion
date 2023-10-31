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
import random
def generar_nros_al_azar(cantidad:int,desde:int,hasta:int) -> Pila:
    p: Pila = Pila()
    while cantidad > 0:
        cantidad -= 1
        numero: int = random.randint(desde,hasta)
        p.put(numero)
    print(list(p.queue))
    return p
#generar_nros_al_azar(10,0,10)

#Ejercio9
def cantidadElementos(p:Pila)-> int:
    res: int=0
    paux: Pila=Pila()
    while not p.empty():
        elem = p.get()
        paux.put(elem)
        res += 1
    print(list(paux.queue))
    while not paux.empty():
        elem = paux.get()
        p.put(elem)
    print(list(p.queue))
    return res
"""""
p = Pila()
p.put(1)
p.put(2)
p.put(3)
p.put(4)
cantidad = cantidadElementos(p)
print("Cantidad de elementos en la pila:", cantidad)
print(list(p.queue))
"""
#Ejercio10
def buscar_el_maximo(p:Pila) -> int:
    res: int = 0
    paux: Pila = Pila()
    lista: list = []
    while not p.empty():
        elem = p.get()
        paux.put(elem)
        lista.append(elem)
    while not paux.empty():
        elem=paux.get()
        p.put(elem)
    for i in lista:
        if i >= res:
            res = i
    return res
"""      
p = Pila()
p.put(1)
p.put(1000)
p.put(5)
p.put(4)
cantidad = buscar_el_maximo(p)
print(cantidad)
"""
#Ejercio11
def esta_bien_balanceada(operacion:str) -> bool:
    p: Pila = Pila()
    for caracter in operacion:
        if caracter == "(":
            p.put(caracter)
        elif caracter == ")":
            if not p.empty():
                p.get()
            else:    
                return False         
    return p.empty()
""""
formula = "1 + 2 x 3 = (20 / 5))"
resultado = esta_bien_balanceada(formula)
print(resultado)
"""
#Ejercicio12
def es_numero(cadena: str) -> bool:
    try:
        float(cadena)
        return True
    except ValueError:
        return False

def polacaInversa (expresion:str) -> float:
    tokens = []
    token_actual = ""
    for caracter in expresion:
        if caracter != " ":
            token_actual += caracter
        elif token_actual:
            tokens.append(token_actual)
            token_actual = ""
    if token_actual:
        tokens.append(token_actual)
    print(tokens)
    operando: Pila = Pila()
    for i in tokens:
        a: float
        b: float
        if es_numero(i):
            operando.put(float(i))
        elif i == "+":
            a = int(operando.get())
            b = int(operando.get())
            operando.put(b+a)
        elif i == "-":
            a = int(operando.get())
            b = int(operando.get())
            operando.put(b-a)
        elif i == "*":
            a = int(operando.get())
            b = int(operando.get())
            operando.put(b*a)
        elif i == "/":
            a = int(operando.get())
            b = int(operando.get())
            operando.put(b/a)
    print(list(operando.queue))
    return operando
#polacaInversa("3 4 + 5 * 2 -")

#Ejercicio13
from queue import Queue as Cola

def generar_nros_al_azar1 (cantidad:int,desde:int,hasta:int) -> Cola:
    c = Cola()
    while cantidad > 0:
        cantidad -= 1
        numero: int = random.randint(desde,hasta)
        c.put(numero)
    print(list(c.queue))
    return c
#generar_nros_al_azar(10,0,10)

#Ejercicio14
def cantidad_elementos (c:Cola) -> int:
    res:int = 0
    caux: Cola = Cola()
    while not c.empty():
        elem = c.get()
        caux.put(elem)
        res += 1
    print(list(caux.queue))
    while not caux.empty():
        elem = caux.get()
        c.put(elem)
    print(list(c.queue))
    return res
"""
c = Cola()
c.put(1)
c.put(2)
c.put(3)
c.put(4)
cantidad = cantidadElementos(c)
print("Cantidad de elementos en la cola:", cantidad)
print(list(c.queue))
"""