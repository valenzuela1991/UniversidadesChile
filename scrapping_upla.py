# Scraping Universidad de Playa Ancha  Personal de Planta - Contrata 2018 (Agosto)


import urllib2
import sqlite3
import pandas as pd

# Busca url de excel planta - contrata
# filedata_planta = urllib2.urlopen(
#   'http://www.upla.cl/transparencia/wp-content/uploads/2018/09/2018_09109_transparencia_planta_ago-2018.xls')
# filedata_contrata = urllib2.urlopen(
#   'http://www.upla.cl/transparencia/wp-content/uploads/2018/09/2018_0910_transparencia_contrata_ago-2018.xls')

# Obtiene los datos
# data_planta = filedata_planta.read()
# data_contrata = filedata_contrata.read()

# Se crea un nuevo excel y se guarda el contenido de la descarga
# with open('/Users/Xino Abarzua/Desktop/upla_planta_2018.xls', 'wb') as f:
#  f.write(data_planta)

# with open('/Users/Xino Abarzua/Desktop/upla_contrata_2018.xls', 'wb') as f:
#   f.write(data_contrata)


datos = pd.read_excel('/Users/Xino Abarzua/Desktop/upla_planta_2018.xls')
dataframe_planta = pd.DataFrame(datos)

# print(dataframe.keys())

nombres = dataframe_planta.get('NOMBRE')
estamento = dataframe_planta.get('ESTAMENTO')
funcion = dataframe_planta.get('FUNCION O CARGO')
fecha = dataframe_planta.get('INICIO CONTRATO')
remuneracion = dataframe_planta.get('TOTAL LIQUIDO PERCIBIDO EN AGOSTO DE 2018')


# CREAR BASE DE DATOS

nombre_bd = "Upla.db"
cursor = sqlite3.connect(nombre_bd)

cursor.execute("CREATE TABLE IF NOT EXISTS datos("
               "nombre VARCHAR(100) NOT NULL,"
               "remuneracion VARCHAR(100) NOT NULL,"
               "estamento VARCHAR(100) NOT NULL,"
               "funcion VARCHAR(100) NOT NULL,"
               "fecha VARCHAR(100) NOT NULL)"
               )
cursor.commit()



#INSERTAR DATOS ACA ESTA LA CAGA
#cursor.execute(
 #   "INSERT INTO datos(nombre,remuneracion,estamento,funcion,fecha)"
  #  "VALUES(?,?,?,?,?);",nombres )
#cursor.commit()
