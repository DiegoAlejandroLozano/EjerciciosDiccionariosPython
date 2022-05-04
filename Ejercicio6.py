'''
Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una 
persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez 
que se añada un nuevo dato debe imprimirse el contenido del diccionario.
'''

informacion = {}
datos = ['nombre', 'edad', 'sexo', 'teléfono', 'correo electrónico']

for dato  in datos:
    informacion[dato] = input("Ingrese su %s: " % dato)
    for elemento in list(informacion.keys()):
        print("%s: %s" % (elemento, informacion[elemento]))

