import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

from click import command
import databaseQuerys as dbQ
import opcionesAdmin
from tkinter import messagebox

class modAd:
    def __init__(self, top=None,idCuenta=None):

        def obtenerPelicula():
            titulo = self.Entry1.get()
            res = dbQ.addMovieThroughApi(titulo,idCuenta)
            if res:
                messagebox.showinfo(title="Exito", message="Se agrego la pelicula")
            else:
                messagebox.showerror(title="Error", message="No se encontro la pelicula")

        def cancelar():
            self.top = opcionesAdmin.opcionesAdmin(self.top,idCuenta=idCuenta)


        def eliminar():
            titulo = self.Entry2.get()
            dbQ.deleteMovie(titulo,idCuenta)
            messagebox.showinfo(title="Exito", message="Se elemino la pelicula")


        '''This class configures and populates the toplevel window.
            top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("443x450+660+210")
        top.minsize(120, 1)
        top.maxsize(3844, 1061)
        top.resizable(1,  1)
        top.title("Rutinas Admin")
        top.configure(background="#d9d9d9")

        self.top = top

        self.Frame1 = tk.Frame(self.top)
        self.Frame1.place(relx=-0.018, rely=0.0, relheight=1.033, relwidth=1.043)

        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#000000")

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.095, rely=0.022, height=51, width=330)
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#000000")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI} -size 16 -weight bold")
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(text='''Añadir pelicula por nombre''')

        self.Entry1 = tk.Entry(self.Frame1)
        self.Entry1.place(relx=0.087, rely=0.172, height=30, relwidth=0.571)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        self.Button1 = tk.Button(self.Frame1, command=obtenerPelicula)
        self.Button1.place(relx=0.087, rely=0.28, height=34, width=147)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#ffffff")
        self.Button1.configure(compound='left')
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#e1031e")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Buscar pelicula''')

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.095, rely=0.387, height=41, width=282)
        self.Label2.configure(anchor='w')
        self.Label2.configure(background="#000000")
        self.Label2.configure(compound='left')
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Segoe UI} -size 14 -weight bold")
        self.Label2.configure(foreground="#ffffff")
        self.Label2.configure(text='''Eliminar pelicula por nombre''')

        self.Entry2 = tk.Entry(self.Frame1)
        self.Entry2.place(relx=0.087, rely=0.516, height=30, relwidth=0.571)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")

        self.Button2 = tk.Button(self.Frame1,command=eliminar)
        self.Button2.place(relx=0.087, rely=0.667, height=34, width=147)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#ffffff")
        self.Button2.configure(compound='left')
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#e1031e")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Eliminar''')

        self.Button3 = tk.Button(self.Frame1, command=cancelar)
        self.Button3.place(relx=0.4, rely=0.800, height=34, width=147)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#ffffff")
        self.Button3.configure(compound='left')
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#e1031e")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Cancelar''')