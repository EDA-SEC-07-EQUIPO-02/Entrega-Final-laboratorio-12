"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 * Contribución de:
 *
 * Dario Correal
 *
 """
import config
from DISClib.ADT.graph import gr
from DISClib.ADT import map as m
from DISClib.ADT import list as lt
from DISClib.DataStructures import listiterator as it
from DISClib.Algorithms.Graphs import scc
from DISClib.Algorithms.Graphs import dijsktra as djk
from DISClib.Algorithms.Graphs import dfs as dfs
from DISClib.Utils import error as error
from DISClib.Algorithms.Graphs import scc
import math as ma
assert config

"""
En este archivo definimos los TADs que vamos a usar y las operaciones
de creacion y consulta sobre las estructuras de datos.
"""

# -----------------------------------------------------
#                       API
# -----------------------------------------------------
def neyAnalyzer():
    try:
        citibike={
                  'graph' : None
                  'trips' : 0
                  }
        citibike['graph']= gr.newGraph(datastructure='ADJ_LIST',
                                            directed=TRUE,
                                            size=1000
                                            comparefunction=compareStations)
        citibike['salida']= m.newmap(numelements=1000, 
                                            maptype='PROBING',
                                            comparefunction=compareRoutes)
        citibike['llegada']=m.newmap(numelements=1000, 
                                            maptype='PROBING',
                                            comparefunction=compareRoutes)
                                       
        return citibike
    except Exception as exp:
        error.reraise(exo,'model:newAnalyzer')   


# Funciones para agregar informacion al grafo
def addStation(citibike, stationid):
    """
    Adiciona una estación como un vertice del grafo
    """
    if not gr.containsVertex(citibike ['graph'], stationid):
            gr.insertVertex(citibike ['graph'], stationid)
    return citibike

def addTrip(citibike, trip):
    """
    """
    duration = int(trip['tripduration'])
    origin = trip['start station id']
    destination = trip['end station id']
    citibike['trips'] +=1
    addStation(citibike, origin)
    addStation(citibike, destination)
    addConnection(citibike, origin, destination, duration)
    

def addConnection(citibike, origin, destination, duration):
    """
    Adiciona un arco entre dos estaciones
    """
    edge = gr.getEdge(citibike ['graph'], origin, destination)
    if edge is None:
        wieght=[duration,1]
        gr.addEdge(analyzer['graph'], origin, destination, wieght)  
    return citibike

# ==============================
# Funciones de consulta
# ==============================

def totalConnections(analyzer):
    return gr.numEdges(analyzer['graph'])

def totalTrips(analyzer):
    return analyzer['trip']

def totalStations(analyzer):
    return gr.numVertices(analyzer['graph'])


def numSCC(graph, sc):
"""
invoca el algoritmo de Kosaraju para informar cuántos componentes fuertemente conectados se encontraron. 
"""
    sc = scc.KosarajuSCC(graph)
    return scc.connectedComponents(sc)

def sameCC(sc, station1, station2)
"""
función informa si dos estaciones están en el mismo componente conectado.
"""
    return scc.stronglyConnected(sc, station1, station2)


# ==============================
# Funciones Helper
# ==============================

# ==============================
# Funciones de Comparacion
# ==============================


def compareStations(stop, keyvaluestop):
    """
    Compara dos estaciones
    """
    stopcode = keyvaluestop['key']
    if (stop == stopcode):
        return 0
    elif (stop > stopcode):
        return 1
    else:
        return -1


def compareRoutes(route1, route2):
    """
    Compara dos rutas
    """
    if (route1 == route2):
        return 0
    elif (route1 > route2):
        return 1
    else:
        return -1

# ==============================
# Funciones req
# ==============================
def cantidadDeClustersReq1(citibike, estacion1,estacion2):
    cluster= scc.KosarajuSCC(citibike['graph'])
    return scc.connectedComponents(clusters), scc.stronglyConnected(clusters)

def estacionesCriticasReq3(citibike):

    estacionLlegada = lt.newList(datastructure='SINGLE_LINKED', cmpfunction=compareRoutes)
    estacionSalida = lt.newList(datastructure='SINGLE_LINKED', cmpfunction=compareRoutes)
    menosUsadas = lt.newList(datastructure='SINGLE_LINKED', cmpfunction=compareRoutes)
    llegada = 0
    salida = 0
    usadas= 0
    lista = []
    lista2=[]
    top3 = []
    conecciones = gr.edges(citibike['graph'])

    for ruta in range(1, lt.size(conecciones)):
        lt.addLast(lista2, lt.getElement(conecciones, ruta))

    for ruta in range(1,3):
        lt.addLast(lista, lt.getElement(lista2, ruta))
        lt.addLast(top3, lt.getElement(lista2, lt.size(lista2)-ruta))

    while llegada <= lt.size(lista2) and lt.size(estacionLlegada):
        if lt.isPresent(lista, lt.getElement(conecciones, llegada)['llegada'])['vertexA']:
            Ellegada = getStation(citibike, lt.getElement(conecciones, llegada)
            lt.addLast(estacionLlegada, Ellegada)
        llegada +=1

    while salida <= lt.size(lista2) and lt.size(estacionSalida):
        if lt.isPresent(lista, lt.getElement(conecciones, salida)['salida'])['vertexB']:
            Esalida = getStation(citibike, lt.getElement(conecciones, salida)
            lt.addLast(estacionSalida, Esalida)
        salida +=1

    while usadas <= lt.size(lista2) and lt.size(menosUsadas):
        if lt.isPresent(top3, lt.getElement(conecciones, usadas)['salida'])['vertexA']:
            Eusada =  getStation(citibike, lt.getElement(conecciones, usadas)
            if not lt.isPresent(menosUsadas, Eusada):
                lt.addLast(menosUsadas, Eusada)
        usadas +=1

    return estacionSalida, estacionLlegada, menosUsadas


def rutaInteresTuristicoReq6(citibike,latitud1,latitud2,longitud1,longitud2):
    x=ma.radians(latitude)
    y=ma.radians(latitud2)
    z=ma.radians(latitude-latitud1)
    w=ma.raidans(longitude-longitud1)
    p=ma.radians(latitude-latitud2)
    r=ma.radians(longitude-longitud2)
    a=ma.asin(match.sqrt(coordenadas_salida))
    dic=[]
    b=ma.asin(match.sqrt(coordenadas_llegada))
    salida=20000
    llegada=20000
    Ellegda=""
    Esalida=""
    iterator=it.newIterator(m.keyset(citibike['graph']))
    while it.hasNext(iterator):
        key=it.next(iterator)
        location=m.get(citibike['graph'],llave)
        longitude=location[0]
        latitude=location[1]
        coordenadas_salida= (ma.sin(z/2))**2 + ma.cos(x)*(ma.sin(z)/2)**2*((ma.sin(z/2))**2 + ma.cos(x)*(ma.sin(w)/2)**2)
        coordenadas_llegada=(ma.sin(p/2))**2 + ma.cos(x)*(ma.sin(r)/2)**2*((ma.sin(p/2))**2 + ma.cos(x)*(ma.sin(r)/2)**2)
        dLlegada=12742*a
        dSalida=12742*b
        if dLlegada <=salida:
           salida=dLlegada
           Ellegada=location['value']
        if dSalida<=llegada:    
           salida=dSalida
           Esalida=location['value']
    if djk.hasPathTo(djk.Dijkstra(citibike['graph'],str(Esalida)), Ellegada):
        rutas=djk.pathTo(djk.Dijkstra(citibike['graph'],str(Esalida)), Ellegada)
        ite=it.newIterator(rutas)
        while it.hasNext(ite):
            keys=it.next(ite)
            dic.append(keys['vertexB'])
    return Ellegada, Esalida, dic        

def circularRoute1(analyzer, stationID, time):
    


def circularRoute2(analyzer, stationID, time):
    analyzer['paths'] = djk.Dijkstra(analyzer['connections'], stationID)
    djk.hasPathTo

def routeByAge(age):
    byear = 2020 - age
    
    
    
