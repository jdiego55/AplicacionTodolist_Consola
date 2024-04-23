from tareas.tarea import Tarea

class GestorTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, nombre):
        tarea = Tarea(nombre)
        self.tareas.append(tarea)

    def eliminar_tarea(self, nombre):
        self.tareas = [tarea for tarea in self.tareas if tarea.nombre != nombre]

    def completar_tarea(self, nombre):
        for tarea in self.tareas:
            if tarea.nombre == nombre:
                tarea.completada = True

    def ver_tareas_pendientes(self):
        tareas_pendientes = [tarea.nombre for tarea in self.tareas if not tarea.completada]
        return tareas_pendientes
