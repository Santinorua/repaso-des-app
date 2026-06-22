from estudiantes import Estudiante
from profesores import Profesor
from cursos import Curso

estudiantes = []

print("Ingresando estudiantes: ")
for i in range(3):
    nombre = input("Ingrese el nombre del estudiante: ")
    edad = int(input("Ingrese la edad del estudiante: "))
    dni = input("Ingrese el DNI del estudiante: ")
    notas = {}
    nivel_ingles = input("Ingrese el nivel de inglés del estudiante (A1, A2, B1, B2, C1, C2): ")
    estudiantes.append(Estudiante(nombre, edad, dni, notas, nivel_ingles))

cursos = set()
print("Ingresando cursos: ")

for i in range(2):
    nombre = input("Ingrese el nombre del curso: ")
    anno = int(input("Ingrese el año del curso: "))
    materias = input("Ingrese las materias del curso (separadas por comas): ").split(",")
    especializacion = input("Ingrese la especialización del curso: ")
    cursos.add(Curso(nombre, anno, materias, estudiantes, especializacion))

profesores = []

for i in range(3):
    nombre = input("Ingrese el nombre del profesor: ")
    salario = float(input("Ingrese el salario del profesor: "))
    materia = input("Ingrese la materia que enseña el profesor: ")
    dni = input("Ingrese el DNI del profesor: ")
    nombre_cursos_profesor = input("Ingrese los cursos que dicta el profesor (separados por comas): ").split(",")
    
    cursos_profesor = [curso for curso in cursos if curso.nombre in nombre_cursos_profesor]
    profesores.append(Profesor(nombre, salario, materia, dni, cursos_profesor))


