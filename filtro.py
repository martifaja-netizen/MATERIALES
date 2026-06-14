# Archivo: filtro.py
class Filtro:
    """
    Esta clase actúa como un 'contenedor' o 'sobre' de datos.
    Su único objetivo es empaquetar los 4 criterios de búsqueda que se
    escribe en la pantalla para poder transportarlos juntos.
    """

    def __init__(self, res_min: float, dens_max: float, coste_max: float, temp_min: float):
        """
        El constructor recibe los 4 valores desde la interfaz:
        - res_min: La resistencia mínima exigida
        - dens_max: La densidad máxima permitida
        - coste_max: El precio máximo que se quiere pagar
        - temp_min: La temperatura mínima que debe soportar
        """
        self.res_min = res_min
        self.dens_max = dens_max
        self.coste_max = coste_max
        self.temp_min = temp_min