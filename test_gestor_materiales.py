# Archivo: test_gestor_materiales.py

import unittest
from gestor_materiales import GestorMateriales
from filtro import Filtro


class TestGestorMateriales(unittest.TestCase):
    """
    Clase de pruebas unitarias para validar el comportamiento del Gestor.
    El gestor debe ser capaz de recibir un filtro, procesarlo a través
    de la Base de Datos y retornar únicamente los materiales que cumplen.
    """

    def setUp(self):
        """El método setUp se ejecuta automáticamente ANTES de cada test."""
        # Creamos una instancia limpia del gestor para usarla en las pruebas
        self.gestor = GestorMateriales()

    def test_buscar_encuentra_materiales_correctos(self):
        """Prueba que el gestor devuelva materiales cuando existen opciones válidas."""
        # 1. Creamos un filtro realista (ej. buscando algo similar al Titanio o Acero)
        # Resistencia mín: 300, Densidad máx: 5.0, Coste máx: 10.0, Temp mín: 200
        filtro_ejemplo = Filtro(res_min=300.0, dens_max=5.0, coste_max=10.0, temp_min=200.0)

        # 2. Le pedimos al gestor que busque
        resultados = self.gestor.buscar(filtro_ejemplo)

        # 3. Comprobaciones (Asserts)
        self.assertIsInstance(resultados, list)  # Garantiza que devuelve una lista
        self.assertTrue(len(resultados) > 0)  # Garantiza que la lista no está vacía

        # Verificamos que el primer resultado sea el "Titanio (Grado 2)"
        # ya que cumple con una densidad baja (< 5.0) y coste bajo (< 10.0)
        self.assertEqual(resultados[0].nombre, "Titanio (Grado 2)")

    def test_buscar_sin_resultados(self):
        """Prueba que el gestor devuelva una lista vacía si los requisitos son imposibles."""
        # Filtro imposible: Resistencia altísima (2000) y precio ridículamente barato (0.1)
        filtro_imposible = Filtro(res_min=2000.0, dens_max=1.0, coste_max=0.1, temp_min=1500.0)

        resultados = self.gestor.buscar(filtro_imposible)

        # Garantiza que el programa no explota, sino que devuelve una lista vacía de forma limpia
        self.assertEqual(len(resultados), 0)


if __name__ == "__main__":
    unittest.main()