class Auto():
  def __init__(self):
    self._estado = "apagado"

  def encender(self):
    self._estado = "encendido"
    print("El auto está encendido")

  def conducir(self):
    if self._estado == "apagado":
      self.encender()
    print("Conduciendo el auto")

mi_auto = Auto()
mi_auto.conducir() # la abstracción es esconder toda la logica interna para el usuario, por ejemplo el usuario al encender el auto no sabe que hubo un condicional para saber si el auto estaba apagadoque cuando se cumplio llamo al metodo self.encender(), etc.and

# otro ejemplo de abstraccion es como cuando entras a un login, solo le das tus datos de usuario y contraseña y no sabes toda la logica que hay detras de

# abstraccion es ocultar la complejidad interna de un sistema

