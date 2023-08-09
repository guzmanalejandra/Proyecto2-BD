#Importamos los modulos a utilizar
from datetime import datetime
import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import databaseQuerys as dbQ
from tkinter import messagebox
import signup
import profiles
import opcionesAdmin
#Clase del login
class login:
    #Constructor
    def __init__(self, top=None):
        #Función para realizar un login
        def ingresarBtnClick():
            correo = self.Entry1.get()
            psw = self.Entry2.get()
            #Llamamos a la función login del modulo databaseQuerys
            resultado = dbQ.login(correo, psw)

            if resultado[1] == None:

                dbQ.registrarLogin(-1, datetime.date(datetime.now()),resultado[0])
            else:
                if resultado[2] == -1:
                    dbQ.registrarLoginAdministrador(resultado[1],datetime.date(datetime.now()))
                else:
                    dbQ.registrarLogin(resultado[1], datetime.date(datetime.now()),resultado[0])


            #Si obtenemos un valor True, el proceso fue exitoso
            if resultado[0]:
                #Cambiamos de pantalla a la pantalla de perfiles
                #Mandamos como parametro el Id de la cuenta en la que se hizo el login
                if resultado[2] == -1:
                    self.top = opcionesAdmin.opcionesAdmin(self.top,idCuenta=resultado[1])
                else:
                    self.top = profiles.profiles(self.top,idCuenta=resultado[1])
                
            #Ocurrio un error
            else:
                messagebox.showerror(title="Error", message="Correo y/o contraseña invalidos")

        #Función para cambiar a la pantalla de crear una cuenta
        def crearCuenta():
            self.top = signup.signup(self.top)

        #Colores de la ventana
        _bgcolor = '#d9d9d9'  
        _fgcolor = '#000000'  
        _compcolor = '#d9d9d9' 
        _ana1color = '#d9d9d9' 
        _ana2color = '#ececec'

        #Atributos de la ventana
        top.geometry("600x450+468+138")
        top.minsize(120, 1)
        top.maxsize(3844, 1061)
        top.resizable(1,  1)
        top.title("Netflix a la tortix")
        top.configure(background="#0d0000")

        #Widgets y su configuración
        self.top = top
        self.Frame2 = tk.Frame(self.top)
        self.Frame2.place(relx=0.0, rely=0.0, relheight=1, relwidth=1)
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief="groove")
        self.Frame2.configure(background="#000000")


        self.Label1 = tk.Label(self.Frame2)
        self.Label1.place(relx=0.333, rely=0.178, height=51, width=224)
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#000000")
        self.Label1.configure(compound='left')
        self.Label1.configure(cursor="fleur")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Open Sans} -size 18 -weight bold")
        self.Label1.configure(foreground="#e10000")
        self.Label1.configure(text='''Netflix a la tortix''')

        self.Frame1 = tk.Frame(self.Frame2)
        self.Frame1.place(relx=0.267, rely=0.289, relheight=0.589
                , relwidth=0.492)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#ffffff")

        self.Entry1 = tk.Entry(self.Frame1)
        self.Entry1.place(relx=0.339, rely=0.128, height=30, relwidth=0.454)
        self.Entry1.configure(background="white")
        self.Entry1.configure(cursor="fleur")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.136, rely=0.17, height=24, width=54)
        self.Label2.configure(anchor='w')
        self.Label2.configure(background="#ffffff")
        self.Label2.configure(compound='left')
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Usuario''')

        self.Label2_1 = tk.Label(self.Frame1)
        self.Label2_1.place(relx=0.068, rely=0.426, height=23, width=74)
        self.Label2_1.configure(activebackground="#f9f9f9")
        self.Label2_1.configure(activeforeground="black")
        self.Label2_1.configure(anchor='w')
        self.Label2_1.configure(background="#ffffff")
        self.Label2_1.configure(compound='left')
        self.Label2_1.configure(disabledforeground="#a3a3a3")
        self.Label2_1.configure(foreground="#000000")
        self.Label2_1.configure(highlightbackground="#d9d9d9")
        self.Label2_1.configure(highlightcolor="black")
        self.Label2_1.configure(text='''Contraseña''')

        self.Entry2 = tk.Entry(self.Frame1,show="*")
        self.Entry2.place(relx=0.339, rely=0.381, height=30, relwidth=0.454)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")

        self.Button1 = tk.Button(self.Frame1,command=ingresarBtnClick)
        self.Button1.place(relx=0.373, rely=0.638, height=34, width=97)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#ff2227")
        self.Button1.configure(compound='left')
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#ffffff")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Ingresar''')

        self.Button1_1 = tk.Button(self.Frame1,command=crearCuenta)
        self.Button1_1.place(relx=0.373, rely=0.83, height=34, width=97)
        self.Button1_1.configure(activebackground="#ececec")
        self.Button1_1.configure(activeforeground="#000000")
        self.Button1_1.configure(background="#ff2227")
        self.Button1_1.configure(compound='left')
        self.Button1_1.configure(disabledforeground="#a3a3a3")
        self.Button1_1.configure(foreground="#ffffff")
        self.Button1_1.configure(highlightbackground="#d9d9d9")
        self.Button1_1.configure(highlightcolor="black")
        self.Button1_1.configure(pady="0")
        self.Button1_1.configure(text='''Crear cuenta''')

