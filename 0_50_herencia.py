# HERENCIA SIMPLE

class Persona:
  def __init__(self, nombre, edad, nacionalidad):
    self.nombre = nombre
    self.edad = edad
    self.nacionalidad = nacionalidad

  def hablar(self):
    print("hola estoy hablando un poco")
    
# Empleado es hijo y Persona es la clase Padre
class Empleado(Persona):
  def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
    super().__init__(nombre, edad, nacionalidad)
    # super(). es para indicar herencia y ponemos lo que se hereda de la clase Padre en este caso de Persona
    self.trabajo = trabajo
    self.salario = salario

# HERENCIA JERARQUICA
"""class Estudiate(Persona):
  def __init__(self, nombre, edad, nacionalidad, notas, universidad):
    super().__init__(nombre, edad, nacionalidad)
    self.notas = notas
    self.universidad = universidad"""

roberto = Empleado("Roberto", 43, "argentino", "programador", 10000)

roberto.hablar()