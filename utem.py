# SCRAPING UTEM
# -*- encoding: utf-8 -*-


import urllib2
import sqlite3
import pandas as pd

# DESCARGA DE DOCUMENTOS
filedata_planta = urllib2.urlopen(
    'http://transparencia.utem.cl/1ej6')

filedata_contrata = urllib2.urlopen(
    'http://transparencia.utem.cl/dcu7')

# GUARDA LOS DATOS EN ESTAS VARIABLES

data_planta = filedata_planta.read()
data_contrata = filedata_contrata.read()

# CREAMOS UN XLS NUEVO Y GUARDAMOS LOS DATOS EN ESTE

#with open('/Users/Xino Abarzua/Desktop/utem_planta_2018.xlsx', 'wb') as f:
  #  f.write(data_planta)

#with open('/Users/Xino Abarzua/Desktop/utem_contrata_2018.xlsx', 'wb') as f:
 #   f.write(data_contrata)

# FIN DEL PROCESO DE DESCARGA

# CARGAMOS LOS DATOS EN UN DATAFRAME

datos_planta = pd.read_excel('/Users/Xino Abarzua/Desktop/utem_planta_2018.xlsx')
dataframe_planta = pd.DataFrame(datos_planta)

datos_contrata = pd.read_excel('/Users/Xino Abarzua/Desktop/utem_contrata_2018.xlsx')
dataframe_contrata = pd.DataFrame(datos_contrata)

# VERIFICAMOS LOS INDICES DE LOS DATAFRAME

print "DataFrame Planta"
print(dataframe_planta.keys())
print "DataFrame Contrata"
print(dataframe_contrata.keys())

#OBTENIENDO DATOS DEL DATAFRAME PLANTA

remuneracion_utf8 = "Remuneración bruta mensualizada"


def force_to_unicode(text):
    return text if isinstance(text , unicode) else text.decode('utf8')

remuneracion_2=force_to_unicode(remuneracion_utf8)



nombres = dataframe_planta.get('Nombres')
apellidoP = dataframe_planta.get('Apellido Paterno')
apellidoM = dataframe_planta.get('Apellido Materno')
estamento = dataframe_planta.get('Estamento')
funcion = dataframe_planta.get('Cargo o Funcion')
remuneracion = dataframe_planta.get(remuneracion_2)
fecha_inicio = dataframe_planta.get('Fecha de inicio dd/mm/aa')

print remuneracion

nombre_bd = "Utem.db"
cursor = sqlite3.connect(nombre_bd)

# CREANDO LA BASE DE DATOS PARA PLANTA

cursor.execute("CREATE TABLE IF NOT EXISTS datos_planta("
               "nombres VARCHAR(40) NOT NULL,"
               "apellidoP VARCHAR(40) NOT NULL,"
               "apellidoM VARCHAR(40) NOT NULL,"
               "remuneracion VARCHAR(40) NOT NULL,"
               "estamento VARCHAR(40) NOT NULL,"
               "funcion VARCHAR(40) NOT NULL,"
               "fecha VARCHAR(40) NOT NULL)"
               )

cursor.commit()


#AGREGANDO LOS DATOS A LA BD


