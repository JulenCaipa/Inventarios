import customtkinter as ctk
import tkinter as tk
import sys
import os

# Importar las GUIs de actas y contratos

from Actas.Acta_de_entrega import EntregaApp
from Actas.Acta_Restitucion import RestitucionApp
from Actas.Acta_pre_Visita import PreVisitaApp

# Para contratos, se asume que la interfaz está en 'interfaz.py' y se ejecuta como script

def abrir_entrega():
    win = EntregaApp()
    win.mainloop()

def abrir_restitucion():
    win = RestitucionApp()
    win.mainloop()


def abrir_previsita():
    win = PreVisitaApp()
    win.mainloop()

def abrir_contratos():
    # Ejecutar el script de contratos (interfaz.py) correctamente desde .exe o script, evitando problemas con espacios en el nombre del ejecutable
    import sys
    import os
    import subprocess
    if getattr(sys, 'frozen', False):
        # Ejecutable PyInstaller: usa la ruta del bundle
        base_path = sys._MEIPASS
        script_path = os.path.join(base_path, 'interfaz.py')
        python_exec = '/usr/bin/python3'  # Ruta estándar en macOS
        subprocess.Popen([python_exec, script_path])
    else:
        os.system(f'{sys.executable} interfaz.py')

class MainMenu(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Menú Principal")
        self.geometry("400x300")
        self.minsize(400, 300)
        self.resizable(False, False)

        ctk.CTkLabel(self, text="Seleccione una opción", font=("Arial", 20, "bold")).pack(pady=30)

        btn_actas = ctk.CTkButton(self, text="Actas", width=200, height=40, font=("Arial", 16), command=self.menu_actas)
        btn_actas.pack(pady=15)

        btn_contratos = ctk.CTkButton(self, text="Contratos", width=200, height=40, font=("Arial", 16), command=abrir_contratos)
        btn_contratos.pack(pady=15)

    def menu_actas(self):
        ventana = tk.Toplevel(self)
        ventana.title("Actas")
        ventana.geometry("350x300")
        ctk.CTkLabel(ventana, text="Seleccione el tipo de acta", font=("Arial", 16, "bold")).pack(pady=20)
        ctk.CTkButton(ventana, text="Acta de Entrega", width=180, height=35, command=abrir_entrega).pack(pady=10)
        ctk.CTkButton(ventana, text="Acta de Restitución", width=180, height=35, command=abrir_restitucion).pack(pady=10)
        ctk.CTkButton(ventana, text="Acta Pre-Visita", width=180, height=35, command=abrir_previsita).pack(pady=10)

if __name__ == "__main__":
    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("blue")
    app = MainMenu()
    app.mainloop()
