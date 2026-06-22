from estudiantes import Estudiante


class Curso:
    def __init__(self, nombre: str, anno: int, materias: list[str], estudiantes: list[Estudiante], especializacion: str):
        self.nombre = nombre
        self.anno = anno
        self.materias = materias
        self.especializacion = especializacion
        self.estudiantes = estudiantes

    def ratio_aprobados(self, materia: str) -> float:
        aprobados = filter(lambda x: Estudiante.aprobo_materia(x, materia), self.estudiantes)

        return len(aprobados) / len(self.estudiantes)

    def agregar_estudiante(self, estudiante: Estudiante):
        self.estudiantes.append(estudiante)

    def eliminar_estudiante(self, estudiante: Estudiante):
        idx = self.estudiantes.index(estudiante)
        self.estudiantes.pop(idx)

    def cant_niveles_ingles(self) -> int:
        niveles_ingles = set()
        for est in self.estudiantes:
            niveles_ingles.add(est.nivel_ingles)

        return len(niveles_ingles)
