import csv
import os,time
from comandos import *
os.system

bus=[["o" for x in range(1,11)]for y in range(8)]
for f in bus:
    print(f)

while True:
    print("bienbenido al programa de tubus.")
    print("\n1°. mostrar asientos disponibles ")
    print("\n2°. comprar asiento")
    print("\n3°. mostrar las ventas")
    print("\n4°. guardar asiento o generar archivo csv ")
    print("\n5°. salir")
    opc=int(input("\n ingrese opcion "))
    os.system
    if opc==1:
        opcion_1()
    if opc==2:
        opcion_2()
    if opc==3:
        opcion_3()
    if opc==4:
        opcion_4()
    if opc==5:
        opcion_5()
    
    else:
        print("!!ERROR el numero introducido es incorrecto¡¡")