class Gato():
  def sonido(self):
    return "Miau"

class Perro():
  def sonido(self):
    return "Guau"

def hacer_sonido(animal):
  print(animal.sonido())

gato = Gato()
perro = Perro()

# Esto es Polimorfismo, enviar el mismo mensaje a diferentes objetos y obtener resultados diferentes con ese mismo mensaje
print(gato.sonido())
print(perro.sonido()) #este es polimorfismo con objeto

hacer_sonido(gato) # este es plimorfismo con un argumento

# Hacer esto en java o lenguaje c NO SE PUEDE, ahi si tienes que hacer clases que hereden de otras clases, y usan algo que se llama sobrecarga de metodos, en python esto no existe porque es un lenguaje de tipado dinamico

num1 = 3
num2 = 4.4

resultado = num1 + num2

print(resultado)
print(type(num1))
print(type(num2))
print(type(resultado)) # al sumas un entero msa un flotante python hace algo que se llama cohersion automatica que es convertir el int en float que alfinal es un ejemplo de plimorfismo

def recorrer(elemento):
  for item in elemento:
    print(f"El elemento actual es: {item}")

lista = [1,2,3,4]
lista2 = ["maquina", "como", "andas"]
lista3 = "maquina"
recorrer(lista)
recorrer(lista2)
recorrer(lista3)

# esto es polimorfismo, misma funcion, diferentes datos, y funciona igual


""""Cuando veo un ave que camina como un pato, nada como un pato y suena como un pato, a esa ave yo la llamo un pato."1​2​
En duck typing, el programador solo se ocupa de los aspectos del objeto que van a usarse, y no del tipo de objeto que se trata. Por ejemplo en un lenguaje sin duck-typing uno puede crear una función que toma un objeto de tipo Pato y llama los métodos "caminar" y "parpar" de ese objeto. En un lenguaje con duck-typing, la función equivalente tomaría un objeto de cualquier tipo e invocaría los métodos caminar y parpar. Si el objeto tratado no tiene los métodos pedidos, la función enviará una señal de error en tiempo de ejecución. Este hecho de que la función acepte cualquier tipo de objeto que implemente correctamente los métodos solicitados es lo que evoca la cita precedente y da nombre a la forma de tipificación."""

"""
https://ellibrodepython.medium.com/polimorfismo-vs-duck-typing-6f65bf2e8c0b
"""