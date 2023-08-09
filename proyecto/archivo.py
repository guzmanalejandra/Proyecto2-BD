#ESTE ARCHIVO ES PARA CREAR USUARIOS Y VISUALIZACIONES DE MANERA AUTO


import random
import pandas as pd
import os
import glob
from sqlalchemy import create_engine
from tkinter import messagebox
import random
import hashlib

# * DATOS PARA CONECTARSE A LA BASE DE DATOS DE POSTGRESQL
user = "postgres" # Usario del engine
password = "admin" # Contraseña 
host = "localhost" # HOST
port = "5432" # Puerto
database = "proyecto2" #Base de dato

# Creamos la conexion
engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database}')
  
ids = [25,26,27,28,29]
file1 = open('./proyecto/nombres.txt', 'r')
Lines = file1.readlines()
file1.close()

# for id in ids:
#     for x in range(0,6):
#         nombre = random.choice(Lines)
#         # print(nombre[0:len(nombre)-1])
#         engine.execute(f"INSERT INTO usuarios(idCuenta,nombre,cuentaInfantil) VALUES ({id},'{nombre[0:len(nombre)-1]}',{False})")

lista_Ids_Usuarios = []
result = engine.execute(f"SELECT id FROM usuarios")
for r in result:
    lista_Ids_Usuarios.append(r[0])


lista_Peliculas = []
result = engine.execute(f"SELECT id from peliculacapitulo")
for r in result:
    lista_Peliculas.append(r[0])
# print(lista_Peliculas)

from datetime import date, timedelta

start_date = date(2022, 3, 9)
end_date = date(2022, 5, 26)
delta = timedelta(days=1)

lista_fechas = []
while start_date <= end_date:
    # print(start_date.strftime("%Y-%m-%d"))
    lista_fechas.append(start_date.strftime("%Y-%m-%d"))
    start_date += delta

print(len(lista_fechas))

#15 visualizaciones por fecha
for fecha in lista_fechas:
    for i in range(0,17):
        hours = random.randint(1, 23)
        minutes = random.randint(0, 59)
        seconds = random.randint(0, 59)
        random_hour = f"{hours}:{minutes}:{seconds}"
        random_user_id = random.choice(lista_Ids_Usuarios)
        random_movie = random.choice(lista_Peliculas)

        # engine.execute(f"INSERT INTO informacionsesion(idpeliculacapitulo,fecha,hora,idusuario) VALUES ({random_movie}, '{fecha}', '{random_hour}', {random_user_id})")
        # engine.execute(f"INSERT INTO viendoactualmente(idusuario,idpeliculacapitulo,minuto) VALUES ({random_user_id},{random_movie},{minutes})")
def getListaUsuarios():
    lista_Ids_Usuarios = []
    result = engine.execute(f"SELECT id,email FROM usuarios")
    for r in result:
        lista_Ids_Usuarios.append([r[0],r[1]])

def getListaPeliculas():
    lista_Peliculas = []
    result = engine.execute(f"SELECT id,titulo from peliculacapitulo")
    for r in result:
        lista_Peliculas.append([r[0],r[1]])
        