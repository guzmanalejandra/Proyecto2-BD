CREATE TABLE cuenta (
	id SERIAL PRIMARY KEY NOT NULL,
	tipoCuenta INTEGER,
	contrasena varchar(250),
	correo varchar(100)
);

CREATE TABLE registroLogin (
	id SERIAL PRIMARY KEY NOT NULL,
	idCuenta INTEGER,
	fecha DATE,
	resultado VARCHAR(30),
	FOREIGN KEY(idCuenta) REFERENCES cuenta(id)
);

CREATE TABLE usuarios(
	id SERIAL 	PRIMARY KEY NOT NULL,
	idCuenta	INTEGER,
	nombre		VARCHAR(50),
	cuentaInfantil	BOOL,
	FOREIGN KEY(idCuenta) REFERENCES cuenta(id)
);
-- Se tomara cada capitulo de una serie como una mini pelicula para que cada cap tenga su propio ID
CREATE TABLE peliculaCapitulo (
	id		SERIAL PRIMARY KEY NOT NULL,
	fechaEstreno	DATE,
	director		VARCHAR(100),
	premiosGanados	varchar(250),
	titulo			VARCHAR(100),
	idIMDB	VARCHAR(50)
);
CREATE TABLE actor(
	id 		SERIAL PRIMARY KEY NOT NULL,
	nombre	VARCHAR(100),
	edad	INTEGER,
	reconocimientos	VARCHAR(250)
);
CREATE TABLE elenco(
	id SERIAL PRIMARY KEY NOT NULL,
	idPeliculaCapitulo 	INTEGER,
	idActor				INTEGER,	
	FOREIGN KEY(idPeliculaCapitulo) REFERENCES peliculaCapitulo(id),
	FOREIGN KEY(idActor) REFERENCES actor(id)
);

CREATE TABLE genero(
	idPeliculaCapitulo INTEGER,
	FOREIGN KEY(idPeliculaCapitulo) REFERENCES peliculaCapitulo(id),
	tipo	VARCHAR(50)
);

CREATE TABLE anuncios (
	duracion	DECIMAL, -- Duracion en minutos
	anunciante	VARCHAR(50),
	categoria 	VARCHAR(100)
);


CREATE TABLE informacionSesion(
	id SERIAL PRIMARY KEY NOT NULL,
	idPeliculaCapitulo INTEGER NOT NULL,
	fecha DATE NOT NULL,
	hora	TIME NOT NULL,
	idUsuario INTEGER NOT NULL,
	FOREIGN KEY(idPeliculaCapitulo) REFERENCES peliculaCapitulo(id),
	FOREIGN KEY(idUsuario) REFERENCES usuarios(id)	
);

CREATE TABLE viendoActualmente(
	id SERIAL PRIMARY KEY,
	idUsuario INTEGER NOT NULL,
	idPeliculaCapitulo INTEGER NOT NULL,
	minuto	DECIMAL NOT NULL, -- Minuto en el que dejo el contenido
	FOREIGN KEY(idPeliculaCapitulo) REFERENCES peliculaCapitulo(id),
	FOREIGN KEY(idUsuario) REFERENCES usuarios(id)	
);

CREATE TABLE favoritos(
	id SERIAL PRIMARY KEY NOT NULL,
	idUsuario INTEGER NOT NULL,
	idPeliculaCapitulo INTEGER NOT NULL,
	FOREIGN KEY(idPeliculaCapitulo) REFERENCES peliculaCapitulo(id),
	FOREIGN KEY(idUsuario) REFERENCES usuarios(id)	
);
