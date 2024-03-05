#Escribir un programa que cree un diccionario simulando un carrito de compra. El programa debe preguntar el
#artículo y su precio y añadir la información al diccionario, hasta que el usuario decida terminar. Se debe mostrar en
#pantalla la lista de la compra final y el costo total de la compra.

def crear_carrito():
    carrito = {}
    while True:
        articulo = input("Ingrese el nombre del artículo (o 'terminar' para finalizar la compra): ")
        if articulo.lower() == "terminar":
            break
        precio = float(input("ingrese el precio del articulo: "))
        carrito[articulo]=precio
    return carrito

def calcular_costo_total(carrito):
    total=sum(carrito.values())
    return total

def mostrar_carrito(carrito, total):
    print("lista de la compra: ")
    for articulo, precio in carrito.items():
        print(f"{articulo}: ${precio}")
    print(f"\nCosto total de la compra: ${total}")

carrito = crear_carrito()

total = calcular_costo_total(carrito)

mostrar_carrito(carrito, total)