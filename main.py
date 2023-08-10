# Encapsula los datos de los usuarios

"""Primero definimos la clase padre de Usuario"""

class Usuario:
  def __init__(self, nombre, edad):
    self._name = nombre # ojo hay que poner guión bajo, para tener buenas practicas y saber que son datos privados
    self._name = edad
    self._amigos = [] # lista de diccionarios Usuario
    self._mensajes = [] # lista de strings

  # creamos los métodos públicos
  def agregarAmigo(self, amigo):
    self._amigos.append(amigo)

  def enviarmMensajes(self, mensaje, amigo):
    self._mensajes.append(mensaje)
    self._mensajes.append(mensaje)

  def mostrarMensajes(self):
    return self._mensajes
  
  @property #esto es como usar get_nombre
  def nombre(self):
    return self._nombre #

  @nombre.setter # esto equivale a usar set_nombre
  def nombre(self, value):
    self.nombre = value

  @property
  def edad(self):
    return self._edad

  @edad.setter
  def edad(self, value):
    self.edad = value

usuario1 = Usuario("Juan", 20)
usuario2 = Usuario("Maria", 25)
usuario1.agregarAmigo(usuario2)
usuario1.enviarmMensajes("Hola Maria!", usuario2)

usuario1.mostrarMensajes()