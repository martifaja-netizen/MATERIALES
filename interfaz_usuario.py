# Archivo: interfaz_usuario.py

"""
Clase InterfazUsuario.

Implementa la interfaz gráfica de la aplicación mediante Tkinter.
Permite introducir criterios de búsqueda, crear un objeto Filtro,
consultar el GestorMateriales y mostrar los resultados en una tabla.
"""

import tkinter as tk
from tkinter import ttk, messagebox

from gestor_materiales import GestorMateriales
from filtro import Filtro


class InterfazUsuario:

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Selector de Materiales")
        self.ventana.geometry("900x600")

        self.gestor = GestorMateriales()

    #colores de la interfaz
        COLOR_FONDO = "#eef0f4"
        COLOR_AZUL = "#2f67b1"
        COLOR_BLANCO = "#ffffff"
        COLOR_TEXTO = "#2f3747"

        self.ventana.configure(bg=COLOR_FONDO)

    #titulo y encabezado de la interfaz
        header = tk.Frame(
            self.ventana,
            bg=COLOR_AZUL,
            height=80
        )
        header.pack(fill="x")

        titulo = tk.Label(
            header,
            text="SELECTOR DE MATERIALES - INGENIERÍA MECÁNICA",
            bg=COLOR_AZUL,
            fg="white",
            font=("Arial", 18, "bold")
        )
        titulo.pack(pady=22)

        #label frame para los filtros de busqueda
        frame_filtros = tk.LabelFrame(
            self.ventana,
            text="Criterios de selección",
            bg=COLOR_BLANCO,
            fg=COLOR_TEXTO,
            font=("Arial", 11, "bold"),
            padx=30,
            pady=20
        )
        frame_filtros.pack(pady=25)

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

        #botones de busqueda y limpiar campos
        self.boton_buscar = tk.Button(
            self.ventana,
            text="BUSCAR",
            width=25,
            bg=COLOR_AZUL,
            fg="white",
            font=("Arial", 11, "bold"),
            command=self.buscar_materiales
        )
        self.boton_buscar.pack(pady=10)

        self.boton_limpiar = tk.Button(
            self.ventana,
            text="LIMPIAR CAMPOS",
            width=25,
            bg=COLOR_AZUL,
            fg="white",
            font=("Arial", 10, "bold"),
            command=self.limpiar_campos
        )
        self.boton_limpiar.pack(pady=5)
    # resultados de la busqueda en una tabla
        frame_resultados = tk.LabelFrame(
            self.ventana,
            text="Resultados",
            bg=COLOR_BLANCO,
            fg=COLOR_TEXTO,
            font=("Arial", 11, "bold"),
            padx=10,
            pady=10
        )
        frame_resultados.pack(pady=20, fill="x", padx=40)

        columnas = ("material", "resistencia", "densidad", "coste", "temp_max")


        estilo = ttk.Style()
        estilo.theme_use("default")

        estilo.configure(
            "Treeview",
            background="white",
            foreground="#2f3747",
            rowheight=28,
            fieldbackground="white",
            font=("Arial", 10),
            bordercolor="#d0d0d0",
            borderwidth=1,
            relief="solid"
        )

        estilo.configure(
            "Treeview.Heading",
            background=COLOR_AZUL,
            foreground="white",
            font=("Arial", 10, "bold")
        )

        estilo.map(
            "Treeview.Heading",
            background=[("active", COLOR_AZUL)]
        )



        self.tabla_resultados = ttk.Treeview(
            frame_resultados,
            columns=columnas,
            show="headings",
            height=10
        )


        self.tabla_resultados.tag_configure(
            "fila_par",
            background="#ffffff"
        )

        self.tabla_resultados.tag_configure(
            "fila_impar",
            background="#f2f2f2"
        )



        self.tabla_resultados.heading("material", text="Material",
                                      command=lambda: self.ordenar_columna("material", True))
        self.tabla_resultados.heading("resistencia", text="Resistencia (MPa)",
                                      command=lambda: self.ordenar_columna("resistencia", True))
        self.tabla_resultados.heading("densidad", text="Densidad (g/cm³)",
                                      command=lambda: self.ordenar_columna("densidad", True))
        self.tabla_resultados.heading("coste", text="Coste (€/kg)",
                                      command=lambda: self.ordenar_columna("coste", True))
        self.tabla_resultados.heading("temp_max", text="Temp. Máx. (°C)",
                                      command=lambda: self.ordenar_columna("temp_max", True))

        self.tabla_resultados.column("material", width=260, anchor="w")
        self.tabla_resultados.column("resistencia", width=150, anchor="center")
        self.tabla_resultados.column("densidad", width=150, anchor="center")
        self.tabla_resultados.column("coste", width=130, anchor="center")
        self.tabla_resultados.column("temp_max", width=150, anchor="center")

        self.tabla_resultados.pack(fill="x")

        self.buscar_materiales() #linea extra para ver todos los materiales


    def ejecutar(self):
        self.ventana.mainloop()

#añadida la opcion de buscar con el campo vacio
    def buscar_materiales(self):

        try:
            filtro = Filtro(
                self.obtener_valor(self.entry_res, 0),
                self.obtener_valor(self.entry_dens, 999999),
                self.obtener_valor(self.entry_coste, 999999),
                self.obtener_valor(self.entry_temp, 0)
            )

        except ValueError:
            messagebox.showerror(
                "Error de entrada",
                "Introduce solo valores numéricos en los campos."
            )
            return

        resultados = self.gestor.buscar(filtro)

        for fila in self.tabla_resultados.get_children():
            self.tabla_resultados.delete(fila)

        if len(resultados) == 0:
            messagebox.showinfo(
                "Sin resultados",
                "No se han encontrado materiales que cumplan los criterios."
            )
            return

        for i, material in enumerate(resultados):

            etiqueta_fila = "fila_par" if i % 2 == 0 else "fila_impar"

            self.tabla_resultados.insert(
                "",
                tk.END,
                values=(
                    material.nombre,
                    material.resistencia,
                    material.densidad,
                    material.coste,
                    material.temp_max
                ),
                tags=(etiqueta_fila,)
            )

            
    def obtener_valor(self, entrada, valor_por_defecto):
        texto = entrada.get()

        if texto == "":
            return valor_por_defecto

        return float(texto)

    def ordenar_columna(self, columna, reverse):

        # 1. Extraemos todas las filas actuales de la tabla
        filas = []
        for k in self.tabla_resultados.get_children(""):
            val = self.tabla_resultados.set(k, columna)

            # Si la columna es numérica, convertimos el texto a float para ordenar bien matemáticamente
            if columna != "material":
                val = float(val)

            filas.append((val, k))

        # 2. Ordenamos la lista
        filas.sort(reverse=reverse)

        # 3. Reorganizamos las filas visualmente en la tabla según el nuevo orden
        for index, (val, k) in enumerate(filas):
            self.tabla_resultados.move(k, "", index)

        # 4.Hacemos que si vuelve a clickar la MISMA columna, ahora se ordene al revés
        self.tabla_resultados.heading(columna, command=lambda: self.ordenar_columna(columna, not reverse))

    def limpiar_campos(self):
        self.entry_res.delete(0, tk.END)
        self.entry_dens.delete(0, tk.END)
        self.entry_coste.delete(0, tk.END)
        self.entry_temp.delete(0, tk.END)

        self.buscar_materiales()
