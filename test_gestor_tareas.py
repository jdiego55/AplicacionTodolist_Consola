import unittest
from gestortareas.gestor_tareas import GestorTareas

class TestGestorTareas(unittest.TestCase):
    def setUp(self):
        self.gestor = GestorTareas()

    def test_agregar_tarea(self):
        self.gestor.agregar_tarea("Hacer la compra")
        self.assertEqual(len(self.gestor.tareas), 1)

    def test_eliminar_tarea(self):
        self.gestor.agregar_tarea("Hacer la compra")
        self.gestor.eliminar_tarea("Hacer la compra")
        self.assertEqual(len(self.gestor.tareas), 0)

    def test_completar_tarea(self):
        self.gestor.agregar_tarea("Hacer la compra")
        self.gestor.completar_tarea("Hacer la compra")
        self.assertTrue(self.gestor.tareas[0].completada)

    def test_ver_tareas_pendientes(self):
        self.gestor.agregar_tarea("Hacer la compra")
        self.assertEqual(self.gestor.ver_tareas_pendientes(), ["Hacer la compra"])

if __name__ == "__main__":
    unittest.main()
