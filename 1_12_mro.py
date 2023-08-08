# METODO DE RESOLUCION DE ORDEN

# el mro es algo asi como la especificidad en css

class A:
  def hablar(self):
    print("Hola desde A")
    
class F:
  def hablar(self):
    print("Hola desde F")

class B(A):
  def hablar(self):
    print("Hola desde B")
    
class C(F):
  def hablar(self):
    print("Hola desde C")
    
class D(B,C):
  def hablar(self):
    print("Hola desde D")

d = D()

# B es la clase y d es el objeto
B.hablar(d)
C.hablar(d)
D.hablar(d)

#print(D.mro()) # [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.A'>, <class '__main__.C'>, <class '__main__.F'>, <class 'object'>]

