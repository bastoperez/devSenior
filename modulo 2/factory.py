class Coche:
    def conducir(self):
        print("El coche está conduciendo.")
class Bicicleta:
    def conducir(self):
        print("La bicicleta está pedaleando.")
class VehiculoFactory:
    @staticmethod
    def crear_vehiculo(tipo):
        if tipo == "coche":
            return Coche()
        elif tipo == "bicicleta":
            return Bicicleta()
        else:
            raise ValueError("Tipo de vehículo no reconocido")
# Usando el Factory
vehiculo1 = VehiculoFactory.crear_vehiculo("coche")
vehiculo1.conducir()  # Imprime: El coche está conduciendo.
vehiculo2 = VehiculoFactory.crear_vehiculo("bicicleta")
vehiculo2.conducir()  # Imprime: La bicicleta está pedaleando.