from material import Material


class BaseDatosMateriales:

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