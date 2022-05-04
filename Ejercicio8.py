'''
Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las palabras en 
español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas. El programa debe crear 
un diccionario con las palabras y sus traducciones. Después pedirá una frase en español y utilizará el diccionario para 
traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.
'''

diccionario = {}
continuar = True
palabras = ""

while continuar:
    palabras = input("Ingrese las palabras (español,ingles): ").split(",")
    diccionario[palabras[0]] = palabras[1]
    respuesta = input("¿Quiere agregar más palabras? (si/no)").lower()

    if respuesta == "si":
        continuar = True
    else:
        continuar = False

frase_español = input("\nIngrese la frase en español: ").split()

frase_ingles = ""

for palabra in frase_español:
    frase_ingles += diccionario.get(palabra, palabra) + " "

print(frase_ingles)
