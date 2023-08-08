# Curso de POO con PYTHON desde CERO (Completo)

# https://www.youtube.com/watch?v=HtKqSJX7VoM&list=LL&index=3

# CREDITOS AL CANAL DE SOY DALTO

class Celular(): # esto es la clase celular
  def __init__(self, marca, modelo, camara): # esto se llama método constructor y self es como hacer referencia a si mismo, como decir celular1.marca = self.marca
    self.marca = marca # marca es diferente de marca, self.marca es lo que le estamos pidiendo y marca despues del = es un parametro del constructor
    self.jajaja = modelo # por ejemplo voy a cambiar en self.modelo a self.jajaja y me dio el mismo resultado "S23" o Iphone 15 Pro"
    self.camara = camara

# TODAS LAS FUNCIONES QUE ESTAN DENTRO DE UNA CLASE SE LLAMAN METODOS EJEMPLO EL METODO CONSTRUCTOR def __init__():

  def llamar(self):
    print(f"Estas haciendo una llamada desde un {self.jajaja}")

  def cortar(self):
    print(f"Cortaste la llamada desde un {self.jajaja}")

celular1 = Celular("Samsung", "S23", "48MP") # esos se llaman atributos de instancia y celular1 o celular2 se llaman objetos, estamos instanciando objetos
celular2 = Celular("Apple", "Iphone 15 Pro", "96MP")

#print(celular2.cortar()) 
# Cortaste la llamada
# None
# nos aparece un None porque estamos metiendo todo en un print y esta de mas

celular1.llamar()
celular1.cortar()
celular2.llamar()
celular2.cortar()