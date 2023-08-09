# los decoradores se usan mucho en flask

def decorador(funcion):
  def funcion_modificada():
    print("Antes de llamas a la función")
    funcion()
    print("Después de llamar a la función")
  return funcion_modificada #OJO EL return estaba mal identado y madaba error
  """File "/home/runner/python-poo/2_03_decoradores.py", line 16, in <module>
  saludo_modificado()
TypeError: 'NoneType' object is not callable"""
  
"""def saludo():
  print("Hola Dalto")

#decorador(saludo()) # Hola Dalto

saludo_modificado = decorador(saludo)
saludo_modificado()"""

# lo que sigues es lo mismo que comentamos """ arriba pero usando decoradores, no existen reglas se pueden usar cualquiera de las dos,pero al usar decoradores es una forma mas legible de hacer codigo y es una buena practica
@decorador # con esto estamos indicando que es un decorador
def saludo():
  print("Hola Dalto como estas")

saludo() 
# Antes de llamas a la función
# Hola Dalto como estas
# Después de llamar a la función

# un decorar te agarra una fucion y le agrega funcionalidad antes o/y despues de ejecutar la funcion  