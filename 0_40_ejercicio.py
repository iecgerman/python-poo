class Estudiante:
  def __init__(self, nombre, edad, grado):
    self.nombre = nombre
    # OBJETO = PARAMETRO
    self.edad = edad
    self.grado = grado

# INSTANCIAMOS LOS OBJETOS:
pedro = Estudiante("Pedro", 23, 3)

print(pedro.nombre) # Pedro
print(pedro.edad) # 23
print(pedro.grado) # 3

