#scrapy runspider DatosUSACHPlanta.py

from bs4 import BeautifulSoup
import sqlite3 as sqlite
from scrapy.spiders import Spider

#Ingresar / crear base de datos
nombre_db = "Universidades.db"
cursor = sqlite.connect(nombre_db)


class UTEMContrata(Spider):
    name = 'Universidad de Playa Ancha'
    start_urls = ['https://www.transparenciaactiva.usach.cl/planta-septiembre-2018']

    def parse(self, response):
                milista=[]
                InfoTabla = response.xpath('//*[@id="node-page-1391"]/div[1]/div/div/div/table/tbody').extract_first()
                soup = BeautifulSoup(InfoTabla)
                line = soup.select('td')
                campos = 19
                universidad = response.xpath('//*[@id="region-branding"]/div/div/hgroup/h6/text()').extract()
                #tipo = response.xpath('/html/body/div[3]/div[1]/div/h1/text()').extract()

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
                    Dato15 = milista[(campos * v) + 15]
                    Dato16 = milista[(campos * v) + 16]
                    Dato17 = milista[(campos * v) + 17]
                    Dato18 = milista[(campos * v) + 18]

                    insUniversidad = " ".join(universidad)

                    datosUniversidad = (
                        Dato4, Dato2, Dato3, Dato0, Dato14, Dato1, Dato7,
                        insUniversidad, Dato9, Dato10)

                    print "-----Datos Persona-----"
                    print "Nombre :", Dato4, "."
                    print "Apellido Paterno :", Dato2, "."
                    print "Apellido Materno :", Dato3, "."
                    print "Tipo: ", Dato0, "."
                    print "Remuneracion Bruta Mensual :", Dato14, "."
                    print "Estamento :", Dato1, "."
                    print "Funcion :", Dato7, "."
                    print "Universidad :", insUniversidad, "."
                    print "Fecha_Ingreso :", Dato9, "."
                    print "Fecha_Termino :", Dato10, "."
                    #print "------------------------------"
                    #print "------------------------------"

                    cursor.execute(
                        "INSERT INTO Mostrar_persona(Nombre,apellidoP,apellidoM,tipo,remuneraciones,estamento,funcion,universidad,fecha_Ingreso,fecha_Informacion)"
                        "VALUES(?,?,?,?,?,?,?,?,?,?);", (datosUniversidad))
                    cursor.commit()


                    v += 1

