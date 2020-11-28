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


import sys
import config
from App import controller
from DISClib.ADT import stack
import timeit
assert config

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones  y  por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Variables
# ___________________________________________________

citiBikeTripData= '201801-1-citibike-tripdata'
recursionLimit= 20000
# ___________________________________________________
#  Menu principal
# ___________________________________________________

def printMenu():
    print("\n")
    print("*******************************************")
    print("Bienvenido")
    print("1- Inicializar Analizador")
    print("2- Cargar información de Cantidad de clusters de Viajes")
    print("3- requerimiento 1")
    print("4- requerimiento 2")
    print("5- requerimiento 3 ")
    print("6- requerimiento 4 ")
    print("7- requerimiento 5 ")
    print("8- requerimiento 6")
    print("9- requerimiento 7")
    print("10- requeirmiento 8")
    print("0- Salir")
    print("*******************************************")

def optionTwo():
    print("\nCargando información de transporte de singapur ....")
    controller.loadFile(cont, citiBikeTripData)
    trips= controller.totalTrips(cont)
    numVertex= controller.totalStations(cont)
    numEdges= controller.totalConnections(cont)
    print('Numero de vertices: ' + str(numvertex))
    print('Numero de arcos: ' + str(numedges))
    print('Total de viajes: ') + str(trips)
    print('El limite de recursion actual: ' + str(sys.getrecursionlimit()))
    sys.setrecursionlimit(recursionLimit)
    print('El limite de recursion se ajusta a: ' + str(recursionLimit))


def optionThree():
    estacion1=input('ingrese estacion 1: ')
    estacion2=input('ingrese estacion 2: ')
    respuesta= controller.cantidadDeClustersReq1(cont,estacion1,estacion2)
    if respuesta[1] is True:
       print('las estaciones estan en el  mismo cluster')
    else:
       print('las estaciones no estan en el mismo cluster')
    print('el numero de clusters son:' + respuesta[0])


def optionfour():


def optionfive():
    print('El top tres de estaciones de salida, llegada y menos usadas respectivamente son: ' + 
    controller.estacionesCriticasReq3(cont))

def optionsix():

def optionseven():
    

def optioneight():
    latitud1=float(input("Ingrese la latitud 1: "))
    latitud2=float(input("Ingrese la latitud 2: "))
    longitud1=float(input("Ingrese la longitud 1: "))
    longitud1=float(input("Ingrese la longitud 2: "))
    respuesta=controller.rutaInteresTuristicoReq6(citibike,latitud1,latitud2,longitud1,longitud2)
    print(respuesta)
    
"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n>')

    if int(inputs[0]) == 1:
        print("\nInicializando....")
        cont = controller.init()
    
    elif int(inputs[0]) == 2: 
        executiontime = timeit.timeit(optionTwo, number=1)
        print("Tiempo de ejecución: " + str(executiontime)) 

    elif int(inputs[0]) == 3:  
         station1= input("ingrese estacion 1")
         statin2= input("ingrese estacion 2")
         executiontime = timeit.timeit(optionThree, number=1)
         print("Tiempo de ejecución: " + str(executiontime))

    elif int(inputs[0]) == 4:


    elif int(inputs[0]) == 5:
        executiontime = timeit.timeit(optionFive, number=1)
        print("Tiempo de ejecución: " + str(executiontime)) 
         
    elif int(inputs[0]) == 6:  


    elif int(inputs[0]) == 7:
        executiontime = timeit.timeit(optionSeven, number=1)
        print("Tiempo de ejecución: " + str(executiontime)) 
          

    elif int(inputs[0]) == 8:    
        executiontime = timeit.timeit(optionEight, number=1)
        print("Tiempo de ejecución: " + str(executiontime)) 

    else:
        sys.exit(0)
sys.exit(0)                      
