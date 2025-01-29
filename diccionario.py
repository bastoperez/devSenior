carro={"marca":"mazda",
       "modelo":"626",
       "annio":"1985",
       "colores":["rojo","azul","amarillo"]}
print(type(carro))
print(len(carro))
#print(carro.keys())
#print(carro.values())
carro["marca"]="renault"### cambie el valor asociado

print(carro.items())##items de un diccioario lo muestra como una lista de tupla

otro=carro.fromkeys
print(otro)
x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)

print(thisdict)