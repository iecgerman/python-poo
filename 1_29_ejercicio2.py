class Animal:
  def comer(self):
    print("El animal está comiendo")

class Ave(Animal):
  def volar(self):
    print("El animal está volando")

class Mamifero(Animal):
  def amamantar(self):
    print("El animal está amamantando")

class Murcielago(Mamifero, Ave):
  pass

"""murcielago = Murcielago()

murcielago.comer() # El animal está comiendo
murcielago.amamantar() # El animal está amamantando
murcielago.volar() # El animal está volando"""

ave = Ave()

ave.comer()
#ave.amamantar() # AttributeError: 'Ave' object has no attribute 'amamantar'
ave.volar()

print(Murcielago.mro()) # [<class '__main__.Murcielago'>, <class '__main__.Mamifero'>, <class '__main__.Ave'>, <class '__main__.Animal'>, <class 'object'>]