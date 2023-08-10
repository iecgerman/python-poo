# los metodos especiales son por ejemplo __init__

# los metodos especiales son funciones que inician con __ y terminan con __

class Persona:
  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad

  def __str__(self): # nos devuelve la representacion del objeto en una cadena de texto
    return f"Persona(nombre={self.nombre}, edad={self.edad})"

  def __repr__(self):
    return f"Persona('{self.nombre}',{self.edad})"

  def __add__(self, otro):
    nuevo_valor = self.edad + otro.edad
    return Persona(self.nombre+otro.nombre, nuevo_valor)

dalto = Persona("Lucas", 21)
pedro = Persona("Pedro", 30)
maria = Persona("Maria", 18)

resultado = dalto + pedro
print(resultado)

nueva_persona = dalto + pedro
print(nueva_persona.nombre) # LucasPedro
print(nueva_persona.edad) # 51

nueva_persona = dalto + pedro +maria
print(nueva_persona.nombre) # LucasPedroMaria
print(nueva_persona.edad) # 69 <= que chingon esto de sumar objetos


#print(dalto) # nombre, edad, sexo, actividad

# si quitamos __str__ nos devuelve # <__main__.Persona object at 0x7f32d9402ec0>

# todo es un objeto en python

"""repre = repr(dalto)
resultado = eval(repre)

print(resultado) # Persona(nombre=Lucas, edad=21)

print(resultado.nombre) # Lucas
print(resultado.edad) # 21"""



