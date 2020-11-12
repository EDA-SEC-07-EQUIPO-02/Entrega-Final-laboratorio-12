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
from DISClib.Utils import error as error
from DISClib.Algorithms.Graphs import scc
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
                  }
        citibike['graph']= gr.newGraph(datastructure='ADJ_LIST',
                                            directed=TRUE,
                                            size=1000
                                            comparefunction=compareStations)

        citibike['trips'] = m.newMap(numelements=14000,
                                     maptype='PROBING',
                                     comparefunction=compareTrip)
                                       
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
    origin = trip['start station id']
    destination = trip['end station id']
    duration = int(trip['tripduration'])
    addStation(citibike, origin)
    addStation(citibike, destination)
    addConnection(citibike, origin, destination, duration)

def addConnection(citibike, origin, destination, duration):
    """
    Adiciona un arco entre dos estaciones
    """
    edge = gr.getEdge(citibike ['graph'], origin, destination)
    if edge is None:
        gr.addEdge(analyzer['graph'], origin, destination, duration)
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


def compareTrip(route1, route2):
    """
    Compara dos rutas
    """
    if (route1 == route2):
        return 0
    elif (route1 > route2):
        return 1
    else:
        return -1

