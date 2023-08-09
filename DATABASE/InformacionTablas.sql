-- Insertar informacion en tabla cuentas
INSERT INTO Cuenta(ID_, tipo_cuenta, constraseña, correo)
VALUES('12346', 'No freemium', 'espada', 'gonz@gmail.com');

INSERT INTO Cuenta(ID_, tipo_cuenta, constraseña, correo)
VALUES('12347', 'freemium', 'sanguijuela', 'ren@gmail.com');

INSERT INTO Cuenta(ID_, tipo_cuenta, constraseña, correo)
VALUES('12348', 'freemium', 'basesdedatos', 'bada@gmail.com');

INSERT INTO Cuenta(ID_, tipo_cuenta, constraseña, correo)
VALUES('12349', 'No freemium', 'proyecto2', 'proy@gmail.com');


SELECT * 
FROM Cuenta;

-- Insertar en Usuarios

INSERT INTO Usuarios(ID_, ID_Cuenta, nombre)
VALUES('23456', '12345', 'Alejandra');

INSERT INTO Usuarios(ID_, ID_Cuenta, nombre)
VALUES('23457', '12346', 'Bartolo');

INSERT INTO Usuarios(ID_, ID_Cuenta, nombre)
VALUES('23458', '12347', 'Pamela');

INSERT INTO Usuarios(ID_, ID_Cuenta, nombre)
VALUES('23459', '12348', 'Chu');

INSERT INTO Usuarios(ID_, ID_Cuenta, nombre)
VALUES('23450', '12349', 'Benitez');

SELECT * 
FROM Usuarios;

-- Insertar ViendoActualmente
INSERT INTO viendoActualmente(ID_usuario, minuto, capitulo, ID_pelicula_serie, SerieOpelicula)
VALUES('23456', '5:00', '3', '123', 'Serie');

INSERT INTO viendoActualmente(ID_usuario, minuto, capitulo, ID_pelicula_serie, SerieOpelicula)
VALUES('23457', '10:00', '4', '234', 'Serie');

INSERT INTO viendoActualmente(ID_usuario, minuto, capitulo, ID_pelicula_serie, SerieOpelicula)
VALUES('23458', '25:00', '5', '345', 'Pelicula');

INSERT INTO viendoActualmente(ID_usuario, minuto, capitulo, ID_pelicula_serie, SerieOpelicula)
VALUES('23459', '7:00', '6', '567', 'Serie');

INSERT INTO viendoActualmente(ID_usuario, minuto, capitulo, ID_pelicula_serie, SerieOpelicula)
VALUES('23450', '13:00', '7', '789', 'Pelicula');


SELECT * 
FROM viendoActualmente;

-- peliculaSerie insert

INSERT INTO peliculaserie(ID_, titulo, estreno, director, categoria, genero, premio)
VALUES('123', '2006', 'Steven Spielberg', 'pelicula', 'accion', 'Goya');

INSERT INTO peliculaserie(ID_, titulo, estreno, director, categoria, genero)
VALUES('234', '2015', 'Jacob Raynolds', 'pelicula', 'romance', 'Oscar');

INSERT INTO peliculaserie(ID_, titulo, estreno, director, categoria, genero)
VALUES('345', '1995', 'Martin Scorsese', 'serie', 'comedia', 'No tiene');

INSERT INTO peliculaserie(ID_, titulo, estreno, director, categoria, genero)
VALUES('567', '2020', 'Quentin Tarantino', 'pelicula', 'drama', 'Academy');

INSERT INTO peliculaserie(ID_, titulo, estreno, director, categoria, genero)
VALUES('789', '1975', 'Steven Spielberg', 'serie', 'accion', 'Goya');


SELECT * 
FROM peliculaserie;

-- INSERT INTO ACTORES
INSERT INTO actores(ID_actor, ID_pelicula)
VALUES(012, 234)




