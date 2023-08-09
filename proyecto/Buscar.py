import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
from PIL import Image, ImageTk
import urllib.request
from io import BytesIO
import databaseQuerys as dbQ
from tkinter import messagebox


class Buscar:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
            top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        
        def buscar():
            entry = self.Entry1.get()
            categoria = self.TCombobox1.get()
            lista= []
            if categoria=='año':
                try:
                    ano = int(entry)
                    lista = dbQ.getMoviesByYear(ano)
                except:
                    messagebox.showerror(title="Error", message="Valor invalido")


            elif categoria=='Titulo':
                lista = dbQ.getMoviesByTitle(entry)





            canvas.delete("all")
            self.botones = []
            windows = []
            
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
                canvas.create_window(100+(i*110), 10, anchor=NW, window=self.botones[i],height=130,width=100)
           
            canvas.grid(row=0, column=0)

            scroll_x = tk.Scrollbar(self.Frame2, orient="horizontal", command=canvas.xview)
            scroll_x.grid(row=1, column=0, sticky="ew")

            # scroll_y = tk.Scrollbar(self.Frame2, orient="vertical", command=canvas.yview)
            # scroll_y.grid(row=0, column=1, sticky="ns")

            # canvas.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
            canvas.configure( xscrollcommand=scroll_x.set)

            canvas.configure(scrollregion=canvas.bbox("all"))






        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("600x450+468+138")
        top.minsize(120, 1)
        top.maxsize(3844, 1061)
        top.resizable(1,  1)
        top.title("Buscar")
        top.configure(background="#d9d9d9")

        self.top = top
        self.combobox = tk.StringVar()

        self.Frame1 = tk.Frame(self.top)
        self.Frame1.place(relx=0.0, rely=0.0, relheight=1.011, relwidth=1.008)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#000000")

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.017, rely=0.022, height=41, width=175)
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#000000")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI} -size 14 -weight bold")
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(text='''Buscar por:''')

        self.TCombobox1 = ttk.Combobox(self.Frame1)
        self.TCombobox1.place(relx=0.198, rely=0.044, relheight=0.046
                , relwidth=0.236)
        self.TCombobox1.configure(takefocus="")
        self.TCombobox1['values']=('Titulo','año')
        self.TCombobox1.current(1)
        self.TCombobox1['state']='readonly'
        self.Entry1 = tk.Entry(self.Frame1)
        self.Entry1.place(relx=0.017, rely=0.154, height=20, relwidth=0.354)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        self.Frame2 = tk.Frame(self.Frame1)
        self.Frame2.place(relx=0.017, rely=0.418, relheight=0.35
                , relwidth=0.952)
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief="groove")
        self.Frame2.configure(background="#000000")

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.017, rely=0.33, height=31, width=144)
        self.Label2.configure(anchor='w')
        self.Label2.configure(background="#000000")
        self.Label2.configure(compound='left')
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Segoe UI} -size 14 -weight bold")
        self.Label2.configure(foreground="#ffffff")
        self.Label2.configure(text='''RESULTADOS''')


        canvas = tk.Canvas(self.Frame2, width=970, height=130,bg='black')


        self.Button1 = tk.Button(self.Frame1,command=buscar)
        self.Button1.place(relx=0.5, rely=0.154, height=34, width=97)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#ff0000")
        self.Button1.configure(compound='left')
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#ffffff")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Buscar''')