def saludar_con_adjetivo(nombre,adjetivo):
    print ("hola " + nombre+ " "+adjetivo +" como estas?")

saludar_con_adjetivo("andres","el inteligente")

## funcion return
"""
def multiplicar_numeros(numero1,numero2):
   resultado=numero1*numero2
   return resultado

print(multiplicar_numeros(15,5))
"""
#ejercicio de tutoria
def potencia(base,exponente):
    total=base**exponente
    return total
print(potencia(5,2))

# usdt a eeuros 1 dolar=0,90 eu

def casa_de_cambio(dolar):
    valor_euros=0.90
    cantidad=dolar*valor_euros
    return cantidad
print(casa_de_cambio(5))

#imprimir caracteres n veces
palabra=input("escriba una palabra")
cantidad_veces_=int(input("digite la cantidad de veces a repetir"))

def imprimir_caracteres(palabra,n):
    resultado=palabra*cantidad_veces_
    print(f"la palabra:",resultado)
    return resultado
imprimir_caracteres(palabra,cantidad_veces_)

