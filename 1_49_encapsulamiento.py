# el encapsulamiento consiste en proteger datos, proteger metodos, por ejemplo que no accedan a un password de usuario

class MiClase:
  def __init__(self):
    self.__atributo_privado = "Valor"

  def __hablar(self):
    print("hola, como estas") # no me va a dejar imprimir porque por el doble __ es un metodo muy privado


objeto = MiClase()
# si ponemos doble __ es un atributo super privado y nos tirara error
print(objeto.__hablar()) # AttributeError: 'MiClase' object has no attribute '__atributo_privado'
"""print(objeto.__atributo_privado) # AttributeError: 'MiClase' object has no attribute '__atributo_privado'"""