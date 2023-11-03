def ultima_aparicion(lista: list, numero: int) -> int:
    apariciones: int
    for i in range(0,len(lista),1):
        if lista[i] == numero:
            apariciones = i
    return apariciones
print(ultima_aparicion([-1, 4, 0, 4, 100, 0, 100, 0, -1, -1],-1))

def sacarRepetidos (lista:list) -> list:
    listaNueva: list = []
    for elemento in lista:
        if elemento not in listaNueva:
            listaNueva += [elemento]
    return listaNueva

def elementos_exclusivos(s: list, t: list) -> list:
    listaS: list = sacarRepetidos(s)
    listaT: list = sacarRepetidos(t)
    listaNueva: list = []
    for elemento in listaS:
        if elemento not in listaT:
            listaNueva.append(elemento)
    for elemento in listaT:
        if elemento not in listaS:
            listaNueva.append(elemento)
    return listaNueva
s = [-1, 4, 0, 4, 3, 0, 100, 0, -1, -1]
t = [0, 100, 5, 0, 100, -1, 5]
print(elementos_exclusivos(s,t))

def contar_traducciones_iguales(ingles: dict, aleman: dict) -> int:
    palabrasIguales: int = 0
    for clave1 in ingles:
        for clave2 in aleman:
            if clave1 == clave2 and ingles[clave1] == aleman[clave2]:
                palabrasIguales += 1
    return palabrasIguales

aleman = {"Mano": "Hand", "Pie": "Fuss", "Dedo": "Finger", "Cara": "Gesicht"}
inglés = {"Pie": "Foot", "Dedo": "Finger", "Mano": "Hand"}
print(contar_traducciones_iguales(inglés,aleman))

def convertir_a_diccionario(lista:list) -> dict:
    res: dict = {}
    for numero in lista:
        if numero in res: 
            res[numero] += 1 
        else:
            repeticiones = 1
            res[numero] = repeticiones
    return res
lista = [1,1,1,1,1,1,1,1,1,1]
print(convertir_a_diccionario(lista))
