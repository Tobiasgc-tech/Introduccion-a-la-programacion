from queue import Queue as Cola
menu: dict =  {
    "hamburguesa": {
        "nombre": "Hamburguesa",
        "precio": 5.99,
        "stock": 50
    },
    "pizza": {
        "nombre": "Pizza",
        "precio": 8.99,
        "stock": 30
    },
    "ensalada": {
        "nombre": "Ensalada",
        "precio": 3.99,
        "stock": 20
    },
    "refresco": {
        "nombre": "Refresco",
        "precio": 1.99,
        "stock": 100
    }
}

def agregar_productos_al_menu(menu:dict, nombre:str, precio:float, cantidad:int):
    if nombre in menu:
       for clave in menu[nombre]:
            if clave == "precio":
               menu[nombre][clave] = precio
            elif clave == "stock":
               menu[nombre][clave] = cantidad
    else:
        menu[nombre] = {"nombre":nombre, "precio":precio,"stock":cantidad}
    return menu
agregar_productos_al_menu(menu,"manzana",21.99,50)

def cola_pedidos(nombre:str, producto:str,cantidad:int):
    d: dict = {}
    d[nombre] = {"producto":producto, "cantidad":cantidad}
    return d
cola_pedidos("Tobias","Pizza",2)