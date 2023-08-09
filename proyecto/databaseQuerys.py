#Importamos modulos a usar
from dataclasses import replace
import pandas as pd
import os
import glob
from sqlalchemy import create_engine
from tkinter import messagebox
import random
import hashlib
import requests
import json
from datetime import datetime
# * DATOS PARA CONECTARSE A LA BASE DE DATOS DE POSTGRESQL
user = "postgres" # Usario del engine
password = "admin" # Contraseña 
host = "localhost" # HOST
port = "5432" # Puerto
database = "proyecto2" #Base de dato

# Creamos la conexion
engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database}')
    
#Función para realizar un login
# @param email -> correo de la cuenta
# @param psw -> contraseña de la cuenta
def login(email,psw):
    PSW = hashlib.sha256(psw.encode('utf-8')).hexdigest() # HASH de la contraseña
    result = engine.execute(f"SELECT id,tipocuenta FROM cuenta WHERE correo = '{email}' AND contrasena='{PSW}'")
    bandera = False
    for r in result:
        bandera = True
        return (bandera, r[0],r[1])
    return (bandera, None) 

def registrarLoginAdministrador(id,date):
    resultado = engine.execute(f"INSERT INTO registrologinadmin(idcuenta,fecha) VALUES ({id}, '{date}')")


#Función para obtener el ID de una cuenta dado su correo
# @param email -> correo de la cuenta
def getIdCuentaByEmail(email):
    result = engine.execute(f"SELECT id FROM cuenta WHERE correo = '{email}'")
    for r in result:
        return r[0]


#Función para crear una cuenta
# @param email -> correo de la cuenta
# @param password -> contraseña de la cuenta
# @param tipo -> tipo de suscripción 
def createAccount(email,password,tipo):
    #Validacion de que no exista una cuenta con ese correo
    result_set = engine.execute(f"SELECT correo FROM cuenta WHERE correo='{email}'")
    contador = 0
    for r in result_set:
        contador += 1
    
    if contador == 0: #no existe el correo
        PSW = hashlib.sha256(password.encode('utf-8')).hexdigest()
        engine.execute(f"INSERT INTO cuenta(tipoCuenta, contrasena,correo) VALUES ({tipo},'{PSW}','{email}')")
        idCuenta = getIdCuentaByEmail(email)
        nombreUsuarioDefault = getNameFromEmail(email)
        infantil = False
        #Creamos un perfil default a la cuenta que se creo
        if tipo != -1:
            engine.execute(f"INSERT INTO usuarios(idCuenta,nombre,cuentaInfantil) VALUES ({idCuenta},'{nombreUsuarioDefault}',{infantil})")
        return (True,idCuenta)      
    else: #existe el correo
        messagebox.showerror(title="Error", message="El correo que ya esta registrado")
        return (False,None)


#Función para obtener un username dado un correo
# @param email -> correo de la cuenta
def getNameFromEmail(email):
    username = email.split('@')[0]
    user = username.split('.')[0]
    return user

#Función para obtener todos los perfiles dado un ID de una cuenta
# @param idCuenta -> Id de la cuenta
def getProfilesWithAccountId(idCuenta):
    result = engine.execute(f"SELECT * FROM usuarios WHERE idCuenta = {idCuenta}")
    return result


#Función para crear un perfil en una cuenta
def createProfile(idCuenta,nombre,infantil):
    #Obtenemos el tipo de suscripción que tiene la cuenta
    result_tipoCuenta = engine.execute(f"SELECT tipocuenta FROM cuenta WHERE id = {idCuenta}")
    tipoCuenta = 0
    for r in result_tipoCuenta:
        tipoCuenta=r[0]
    #Obtenemos la cantidad de perfiles en la cuenta
    result_cantidadPerfiles = engine.execute(f"SELECT * FROM usuarios WHERE idCuenta = {idCuenta}")
    cantidad = 0
    for r in result_cantidadPerfiles:
        cantidad=cantidad+1
    
    valido = True
    if tipoCuenta == 0: #SI la cuenta es gratuita
        #Mostrara un error debido a que solo puede crear un perfil
        # y este ya fue creado al momento de crear la cuenta
        messagebox.showerror(title="Error", message="Tu plan gratuito solo te permite crear un perfil")
        valido = False
    elif tipoCuenta == 1 and cantidad>=4: # SI la cuenta es estandar y tiene menos de 4 perfiles
        messagebox.showerror(title="Error", message="Tu plan solo te permite crear 4 perfiles")
        valido = False
    elif tipoCuenta == 2 and cantidad>=8:# SI la cuenta es premium y tiene menos de 8 perfiles
        messagebox.showerror(title="Error", message="Tu plan solo te permite crear 8 perfiles")
        valido = False

    #Si puede crear un perfil
    if valido:
        result = engine.execute(f"SELECT * FROM usuarios WHERE idCuenta = {idCuenta} AND nombre ILIKE '{nombre}'")
        contador = 0
        for r in result:
            contador += 1
        if contador == 0: #No existe el perfil
            engine.execute(f"INSERT INTO usuarios(idCuenta,nombre,cuentaInfantil) VALUES ({idCuenta},'{nombre}',{infantil})")
            messagebox.showinfo(title="Exito",message="Se ha creado el perfil")
            return True
        else: #existe el perfil
            messagebox.showerror(title="Error", message="Ya existe un perfil con este nombre")
            return False
    else:
        return False

