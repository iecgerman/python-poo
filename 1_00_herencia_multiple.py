# HERENCIA MULTIPLE

class Persona:
  def __init__(self, nombre, edad, nacionalidad):
    self.nombre = nombre
    self.edad = edad
    self.nacionalidad = nacionalidad

  """def hablar(self):
    print("hola estoy hablando un poco")"""
    
class Empleado(Persona):
  def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
    super().__init__(nombre, edad, nacionalidad)
    self.trabajo = trabajo
    self.salario = salario

class Artista:
  def __init__(self, habilidad):
    self.habilidad = habilidad

  def mostrar_habilidad(self):
    return f"Mi habilidad es: {self.habilidad}"
      
class EmpleadoArtista(Persona, Artista):
  def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
    Persona.__init__(self, nombre, edad, nacionalidad)
    Artista.__init__(self, habilidad)
    self.salario = salario
    self.empresa = empresa

  """def mostrar_habilidad(self):
    print("si no usamos super() y ponemos self.mostrar... en la linea 36 no haremos referencia a las clases padres")"""

  def presentarse(self):
    #return f"{super().mostrar_habilidad()}" # al usar super() esta haciendo referencia a las clases padres que son 2, Persona y Artista; si pusieramos self.
    print(f'Hola, soy {self.nombre}, {self.mostrar_habilidad()} y trabajo en {self.empresa}')

  # es una buena practica usar super(). pero si podemos usar self. pero se usaran los metodos que se encuentren en la misma clase en este caso de EmpleadArtista

    

roberto = EmpleadoArtista("Roberto", 43, "argentino", "Cantar", 100000, "Google")

#roberto.presentarse()

# ¿Cómo saber si EmpleadoArtista es una subclase de la clase Artista?
herencia = issubclass(EmpleadoArtista, Artista) # Aquí EmpleadoArtista hereda de Artista
print(herencia) # True


herencia = issubclass(Artista, Persona) # Aquí Artista no es una subclase de Persona
print(herencia) # False

# ¿Roberto es una instancia (objeto) de la clase EmpleadoArtista?
instacia = isinstance(roberto, EmpleadoArtista) # es verdadero porque roberto es un objeto de la clase EmpladoArtista, igual de Artista e igual de Persona
print(instacia) # True

