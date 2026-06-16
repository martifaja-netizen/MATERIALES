"""
Clase BaseDatosMateriales.

Actúa como almacén de todos los materiales disponibles
en la aplicación.

Su función es crear y mantener una colección de objetos
Material que posteriormente podrán ser consultados y
filtrados por el GestorMateriales.

Actualmente los materiales se cargan desde una lista
definida en el código, aunque en futuras versiones
podrían obtenerse desde un archivo o una base de datos.
"""
from material import Material


class BaseDatosMateriales:
    """
    Contenedor principal de los materiales disponibles.

    Mantiene una lista de objetos Material y proporciona
    métodos para cargarlos, consultarlos y filtrarlos.
    """
    def __init__(self):
        self.materiales = []

    def cargar_materiales(self):
        self.materiales = [
            Material("Acero Inoxidable 304", 540, 7.9, 3.5, 870),
            Material("Titanio (Grado 2)", 340, 4.5, 8.5, 300),
            Material("Inconel 625", 850, 8.4, 9.5, 980),
            Material("Acero Cromo-Molibdeno", 500, 7.8, 6.2, 500),
            Material("Haynes 230", 660, 8.2, 9.8, 1095)
        ]

    def obtener_todos(self):
        return self.materiales
    
# aixo de sota es nou, per cuadrar amb el gestor de materials
    
    def filtrar(self, filtro):
        resultados = []

        for material in self.materiales:
            if material.cumple_filtro(filtro):
                resultados.append(material)

        return resultados