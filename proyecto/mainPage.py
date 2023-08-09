from enum import auto
import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
from PIL import Image, ImageTk
import urllib.request
from io import BytesIO
import databaseQuerys as dbQ
from sympy import source
import apiManager as aM
import profiles
import json
import videoPlayer
import Buscar
class mainPage:
    def __init__(self, top=None,idCuenta=None,nombrePerfil=None,idUsuario=None,):
        '''This class configures and populates the toplevel window.
            top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        def logout():
            self.top = profiles.profiles(self.top,idCuenta=idCuenta)


        def viewContent(title,idPeliculaCapitulo):
            # videoR(title).run()
            self.top = videoPlayer.videoPlayer(self.top,titulo=title,idCuenta=idCuenta,nombrePerfil=nombrePerfil,idUsuario=idUsuario,idPeliculaCapitulo=idPeliculaCapitulo)

        def buscar():
            self.top = Buscar.Buscar(self.top,)
            
        top.geometry("1026x745+177+22")
        top.minsize(120, 1)
        top.maxsize(3844, 1061)
        top.resizable(1,  1)
        top.title("Netflix")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")
        self.top = top
        self.Frame1 = tk.Frame(self.top)
        self.Frame1.place(relx=0.00, rely=0.0, relheight=1, relwidth=1)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#000000")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")
        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.01, rely=-0.013, height=101, width=503)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#000000")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Open Sans} -size 21 -weight bold")
        self.Label1.configure(foreground="#ff0000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Netflix a la tortrix''')

        self.Button2 = tk.Button(self.Frame1,command=buscar)
        self.Button2.place(relx=0.7,  rely=0.027, height=54, width=127)
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
        self.Button2.configure(text='''Buscar''')


        self.Button1 = tk.Button(self.Frame1,command=logout)
        self.Button1.place(relx=0.841, rely=0.027, height=54, width=127)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#000000")
        self.Button1.configure(borderwidth="1")
        self.Button1.configure(compound='left')
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        photo_location = "./proyecto/src/icons8-logout-30.png"
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.Button1.configure(image=_img0)
        self.Button1.configure(pady="0")
        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.01, rely=0.08, height=67, width=212)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(anchor='w')
        self.Label2.configure(background="#000000")
        self.Label2.configure(compound='center')
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Open Sans} -size 14 -weight bold")
        self.Label2.configure(foreground="#ffffff")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Para ti''')
        self.Label2_1 = tk.Label(self.Frame1)
        self.Label2_1.place(relx=0.01, rely=0.350, height=67, width=264)
        self.Label2_1.configure(activebackground="#f9f9f9")
        self.Label2_1.configure(activeforeground="black")
        self.Label2_1.configure(anchor='w')
        self.Label2_1.configure(background="#000000")
        self.Label2_1.configure(compound='center')
        self.Label2_1.configure(disabledforeground="#a3a3a3")
        self.Label2_1.configure(font="-family {Open Sans} -size 14 -weight bold")
        self.Label2_1.configure(foreground="#ffffff")
        self.Label2_1.configure(highlightbackground="#d9d9d9")
        self.Label2_1.configure(highlightcolor="black")
        self.Label2_1.configure(text='''Seguir viendo''')
        self.Label2_1_1 = tk.Label(self.Frame1)
        self.Label2_1_1.place(relx=0.01, rely=0.650, height=67, width=259)
        self.Label2_1_1.configure(activebackground="#f9f9f9")
        self.Label2_1_1.configure(activeforeground="black")
        self.Label2_1_1.configure(anchor='w')
        self.Label2_1_1.configure(background="#000000")
        self.Label2_1_1.configure(compound='center')
        self.Label2_1_1.configure(disabledforeground="#a3a3a3")
        self.Label2_1_1.configure(font="-family {Open Sans} -size 14 -weight bold")
        self.Label2_1_1.configure(foreground="#ffffff")
        self.Label2_1_1.configure(highlightbackground="#d9d9d9")
        self.Label2_1_1.configure(highlightcolor="black")
        self.Label2_1_1.configure(text='''Mi Lista''')
        self.Frame2 = tk.Frame(self.Frame1)
        self.Frame2.place(relx=0.01, rely=0.146, relheight=0.219, relwidth=0.956)
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief="groove")
        self.Frame2.configure(background="#000000")
        self.Frame2.configure(highlightbackground="#d9d9d9")
        self.Frame2.configure(highlightcolor="black")

        canvas = tk.Canvas(self.Frame2, width=970, height=140,bg='black')
        # canvas.create_oval(5000, 10, 5010, 20, fill="red")
        # canvas.create_oval(200, 200, 220, 220, fill="blue")
        self.botones = []
        windows = []
        lista= dbQ.getMoviesPosters()
        for i in range(len(lista)):
            imageURL = lista[i][0]
            if(imageURL!="N/A"):
                URL = imageURL
                u = urllib.request.urlopen(URL)
                raw_data = u.read()
                u.close()

                im = Image.open(BytesIO(raw_data))
                im = im.resize((120,180),Image.ANTIALIAS)
                photo = ImageTk.PhotoImage(im)
            

            
                self.botones.append(tk.Button(canvas,image=photo,compound="c"))
                self.botones[i].image = photo
            else:
                self.botones.append(tk.Button(canvas))
                self.botones[i].configure(text=f"{lista[i][1]}")

            windows.append('')
            self.botones[i].place(relx=0.05, rely=0.05, relheight=1, relwidth=1)
            self.botones[i].configure(activebackground="#045762")
            self.botones[i].configure(activeforeground="#FFF")
            self.botones[i].configure(background="#045762")
            self.botones[i].configure(compound='left')
            self.botones[i].configure(disabledforeground="#a3a3a3")
            self.botones[i].configure(foreground="#FFF")
            self.botones[i].configure(highlightbackground="#d9d9d9")
            self.botones[i].configure(highlightcolor="black")
            self.botones[i].configure(pady="0")
            self.botones[i].bind('<Button-1>',lambda event,
                                                               titulo=lista[i][1],
                                                               idPeliculaCapitulo = lista[i][2]
                                                               : viewContent(titulo,idPeliculaCapitulo))
            canvas.create_window(100+(i*110), 10, anchor=NW, window=self.botones[i],height=130,width=100)
           
        canvas.grid(row=0, column=0)

        scroll_x = tk.Scrollbar(self.Frame2, orient="horizontal", command=canvas.xview)
        scroll_x.grid(row=1, column=0, sticky="ew")

        # scroll_y = tk.Scrollbar(self.Frame2, orient="vertical", command=canvas.yview)
        # scroll_y.grid(row=0, column=1, sticky="ns")

        # canvas.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        canvas.configure( xscrollcommand=scroll_x.set)

        canvas.configure(scrollregion=canvas.bbox("all"))

       


        self.Frame3 = tk.Frame(self.Frame1)
        self.Frame3.place(relx=0.01, rely=0.43, relheight=0.219, relwidth=0.956)
        self.Frame3.configure(relief='groove')
        self.Frame3.configure(borderwidth="2")
        self.Frame3.configure(relief="groove")
        self.Frame3.configure(background="#000000")
        self.Frame3.configure(highlightbackground="#d9d9d9")
        self.Frame3.configure(highlightcolor="black")

        # h=tk.Scrollbar(self.Frame3, orient='horizontal')
        # h.pack(side=BOTTOM, fill='x')

        # # Add a text widget
        # text=tk.Canva(self.Frame3, wrap=NONE, xscrollcommand=h.set)
        # text.pack()

        # # Add some text in the text widget
        # for i in range(5):
        #     text.insert(END, "Welcome to Tutorialspoint...")

        # # Attach the scrollbar with the text widget
        # h.config(command=text.xview)
        canvas1 = tk.Canvas(self.Frame3, width=970, height=140,bg='black')
        # canvas.create_oval(5000, 10, 5010, 20, fill="red")
        # canvas.create_oval(200, 200, 220, 220, fill="blue")
        self.botones1 = []
        windows1 = []

        viendoactualmente = dbQ.getWatchlist(idUsuario)
        for i in range(len(viendoactualmente)):
            imageURL = viendoactualmente[i][0]
            if(imageURL!="N/A"):
                URL = imageURL
                u = urllib.request.urlopen(URL)
                raw_data = u.read()
                u.close()

                im = Image.open(BytesIO(raw_data))
                im = im.resize((120,180),Image.ANTIALIAS)
                photo = ImageTk.PhotoImage(im)
            

            
                self.botones1.append(tk.Button(canvas1,image=photo,compound="c"))
                self.botones1[i].image = photo
            else:
                self.botones1.append(tk.Button(canvas1))
                self.botones1[i].configure(text=f"{viendoactualmente[i][1]}")
            windows1.append('')
            self.botones1[i].place(relx=0.05, rely=0.05, relheight=1, relwidth=1)
            self.botones1[i].configure(activebackground="#045762")
            self.botones1[i].configure(activeforeground="#FFF")
            self.botones1[i].configure(background="#045762")
            self.botones1[i].configure(compound='left')
            self.botones1[i].configure(disabledforeground="#a3a3a3")
            self.botones1[i].configure(foreground="#FFF")
            self.botones1[i].configure(highlightbackground="#d9d9d9")
            self.botones1[i].configure(highlightcolor="black")
            self.botones1[i].configure(pady="0")
            self.botones1[i].bind('<Button-1>',lambda event,
                                                               titulo=viendoactualmente[i][1],
                                                               idPeliculaCapitulo = viendoactualmente[i][2]
                                                               : viewContent(titulo,idPeliculaCapitulo))
            canvas1.create_window(100+(i*110), 10, anchor=NW, window=self.botones1[i],height=130,width=100)

        canvas1.grid(row=0, column=0)

        scroll_x1 = tk.Scrollbar(self.Frame3, orient="horizontal", command=canvas1.xview)
        scroll_x1.grid(row=1, column=0, sticky="ew")

        # scroll_y1= tk.Scrollbar(self.Frame3, orient="vertical", command=canvas1.yview)
        # scroll_y1.grid(row=0, column=1, sticky="ns")

        # canvas1.configure(yscrollcommand=scroll_y1.set, xscrollcommand=scroll_x1.set)
        canvas1.configure( xscrollcommand=scroll_x1.set)
        canvas1.configure(scrollregion=canvas1.bbox("all"))




        self.Frame3_1 = tk.Frame(self.Frame1)
        self.Frame3_1.place(relx=0.01, rely=0.75, relheight=0.219, relwidth=0.956)
               
        self.Frame3_1.configure(relief='groove')
        self.Frame3_1.configure(borderwidth="2")
        self.Frame3_1.configure(relief="groove")
        self.Frame3_1.configure(background="#000000")
        self.Frame3_1.configure(highlightbackground="#d9d9d9")
        self.Frame3_1.configure(highlightcolor="black")


        canvas2 = tk.Canvas(self.Frame3_1, width=970, height=140,bg='black')
        # canvas.create_oval(5000, 10, 5010, 20, fill="red")
        # canvas.create_oval(200, 200, 220, 220, fill="blue")
        self.botones2 = []
        windows2 = []

        listaFavoritos = dbQ.getFavoriteMovies(idUsuario)
        # for i in range(100,150):
        for i in range(len(listaFavoritos)):
            imageURL = listaFavoritos[i][0]
            if(imageURL!="N/A"):
                URL = imageURL
                u = urllib.request.urlopen(URL)
                raw_data = u.read()
                u.close()

                im = Image.open(BytesIO(raw_data))
                im = im.resize((120,180),Image.ANTIALIAS)
                photo = ImageTk.PhotoImage(im)
            

            
                self.botones2.append(tk.Button(canvas2,image=photo,compound="c"))
                self.botones2[i].image = photo
            else:
                self.botones2.append(tk.Button(canvas2))
                self.botones2[i].configure(text=f"{listaFavoritos[i][1]}")
            windows2.append('')

            self.botones2[i].place(relx=0.05, rely=0.05, relheight=1, relwidth=1)
            self.botones2[i].configure(activebackground="#045762")
            self.botones2[i].configure(activeforeground="#FFF")
            self.botones2[i].configure(background="#045762")
            self.botones2[i].configure(compound='left')
            self.botones2[i].configure(disabledforeground="#a3a3a3")
            self.botones2[i].configure(foreground="#FFF")
            self.botones2[i].configure(highlightbackground="#d9d9d9")
            self.botones2[i].configure(highlightcolor="black")
            self.botones2[i].configure(pady="0")
            self.botones2[i].bind('<Button-1>',lambda event,
                                                               titulo=listaFavoritos[i][1],
                                                               idPeliculaCapitulo = listaFavoritos[i][2]
                                                               : viewContent(titulo,idPeliculaCapitulo))
            canvas2.create_window(100+(i*110), 10, anchor=NW, window=self.botones2[i],height=130,width=100)

        canvas2.grid(row=0, column=0)

        scroll_x2 = tk.Scrollbar(self.Frame3_1, orient="horizontal", command=canvas2.xview)
        scroll_x2.grid(row=1, column=0, sticky="ew")

        # scroll_y2= tk.Scrollbar(self.Frame3_1, orient="vertical", command=canvas2.yview)
        # scroll_y2.grid(row=0, column=1, sticky="ns")

        # canvas2.configure(yscrollcommand=scroll_y2.set, xscrollcommand=scroll_x2.set)
        canvas2.configure( xscrollcommand=scroll_x2.set)
        canvas2.configure(scrollregion=canvas2.bbox("all"))





        self.Label2_2 = tk.Label(self.Frame1)
        self.Label2_2.place(relx=0.397, rely=0.013, height=67, width=212)
        self.Label2_2.configure(activebackground="#f9f9f9")
        self.Label2_2.configure(activeforeground="black")
        self.Label2_2.configure(anchor='w')
        self.Label2_2.configure(background="#000000")
        self.Label2_2.configure(compound='center')
        self.Label2_2.configure(disabledforeground="#a3a3a3")
        self.Label2_2.configure(font="-family {Open Sans} -size 14 -weight bold")
        self.Label2_2.configure(foreground="#ffffff")
        self.Label2_2.configure(highlightbackground="#d9d9d9")
        self.Label2_2.configure(highlightcolor="black")
        self.Label2_2.configure(text=f"Logged as: {nombrePerfil}")