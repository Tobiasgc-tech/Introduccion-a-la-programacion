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

#def vocales (palabra:str) -> bool:
#     for letra in range (0,len(palabra),1):
         

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
    for i in notas:
        while i >= 4 and i <= 10:
            if (sumaTotal2(notas) // len (notas)) >= 7:
                return (1)
            else:
                return (2)
        return (3)

print(aprobado([10,1,1,1,1,1]))