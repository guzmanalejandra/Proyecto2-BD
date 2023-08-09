#Importamos los modulos
import imp
import sys
import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
from tkinter.constants import *
import databaseQuerys as dbQ
import createProfile
import login
import mainPage 
import configurarCuenta as cC
#Clase de perfiles
class profiles:
    #Constructor
    def __init__(self,top=None,idCuenta=None):
        
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
        top.title("Perfiles")
        top.configure(background="#d9d9d9")
        
        self.tipoCuenta = dbQ.getTipoCuentaWithId(idCuenta)
        #Función para cerrar la sesión
        def logout():
            self.top = login.login(self.top)


        def goToMainPageWithUser(name,id,idCuenta):
            self.top = mainPage.mainPage(self.top,idCuenta=idCuenta,nombrePerfil=name,idUsuario=id)
            # messagebox.showerror(title="navegar", message=f"Ingreso con {name} con id {id} de la cuenta {idCuenta}")

        
        #Función para crear los botones de los perfiles de una cuenta
        # @param perfiles -> lista de nombres de los perfiles
        
        def generateProfilesButtons(perfiles):
            contador = 0
            cantidadMaxima = 8 if self.tipoCuenta==2 else ( 4 if self.tipoCuenta==1 else 1)
            self.botones = []
            for i in range(0,len(perfiles)):
                self.botones.append(tk.Button(self.Frame2))
                if i<4:
                    self.botones[i].place(relx=0.1+(i*0.2), rely=0.05, height=120, width=80)
                else:
                    self.botones[i].place(relx=0.1+((i%4)*0.2), rely=0.5, height=120, width=80)
                
                color ="#045762" if contador<cantidadMaxima else "#112f33"

                if(contador<cantidadMaxima):
                    self.botones[i].bind('<Button-1>',lambda event,nombre=perfiles[i]["nombre"],
                                                               id=perfiles[i]["id"],
                                                               idCuenta=perfiles[i]["idCuenta"]: goToMainPageWithUser(nombre,id,idCuenta))
                contador = contador+1
                self.botones[i].configure(activebackground="#045762")
                self.botones[i].configure(activeforeground="#FFF")
                self.botones[i].configure(background=color)
                self.botones[i].configure(compound='left')
                self.botones[i].configure(disabledforeground="#a3a3a3")
                self.botones[i].configure(foreground="#FFF")
                self.botones[i].configure(highlightbackground="#d9d9d9")
                self.botones[i].configure(highlightcolor="black")
                self.botones[i].configure(pady="0")
                self.botones[i].configure(text=str(perfiles[i]["nombre"]))
                
        
        #Función para cambiar de pantalla a la de crear un perfil
        def crearPerfil():
            self.top = createProfile.createProfile(self.top,idCuenta=idCuenta)


        def configurarPerfil():
            self.top = cC.configurar(self.top,idCuenta=idCuenta)



        #Widgets y su configuración
        self.top = top

        self.Frame1 = tk.Frame(self.top)
        self.Frame1.place(relx=0.0, rely=0.0, relheight=1, relwidth=1)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#000000")

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.397, rely=0.088, height=51, width=134)
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#000000")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Open Sans} -size 18 -weight bold")
        self.Label1.configure(foreground="#ff0000")
        self.Label1.configure(text='''Perfiles''')

        self.Frame2 = tk.Frame(self.Frame1)
        self.Frame2.place(relx=0.099, rely=0.22, relheight=0.692, relwidth=0.77)
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief="groove")
        self.Frame2.configure(background="#000000")

        centrar = 0.10
        self.Button2 = tk.Button(self.Frame1,command=crearPerfil)
        self.Button2.place(relx=0.273-centrar, rely=0.91, height=34, width=97)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#ff2227")
        self.Button2.configure(compound='left')
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#ffffff")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Crear perfil''')

        self.Button3 = tk.Button(self.Frame1,command=logout)
        self.Button3.place(relx=0.5-centrar, rely=0.91, height=34, width=97)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#fff")
        self.Button3.configure(compound='left')
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#ff2227")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''logout''')

        self.Button4 = tk.Button(self.Frame1,command=configurarPerfil)
        self.Button4.place(relx=0.7-centrar, rely=0.91, height=34, width=110)
        self.Button4.configure(activebackground="#ececec")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#fff")
        self.Button4.configure(compound='left')
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(foreground="#ff2227")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''Configurar cuenta''')

        listaPerfiles = []
        profiles = dbQ.getProfilesWithAccountId(idCuenta)

        for r in profiles:
            # listaPerfiles.append(r[2])
            listaPerfiles.append({"id":r[0],"idCuenta":r[1],"nombre":r[2],"infantil":r[3]})
        generateProfilesButtons(listaPerfiles)


     
        




