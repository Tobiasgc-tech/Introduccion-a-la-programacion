#Ejercio1.1
def pertenece (s:[int],numero:int) -> bool:
    indice: int=0
    while indice < len(s):
        if s[indice] == numero:
            return True
        indice += 1
    return False

def pertenece2 (s:[int],numero:int) -> bool:
    for i in range (0,len(s),1):
        if numero == s[i]:
            return True
    return False

#Ejercio1.2
def divideATodos (s:[int],numero:int) -> bool:
    indice: int=0
    while indice < len(s):
       if s[indice] % numero != 0:
           return False
       indice += 1
    return True

#Ejercio1.3
def sumaTotal (s: [int]) -> int:
    total: int=0
    indice: int=0
    while indice < len(s):
        total +=[indice]
        indice += 1
    return total

def sumaTotal2 (s: [int]) -> int:
    total:int = 0
    for elemento in s:
        total=total+elemento
    return total

#Ejercicios1.4
def ordenados (s: [int]) -> bool:
    for i in range (0,(len(s)-1),1):
        if s[i] >= s[i+1]:
            return False
    return True

#Ejercio1.5
def palabrasMayorA7 (s:[str]) -> bool:
    for palabra in s:
        if len(palabra) > 7:
            return True
    return False 

#Ejercio1.7
def hayMinuscula(contra:str) -> bool:
    for letra in contra:
        if "a" <= letra <= "z":
            return True
    return False

def hayMayuscula(contra:str) -> bool:
    for letra in contra:
        if "A" <= contra <= "Z":
            return True
    return False

def hayDigitos(contra:str) -> bool:
    for letra in contra:
        if "0" <= letra <= "9":
            return True
    return False

def contraseña (contra:str) -> str:
    if len(contra) < 5:
        return "ROJA"
    if len(contra) > 8:
        if hayMinuscula(contra) and hayMayuscula(contra) and hayDigitos(contra):
            return "VERDE"
    return "AMARILLA"

#Ejercio1.8
def banco (movimentos:[(chr,int)]) -> int:
    saldo: int = 0
    for i in range (0,len(movimentos),1):
        if movimentos[i][0] == "I":
            saldo += movimentos[i][1]
        elif movimentos[i][0] == "R":
            saldo -= movimentos[i][1]
    return saldo

def vocales (palabra:str) -> bool:
     a: bool
     e: bool
     i: bool
     o: bool
     u: bool
     for letra in palabra:
        if letra in "a":
            a = True
        elif letra in "b":
            b = True
        elif letra in "i":
            i = True
        elif letra in "o":
            o = True
        elif letra in "u":
            u = True     

#Ejercio2.1
def ejercio2_1 (s:[int]) -> None:
    for i in range (0,len(s),2):
        s[i] = 0

#Ejercio2.2
def ejercio2_2 (s:[int]) -> [int]:
    x: list = s.copy()
    for i in range (0,len(x),2):
        x[i] = 0

#Ejercicio2.3
def eliminarVocales (palabra:str) -> str:
    palabranueva = ""
    for letra in palabra:
        if letra not in  "aeiouAEIOU":
            palabranueva += letra
    return palabranueva

#Ejercicio2.4
def reemplazarVocales (palabra:str) -> str:
    palabranueva: str = ""
    for letra in palabra:
        if letra in "aeiou":
            palabranueva += " "
        else:
            palabranueva += letra
    return palabranueva

#Ejercicio2.5
def daVueltaStr (palabra:str) -> str:
    palabranueva: str = ""
    for i in range (len(palabra)-1,-1,-1):
        palabranueva += palabra[i]
    return palabranueva

#Ejercicio2.6
def eliminarRepetidos (palabra:str) -> str:
    palabranueva: str = ""
    for letra in palabra:
        if letra not in palabranueva:
            palabranueva += letra
    return palabranueva

#Ejercicio3
def aprobado (notas:[int]) -> int:
    sumanotas: int = 0
    for i in range (0,len(notas),1):
        if notas[i] in (1,2,3):
            return 3
        else:
            sumanotas += notas[i]
    if sumanotas/len(notas) >= 7:
        return 1
    else:
        return 2
    
#Ejercicio4.1
def estudiantes () -> [str]:
    listadenombres: list = []
    nombre: str
    while True:
        nombre = input ("Ingresa un nombre de estudiante (o 'listo' para terminar): ")
        if nombre != "listo": 
            listadenombres.append(nombre)
        else:
            break
    print("Los nombres que ingresó son: " + ", ".join(listadenombres))
    return listadenombres
#estudiantes()

#Ejercicio4.2
def movimientos () -> [(chr,int)]:
    monto: int = 0
    montototal: int = 0
    operacion: chr
    historial: [(chr,int)] = []
    while True:
        operacion = input ("Ingrese:\n'C' para cargar monto\n'D' para descontar monto\n'X' para finalizar\n ")
        if operacion == "C":
            monto = int(input ("¿Que monto quiere ingresar? "))
            historial.append((operacion,monto))
            montototal += monto
        elif operacion == "D":
            monto = int(input ("¿Que monto quiere descontar? "))
            historial.append((operacion,monto))
            montototal -= monto
        elif operacion == "X":
            break
    print (historial)
    print ("Su monto total es de " + str(montototal))
    return historial
#movimientos()

import random

def jugar_siete_y_medio() -> None:
    historial: [int] = []
    total: float = 0
    mazo: [int] = [1,2,3,4,5,6,7,10,11,12]
    decision: str
    while True:
        carta = random.choice(mazo)
        historial.append(carta)
        if carta == 10 or carta == 11 or carta == 12:
            total += 0.5
        else:
            total += carta
        print("Su carta es " + str(carta))
        print("Sus puntos son: " + str(total))
        if total > 7.5:
            print("Te pasaste de 7.5. ¡Has perdido!")
            break
        
        decision = input ("¿Deseas seguir sacando cartas? (s/n): ")
        if decision != "s":
            break
    return historial

jugar_siete_y_medio()