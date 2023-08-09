# los getters y setters sirven para obtener y modificar los valores de una clase

class Persona():
  def __init__(self, nombre, edad):
    self._nombre = nombre
    self._edad = edad

  def get_nombre(self):
    return self._nombre

  # los setters serian asi:
  def set_nombre(self, new_nombre):
    self._nombre = new_nombre

dalto = Persona("Lucas", 21)

nombre = dalto.get_nombre()
print(nombre) # Lucas <- esta es la forma correcta de obtener una propiedad (_nombre) que esta privada y la almacena en el objeto nombre

dalto.set_nombre("Pepito") # OJO no se pone dalto = 

nombre = dalto.get_nombre()
print(nombre)

#print(dalto._edad) # esto no se debe de hacer as{i para eso existen reglas