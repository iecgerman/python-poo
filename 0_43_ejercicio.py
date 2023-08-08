class Estudiante:
  def __init__(self, nombre, edad, grado):
    self.nombre = nombre
    # OBJETO = PARAMETRO
    self.edad = edad
    self.grado = grado

  def estudiar(self):
    print("Estudiando...")


nombre = input("Digame su nombre: ")
edad = input("Cuantos años tienes: ")
grado = input("En que grado vas: ")

estudiante = Estudiante(nombre, edad, grado)

print(f"""
      DATOS DEL ESTUDIANTE: \n\n
      Nombre: {estudiante.nombre} \n
      Edad: {estudiante.edad} \n
      Grado: {estudiante.grado} \n

    """)

while True:
  estudiar = input()
  if (estudiar.lower() == "estudiar"):
    estudiante.estudiar() #ojo me faltaron los parentesis y por eso no ejecutaba el metodo estudiar()