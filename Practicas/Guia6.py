import math
#Ejercio1.1
def imprimir_hola_mundo() -> None:
    print("Hola mundo!")

imprimir_hola_mundo ()
imprimir_hola_mundo ()
imprimir_hola_mundo ()
#Ejercio1.2
def imprimir_un_verso() -> None:
    print("hola \ncomo estas")

imprimir_un_verso ()

#Ejercio1.3
def raizDe2() -> float:
    return (round (math.sqrt(2), 4))

#Ejercio1.4
def factorialDeDos () -> int:
    return 2

#Ejercio1.5
def perimetro () -> float:
    return 2 * math.pi

a = perimetro()
print (a)
print (perimetro())

#Ejercio2.1
def imprimirSaludo (nombre: str) -> None:
    print ("Hola " + nombre)

#Ejercio2.2
def raiz_cuadrada_de (x:float) -> float:
    return math.sqrt(x)

#Ejercio2.3
def fahrenheit_a_celsius (x:float) -> float:
    return ((x-32)*5)/9

#Ejercio2.4
def imprimir_dos_veces(estribillo:str) -> None:
    estribillo = estribillo + " "
    print (estribillo*2)

#Ejercio2.5
def es_multiplo_de(n: int, m: int) -> bool:
    return n % m == 0

#Ejecio2.6
def es_par (n:int) -> bool:
    return (es_multiplo_de (n, 2))

#Ejercio2.7
def cantidad_de_pizzas (comensales:int, porciones:int) -> int:
    return math.ceil((comensales*porciones) / 8)

#Ejercio3.1
def alguno_es_0 (x:int, y:int) -> bool:
    return x==0 or y==0

#Ejercio3.2
def ambos_son_0 (x:int, y:int) -> bool:
    return x==0 and y==0

#Ejercio3.3
def es_nombre_largo (nombre: str) -> bool:
    return len(nombre) >= 3 and len(nombre) <= 8

def es_nombre_largo_con_if (nombre: str) -> bool:
    if len (nombre) < 3 or len (nombre) > 8:
        return False
    return True

#Ejercio3.4
def es_bisiesto (año:int) -> bool:
    return not ((año % 4 != 0 or año % 100 == 0) and año % 400 != 0) 

#Ejercio4.1
#Ejercio5.1
def el_doble_si_es_par (numero:int) -> int:
    if numero % 2 == 0:
        return numero*2
    return numero

#Ejercio6.2
def numeros_pares_entre_10_40 () -> None:
    a: int=10
    while  a <= 40:
        print(a)
        a= a+2
        
#Ejercio7
def numeros_pares_entre_10_40_con_for () -> None:
    for num in range (10, 41, 2):
        print(num)