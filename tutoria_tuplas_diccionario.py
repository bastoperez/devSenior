#Tarea fromkeys() y otros métodos: # Fromkeys()

"""claves = ['a', 'b', 'c']

diccionario2 = dict.fromkeys(claves)
#print(diccionario2)

#Setdefault() ---------------------

mi_diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}

mi_diccionario.setdefault("Nombre" , "Manuel")
#print(mi_diccionario)

# update() --------------------------

mi_diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}

mi_diccionario.update({'Telefono': 3106674953, 'identificacion': 1006508160})
mi_diccionario.update({'nombre': "Maria", 'edad': 20})

mi_diccionario["nombre"] = "Mario"

#print(mi_diccionario)

# TUPLE
# enumarete() ------------------
"""
tupla = (1,2,3,4,5)
for i, valor in enumerate(tupla):
    print(f"Indice: {i}, valor: {valor}")

#ejercicio
def añadir_Estudiante_List(nombre_estudiante, correo, cedula):
        
    estudianteList = []
    estudianteList.append(nombre_estudiante)
    estudianteList.append(correo)
    estudianteList.append(cedula)
    return estudianteList

def editar_Nombre_Estudiante_List(listaEstudiante: list, indice, nombre_estudiante):
    
    if indice < len(listaEstudiante):
        listaEstudiante[indice] = nombre_estudiante
    else:
        print("Indice esta fuera de rango")
        
    return listaEstudiante
    
# INPUTS ----------------------

#nombre_Estudiante = input("Ingrese el nombre del estudiante: ")
#correo = input("Ingrese el correo del estudiante: ")
#cedula = int(input("Ingrese el cedula del estudiante: "))

listEstudiantes = añadir_Estudiante_List(nombre_Estudiante, correo, cedula)
print(listEstudiantes)
print(editar_Nombre_Estudiante_List(listEstudiantes, 0, "Mario"))

# eliminar por indice
#Funcion eliminar por índice:
 def eliminar_Por_Indice_Estudiante(listaEstudiante: list, indice):
    if indice < len(listaEstudiante):
        listaEstudiante = listaEstudiante.pop(indice)
    else:
        print("Indice esta fuera de rango")
        
    return listaEstudiante