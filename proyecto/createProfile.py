#Importamos los modulos a utilizar
import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import databaseQuerys as dbQ
from tkinter import messagebox
import login
import re
import profiles as profiles

#Clase de crear un perfil
class createProfile:
    #Constructor
    #  @param idCuenta -> id de la cuenta 
    def __init__(self, top=None,idCuenta=None):

        #Función para cambiar de pantalla 
        #Como estamos cancelando el crear un perfil, nos lleva a la pantalla de perfiles
        def cancelar():
            self.top = profiles.profiles(self.top,idCuenta=idCuenta)

        #Función que nos permite crear un perfil
        def crearPerfil():
            nombre = self.Entry1.get()
            infantil = self.TCombobox1.get()
            tipo = True if infantil=="Infantil" else False
            #Llamamos a la función createProfile del modulo databaseQuerys
            result = dbQ.createProfile(idCuenta,nombre,tipo)
            #Si retorna un valor True, se logro realizar la consulta y procedemos a cambiar de pantalla
            if result:
                self.top = profiles.profiles(self.top,idCuenta=idCuenta)
            


      
        #Colores de la ventana
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])
        
        #Atributos de la pantalla
        top.geometry("600x450+468+138")
        top.minsize(120, 1)
        top.maxsize(3844, 1061)
        top.resizable(1,  1)
        top.title("Crear perfil")
        top.configure(background="#020202")
        

        self.top = top
        #Frame que contiene todo
        self.todo = tk.Frame(self.top)
        self.todo.place(relx=0.0, rely=0.0, relheight=1, relwidth=1)
        self.todo.configure(relief='groove')
        self.todo.configure(borderwidth="2")
        self.todo.configure(relief="groove")
        self.todo.configure(background="#000000")
        

        #Widgets y configuración
        self.combobox = tk.StringVar()
        self.top.configure(background="#000")
        self.Label1 = tk.Label(self.todo)
        self.Label1.place(relx=0.35, rely=0.089, height=61, width=184)
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#0d0000")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Open Sans} -size 18 -weight bold")
        self.Label1.configure(foreground="#ff0000")
        self.Label1.configure(text='''Crear Perfil''')

        self.Frame1 = tk.Frame(self.todo)
        self.Frame1.place(relx=0.183, rely=0.2, relheight=0.722, relwidth=0.658)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#ffffff")

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.101, rely=0.154, height=21, width=74)
        self.Label2.configure(anchor='w')
        self.Label2.configure(background="#ffffff")
        self.Label2.configure(compound='center')
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Nombre''')

        

        self.TCombobox1 = ttk.Combobox(self.Frame1)
        self.TCombobox1['values']=('Infantil','Normal')
        self.TCombobox1.current(1)

        self.TCombobox1['state']='readonly'

        self.TCombobox1.place(relx=0.43, rely=0.492, relheight=0.095
                , relwidth=0.463)
       
        self.TCombobox1.configure(takefocus="")

        self.Label2_1_1 = tk.Label(self.Frame1)
        self.Label2_1_1.place(relx=0.101, rely=0.492, height=21, width=74)
        self.Label2_1_1.configure(activebackground="#f9f9f9")
        self.Label2_1_1.configure(activeforeground="black")
        self.Label2_1_1.configure(anchor='w')
        self.Label2_1_1.configure(background="#ffffff")
        self.Label2_1_1.configure(compound='center')
        self.Label2_1_1.configure(disabledforeground="#a3a3a3")
        self.Label2_1_1.configure(foreground="#000000")
        self.Label2_1_1.configure(highlightbackground="#d9d9d9")
        self.Label2_1_1.configure(highlightcolor="black")
        self.Label2_1_1.configure(text='''Tipo Cuenta''')

        self.Entry1 = tk.Entry(self.Frame1)
        self.Entry1.place(relx=0.43, rely=0.154, height=30, relwidth=0.466)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        

        self.Button1 = tk.Button(self.Frame1,command=crearPerfil)
        self.Button1.place(relx=0.354, rely=0.708, height=34, width=97)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#ff0000")
        self.Button1.configure(compound='left')
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#ffffff")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Crear perfil''')

        self.Button1_1 = tk.Button(self.Frame1,command=cancelar)
        self.Button1_1.place(relx=0.354, rely=0.862, height=34, width=97)
        self.Button1_1.configure(activebackground="#ececec")
        self.Button1_1.configure(activeforeground="#000000")
        self.Button1_1.configure(background="#ffffff")
        self.Button1_1.configure(compound='left')
        self.Button1_1.configure(disabledforeground="#a3a3a3")
        self.Button1_1.configure(foreground="#ff0000")
        self.Button1_1.configure(highlightbackground="#d9d9d9")
        self.Button1_1.configure(highlightcolor="#ff0000")
        self.Button1_1.configure(pady="0")
        self.Button1_1.configure(text='''Cancelar''')    
