import sqlite3
import os
import threading
import time
from colorama import Fore

#functions
def dbcreator(bdname,dataPath):
    try:
        newDB = sqlite3.connect(dataPath+bdname+".db")
    except sqlite3.OperationalError as error:
        print("Error en la base de datos", error)
    finally:
        try:
            newBD.close()
        except NameError:
            pass

def addNamesToList(recordsPath):
    namesList = []
    try:
        rec = open(recordsPath+"dbnames.txt", "rt")
        for linea in rec:
            lineaSinSalto = linea.rstrip('\n')
            if lineaSinSalto == "":
                pass
            elif lineaSinSalto not in namesList:
                namesList.append(lineaSinSalto)
                
    except IOError:
        print("Error al abrir el archivo")
    else:
        return namesList 
    finally:
        try:
            rec.close()
        except NameError:
            pass

def deleteDB(dbtodelete, dataPath):  #funcion para borrar una base de datos del data path
    os.remove(dataPath+"{}.db".format(dbtodelete))  #"remove" elimina un directorio

def deleteDBnameFromRecordsPath(nameToDelete, recordsPath): #funcion para borrar un nombre de una db del records path
    try:
        rec = open(recordsPath+"dbnames.txt","rt")
        for linea in rec:
            lineaSinSalto = linea.rstrip('\n')
            if linea == nameToDelete:
                #TO DO
                #LO QUE DEBO HACER ACA ES ABRIR TAMBIEN EL ARCHIVO EN MODO ESCRITURA PARA PODER BORRAR LA LINEA ESA, SINO QUEDA SIEMPRE IGUAL
    except IOError:
        print("Error al abrir el archivo")
    finally:
        try:
            rec.close()
        except NameError:
            pass

#main program
#IMPORTANTE NOTA ANTES DE EJECUTAR (APRETAR F5) EL PROGRAMA, LEER ATENTAMENTE:
#Si queres usar el programa en tu pc, lo unico que tenes que hacer es cambiar lo que este entre las comillas DOBLES (")(NO BORRES LAS COMILLAS SIMPLES)
#de estas 3 rutas, y ponerle la ruta de la carpeta en la que quieras "instalar" el programa, asi como cuando elegis la
#ruta de instalacion de cualquier otro programa. Si te preguntas por que se llama THY, es porque mi familia de usa me decia timoTHY,
#bueno, es lo primero que se me vino a la cabeza, te quiero mucho disfrutalo, igual seguro si lees esto el programa ni siquiera esta
#terminado. 
dataPath = r'"C:\Users\Timoteo Güerini\Desktop\Thy-BD\data\"'.strip('"')
programsPath = r'"C:\Users\Timoteo Güerini\Desktop\Thy-BD\programs"'.strip('"')
recordsPath = r'"C:\Users\Timoteo Güerini\Desktop\Thy-BD\records\"'.strip('"')

#OTRA NOTA: PARA PODER VER EL CORRECTO FORMATO DEL PROGRAMA, TENES QUE EJECUTARLO DESDE LA CARPETA "PROGRAMS", Y HACER DOBLE CLICK
#EN EL ARCHIVO DE PYTHON DE UNA. SI CORRES EL PROGRAMA DESDE EL IDLE, VA A SER CUALQUIER COSA, NO SEAS BOLUDO Y HACEME CASO. GRACIAS
while True:
    try:        
        dbnames = open(recordsPath+"dbnames.txt", "at")
        dbnamesList = addNamesToList(recordsPath)  #creo la lista con los nombres de las bases de datos tomados desde el unico archivo existente en el recordsPath    
        print("".center(100,'|'))
        print("||| Escoja una opcion {:>78}".format('|||'))
        print("||| 1) CREAR UNA BASE DE DATOS {:>69}".format('|||'))
        print("||| 2) MENU BASES DE DATOS {:>73}".format('|||'))
        print("||| 3) SALIR {:>87}".format('|||'))
        print("".center(100,'|'))
        while True:
            try:
                opcionPpal = int(input("Opcion: "))
                assert 1<= opcionPpal <= 3, "Ingrese una opcion correcta".center(80)
            except (AssertionError) as errormsg:
                print(errormsg)
            except ValueError:
                print("Ingrese una opcion correcta".center(80))
            else:
                break

        if opcionPpal == None:
            print("No puede salir de este menu, ingrese una opcion correcta")
        #opcion 1
        if opcionPpal == 1:
             os.system('cls')
             print("".center(100,'|'))
             newDB = input("Ingrese el nombre de la base de datos a crear: ")
             if newDB is "":
                 time.sleep(1)
                 os.system('cls')
                 pass  
             else:
                while newDB in dbnamesList:
                    os.system('cls')
                    print("".center(100,'|'))
                    newDB = input("La base de datos que quiere crear ya existe, reingrese el nombre: ")
                os.system('cls')
                print("|"*100)
                print("Creando la base de datos...")
                dbcreator(newDB,dataPath)
                dbnames.write(newDB+"\n") #guardo el nombre de la base de datos en el archivo para consultarla mas tarde
                time.sleep(1)
                os.system('cls')
                print("".center(100,'|'))
                print("Base de datos creada correctamente, espere para continuar...")
                time.sleep(1)
                os.system('cls')
                pass 
        #opcion 2
        elif opcionPpal == 2:
            while True:
                os.system('cls')
                lengthNamesList = len(dbnamesList)
                print("".center(100,'|'))
                for i in range(lengthNamesList): #muestro en formato lista todas las bases de datos disponibles
                    op = i+1
                    print("||| *",dbnamesList[i])
                #MENU EDITAR BD
                print("".center(100,'|'))
                print("||| Escoja una opcion: ")
                print("||| 1) Eliminar una DB")
                print("||| 2) Editar")
                print("||| 3) Atras")
                while True:
                    try:
                        opcionMenuEditarDB = int(input("Opcion: "))
                        assert 1<= opcionPpal <= 2 , "Ingrese una opcion correcta"
                    except (AssertionError,ValueError) as errormsg:
                        print(errormsg)
                    else:
                        break
    
                if opcionMenuEditarDB is 1:    # aca is es lo mismo que poner "==" solo que mas formal, es para practicar otras formas de interpretacion.
                    while True:
                        try:
                            if len(dbnamesList) > 0:
                                lengthNamesList = len(dbnamesList)
                                os.system('cls')
                                for i in range(lengthNamesList): #muestro en formato lista todas las bases de datos disponibles
                                    print("||| *",dbnamesList[i])
                                deleteThisDB = input("Ingrese el nombre de la db a eliminar, o enter para volver atras: ")
                                if deleteThisDB is "":
                                    break
                                assert deleteThisDB in dbnamesList
                                deleteDBnameFromRecordsPath(deleteThisDB, recordsPath) #elimino el NOMBRE de la db del archivo "dbnames.txt"
                                dbnamesList.remove(deleteThisDB) #elimino la db de la lista
                                deleteDB(deleteThisDB, dataPath) #finalmente, elimino la base de datos para anular su completa existencia
                                print("Base de datos eliminada correctamente")
                                time.sleep(2)
                                pass
                            else:
                                print("No existe ninguna base de datos a eliminar, cree una")
                                print("Volviendo atras...")
                                time.sleep(2)
                                break
                        except AssertionError:
                            print("La db que escogio no existe")
                            
                elif opcionMenuEditarDB is 3:
                    os.system('cls')
                    break
                
    except sqlite3.OperationalError as error:
        print("Error en la base de datos", error)
    except ValueError:
        print("Ingrese una opcion valida")
    else:
        pass
    finally:
        try:
            dbnames.close()
        except NameError:
            pass
