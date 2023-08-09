# Importamos los modulos
import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import login
import profiles
import databaseQuerys as dbQ
import videoPlayer
#Root de la aplicación
root = tk.Tk()
#Pantalla a mostrar
my_gui = login.login(root)
root.mainloop()