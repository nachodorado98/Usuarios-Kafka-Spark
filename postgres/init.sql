CREATE DATABASE bbdd_usuarios;

\c bbdd_usuarios;

CREATE TABLE usuarios (Id SERIAL PRIMARY KEY,
						Nombre VARCHAR(255),
						Apellido VARCHAR(255),
						Genero VARCHAR(255),
						Direccion VARCHAR(255),
						Correo VARCHAR(255),
						Usuario VARCHAR(255),
						Fecha_Nacimiento DATE,
						Telefono VARCHAR(255),
						Imagen VARCHAR(255));