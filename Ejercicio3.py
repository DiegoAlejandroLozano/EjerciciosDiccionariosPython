'''
Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario 
por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la 
fruta no está en el diccionario debe mostrar un mensaje informando de ello.

Fruta	    Precio
Plátano	    1.35
Manzana	    0.80
Pera	    0.85
Naranja	    0.70
'''

frutas = {
    'Plátano':1.35,
    'Manzana':0.80,
    'Pera':0.85,
    'Naranja':0.70
}

fruta = input("Ingrese la fruta: ")
kilos = float(input("Ingrese los kilos: "))

if fruta in list(frutas.keys()):
    precio = frutas[fruta] * kilos
    print("%.2f kilos de %s cuestan %.2f" % (kilos, fruta, precio))
else:
    print("La fruta no está en la lista")
