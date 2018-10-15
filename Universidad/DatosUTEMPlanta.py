#scrapy runspider DatosUTEMPlanta.py

from bs4 import BeautifulSoup
import sqlite3 as sqlite
from scrapy.spiders import Spider

#Ingresar / crear base de datos
nombre_db = "Universidades.db"
cursor = sqlite.connect(nombre_db)


class UTEMContrata(Spider):
    name = 'Universidad Tecnologica Metropolitana'
    start_urls = ['http://transparencia.utem.cl/personal-y-remuneraciones/personal-y-remuneraciones-personal-de-planta/']

    def parse(self, response):
                milista=[]
                InfoTabla = response.xpath('//*[@id="tablepress-54"]/tbody').extract_first()
                soup = BeautifulSoup(InfoTabla)
                line = soup.select('td')
                campos = 15
                universidad = response.xpath('/html/body/div[1]/div/div[2]/h1/text()').extract()
                tipo = response.xpath('/html/body/div[3]/div[1]/div/h1/text()').extract()

                for i, y in enumerate(line):
                    palabra = y.next_element
                    milista.append(palabra)
                    maximo = len(milista)
                    # GUARDAMOS LOS DATOS DE LA TABLA
                    v = 0
                while palabra != '':
                    # DATOS OBTENIDOS DE LA PAGINA
                    print ("Hay 13 campos")
                    Dato0 = milista[(campos * v) + 0]
                    Dato1 = milista[(campos * v) + 1]
                    Dato2 = milista[(campos * v) + 2]
                    Dato3 = milista[(campos * v) + 3]
                    Dato4 = milista[(campos * v) + 4]
                    Dato5 = milista[(campos * v) + 5]
                    Dato6 = milista[(campos * v) + 6]
                    Dato7 = milista[(campos * v) + 7]
                    Dato8 = milista[(campos * v) + 8]
                    Dato9 = milista[(campos * v) + 9]
                    Dato10 = milista[(campos * v) + 10]
                    Dato11 = milista[(campos * v) + 11]
                    Dato12 = milista[(campos * v) + 12]
                    Dato13 = milista[(campos * v) + 13]
                    Dato14 = milista[(campos * v) + 14]

                    insTipo = " ".join(tipo)
                    insUniversidad = " ".join(universidad)
                    insFechaInformacion = "VACIO"

                    datosUniversidad = (
                        Dato3, Dato1, Dato2, insTipo, Dato10, Dato5, Dato6,
                        insUniversidad, Dato12, insFechaInformacion)

                    print "-----Datos Persona-----"
                    print "Nombre :", Dato3, "."
                    print "Apellido Paterno :", Dato1, "."
                    print "Apellido Materno :", Dato2, "."
                    print "Tipo: ", insTipo, "."
                    print "Remuneracion Bruta Mensual :", Dato10, "."
                    print "Estamento :", Dato5, "."
                    print "Funcion :", Dato6, "."
                    print "Universidad :", insUniversidad, "."
                    print "Fecha_Ingreso :", Dato12, "."
                    print "------------------------------"
                    print "------------------------------"

                    cursor.execute(
                        "INSERT INTO Mostrar_persona(Nombre,apellidoP,apellidoM,tipo,remuneraciones,estamento,funcion,universidad,fecha_Ingreso,fecha_Informacion)"
                        "VALUES(?,?,?,?,?,?,?,?,?,?);", (datosUniversidad))
                    cursor.commit()


                    v += 1