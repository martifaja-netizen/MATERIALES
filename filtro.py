# Archivo: filtro.py
class Filtro:
    """
    Esta clase actúa como un 'contenedor' o 'sobre' de datos.
    Su único objetivo es empaquetar los 4 criterios de búsqueda que el usuario
    escribe en la pantalla de Tkinter para poder transportarlos juntos.
    """

    def __init__(self, res_min: float, dens_max: float, coste_max: float, temp_min: float):
        """
        El constructor recibe los 4 valores desde la interfaz:
        - res_min: La resistencia mínima exigida (ej. 300)
        - dens_max: La densidad máxima permitida (ej. 8.0)
        - coste_max: El precio máximo que se quiere pagar (ej. 10)
        - temp_min: La temperatura mínima que debe soportar (ej. 200)
        """
        self.res_min = res_min  # Guarda el límite inferior de Resistencia
        self.dens_max = dens_max  # Guarda el límite superior de Densidad
        self.coste_max = coste_max  # Guarda el límite superior de Coste
        self.temp_min = temp_min  # Guarda el límite inferior de Temperatura