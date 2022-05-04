'''
Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las facturas 
se almacenarán en un diccionario donde la clave de cada factura será el número de factura y el 
valor el coste de la factura. El programa debe preguntar al usuario si quiere añadir una nueva 
factura, pagar una existente o terminar. Si desea añadir una nueva factura se preguntará por el 
número de factura y su coste y se añadirá al diccionario. Si se desea pagar una factura se preguntará 
por el número de factura y se eliminará del diccionario. Después de cada operación el programa debe mostrar 
por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.
'''

facturas = {}
continuar = True

while continuar:
    #Preguntando al usuario que quiere hacer
    respuesta = input("\n¿Qué quiere realizar: ?\na)Añadir una nueva factura\nb)Pagar factura existente\nc)Terminar\nRespuesta: ")
    #Si la respuesta es añadir una nueva factura
    if respuesta.lower() == 'a':
        numero_factura = int(input("\nIngrese el número de factura: "))
        coste_factura = float(input("Ingrese el coste de la factura: "))
        facturas[numero_factura] = coste_factura
        cantidad_total_cobro = 0 
        for costo_factura in facturas.values():
            cantidad_total_cobro += costo_factura
        print("La cantidad pendiente de cobro: %.2f" % cantidad_total_cobro)  
    #Si la respuesta es pagar factura existente 
    elif respuesta.lower() == 'b':
        numero_factura = int(input("\nIngrese el número de factura: "))
        if numero_factura in facturas: 
            coste_factura = facturas[numero_factura]
            facturas.pop(numero_factura)
            cantidad_total_cobro = 0
            for costo_factura in facturas.values():
                cantidad_total_cobro += costo_factura
            print("La cantidad pendiente de cobro: %.2f" % cantidad_total_cobro)
            print("La cantidad cobrada: %.2f" % coste_factura) 
        else:
            print("\nEl número de factura no existe...")
    #Si la respuesta es terminar 
    elif respuesta.lower() == 'c':
        print("\nGracias por utilizar nuestro sistema!!! :D")
        continuar = False


