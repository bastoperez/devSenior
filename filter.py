edades=[5, 12, 17, 18,24,32]

def mayorDeEdad (x):
    if x<18:
        return False
    else:
        return True

adultos = filter(mayorDeEdad,edades)

for x in adultos:
    print(x)
