'''
Descripcion: Programa que simula un Cajero Automatico dispensador
             de efectivo (ATM). El usuario puede logearse y realizar
             tres funciones contenidas en el programa Back-Office.
             *Inicialice este Programa para usar el cajero.

Autor: Evelyn Carolina Jorge
Matricula: 20-0084

Segundo parcial
'''
import time

nombre = ["Maria Perez", "Pedro Martin", "Mari Mendoza", "Kelly Molly"]
pin = [1234,4321,9876, 7654]
nocuenta= [20091302,38103827,1083728,92836234]

contru = 0
x= 0
indice = 0


#Login=========================

print("< C A J E R O >")
print("Bienvenido a su cajero favorito,")
time.sleep(1)
while contru == 0 and x <=2:
    pinlo = input("Escriba su Pin para ingresar: ")
    try:
        pinlo = int(pinlo)
    except ValueError:
        print("Escriba datos enteros.")
        time.sleep(0.5)
        exit
    for f in range (3):
        l = pin[f]
        if pinlo == l:
            contru =+1
            indice = f
    if contru == 0:
        print("PIN Invalido.")        
    x = 1 + x
    

if x >2:
    print("Operacion cancelada")
    #Salir del programa


# Menu========================

from funcionesBack import *
if contru == 1:
    op = 0
    y=0
    while y==0:
        print("< M E N U >")
        print("Consultar balance (1)")
        print("Retiro de Efectivo(2)")
        print("Depositar (3)")
        op = input("Elija una Opcion: ")
        try:
            op = int(op)
        except ValueError:
            print("Escriba datos enteros.")
            time.sleep(0.5)
        
        if op==1 or op==2 or op==3:
            y = y+1
    
        else:
            print("----")
            print("ingrese un numero de opcion valido.")
            print("----")
    
if op == 1:
    Consultar_Balance(indice)
elif op == 2:
    Retiro(indice)
else:
    Deposito(indice)

    
print("="*5)
print("Bye")
print(" ")




