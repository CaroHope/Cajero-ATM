'''
Descripcion: Programa que simula un Cajero Automatico dispensador
             de efectivo (ATM). El usuario puede ingresar y realizar
             tres funciones contenidas en el progr5ama Back-Office.
             *Inicialice este Programa para usar el cajero.

Autor: Evelyn Carolina Jorge
Matricula: 20-0084

Segundo parcial
'''

nombre = ["Maria Perez", "Pedro Martin", "Mari Mendoza"]
pin = [1234,4321,9876]



contru = 0
x= 0
indice = 0


#Login=========================

while contru == 0 and x <=2:
    pinlo = int(input("Ingrese su Pin: "))
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
        op = int(input("Elija una Opcion: "))
        
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
#desea ir al menu
#desea salir




