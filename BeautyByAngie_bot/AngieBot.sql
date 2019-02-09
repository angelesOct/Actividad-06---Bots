CREATE DATABASE bot;

USE bot;

CREATE TABLE Tips(
    tip_de varchar(20) NOT NULL PRIMARY KEY,
    tip varchar(1000) NOT NULL,
    tiempo varchar(100) NULL
)ENGINE=InnoDB DEFAULT CHARSET=latin1;


INSERT INTO Tips VALUES 
    ('cremas','No importa si tu piel es seca, normal, o grasosa. No tienes que invertir en muchas cremas, con un solo producto que sea bueno puedes tener una piel de ensuenio.','Uso Diario'),
    ('antienvejecimiento','Antes de ver un cirujano plastico, antes de gastar la mitad del sueldo en cremas anti-envejecimiento, ponte protector solar','en dias soliados'),
    ('limpieza','Si lo que usas diariamente para limpiarte la cara es agua y jabon, puedes ir reconsiderando tu estrategia de limpieza. Los dermatologos dicen que uno de los mejores consejos de belleza es utilizar un limpiador suave y utilizarlo con moderacion','Uso periodicamente'),
    ('sombras','Si mojas un pincel en la sombra o rubor y el color se cae antes de llegar a tu cara, este es un pincel malo, dicen los expertos.','Usalo Cuando te vayas a maquillar'),
    ('tratamientos','Si ha pasado un tiempo largo desde que has tenido un cambio, aprovecha y vete a tu peluqueria y tienda de belleza y no tengas miedo de pedir ayuda.','Uso cada 2 anios ');

SHOW TABLES;

SELECT * FROM Tips;

DESCRIBE Tips;

CREATE USER 'angiebot'@'localhost' IDENTIFIED BY 'angiebot.2019';
GRANT ALL PRIVILEGES ON bot.* TO 'angiebot'@'localhost';
FLUSH PRIVILEGES;