import os

class Coche:

    def __init__(self,marca,modelo,anio,color):
        self._marca=marca
        self._modelo=modelo
        self._anio=anio
        self._color=color
    
    def get_marca(self):
        return self.get_marca
    
    def get_modelo(self):
        return self.get_modelo
    
    def get_anio(self):
        return self.get_anio
    
    def get_color(self):
        return self.get_color
    
    def saludar(self):
        print("hola, soy un ",self._marca,"",self._modelo,"del anio",self._anio)
    
    #metodo actualizar el año del carro
    def set_anio(self,nuevo_anio):
        if(self._anio<nuevo_anio):
            print("se actualizo el anio del vehiculode ",self._anio,"a", nuevo_anio)
            self._anio=nuevo_anio
        else:
            print("el ano nuevo",nuevo_anio,"no pude ser menor o igual al que tenia ")
    
#creamos la instancia de la clase
coche1=Coche("renault","twingo",2008,"verde")

#limpia la pantalla
os.system('clear')

#invoca el metodo para poder imprimir
coche1.saludar()

#actualizar el anio coche
coche1.set_anio(2010)
        
        