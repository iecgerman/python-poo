# una clase abstracta es como una plantilla o modelo para todas las demas

from abc import ABC, abstractclassmethod # este ultimo es un decorador

class Persona(ABC): # con esto ya estamos diciencdo que vamos a crear una clase abstracta
  @abstractclassmethod # con este decorador ya estamos diciendo que vamos a crear un metodo abstracto
  def __init__(self, nombre, edad, sexo, actividad):
    self.nombre = nombre
    self.edad = edad
    self.sexo = sexo
    self.actividad = actividad

  @abstractclassmethod
  def hacer_actividad(self):
    pass

  def presentarse(self):
    print(f"Hola, me llamo: {self.nombre} y tengo {self.edad} años")

# de aqui para arriba todo es una plantilla

class Estudiante(Persona):
  def __init__(self, nombre, edad, sexo, actividad):
    super().__init__(nombre, edad, sexo, actividad)

  def hacer_actividad(self):
    print(f"Estoy estudiando: {self.actividad}")
    
class Trabajador(Persona):
  def __init__(self, nombre, edad, sexo, actividad):
    super().__init__(nombre, edad, sexo, actividad)

  def hacer_actividad(self):
    print(f"Actual mente estoy trabajando en el giro de: {self.actividad}")

pedrito = Estudiante("Lucas", 25, "Masculino", "Programación")
dalto = Trabajador("Dalto", 21, "No Binario", "Programación")

dalto.presentarse()
dalto.hacer_actividad()
pedrito.presentarse()
pedrito.hacer_actividad()

# las clases abstractas fomentan el polimorfismo porque todas las subclases utilizan los mismos metodos, por ejemplo el trabajador, el estudiante, el jefe, el maestro, etc, todos puedn usar el metodo hacer_actividad()