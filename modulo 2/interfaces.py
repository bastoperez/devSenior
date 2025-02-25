from abc import ABC,abstractclassmethod

class Vehiculo_interface(ABC):
     @abstractclassmethod
     def mover(self):
          pass

class Carro(Vehiculo_interface):
     def mover(self):
          print("el carro esta andando")

class Bicicleta(Vehiculo_interface):
        def mover(self):
              print("la cicla esta en la carretera")

vehiculos=[Carro(),Bicicleta()]

for vehiculo in vehiculos:
    vehiculo.mover()