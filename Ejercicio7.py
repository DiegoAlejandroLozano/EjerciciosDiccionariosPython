'''
Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar el artículo y 
su precio y añadir el par al diccionario, hasta que el usuario decida terminar. Después se debe mostrar por pantalla la 
lista de la compra y el coste total, con el siguiente formato

Lista de la compra

Artículo 1	Precio
Artículo 2	Precio
Artículo 3	Precio
…	…
Total	Coste

'''

cesta_compra = {}
continuar = True
coste = 0
indice = 1

while continuar:
    producto = input("Nombre del artículo: ")
    precio = float(input("Precio del artículo: "))

    cesta_compra[producto] = precio

    respuesta = input("Desear agregar más artículos? (si/no): ")

    if respuesta == "si":
        continuar = True
    else:
        continuar = False

for articulo in list(cesta_compra.keys()):
    print("Artículo %d: %-20s\tPrecio: %.2f" % (indice, articulo, cesta_compra[articulo]))
    coste += cesta_compra[articulo]

print("El coste total es: %.2f" % coste)


