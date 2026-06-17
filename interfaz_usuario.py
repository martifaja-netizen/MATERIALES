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

        titulo = tk.Label(
            self.ventana,
            text="SELECTOR DE MATERIALES - INGENIERÍA MECÁNICA",
            font=("Arial", 16, "bold")
        )
        titulo.pack(pady=15)

        frame_filtros = tk.LabelFrame(
            self.ventana,
            text="Criterios de selección",
            padx=20,
            pady=15
        )
        frame_filtros.pack(pady=10)

        tk.Label(frame_filtros, text="Resistencia mínima (MPa):").grid(row=0, column=0, padx=10, pady=5)
        self.entry_res = tk.Entry(frame_filtros, width=20)
        self.entry_res.grid(row=1, column=0, padx=10, pady=5)

        tk.Label(frame_filtros, text="Densidad máxima (g/cm³):").grid(row=0, column=1, padx=10, pady=5)
        self.entry_dens = tk.Entry(frame_filtros, width=20)
        self.entry_dens.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(frame_filtros, text="Coste máximo (€/kg):").grid(row=2, column=0, padx=10, pady=5)
        self.entry_coste = tk.Entry(frame_filtros, width=20)
        self.entry_coste.grid(row=3, column=0, padx=10, pady=5)

        tk.Label(frame_filtros, text="Temperatura mínima (°C):").grid(row=2, column=1, padx=10, pady=5)
        self.entry_temp = tk.Entry(frame_filtros, width=20)
        self.entry_temp.grid(row=3, column=1, padx=10, pady=5)

        self.boton_buscar = tk.Button(
            self.ventana,
            text="BUSCAR",
            width=20,
            command=self.buscar_materiales
        )
        self.boton_buscar.pack(pady=15)

        frame_resultados = tk.LabelFrame(
            self.ventana,
            text="Resultados",
            padx=10,
            pady=10
        )
        frame_resultados.pack(pady=10, fill="x", padx=30)

        columnas = ("material", "resistencia", "densidad", "coste", "temp_max")

        self.tabla_resultados = ttk.Treeview(
            frame_resultados,
            columns=columnas,
            show="headings",
            height=8
        )

        self.tabla_resultados.heading("material", text="Material")
        self.tabla_resultados.heading("resistencia", text="Resistencia (MPa)")
        self.tabla_resultados.heading("densidad", text="Densidad (g/cm³)")
        self.tabla_resultados.heading("coste", text="Coste (€/kg)")
        self.tabla_resultados.heading("temp_max", text="Temp. Máx. (°C)")

        self.tabla_resultados.column("material", width=220)
        self.tabla_resultados.column("resistencia", width=140, anchor="center")
        self.tabla_resultados.column("densidad", width=140, anchor="center")
        self.tabla_resultados.column("coste", width=120, anchor="center")
        self.tabla_resultados.column("temp_max", width=140, anchor="center")

        self.tabla_resultados.pack(fill="x")

        self.buscar_materiales() #linea extra para ver todos los materiales


    def ejecutar(self):
        self.ventana.mainloop()

#añadida la opcion de buscar con el campo vacio
    def buscar_materiales(self):

        filtro = Filtro(
            self.obtener_valor(self.entry_res, 0),
            self.obtener_valor(self.entry_dens, 999999),
            self.obtener_valor(self.entry_coste, 999999),
            self.obtener_valor(self.entry_temp, 0)
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
    def obtener_valor(self, entrada, valor_por_defecto):
        texto = entrada.get()

        if texto == "":
            return valor_por_defecto

        return float(texto)