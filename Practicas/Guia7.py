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

#Ejercio1.4
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