from filtro import Filtro
from base_datos_materiales import BaseDatosMateriales


bd = BaseDatosMateriales()
bd.cargar_materiales()

materiales = bd.obtener_todos()

filtro = Filtro(
    300,
    8.0,
    10.0,
    200
)

for material in materiales:
    if material.cumple_filtro(filtro):
        print("CUMPLE:")
        material.mostrar_info()
        print("---------------------")