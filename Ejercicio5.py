'''
Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y 
después muestre por pantalla los créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una 
de las asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso.
'''

creditos_total = 0

asignaturas = {
    'Matemáticas':6,
    'Física':4,
    'Química':5    
}

for asignatura in list(asignaturas.keys()):
    print("%s tiene %d créditos" % (asignatura, asignaturas[asignatura]))
    creditos_total += asignaturas[asignatura]

#Total de créditos del curso
print("El créidto total del curso es: %d" % creditos_total)