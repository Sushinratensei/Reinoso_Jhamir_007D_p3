import os
import numpy
import msvcrt
lista_ruts = []
lista_nombres= []
lista_identificador= []
lista_nombre_mascota = []
lista_dias = []

guarderia = numpy.zeros((5,5), int)
columnas = [1,2,3,4,5]
filas = [6,7,8,9,10]
def mostrar_menu():
        os.system('cls')  
        print("""Bienvenido a Mascota Segura
        1. Grabar
        2. Buscar
        3. Retirar
        4. Salir""")

    
def ver_guarderia():
     for x in range(5):
          print("Habitaciones disponibles en primer piso"[x+1], end="")
          for y in range(5):
               print("Habitaciones disponibles en segundo piso" [y+1], end="") 
     
def validar_opcion():
        while True:
            try:
                opcion = int(input("Ingrese opción a elegir: "))
                if opcion in (1,2,3,4):
                    return opcion
                else: 
                    print("Opcion incorrecta")
            except:
                print("Error, debe ser un número entero")

def validar_rut():  
     while True:
            try:
               rut = int(input("Ingrese su rut sin puntos ni digito verificador: "))
               if rut >= 1000000 and rut <= 999999999:
                    return rut
               else:
                    print("Rut, inválido")
            except:
               print("Error, deben ser números enteros")

def nom_dueño():  
     while True:
          nombre = input("Escriba su nombre: ")
          if len(nombre.strip()) >= 3 and nombre.isalpha:
               return nombre
          else:
               print("Error, nombre inválido")

def nom_mascota(): 
     while True:
          nombre_m = input("Escriba el nombre de su mascota: ")
          if len(nombre_m.strip()) >= 3 and nombre_m.isalpha:
               return nombre_m
          else:
               print("Error, nombre inválido")

def cantidad_dias():
     while True:
            try:
               dias = int(input("Ingrese cantidad de días que se quedará: "))
               lista_dias.append(dias)
               if dias > 0:
                    return dias
               else:
                    print("Error, el número de días debe ser superior a 0")
            except:
                print("Error, deben ser números enteros")

def num_identificador():
     identificador = lista_identificador
     if identificador == lista_identificador:
          identificador + 1
     print("Su numero de identificacion es: ", identificador)

   
def grabar():
     rut = validar_rut()
     nombre = nom_dueño()
     nombre_m = nom_mascota()
     dias = cantidad_dias()
     
     lista_ruts.append(rut)
     lista_nombres.append(nombre)
     lista_nombre_mascota.append(nombre_m)
     lista_dias.append(dias)
     
     print("Elija entre las habitaciones disponibles: ")
     if 0 not in ver_guarderia:
          print("No hay habitaciones disponibles")
          return
     while True:
          validar_rut

def buscar(posicion):
    rut = int(input("Indique su rut: "))
    if rut in lista_ruts:
         lista_ruts.index(posicion)