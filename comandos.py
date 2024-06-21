import csv
import os,time
bus=[["o"for x in range(1,5)]for y in range (8)]
nombre=[]
def opcion_1():
    print("asientos del bus")
    for f in bus:
        print(f)
    time.sleep(3)    


def opcion_2():
    print("compra tu asiento")
    print("el valor de los asientos es de 4500 pesos")
    nom=input("ingrese su nombre: ")
    edad=int(input("ingrese su edad: "))
    fono=int(input("ingrese numero telefonico: +56"))
    rut=int(input("ingrese su rut: "))
    for f in bus:
        print(f)
    fila=int(input("ingrese la fila que dese ocupar teniendo en cuenta que \nestan numeradas desde isquierda a derecha"))
    columna=int(input("ingrese la columna que dese ocupar teniendo en cuenta \nque estan numeradas desde arriba hacias abajo "))
    if bus[fila-1][columna-1]=="o":
        bus[fila-1][columna-1]="x"
        for f in bus:
            print(f)
        time.sleep(3)
def opcion_3():
    print("revicion de ventas")

def opcion_4():
    pass

def opcion_5():
    print("gracias por usar el programa ADIOS ")
    exit