"""
Clase Material.

Representa un material individual del catálogo.

Cada objeto Material almacena las propiedades necesarias
para realizar búsquedas y comparaciones dentro de la aplicación:

- nombre
- resistencia mecánica
- densidad
- coste
- temperatura máxima de trabajo

Además, proporciona métodos para mostrar la información
del material y comprobar si cumple un determinado filtro.
"""
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