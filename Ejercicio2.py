'''
Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar 
por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.
'''

import telnetlib


nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
dirección = input("Ingrese su dirección: ")
telefono = input("Ingrese su teléfono: ")

diccionario = {
    'nombre':nombre,
    'edad':edad,
    'dirección':dirección,
    'telefono':telefono 
}

print("%s tiene %s años, vive en %s y su número de teléfono es %s" % (diccionario['nombre'], diccionario['edad'], diccionario['dirección'], diccionario['telefono']))