from tkinter import *
from tkinter import messagebox
from sqlalchemy import create_engine, inspect
import tkinter
import pandas as pd
from sympy import ordered


# * DATOS PARA CONECTARSE A LA BASE DE DATOS DE POSTGRESQL
user = "postgres"  # Usario del engine
password = "test"  # Contraseña
host = "localhost"  # HOST
port = "5432"  # Puerto
database = "proyecto2"  # Base de datos

# Creamos la conexion
engine = create_engine(
    f'postgresql://{user}:{password}@{host}:{port}/{database}')

inspector = inspect(engine)


# Main window
window = Tk()
window.title('Admin Local Interface')
window.configure(width=1200, height=800)


# Add aa movie function
def addMovie():
    notr = engine.execute(f"SELECT * FROM peliculacapitulo")
    lista = []
    for i in notr:
        lista.append(i)

    label = tkinter.Label(window, text=lista)
    label.pack(side='bottom')


def getTop5ActiveAadmins():
    notr = engine.execute(
        f"SELECT 	id_admin, count(operacion)FROM  infoadmingroup by id_adminorder by id_admin DESC limit 5;")
    lista = []
    for i in notr:
        lista.append(i)

    label = tkinter.Label(window, text=lista)
    label.pack(side='bottom')

# delete aa movie function


def searchReview():
    notr = engine.execute(
        f"SELECT buscador, COUNT (buscador) as busquedas FROM busqueda GROUP BY buscador ORDER BY busquedas DESC LIMIT 10;")
    lista = []
    for i in notr:
        lista.append(i)

    label = tkinter.Label(window, text=lista)
    label.pack(side='bottom')


def delMovie():
    print('deleted movie')

# Mod a movie function


def modMovie():
    print('modded movie')


# Add a movie button
addMovieButton = Button(window, text='Agregar Pelicula', bd='5',
                        command=addMovie)

addMovieButton.pack(side='top')


# Delete a movie button
deleteMovieButton = Button(window, text='Eliminar pelicula', bd='5',
                           command=delMovie)

deleteMovieButton.pack(side='top')

# Modify movie button
modifyMovieButton = Button(window, text='Modificar pelicula', bd='5',
                           command=delMovie)

modifyMovieButton.pack(side='top')

# Info about admins movie button
infoAdminButton = Button(window, text='Admins con mas movimientos', bd='5',
                         command=getTop5ActiveAadmins)

# Info about admins movie button
usersRequests = Button(window, text='Datos que los usuarios ', bd='5',
                       command=searchReview)

window.mainloop()
