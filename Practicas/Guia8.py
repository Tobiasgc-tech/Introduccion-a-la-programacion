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
    for linea in range(len(lineas)-1,-1,-1):
        reverso.write(lineas[linea])
    archivo.close()
    reverso.close()
#reverso("Prueba.txt") 

#Ejercicio4
def insertarFrase (nombre_archivo:str, frase:str):
    archivo = open(nombre_archivo,"a")
    archivo.write(frase)
    archivo.close()
#insertarFrase("Prueba.txt","\nESTO ES LA PRUEBA")

#Ejercicio5
def insertarAlPrincipio (nombre_archivo:str, frase:str):
    archivo_viejo = open(nombre_archivo,"r")
    contenido_anterior = archivo_viejo.read()
    archivo = open(nombre_archivo,"w")
    archivo.write(frase)
    archivo.write(contenido_anterior)
    archivo.close()
    archivo_viejo.close()
#insertarAlPrincipio ("Prueba.txt","Esta es una nueva linea al principio.\n")

#Ejercicio7
def promedioEstudiante(lu:str) -> float:
    total_notas: float = 0
    cantidad_notas: float = 0
    archivo = open("Prueba.txt","r")
    for linea in archivo:
        elementos = linea.strip().split(",")
        if elementos[0] == lu:
            nota = float(elementos[3])
            total_notas += nota
            cantidad_notas += 1
    promedio: float = total_notas / cantidad_notas
    archivo.close()
    return promedio
#print(promedioEstudiante("12345"))

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
#Ejercio16
def armarSecuenciaBingo () -> Cola:
    numeros: list = list(range(1,100))
    random.shuffle(numeros)
    c: Cola = Cola()
    for numero in numeros:
        c.put(numero)
    return c
#armarSecuenciaBingo()

def jugarCartonBingo (carton:list,bolillero:Cola) -> int:
    res: int = 0
    contador: int = 0
    caux: Cola = Cola()
    print(list(bolillero.queue))
    while not bolillero.empty():
        elem = bolillero.get()
        caux.put(elem)
        if elem in carton:
            contador += 1
            res += 1
        else:
            res += 1
        if contador >= 12:
            break
    while not caux.empty():
        elem = caux.get()
        bolillero.put(elem)
    print(list(bolillero.queue))
    return res

#print(jugarCartonBingo([1,2,3,4,5,6,7,8,9,77,11,12],armarSecuenciaBingo()))

def n_pacientes_urgentes(c:Cola) -> int:
    res: int = 0
    caux: Cola = Cola()
    while not c.empty():
        elem = c.get()
        caux.put(elem)
        if 1 <= elem[0] <=3:
            res += 1
    while not caux.empty():
        elem1 = caux.get()
        c.put(elem1)
    #print(list(c.queue))    
    return res
"""
cola = Cola()
cola.put((1,"Tobias","Tra"))
cola.put((10,"Tobias","Tra"))
cola.put((3,"Tobias","Tra"))
cola.put((2,"Tobias","Tra"))
cola.put((7,"Tobias","Tra"))
cola.put((7,"Tobias","Tra"))
cola.put((2,"Tobias","Tra"))
cola.put((3,"Tobias","Tra"))
cola.put((5,"Tobias","Tra"))
print(list(cola.queue)) 
print(n_pacientes_urgentes(cola))
"""
def clientes(cola:Cola) -> Cola:
    clientesMas65: Cola = Cola()
    clientesPrefe: Cola = Cola()
    clientesComunes: Cola = Cola()
    clientesOrdenados: Cola = Cola()
    colaaux: Cola = Cola()
    while not cola.empty():
        cliente = cola.get()
        if cliente[3] == True:
            clientesMas65.put(cliente)
        elif cliente[2] == True:
            clientesPrefe.put(cliente)
        else:
            clientesComunes.put(cliente)
        colaaux.put(cliente)
    while not clientesMas65.empty():
        cliente = clientesMas65.get()
        clientesOrdenados.put(cliente)
    while not clientesPrefe.empty():
        cliente = clientesPrefe.get()
        clientesOrdenados.put(cliente)
    while not clientesComunes.empty():
        cliente = clientesComunes.get()
        clientesOrdenados.put(cliente)
    while not colaaux.empty():
        cliente = colaaux.get()
        cola.put(cliente)
    #print(list(cola.queue))
    return clientesOrdenados
"""
cola = Cola()
cola.put(("Tobias Cogliano",6,False,False))
cola.put(("Tobias Cogliano",4,True,False))
cola.put(("Tobias Cogliano",1,False,True))
cola.put(("Tobias Cogliano",2,True,True))
cola.put(("Tobias Cogliano",5,True,False))
cola.put(("Tobias Cogliano",7,False,False))
cola.put(("Tobias Cogliano",3,False,True))
cola.put(("Tobias Cogliano",8,False,False))
print(list(cola.queue))
clientes(cola)
"""
#Ejercicio19
def agruparPorLongitud(nombre_archivo:str) -> dict:
    archivo = open(nombre_archivo,"r")
    d: dict = {}
    for linea in archivo.readlines():
        palabras = linea.split()
        for palabra in palabras:
            clave = len(palabra)
            if clave in d:
                d[clave] += 1
            else:
                d[clave] = 1
    archivo.close()
    return d
#print(agruparPorLongitud("Prueba.txt"))

#Ejercicio20
def promedioEstudianteDiccionario(lu:str) -> dict:
    total_notas: float = 0
    cantidad_notas: float = 0
    archivo = open("Prueba.txt","r")
    alumno: dict = {}
    for linea in archivo:
        elementos = linea.strip().split(",")
        if elementos[0] == lu:
            nota = float(elementos[3])
            total_notas += nota
            cantidad_notas += 1
            promedio: float = total_notas / cantidad_notas
            alumno[elementos[0]] = promedio
    archivo.close()
    return alumno
#print(promedioEstudianteDiccionario("12345"))

#Ejercicico21
def laPalabraMasFrecuente(nombre_archivo:str) -> str:
    archivo = open(nombre_archivo,"r")
    d: dict = {}
    valor_maximo = None
    clave_maxima = None
    for linea in archivo.readlines():
        palabras = linea.split()
        for palabra in palabras:
            if palabra in d:
                d[palabra] += 1
            else:
                d[palabra] = 1
    for clave, valor in d.items():
        if valor_maximo is None or valor > valor_maximo:
            valor_maximo = valor
            clave_maxima = clave
    return clave_maxima
#print(laPalabraMasFrecuente("Prueba.txt"))

#Ejercicio22
historiales: dict = {}
def visitar_sitio(historiales: dict, usuario:str, sitio:str):
    if usuario in historiales:
        historial_usario = historiales[usuario]
    else:
        historial_usario: Pila = Pila()
        historiales[usuario] = historial_usario
    historial_usario.put(sitio)
"""
visitar_sitio(historiales, "usuario1", "sitio1")
visitar_sitio(historiales, "usuario1", "sitio2")
visitar_sitio(historiales, "usuario2", "sitio3")
print("Historial del usuario1:", list(historiales["usuario1"].queue))
print("Historial del usuario2:", list(historiales["usuario2"].queue))
"""