def saveMovie(fechaEstreno,director,premios,titulo,idIMDB,poster):
    result_set = engine.execute(f"SELECT idimdb FROM peliculacapitulo WHERE idimdb='{idIMDB}'")
    contador = 0
    for r in result_set:
        contador += 1

    if contador == 0:
        engine.execute(f"INSERT INTO peliculacapitulo(fechaestreno,director,premiosganados,titulo,idimdb,poster) VALUES ('{fechaEstreno}','{director}','{premios}','{titulo}','{idIMDB}','{poster}')")


def getMoviesPosters():
    result_set = engine.execute(f"SELECT poster,titulo,id FROM peliculacapitulo")
    lista = []
    for r in result_set:
        lista.append([r[0],r[1],r[2]])
    return lista

def addMovieToList(movieId,userId):
    result_set = engine.execute(f"SELECT * FROM favoritos WHERE idusuario = {userId} AND idpeliculacapitulo={movieId} ")
    contador = 0
    for r in result_set:
        contador += 1
    if contador == 0:
        engine.execute(f"INSERT INTO favoritos(idusuario,idpeliculacapitulo) VALUES ({userId},{movieId})")
    else: 
        engine.execute(f"DELETE FROM favoritos WHERE idusuario = {userId} AND idpeliculacapitulo = {movieId} ")

def getFavoriteMovies(idUsuario):
    result = engine.execute(f"SELECT idpeliculacapitulo FROM favoritos WHERE idusuario = {idUsuario}")
    listaPeliculas = []
    for r in result:
        result_set = engine.execute(f"SELECT poster,titulo,id FROM peliculacapitulo WHERE id = {r[0]}")
        for rr in result_set:
            listaPeliculas.append([rr[0],rr[1],rr[2]])
    return listaPeliculas

def addMovieToWatchlist(movieId,userId):
    result_set = engine.execute(f"SELECT * FROM viendoactualmente WHERE idusuario = {userId} AND idpeliculacapitulo={movieId} ")
    contador = 0
    for r in result_set:
        contador += 1
    if contador == 0:
        engine.execute(f"INSERT INTO viendoactualmente(idusuario,idpeliculacapitulo,minuto) VALUES ({userId},{movieId},{0})")
 


def getWatchlist(idUsuario):
    result = engine.execute(f"SELECT idpeliculacapitulo FROM viendoactualmente WHERE idusuario = {idUsuario}")
    listaPeliculas = []
    for r in result:
        result_set = engine.execute(f"SELECT poster,titulo,id FROM peliculacapitulo WHERE id = {r[0]}")
        for rr in result_set:
            listaPeliculas.append([rr[0],rr[1],rr[2]])
    return listaPeliculas

def saveActors(listOfActors,imdbID):
    for actor in listOfActors:
        actor.replace("'"," ")
        validacion = engine.execute(f"SELECT * FROM actor where nombre = '{actor}'")
        contador = 0
        for r in validacion:
            contador += 1
        if contador == 0:
            insertar = engine.execute(f"INSERT INTO actor(nombre) VALUES ('{actor}')")


    peliculaId = engine.execute(f"SELECT id FROM peliculacapitulo WHERE idimdb = '{imdbID}'")
    for r in peliculaId:
        # print(r[0])
        for actor in listOfActors:
            idActor = 0
            getIdActor = engine.execute(f"SELECT id FROM actor WHERE nombre = '{actor}'")
            for id in getIdActor:
                idActor = id[0]
            validacion2 = engine.execute(f"SELECT * FROM elenco WHERE idactor = {idActor} AND idpeliculacapitulo ={r[0]} ")
            contador2 = 0
            for rr in validacion2:
                contador2 += 1

            if contador2 == 0:
                # print('hola')
                engine.execute(f"INSERT INTO elenco (idactor, idpeliculacapitulo) VALUES ({idActor},{r[0]})")


