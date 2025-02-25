import os
class Animal:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
    def hablar(self):
        print("el animal hace un ruido")
    def informacion(self):
         print(f"el animal se llama {self.nombre},su edad es {self.edad} años")
        

class Gato(Animal):

    def __init__(self, nombre, edad,raza):
        super().__init__(nombre, edad)
        self.raza=raza

#sobreescribimos el metodo hablar
    def hablar(self):
        print(f"{self.nombre} dice: ¡miau!")

    def ronronear(self):
         print(f"{self.nombre}se acerca y ronronea")
        
    def informacion(self):
         super().informacion
         print(f"Raza: {self.raza}")

#creamos el objeto a la clase hija 
   
mi_Gato=Gato("pelusa",4,"angora")
mi_Gato.informacion()

#ejecutamos el metodo hablar
mi_Gato.hablar()
mi_Gato.ronronear()
Animal.hablar(Gato)

print("\nmetodo de super clase hablar:")
super(Gato, mi_Gato).hablar()

