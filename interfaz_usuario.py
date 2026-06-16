# Archivo: interfaz_usuario.py

"""
Clase InterfazUsuario.

Implementa la interfaz gráfica de la aplicación mediante Tkinter.
Permite introducir criterios de búsqueda, crear un objeto Filtro,
consultar el GestorMateriales y mostrar los resultados en una tabla.
"""

import tkinter as tk
from tkinter import ttk

from gestor_materiales import GestorMateriales
from filtro import Filtro


class InterfazUsuario:

    def __init__(self):

        self.ventana = tk.Tk()
        self.ventana.title("Selector de Materiales")
        self.ventana.geometry("900x600")

        self.gestor = GestorMateriales()

        tk.Label(self.ventana, text="Resistencia mínima").pack()
        self.entry_res = tk.Entry(self.ventana)
        self.entry_res.pack()

        tk.Label(self.ventana, text="Densidad máxima").pack()
        self.entry_dens = tk.Entry(self.ventana)
        self.entry_dens.pack()

        tk.Label(self.ventana, text="Coste máximo").pack()
        self.entry_coste = tk.Entry(self.ventana)
        self.entry_coste.pack()

        tk.Label(self.ventana, text="Temperatura mínima").pack()
        self.entry_temp = tk.Entry(self.ventana)
        self.entry_temp.pack()

        self.boton_buscar = tk.Button(
            self.ventana,
            text="Buscar",
            command=self.buscar_materiales
        )
        self.boton_buscar.pack(pady=20)

        columnas = ("material", "resistencia", "densidad", "coste", "temp_max")

        self.tabla_resultados = ttk.Treeview(
            self.ventana,
            columns=columnas,
            show="headings",
            height=8
        )

        self.tabla_resultados.heading("material", text="Material")
        self.tabla_resultados.heading("resistencia", text="Resistencia (MPa)")
        self.tabla_resultados.heading("densidad", text="Densidad (g/cm³)")
        self.tabla_resultados.heading("coste", text="Coste (€/kg)")
        self.tabla_resultados.heading("temp_max", text="Temp. Máx. (°C)")

        self.tabla_resultados.pack(pady=10)

    def ejecutar(self):
        self.ventana.mainloop()

    def buscar_materiales(self):

        filtro = Filtro(
            float(self.entry_res.get()),
            float(self.entry_dens.get()),
            float(self.entry_coste.get()),
            float(self.entry_temp.get())
        )

        resultados = self.gestor.buscar(filtro)

        for fila in self.tabla_resultados.get_children():
            self.tabla_resultados.delete(fila)

        for material in resultados:
            self.tabla_resultados.insert(
                "",
                tk.END,
                values=(
                    material.nombre,
                    material.resistencia,
                    material.densidad,
                    material.coste,
                    material.temp_max
                )
            )