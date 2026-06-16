# Archivo: gestor_materiales.py

# Importamos las clases que el gestor necesita para trabajar
from base_datos_materiales import BaseDatosMateriales
from filtro import Filtro


class GestorMateriales:
    """
    El Gestor actúa como el cerebro intermedio (Presentador).
    Su función es recibir las peticiones de la interfaz gráfica,
    comunicarse con la base de datos para obtener los resultados y
    devolvérselos a la pantalla.
    """

    def __init__(self):
        """
        Al crear el gestor, este crea automáticamente una instancia
        de la Base de Datos de materiales para tener acceso al catálogo.
        """
        # Usamos 'self.' para guardar la conexión con la base de datos
        self.bd = BaseDatosMateriales()
        #añado esto: 
        self.bd.cargar_materiales()


    def buscar(self, filtro: Filtro) -> list:
        """
        Recibe el objeto Filtro (con los datos que el usuario puso en la pantalla),
        le ordena a la base de datos que ejecute el filtrado y retorna
        la lista de materiales que cumplen con los requisitos.
        """
        # El gestor no busca él mismo; le pasa el "sobre" del filtro
        # a la base de datos con 'self.bd.filtrar(filtro)'
        resultados = self.bd.filtrar(filtro)

        # Devuelve la lista de materiales aprobados hacia la interfaz
        return resultados