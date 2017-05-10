# -*- coding: utf-8 *-*

import MySQLdb

db = MySQLdb.connect("localhost","root","chapuys","pruebaPython")

cursorCreate = db.cursor()
cursorInsert = db.cursor()
#Creamos la tabla
cadenaCreate = """CREATE TABLE SUPERHEROES (superheroe varchar(20),identidad_secreta varchar(30),sexo varchar(10))"""

cursorCreate.execute(cadenaCreate)
#Añadimos los datos
cadenaInsert = """INSERT INTO SUPERHEROES VALUES
('Superman','Clark Kent','Masculino')"""
cursorInsert.execute(cadenaInsert)
cadenaInsert = """INSERT INTO SUPERHEROES VALUES
('Spiderman','Peter Parkder','Masculino')"""
cursorInsert.execute(cadenaInsert)
cadenaInsert = """INSERT INTO SUPERHEROES VALUES
('Boltie','Libby','Femenino')"""
cursorInsert.execute(cadenaInsert)
cadenaInsert = """INSERT INTO SUPERHEROES VALUES
('Capitan America','Steve Rogers','Masculino')"""
cursorInsert.execute(cadenaInsert)
cadenaInsert = """INSERT INTO SUPERHEROES VALUES
('Green Lantern','Hal Jordan','Masculino')"""
cursorInsert.execute(cadenaInsert)
cadenaInsert = """INSERT INTO SUPERHEROES VALUES
('WonderWoman','Diana Prince','Femenino')"""
cursorInsert.execute(cadenaInsert)
cadenaInsert = """INSERT INTO SUPERHEROES VALUES
('Wolverine','Logan','Masculino')"""
cursorInsert.execute(cadenaInsert)
cadenaInsert = """INSERT INTO SUPERHEROES VALUES
('Mujer Invisible','Susan Storm','Femenino');"""
cursorInsert.execute(cadenaInsert)
cadenaInsert = """INSERT INTO SUPERHEROES VALUES
('Thor','Donald Blake','Masculino');"""
cursorInsert.execute(cadenaInsert)
cadenaInsert = """INSERT INTO SUPERHEROES VALUES
('Viuda Negra','Natasha Romanoff','Femenino');"""
cursorInsert.execute(cadenaInsert)
cadenaInsert = """INSERT INTO SUPERHEROES VALUES
('IronMan','Tony Stark','Masculino');"""
cursorInsert.execute(cadenaInsert)
cadenaInsert = """INSERT INTO SUPERHEROES VALUES
('Batman','Bruce Waine','Masculino');"""
cursorInsert.execute(cadenaInsert)
cadenaInsert = """INSERT INTO SUPERHEROES VALUES
('Ruby Thursday','Thursday Rubinstein','Femenino');"""
cursorInsert.execute(cadenaInsert)
cursor.close()
db.commit()
db.close()


