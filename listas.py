
"""
nombre="johan"
frutas=["fresa","papaya","manzana","pera",5,True]
print (frutas[5])
# las listas son ordenadas,mutables, permiten duplicados
print(len(frutas))# abreviatura de lenght
ensayis=["carlos",[1,6,8],52,True]
print(type(frutas))
"""
#nombre= "carlos"
#print(type(nombre))
"""
marcas=list(("mazda","renault","fiat"))
frutas=["manzana","papaya","pera","piña","guanabana"]
print(frutas[:5])
print(frutas[0])
print(frutas[2])
"""
#busqueda dentro de listas
#frutas=["manzana","papaya","pera","piña","guanabana"]
#frutas.append("naranja")

##frutas.clear()
#print(frutas)

#frutas2=frutas.copy()#copia la lista pero no son la misma si se agregan mas objetos
#print(frutas2)
"""
frutas=["manzana","papaya","pera","piña","guanabana","papaya"]
frutas_malucas= ["chontaduro","marañon"]
print(frutas.count("papaya"))
frutas.extend(frutas_malucas)
print(frutas)
print(frutas.index("papaya"))
frutas.insert(1,frutas_malucas)
print(frutas[1][1])"""

#saca un objeto de la lista
"""frutas=["manzana","papaya","pera","piña","guanabana","papaya"]
frutas[1]="toronja"
frutas.pop(1)
print(frutas)"""
frutas=["manzana","papaya","pera","piña","guanabana","papaya"]
frutas.remove("papaya")


#revierte la lista
frutas.reverse()
print(frutas)
#organiza la lista
frutas.sort()
print(frutas)