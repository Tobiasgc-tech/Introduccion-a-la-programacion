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

