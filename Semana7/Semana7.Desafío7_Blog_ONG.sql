-- Crea base DB
DROP DATABASE IF EXISTS Blog_ONG;
CREATE DATABASE Blog_ONG;

-- Usa DB
USE Blog_ONG;

-- Crea tabla USUARIO y PK
CREATE TABLE USUARIO (
  id INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(25) NOT NULL,
  apellido VARCHAR(25) NOT NULL,
  telefono VARCHAR(14),
  username VARCHAR(10),
  email VARCHAR(45),
  contrasena VARCHAR(16),
  estado VARCHAR(15) CHECK (estado='activo' Or estado='inactivo'),
  fecha_creacion DATETIME NOT NULL,
  avatar BLOB,
  es_publico BOOLEAN,
  es_colaborador BOOLEAN,
  es_admin BOOLEAN,
  PRIMARY KEY (id)
);

-- Crea tabla ARTICULO, PK y FK
CREATE TABLE ARTICULO (
  id INT NOT NULL AUTO_INCREMENT,
  id_usuario INT NULL,
  titulo VARCHAR(50) NOT NULL,
  resumen TEXT(500),
  contenido LONGTEXT,
  fecha_publicacion DATETIME,
  estado VARCHAR(15) DEFAULT 'Publicado',
  imagen BLOB,
  PRIMARY KEY (id),
  FOREIGN KEY (id_usuario) REFERENCES USUARIO(id)
);

-- Crea tabla COMENTARIO, PK y FK
CREATE TABLE COMENTARIO (
  id INT NOT NULL AUTO_INCREMENT,
  id_articulo INT NOT NULL,
  id_usuario INT NOT NULL,
  contenido MEDIUMTEXT NOT NULL,
  fecha_hora DATETIME,
  estado VARCHAR(15) DEFAULT 'Publicado',
  PRIMARY KEY (id),
  FOREIGN KEY (id_articulo) REFERENCES ARTICULO(id),
  FOREIGN KEY (id_usuario) REFERENCES USUARIO(id)
);

-- Crea tabla CATEGORIA, PK y FK
CREATE TABLE CATEGORIA (
  id INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(25) NOT NULL,
  descripcion VARCHAR(100),
  imagen BLOB,
  estado VARCHAR(15) DEFAULT 'Activo',
  PRIMARY KEY (id)
);

-- Crea tabla CATEGORIA_ARTICULO y FK
CREATE TABLE CATEGORIA_ARTICULO (
  id_articulo INT NOT NULL,
  id_categoria INT NOT NULL,
  FOREIGN KEY (id_articulo) REFERENCES ARTICULO(id),
  FOREIGN KEY (id_categoria) REFERENCES CATEGORIA(id)
);

/* Agrega usuarios con roles */

INSERT INTO USUARIO (nombre, apellido, telefono, username, email, contrasena, fecha_creacion, es_publico, es_colaborador, es_admin) 
VALUES 
  ('Soyadmin', 'Istrador', '+541596378524', 'admin', 'admin@ejemplo.com', 'queteimporta', CURDATE(), false, false, true),
  ('Ernesto', 'Colaborador1', '+541596378524', 'colabora1', 'colabora1@ejemplo.com', 'col123456or', CURDATE(), false, true, false),
  ('Pepito', 'Colaborador2', '+541596378524', 'colabora2', 'colabora2@ejemplo.com', ' col123789or', CURDATE(), false, true, false),
  ('Celestino', 'Colaborador3', '+541596378524', 'colabora3', 'colabora3@ejemplo.com', 'col123123', CURDATE(), false, true, false),
  ('Fulgencio', 'Colaborador4', '+541596378524', 'colabora4', 'colabora4@ejemplo.com', 'col123987', CURDATE(), false, true, false),
  ('Pablo', 'Publico1', '+541596258639', 'publico1', 'publico1@ejemplo.com', 'pub12385co', CURDATE(), true, false, false),
  ('Ana', 'Publico2', '+541596258639', 'publico2', 'publico2@ejemplo.com', 'pub14765co', CURDATE(), true, false, false),
  ('Sara', 'Publico3', '+541596258639', 'publico3', 'publico3@ejemplo.com', 'pub32165co', CURDATE(), true, false, false),
  ('Pedro', 'Publico4', '+541596258639', 'publico4', 'publico4@ejemplo.com', 'pub78954co', CURDATE(), true, false, false),
  ('Carolina', 'Publico1', '+541596258639', 'publico5', 'publico5@ejemplo.com', 'pub54217co', CURDATE(), true, false, false);
 
/*Actualiza uno de los usuarios a admin*/
 
  UPDATE USUARIO SET es_admin = true WHERE id = 5; 

-- Introduce artículos y sus estados

INSERT INTO ARTICULO (id_usuario, titulo, resumen, contenido, fecha_publicacion, estado) 
VALUES 
  
  (7, 'Artículo1', 'Resumen1', 'Contenido1', CURDATE(), true),
  (9, 'Artículo2', 'Resumen2', 'Contenido2', CURDATE(), true),
  (8, 'Artículo3', 'Resumen3', 'Contenido3', CURDATE(), true),
  (10, 'Artículo4', 'Resumen4', 'Contenido4', CURDATE(), false),
  ('Artículo5', 'Resumen5', 'Contenido5', CURDATE(), true),
  ('Artículo8', 'Resumen8', 'Contenido8', CURDATE(), true);

/* Elimina el artículo con estado False*/

  DELETE FROM ARTICULO WHERE estado = false;
  
/* Comentar*/
  
INSERT INTO COMENTARIO (id_articulo, id_usuario, contenido, fecha_hora) 
VALUES 
  (5, 7, 'Comentario 1 del artículo 5', NOW()),
  (5, 9, 'Comentario 2 del artículo 5', NOW()),
  (5, 6, 'Comentario 3 del artículo 5', NOW()),
  (8, 6, 'Comentario 1 del artículo 8', NOW()),
  (8, 8, 'Comentario 2 del artículo 8', NOW());
  
/*Listar los artículos que tengan comentarios*/
  
SELECT a.titulo, a.fecha_publicacion, u.nombre, c.fecha_hora 
FROM ARTICULO a
INNER JOIN COMENTARIO c ON a.id  = c.id_articulo
INNER JOIN USUARIO u ON u.id  = c.id_usuario
GROUP BY a.id;