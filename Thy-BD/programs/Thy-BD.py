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

#main program
dataPath = r'"C:\Users\Timoteo Güerini\Desktop\Thy-BD\data\"'.strip('"')
programsPath = r'"C:\Users\Timoteo Güerini\Desktop\Thy-BD\programs"'.strip('"')
recordsPath = r'"C:\Users\Timoteo Güerini\Desktop\Thy-BD\records\"'.strip('"')
while True:
    try:        
        
        dbnames = open(recordsPath+"dbnames.txt", "at")
        dbnamesList = addNamesToList(recordsPath)  #creo la lista con los nombres de las bases de datos      
        print("".center(100,'|'))
        print("||| Escoja una opcion {:>78}".format('|||'))
        print("||| 1) CREAR UNA BASE DE DATOS {:>69}".format('|||'))
        print("||| 2) EDITAR UNA BASE DE DATOS {:>68}".format('|||'))
        print("||| 3) ELIMINAR UNA BASE DE DATOS {:>66}".format('|||'))
        print("||| 4) SALIR {:>87}".format('|||'))
        print("".center(100,'|'))
        while True:
            try:
                opcionPpal = int(input("Opcion: "))
                assert 1<= opcionPpal <= 4, "Ingrese una opcion correcta".center(80)
            except (AssertionError,ValueError) as errormsg:
                print(errormsg)
            else:
                break
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
        if opcionPpal == 2:
            os.system('cls')
            lengthNamesList = len(dbnamesList)
            print("".center(100,'|'))
            for i in range(lengthNamesList):
                op = i+1
                print("|||"+str(op)+")",dbnamesList[i])
            while True:
                try:
                    opcionPpal = int(input("Opcion: "))
                    assert 1<= opcionPpal <= lengthNamesList , "Ingrese una opcion correcta"
                except (AssertionError,ValueError) as errormsg:
                    print(errormsg)
                else:
                    break       
    except sqlite3.OperationalError as error:
        print("Error en la base de datos", error)
    else:
        pass
    finally:
        try:
            dbnames.close()
        except NameError:
            pass
