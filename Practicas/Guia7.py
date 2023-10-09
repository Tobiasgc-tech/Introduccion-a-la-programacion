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
    indice: int=0
    while indice < len(s):
        if s[indice] > s[indice + 1]:
            return False
        else:
            indice += 1
    return True
