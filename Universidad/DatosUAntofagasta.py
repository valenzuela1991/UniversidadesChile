#scrapy runspider DatosUAntofagasta.py
from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup
import sqlite3 as sqlite

#Ingresar / crear base de datos
nombre_db = "Universidades.db"
cursor = sqlite.connect(nombre_db)

cursor.execute("CREATE TABLE IF NOT EXISTS datos("
               "nombre VARCHAR(40) NOT NULL,"
               "apellidoP VARCHAR(40) NOT NULL,"
               "apellidoM VARCHAR(40) NOT NULL,"
               "tipo VARCHAR(40) NOT NULL,"
               "remuneraciones VARCHAR(40) NOT NULL,"
               "estamento VARCHAR(40) NOT NULL,"
               "funcion VARCHAR(40) NOT NULL,"
               "universidad INTEGER NOT NULL,"
               "fecha VARCHAR(40) NOT NULL)"
               )

class UniversidadAntofagastaCrawler(CrawlSpider):
    name = 'Universidad de Antofagasta'
    allowed_domains = ['transparencia.uantof.cl']
    start_urls = ['http://transparencia.uantof.cl/index.php?action=plantillas_selec_fecha&ig=21', #Personal Planta
                  'http://transparencia.uantof.cl/index.php?action=plantillas_selec_fecha&ig=22'] #Personal Contrata

    #comportamiento del crawl
    rules = (
        Rule(LinkExtractor(allow=(), restrict_xpaths=('//*[@id="columna1_interiores"]/p[1]/a')),follow= True),
        Rule(LinkExtractor(allow=(), restrict_xpaths=('/html//body')), callback='parse_items')
    )

    def parse_items(self, response):
            milista = []
            #Extraemos el codigo de la tabla
            InfoTabla = response.xpath('//*[@id="batalla"]').extract_first()
            soup = BeautifulSoup(InfoTabla)
            #separamos los datos de la tabla por td
            line = soup.select('td')
            fechaRegistro = response.xpath('//*[@id="detalle_actualizacion"]/h3/text()').extract()
            insfechaRegistro = " ".join(fechaRegistro)
            #Personal Planta :  06/07/2017 ---> 16 campos la tabla
                                #08/08/2017 ---> 18 campos la tabla

            #Personal Contrata : 06/07/2017 ---> 16 campos la tabla
                                #08/08/2017 ---> 18 campos la tabla
            if fechaRegistro > " 07/08/2017":
                campos = 18
                print "La fecha: ", fechaRegistro, " es mayor que:  07/08/2017 y usa:", campos,"campos"
                for i, y in enumerate(line):
                    palabra = y.next_element
                    milista.append(palabra)
                    # GUARDAMOS LOS DATOS DE LA TABLA
                    v = 0
                while palabra != '':
                    # DATOS OBTENIDOS DE LA PAGINA
                    print ("Hay 18 campos")
                    Nombre = milista[(campos * v) + 4]
                    ApellidoP = milista[(campos * v) + 2]
                    ApellidoM = milista[(campos * v) + 3]
                    Tipo = response.xpath('normalize-space(//*[@id="detalle_content"]/h4/text())').extract()
                    Remuneracion_Bruta = milista[(campos * v) + 11]
                    Estamento = milista[(campos * v) + 1]
                    Funcion = milista[(campos * v) + 7]
                    Universidad = response.xpath(
                        'normalize-space(//*[@id="footer"]/div/table/tbody/tr[1]/td/h1/text())').extract()
                    Fecha = milista[(campos * v) + 15]
                    FechaTablas = response.xpath('//*[@id="detalle_actualizacion"]/h3/text()').extract()

                    # Convertimos los xpath en string para guardarlos en la base de datos.
                    insTipo = " ".join(Tipo)
                    insUniversidad = " ".join(Universidad)
                    insFechaTabla = " ".join(FechaTablas)

                    datosUniversidad = (
                        Nombre, ApellidoP, ApellidoM, insTipo, Remuneracion_Bruta, Estamento, Funcion,
                        insUniversidad, Fecha, insFechaTabla)

                    print "-----Datos Persona-----"
                    print "Nombre :", Nombre, "."
                    print "Apellido Paterno :", ApellidoP, "."
                    print "Apellido Materno :", ApellidoM, "."
                    print "Tipo: ", insTipo, "."
                    print "Remuneracion Bruta Mensual :", Remuneracion_Bruta, "."
                    print "Estamento :", Estamento, "."
                    print "Funcion :", Funcion, "."
                    print "Universidad :", insUniversidad, "."
                    print "Fecha_Ingreso :", Fecha, "."
                    print "Fecha_Informacion * ", campos, " :", insFechaTabla, "."
                    print "------------------------------"
                    print "------------------------------"

                    cursor.execute(
                        "INSERT INTO Mostrar_persona(Nombre,apellidoP,apellidoM,tipo,remuneraciones,estamento,funcion,universidad,fecha_Ingreso,fecha_Informacion)"
                        "VALUES(?,?,?,?,?,?,?,?,?,?);", (datosUniversidad))
                    cursor.commit()

                    v += 1
            else:
                campos = 16
                print "La fecha: ", fechaRegistro, " es menor que:  07/08/2017 y usa:", campos,"campos"
                for i, y in enumerate(line):
                    palabra = y.next_element
                    milista.append(palabra)
                    # GUARDAMOS LOS DATOS DE LA TABLA
                    v = 0
                while palabra != '':
                        # DATOS OBTENIDOS DE LA PAGINA
                        Nombre = milista[(campos*v)+4]
                        ApellidoP = milista[(campos*v)+2]
                        ApellidoM = milista[(campos*v)+3]
                        Tipo = response.xpath('normalize-space(//*[@id="detalle_content"]/h4/text())').extract()
                        Remuneracion_Bruta = milista[(campos*v)+11]
                        Estamento = milista[(campos*v)+1]
                        Funcion = milista[(campos*v)+7]
                        Universidad = response.xpath('normalize-space(//*[@id="footer"]/div/table/tbody/tr[1]/td/h1/text())').extract()
                        Fecha = milista[(campos*v)+13]
                        FechaTablas = response.xpath('//*[@id="detalle_actualizacion"]/h3/text()').extract()

                        # Convertimos los xpath en string para guardarlos en la base de datos.
                        insTipo = " ".join(Tipo)
                        insUniversidad = " ".join(Universidad)
                        insFechaTabla = " ".join(FechaTablas)

                        datosUniversidad = (
                            Nombre, ApellidoP, ApellidoM, insTipo, Remuneracion_Bruta, Estamento, Funcion,
                            insUniversidad, Fecha,insFechaTabla)

                        print "-----Datos Persona-----"
                        print "Nombre :", Nombre, "."
                        print "Apellido Paterno :", ApellidoP, "."
                        print "Apellido Materno :", ApellidoM, "."
                        print "Tipo: ", insTipo, "."
                        print "Remuneracion Bruta Mensual :", Remuneracion_Bruta, "."
                        print "Estamento :", Estamento, "."
                        print "Funcion :", Funcion, "."
                        print "Universidad :", insUniversidad, "."
                        print "Fecha_Ingreso :", Fecha, "."
                        print "Fecha_Informacion * ",campos," :", insFechaTabla, "."
                        print "------------------------------"
                        print "------------------------------"

                        cursor.execute(
                            "INSERT INTO Mostrar_persona(Nombre,apellidoP,apellidoM,tipo,remuneraciones,estamento,funcion,universidad,fecha_Ingreso,fecha_Informacion)"
                            "VALUES(?,?,?,?,?,?,?,?,?,?);", (datosUniversidad))
                        cursor.commit()

                        v += 1

#scrapy runspider DatosUAntofagasta.py