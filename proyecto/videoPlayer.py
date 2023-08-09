import tkinter as tk
from tkinter import messagebox
import mainPage
from tkVideoPlayer import TkinterVideo
import sys
import tkinter.ttk as ttk
from tkinter.constants import *
import mainPage
import databaseQuerys as dbQ
import time
from datetime import datetime
class videoPlayer:
    def __init__(self, top=None,titulo=None,idCuenta=None,nombrePerfil=None,idUsuario=None,idPeliculaCapitulo=None):
        '''This class configures and populates the toplevel window.
            top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        

        def regresar():
            self.seguir = False
            self.top = mainPage.mainPage(self.top,idCuenta=idCuenta,nombrePerfil=nombrePerfil,idUsuario=idUsuario)

        def addToList():
            dbQ.addMovieToList(idPeliculaCapitulo,idUsuario)


        curr_time = time.localtime()
        curr_clock = time.strftime("%H:%M:%S", curr_time)
        
        dbQ.addMovieToWatchlist(idPeliculaCapitulo,idUsuario)
        dbQ.registrarSesion(idPeliculaCapitulo,datetime.date(datetime.now()),curr_clock,idUsuario)
        self.tipoCuenta = dbQ.getTipoCuentaWithId(idCuenta)
        top.geometry("851x614+306+138")
        top.minsize(120, 1)
        top.maxsize(3844, 1061)
        top.resizable(1,  1)
        top.title("netflix a la tortix")
        top.configure(background="#d9d9d9")

        self.top = top
        self.contador = 0
        self.seguir =True
        self.Frame1 = tk.Frame(self.top)
        self.Frame1.place(relx=0.0, rely=0.0, relheight=0.081, relwidth=1.004)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#000000")

        self.Button1 = tk.Button(self.Frame1,command=regresar)
        self.Button1.place(relx=0.012, rely=0.2, height=34, width=94)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#000000")
        self.Button1.configure(compound='left')
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family {Segoe UI} -size 14 -weight bold")
        self.Button1.configure(foreground="#ffffff")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''<-''')

        self.Button2 = tk.Button(self.Frame1,command=addToList)
        self.Button2.place(relx=0.72, rely=0.2, height=34, width=200)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#000000")
        self.Button2.configure(compound='left')
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.Button2.configure(foreground="#ffffff")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Añadir/Quitar de favoritos''')

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.129, rely=0.2, height=31, width=470)
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#000000")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Open Sans} -size 14 -weight bold")
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(text=f"{titulo}")

        self.Frame2 = tk.Frame(self.top)
        self.Frame2.place(relx=0.0, rely=0.081, relheight=0.92, relwidth=1.006)
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief="groove")
        self.Frame2.configure(background="#000000")
        self.Label1.after(1000, self.update)

        # videoPlayer = TkinterVideo(master=self.Frame2, scaled=True,pre_load=True)
        # videoPlayer.load(r"video.mp4")
        # videoPlayer.pack(expand=True,fill="both")
        # videoPlayer.play()

        
        
    def update(self):
        """ update the label every 1 second """
        self.contador=self.contador+1


        if self.contador ==5 and self.tipoCuenta==0:
            messagebox.showinfo(title="Anuncio", message="Este es un anuncio")
            self.contador = 0
            

        # schedule another timer
        if self.seguir:
            self.Label1.after(1000, self.update)

        

        

       