import tkinter as tk

from gestor_materiales import GestorMateriales
from filtro import Filtro


class InterfazUsuario:

    def __init__(self):

        self.ventana = tk.Tk()
        self.ventana.title("Selector de Materiales")
        self.ventana.geometry("800x600")

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

        self.texto_resultados = tk.Text(self.ventana, height=10, width=60)
        self.texto_resultados.pack()

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

        self.texto_resultados.delete("1.0", tk.END)

        for material in resultados:
            self.texto_resultados.insert(tk.END, str(material) + "\n")