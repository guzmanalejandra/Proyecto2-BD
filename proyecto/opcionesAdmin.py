import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import createAdmin 
import genVistas
import modAd
import login
import databaseQuerys as dbQ
import htmlPlantilla
import webbrowser
import os
class opcionesAdmin:
    def __init__(self, top=None,idCuenta=None):

        def crearAdmin():
            self.top = createAdmin.createAdmin(self.top,idCuenta=idCuenta)


        def simular():
            self.top = genVistas.genVistas(self.top,idCuenta=idCuenta)


        def rutinas():
            self.top = modAd.modAd(self.top,idCuenta=idCuenta)

        def salir():
            self.top = login.login(self.top)

        def bitacora():
            datos = dbQ.getAdminData()
            tableContent =""
            first = htmlPlantilla.returnPlantillaADMIN()
            for i in datos:
                id = i[0]
                idAdmin = i[1]
                fecha = i[2]
                operacion = i[3]
                tableContent += f'''
                     <tr>
                  <td><h2>{id}</h2></td>
                  <td><h2>{idAdmin}</h2></td>
                  <td><h2>{fecha}</h2></td>
                  <td><h2>{operacion}</h2></td>
                </tr>
                '''
            last = htmlPlantilla.returnPlantilla2()
            file = open("./proyecto/indexa.html","w")
            file.write(first+tableContent+last)
            file.close()
            filename = 'file:///'+os.getcwd()+'/proyecto/' + 'indexa.html'
            webbrowser.open_new_tab(filename)




        '''This class configures and populates the toplevel window.
            top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("329x411+468+138")
        top.minsize(120, 1)
        top.maxsize(3844, 1061)
        top.resizable(1,  1)
        top.title("OpcionesAdmin")
        top.configure(background="#d9d9d9")

        self.top = top

        self.Frame1 = tk.Frame(self.top)
        self.Frame1.place(relx=0.0, rely=-0.049, relheight=1.071, relwidth=1.021)

        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#000000")

        self.Button1 = tk.Button(self.Frame1,command = crearAdmin)
        self.Button1.place(relx=0.268, rely=0.143, height=44, width=157)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#ffffff")
        self.Button1.configure(compound='left')
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#e1031e")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Crear admin''')

        self.Button2 = tk.Button(self.Frame1, command=rutinas)
        self.Button2.place(relx=0.268, rely=0.309, height=44, width=157)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#ffffff")
        self.Button2.configure(compound='left')
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#e1031e")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Rutinas admin''')

        self.Button3 = tk.Button(self.Frame1,command=bitacora)
        self.Button3.place(relx=0.268, rely=0.475, height=44, width=157)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#ffffff")
        self.Button3.configure(compound='left')
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#e1031e")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Bitácora''')

        self.Button4 = tk.Button(self.Frame1, command= simular)
        self.Button4.place(relx=0.268, rely=0.666, height=44, width=157)
        self.Button4.configure(activebackground="#ececec")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#ffffff")
        self.Button4.configure(compound='left')
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(foreground="#e1031e")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''Simulación de operaciones''')

        self.Button5 = tk.Button(self.Frame1, command= salir)
        self.Button5.place(relx=0.268, rely=0.850, height=44, width=157)
        self.Button5.configure(activebackground="#ececec")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="#ffffff")
        self.Button5.configure(compound='left')
        self.Button5.configure(disabledforeground="#a3a3a3")
        self.Button5.configure(foreground="#e1031e")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(text='''Salir''')

