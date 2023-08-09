class Persona():
  def __init__(self, nombre, edad):
    self.__nombre = nombre
    self._edad = edad
    
  @property # con esto le quitamos los parentesis en la linea 19 a get_nombre() si no nos tira error, y funciona incluso poniendo metodo super privado ejemplo __nombre
  def nombre(self):
    return self.__nombre

  @nombre.setter # con esto podremos modificar
  def nombre(self, new_nombre): # ya no le ponemos set_nombre, parece el mismo metodo pero no porque estamos usando decoradores
    self.__nombre = new_nombre
    
  @nombre.deleter
  def nombre(self): 
    del self.__nombre
    
dalto = Persona("Lucas", 21)

nombre = dalto.nombre # <= ya no es una funcion es una propiedad de hecho podemos quitar get_nombre y poner solo nombre y asi escondemos que es un getter
print(nombre)

dalto.nombre = "Pepe"

nombre = dalto.nombre 
print(nombre) # Pepe <= aqui si mi me lo modifico

#del dalto.nombre

nombre = dalto.nombre 
print(nombre) # aqui tira error porque eliminamos, comentaremos del y nos imprimira 2 veces Pepe

"""C'MAMUT ESTA CLASE ME GUSTO MUCHO LO DE LAS PROPIEDADES"""