def getMoviesByYear(ano):
    result_set = engine.execute(f"SELECT poster,titulo,id FROM peliculacapitulo WHERE EXTRACT(YEAR FROM fechaestreno)={ano}")
    lista = []
    for r in result_set:
        lista.append([r[0],r[1],r[2]])
    return lista

def getMoviesByTitle(title):
    result_set = engine.execute(f"SELECT poster,titulo,id FROM peliculacapitulo WHERE titulo ILIKE '{title}'")
    lista = []
    for r in result_set:
        lista.append([r[0],r[1],r[2]])
    return lista

def getTipoCuentaWithId(id):
    result = engine.execute(f"SELECT tipocuenta FROM cuenta where id = {id}")
    for r in result:
        return r[0]
def getCuentaWithId(id):
    result = engine.execute(f"SELECT correo,tipocuenta FROM cuenta where id = {id}")
    for r in result:
        return [r[0],r[1]]

def updatePlanCuenta(id,tipo):
    result = engine.execute(f"UPDATE cuenta SET tipocuenta ={tipo} WHERE id = {id}")
    
def registrarLogin(idCuenta,fecha,resultado):
    resultado = engine.execute(f"INSERT INTO registrologin(idcuenta,fecha,resultado) VALUES ({idCuenta}, '{fecha}', {resultado})")

def registrarSesion(idpeliculacapitulo,fecha,hora,idUsuario):
    resultado = engine.execute(f"INSERT INTO informacionsesion(idpeliculacapitulo,fecha,hora,idusuario) VALUES ({idpeliculacapitulo}, '{fecha}', '{hora}', {idUsuario})")

def getListaUsuariosA():
    lista_Ids_Usuarios = []
    result = engine.execute(f"SELECT id,nombre FROM usuarios")
    for r in result:
        lista_Ids_Usuarios.append([r[0],r[1]])
    return lista_Ids_Usuarios

def getListaPeliculasA():
    lista_Peliculas = []
    result = engine.execute(f"SELECT id,titulo from peliculacapitulo")
    for r in result:
        lista_Peliculas.append([r[0],r[1]])
    return lista_Peliculas
def deleteDataSimulacion():
    en = engine.execute(f"DELETE FROM simulacion")
def saveDataSimulation(idPelicula,titulo,idUsuario,usuario,fecha,hora):
    result = engine.execute(f"INSERT INTO simulacion(id_pelicula,titulopelicula,id_usuario,user_name,fecha,hora) VALUES ({idPelicula}, '{titulo}',{idUsuario},'{usuario}','{fecha}', '{hora}')")


def addMovieThroughApi(title,id):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    engine.execute(f"INSERT INTO infoadmin(id_admin,fecha,operacion) VALUES ({id},'{dt_string}','INSERT - peliculacapitulo')")
    url = f"http://www.omdbapi.com/?apikey=482161e2&t={title}"
    response = requests.request("GET", url)
    data = json.loads(response.text)
    if data['Response']=="True" or data['Response']==True:
        saveMovie(data['Released'],data['Director'],data['Awards'],data['Title'],data['imdbID'],data['Poster'])
        actores = data['Actors']
        listaA = actores.split(', ')
        lista2 = []
        for actor in listaA:
            if "'" in actor:
                actor = actor.replace("'"," ")
            if '"' in actor:
                actor = actor.replace('"'," ")
            lista2.append(actor)
        id = data['imdbID']
        saveActors(lista2, id)

        return True
    else:
        return False

def deleteMovie(title,id):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    engine.execute(f"INSERT INTO infoadmin(id_admin,fecha,operacion) VALUES ({id},'{dt_string}','DELETE - peliculacapitulo')")
    result = engine.execute(f"SELECT id FROM peliculacapitulo where titulo ILIKE '{title}'")
    for r in result:
        id = r[0]

        engine.execute(f"DELETE FROM elenco where idpeliculacapitulo={id}")
        engine.execute(f"DELETE FROM simulacion where id_pelicula={id}")
        engine.execute(f"DELETE FROM viendoactualmente where idpeliculacapitulo={id}")
        engine.execute(f"DELETE FROM favoritos where idpeliculacapitulo={id}")
        engine.execute(f"DELETE FROM informacionsesion where idpeliculacapitulo={id}")
        engine.execute(f"DELETE FROM peliculacapitulo where id={id}")

def getAdminData():
    result = engine.execute(f"SELECT * from infoadmin")
    data = []
    for r in result:
        data.append([r[0],r[1],r[2],r[3]])
    return data
