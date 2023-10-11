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

#Ejercio4
def peso_pino (metros:float) -> float:
    if metros <= 3:
        return metros*100*3
    return 300*3 + (metros-3)*100*2

def es_peso_util (peso:float) -> None:
    if peso >= 400 and peso <= 1000:
        print("Si, si es util")
    else:
        print("No, no es util")


def sirve_pino (metros:float) -> None:
    if metros >= 4/3 and metros <= 3.5:
        print("Si, si sirve el pino")
    else:
        print("No, no sirve el pino")

def sirve_pino_com (metros:float) -> None:
    es_peso_util(peso_pino(metros))

#Ejercio5.1
def el_doble_si_es_par (numero:int) -> int:
    if numero % 2 == 0:
        return numero*2
    return numero

#Ejercio5.2
def devolver_valor_si_es_par_sino_el_que_sigue (numero:int) -> int:
    if numero % 2 == 0:
        return numero
    return numero + 1

#Ejercio5.3
def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9 (numero:int) -> int:
    if numero % 9 == 0:
        return numero*3
    elif numero % 3 == 0:
        return numero*2
    return numero

#Ejercio5.4
def lindoNombre (nombre:str) -> str:
    if len(nombre) >= 5:
        return "Tu nombre tiene muchas letras!"
    return "Tu nombre tiene menos de 5 caracteres!"

#Ejercio5.5
def elRango (numero:int) -> None:
    if numero < 5:
        print("Menor a 5")
    elif 10 <= numero <= 20:
        print("Entre 10 y 20")
    elif 20 < numero:
        print("Mayor a 20")

#Ejercio5.6
def queMeToca (sexo:str, edad:int) -> None:
    if sexo == "F" and edad >= 60:
        print("Andá de vacaciones")
    elif sexo == "M" and edad >= 65:
        print("Andá de vacaciones")
    elif edad < 18:
        print("Andá de vacaciones")
    else:
        print("Te toca trabajar")

#Ejercio6.1
def numerosDel1al10 () -> None:
    a: int=1
    while a <= 10:
        print(a)
        a= a+1

#Ejercio6.2
def numeros_pares_entre_10_40 () -> None:
    a: int=10
    while  a <= 40:
        print(a)
        a= a+2

#Ejercio6.3
def eco10veces() -> None:
    a: int=1
    while a <= 10:
        print("eco")
        a=a+1

#Ejercio6.4
def despegue(numero:int) -> None:
    while numero > 0 :
        print(numero)
        numero = numero - 1
    print("Despegue")

#Ejercio6.5
def viajeEnElTiempo (añopartida:int,añolleguada:int) -> None:
    while añopartida > añolleguada:
        añopartida = añopartida - 1
        print("Viajo un año al pasado, estamos en el año "+str(añopartida))
        

#Ejercio7
def numeros_pares_entre_10_40_con_for () -> None:
    for num in range (10, 41, 2):
        print(num)