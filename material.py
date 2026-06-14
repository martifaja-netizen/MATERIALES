class Material:

    def __init__(self, nombre, resistencia, densidad, coste, temp_max):
        self.nombre = nombre
        self.resistencia = resistencia
        self.densidad = densidad
        self.coste = coste
        self.temp_max = temp_max

    def mostrar_info(self):
        print(f"Material: {self.nombre}")
        print(f"Resistencia: {self.resistencia} MPa")
        print(f"Densidad: {self.densidad} g/cm³")
        print(f"Coste: {self.coste} €/kg")
        print(f"Temperatura máxima: {self.temp_max} °C")

    def __str__(self):
        return self.nombre
    
    
    def cumple_filtro(self, filtro):
        return (
        self.resistencia >= filtro.res_min
        and self.densidad <= filtro.dens_max
        and self.coste <= filtro.coste_max
        and self.temp_max >= filtro.temp_min
        )