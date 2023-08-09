import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
from tkinter import messagebox
import htmlPlantilla
import datetime
import databaseQuerys as dbQ
import random
import webbrowser
import os
import opcionesAdmin
class genVistas:
    def __init__(self, top=None,idCuenta=None):
        '''This class configures and populates the toplevel window.
            top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        def genHTML(vistas,fecha):
            firstPart = htmlPlantilla.returnPlantilla1()
            usuarios = dbQ.getListaUsuariosA()
            peliculas = dbQ.getListaPeliculasA()
            tableContent = ""
            dbQ.deleteDataSimulacion()
            for vista in range(0,vistas):
                hours = random.randint(1, 23)
                minutes = random.randint(0, 59)
                seconds = random.randint(0, 59)
                random_hour = f"{hours}:{minutes}:{seconds}"
                randomMovie = random.choice(peliculas)
                movieTitle = randomMovie[1]
                movieId = randomMovie[0]
                randomUser = random.choice(usuarios)
                userName = randomUser[1]
                userId = randomUser[0]
                tableContent +=f''' <tr>
                  <td><h2>{vista+1}</h2></td>
                  <td><h2>{movieTitle}</h2></td>
                  <td><h2>{userName}</h2></td>
                  <td><h2>{fecha}</h2></td>
                  <td><h2>{random_hour}</h2></td>
                </tr>
                '''
                dbQ.saveDataSimulation(movieId,movieTitle,userId,userName,fecha,random_hour)
            lastPart = htmlPlantilla.returnPlantilla2()
            file = open("./proyecto/index.html","w")
            file.write(firstPart+tableContent+lastPart)
            file.close()
            filename = 'file:///'+os.getcwd()+'/proyecto/' + 'index.html'
            webbrowser.open_new_tab(filename)
            
            self.top = opcionesAdmin.opcionesAdmin(self.top,idCuenta=idCuenta)
            

            
        def validate():
            vistas = self.Entry1.get()
            fecha = self.Entry2.get()

            try:
                vistas =int(vistas)
                fecha =  datetime.datetime.strptime(fecha, '%Y-%m-%d')
                genHTML(vistas,fecha.strftime('%Y-%m-%d'))
            except Exception as e:
                messagebox.showerror(title="Datos invalidos", message="Asegurese que los datos son validos")

        def salir():
            self.top = opcionesAdmin.opcionesAdmin(self.top,idCuenta=idCuenta)

        top.geometry("600x450+660+210")
        top.minsize(120, 1)
        top.maxsize(3844, 1061)
        top.resizable(1,  1)
        top.title("Toplevel 0")
        top.configure(background="#d9d9d9")

        self.top = top

        self.Frame1 = tk.Frame(self.top)
        self.Frame1.place(relx=-0.017, rely=-0.022, relheight=1.033
                , relwidth=1.025)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#000000")

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.098, rely=0.086, height=41, width=224)
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#000000")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI} -size 22 -weight bold")
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(justify='right')
        self.Label1.configure(text='''Cantidad vistas''')

        self.Entry1 = tk.Entry(self.Frame1)
        self.Entry1.place(relx=0.537, rely=0.108, height=30, relwidth=0.299)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        self.Label1_1 = tk.Label(self.Frame1)
        self.Label1_1.place(relx=0.098, rely=0.28, height=41, width=224)
        self.Label1_1.configure(activebackground="#f9f9f9")
        self.Label1_1.configure(activeforeground="black")
        self.Label1_1.configure(anchor='w')
        self.Label1_1.configure(background="#000000")
        self.Label1_1.configure(compound='left')
        self.Label1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1.configure(font="-family {Segoe UI} -size 22 -weight bold")
        self.Label1_1.configure(foreground="#ffffff")
        self.Label1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1.configure(highlightcolor="black")
        self.Label1_1.configure(justify='right')
        self.Label1_1.configure(text='''Fecha''')

        self.Entry2 = tk.Entry(self.Frame1)
        self.Entry2.place(relx=0.537, rely=0.301, height=30, relwidth=0.299)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.098, rely=0.366, height=31, width=154)
        self.Label2.configure(anchor='w')
        self.Label2.configure(background="#000000")
        self.Label2.configure(compound='left')
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#ffffff")
        self.Label2.configure(text='''Year-Month-Day''')

        self.Button1 = tk.Button(self.Frame1, command=validate)
        self.Button1.place(relx=0.325, rely=0.581, height=34, width=197)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#ffffff")
        self.Button1.configure(compound='left')
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#e1031e")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Generar Vistas''')

        self.Button2 = tk.Button(self.Frame1, command=salir)
        self.Button2.place(relx=0.325, rely=0.688, height=34, width=197)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#ffffff")
        self.Button2.configure(compound='left')
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#e1031e")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Salir''')