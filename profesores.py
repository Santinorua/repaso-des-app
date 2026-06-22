class Profesor:
    def __init__(self, nombre, salario, materia, dni, cursos):
        self.nombre = nombre
        self.salario = salario
        self.materia = materia
        self.dni = dni
        self.cursos = cursos

    def agregar_curso(self, curso):
        self.cursos.append(curso)
    
    def eliminar_curso(self, curso):
        idx = self.cursos.index(curso)
        self.cursos.pop(idx)

    def poner_notas(self, curso):
        if curso not in self.cursos:
            return None
        for estudiante in curso.estudiantes:
            estudiante.agregar_nota(self.materia, float(input(f"Ingrese la nota para el estudiante {estudiante.nombre}: ")))

    def aumento_salarial(self, porcentaje):
        self.salario += self.salario * (porcentaje / 100)