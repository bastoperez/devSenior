"""edad=18
if edad>= 18:
    print("la persona es mayor de edad")
else :
    print("la persona es menor de edad")
"""
"""sexo="M"
if sexo=="M":
    print("masculino")
elif sexo=="F":
    print("femenino")
else:
    print("es otro sexo")"""
"""
primera infancia sea de 0 a 5 años
infancia 6 y 13 anos
adolescencia 14 y 17
18+ adultos
"""
edad= int(input ("ingrese su edad:"))
if edad <6:
    print("primera infancia")
elif edad>= 6 and edad <14:
    print ("infancia")
elif edad>=14 and edad< 18:
    print("adolescencia")
elif edad>= 18 and edad< 116:
    print("adulto")
else:
    print("edad incorrecta")
