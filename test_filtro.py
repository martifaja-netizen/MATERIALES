# Archivo: test_filtro.py

import unittest
from filtro import Filtro


class TestFiltro(unittest.TestCase):
    """
    Esta clase contiene las pruebas unitarias para validar
    que el objeto Filtro guarda y mantiene los datos correctamente.
    """

    def test_creacion_filtro_valores_correctos(self):
        """Prueba que los atributos se asignen correctamente en el constructor."""
        # 1. PREPARACIÓN y EJECUCIÓN (Creamos un filtro de prueba)
        filtro_prueba = Filtro(res_min=300.0, dens_max=8.0, coste_max=10.0, temp_min=200.0)

        # 2. COMPROBACIÓN (Comparamos usando 'assertEqual')
        # assertEqual(valor_real, valor_esperado) comprobará si son idénticos
        self.assertEqual(filtro_prueba.res_min, 300.0)
        self.assertEqual(filtro_prueba.dens_max, 8.0)
        self.assertEqual(filtro_prueba.coste_max, 10.0)
        self.assertEqual(filtro_prueba.temp_min, 200.0)

    def test_valores_negativos(self):
        """Prueba que el filtro acepte valores en cero o negativos si fuera necesario."""
        filtro_negativo = Filtro(res_min=0.0, dens_max=-1.0, coste_max=0.0, temp_min=-50.0)

        self.assertEqual(filtro_negativo.res_min, 0.0)
        self.assertEqual(filtro_negativo.dens_max, -1.0)


# Este bloque permite ejecutar los tests directamente desde la consola
if __name__ == "__main__":
    unittest.main()