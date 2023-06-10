INSERT INTO usuario (nombre, rol) VALUES ('UsuarioAdmin', 'admin');

INSERT INTO usuario (nombre, rol) VALUES
    ('UsuarioColaborador1', 'colaborador'),
    ('UsuarioColaborador2', 'colaborador'),
    ('UsuarioColaborador3', 'colaborador'),
    ('UsuarioColaborador4', 'colaborador'),
    ('UsuarioPublico1', 'público'),
    ('UsuarioPublico2', 'público'),
    ('UsuarioPublico3', 'público'),
    ('UsuarioPublico4', 'público'),
    ('UsuarioPublico5', 'público');
    
    INSERT INTO usuario (nombre, es_admin, es_colaborador, es_publico) VALUES
    ('UsuarioAdmin', true, false, false),
    ('UsuarioColaborador1', false, true, false),
    ('UsuarioColaborador2', false, true, false),
    ('UsuarioColaborador3', false, true, false),
    ('UsuarioColaborador4', false, true, false),
    ('UsuarioPublico1', false, false, true),
    ('UsuarioPublico2', false, false, true),
    ('UsuarioPublico3', false, false, true),
    ('UsuarioPublico4', false, false, true),
    ('UsuarioPublico5', false, false, true);

UPDATE usuario SET rol = 'admin' WHERE nombre = 'UsuarioColaborador1';

INSERT INTO articulo (titulo, estado) VALUES
    ('Articulo1', true),
    ('Articulo2', true),
    ('Articulo3', true),
    ('Articulo4', false);

    DELETE FROM articulo WHERE estado = false;

INSERT INTO comments (article_id, comment) VALUES (1, 'Primer comentario');
INSERT INTO comments (article_id, comment) VALUES (1, 'Segundo comentario');
INSERT INTO comments (article_id, comment) VALUES (1, 'Tercer comentario');

INSERT INTO comments (article_id, comment) VALUES (2, 'Primer comentario');
INSERT INTO comments (article_id, comment) VALUES (2, 'Segundo comentario');

SELECT a.title, a.fecha_publicacion, u.nombre, c.fecha_hora
FROM articles AS a
JOIN comments AS c ON a.id = c.article_id
JOIN users AS u ON c.user_id = u.id
GROUP BY a.id;
