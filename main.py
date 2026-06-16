"""
Punto de entrada de la aplicación.

Este archivo inicia el programa creando una instancia
de la InterfazUsuario y ejecutando el bucle principal
de Tkinter.

A partir de este punto, toda la interacción se realiza
a través de la interfaz gráfica.
"""
from interfaz_usuario import InterfazUsuario

app = InterfazUsuario()
app.ejecutar()