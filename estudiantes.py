class Estudiante:
    def __init__(self, nombre, edad, dni, notas, nivel_ingles):
        self.dni = dni
        self.nombre = nombre
        self.edad = edad
        self.notas: dict[str, float] = notas
        self.nivel_ingles = nivel_ingles
    
    def calcular_promedio(self):
        if len(self.notas) == 0:
            return None
        return sum(self.notas.values()) / len(self.notas)
    
    def agregar_nota(self, materia, nota):
        self.notas[materia] = nota
    
    def aprobo_materia(self, materia):
        if materia not in self.notas:
            return None
        return self.notas[materia] >= 6.0
    