"""#definir la clase persona
class Persona:
    #metodo constructor
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
    #metodo para saludar
    def saludar(self):
        #imprimir usando comas
        print("hola¡ mi nombre es",self.nombre,"y tengo",self.edad,"años")
    #crear un objeto
persona1=Persona("juan",25)

#usar el metodo del objeto
persona1.saludar()
"""
#definir  la clase libro
class Libro:
    #metodo constructor
    def __init__(self,titulo,autor,paginas):
        self.titulo=titulo
        self.autor=autor
        self.paginas=paginas
    #metodo descripcion
    def descripcion (self):
        #imprimir
        print("titulo del libro es:",self.titulo,",el autor es:",self.autor,"y tiene ",self.paginas,"de paginas")

    #crear un objeto de la clase libro con los datos
libro1=Libro("alicia en el pais de las maravillas","johan",150)

#usar el metodo del objeto
libro1.descripcion()
