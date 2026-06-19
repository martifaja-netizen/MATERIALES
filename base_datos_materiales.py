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
            Material("Haynes 230", 660, 8.2, 9.8, 1095),

            Material("Aluminio 6061-T6", 310, 2.7, 4.0, 150),
            Material("Aluminio 7075-T6", 570, 2.8, 6.5, 120),
            Material("Acero al Carbono A36", 400, 7.85, 1.2, 425),
            Material("Acero S275", 410, 7.85, 1.0, 400),
            Material("Acero S355", 510, 7.85, 1.2, 450),

            Material("Cobre", 220, 8.96, 7.0, 200),
            Material("Latón", 300, 8.5, 5.5, 250),
            Material("Bronce", 350, 8.8, 6.0, 300),
            Material("Magnesio AZ31", 260, 1.8, 5.0, 120),
            Material("Fundición Gris", 250, 7.2, 0.8, 400),

            Material("Poliamida PA6", 80, 1.14, 3.0, 100),
            Material("PEEK", 100, 1.3, 60.0, 250),
            Material("Fibra de Carbono", 600, 1.6, 35.0, 150),
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