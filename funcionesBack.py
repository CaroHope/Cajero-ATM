'''
Descripcion: Programa Back-Office del ATM. Este le permite al usuario realizar
             las funciones del cajero: Consultar Balance, Retiro de Efectivo Y
             Deposito.
             *Para usar el cajero, Inicialice cajeroATM.py

Autor: Evelyn Carolina Jorge
Matricula: 20-0084

Segundo parcial
'''
import time

#balances por Defalut:
balancee = [500, 100, 2000,100]


def Consultar_Balance (indice):
    mostrarbalance = balancee[indice]
    time.sleep(0.5)
    print("Su balance es:", mostrarbalance)
    

def Retiro (indice):
    monto = int(input("Ingrese Monto a Retirar: "))
    if monto <=balancee[indice]:
        reti = int(balancee[indice]) - monto
        #balancee

        #-Desglosador de Dinero-------
        deMil = int(monto/1000)
        monto = int(monto%1000)

        deCien = int(monto/100)
        monto = int(monto%100)

        deCincuenta = int(monto/50)
        monto = int(monto%50)

        de25 = int(monto/25)
        monto = int(monto%25)

        de10 = int(monto/10)
        monto = int(monto%10)

        de5 = int(monto/5)
        monto = int(monto%5)

        de1 = int(monto/1)
        monto = int(monto%1)
        
        time.sleep(0.5)
        print("Efectivo retirado de: ")
        print(" De Mil:",deMil, "\n","De Cien:", deCien," \n", "De Cincuenta:", deCincuenta," \n", "De 25:", de25, "\n", "De 10:", de10,"\n", "De 5:", de5,"\n","De 1:", de1,"\n")
        print(" ")
        print("Su nuevo monto es: ", reti)

    else:
        print("Usted no tiene balance sufciente para este retiro.")


def Deposito (indice):
    depo = int(input("Ingrese Monto a Depositar:"))
    balancee[indice] = depo + balancee[indice]
    time.sleep(0.5)
    print("Su cuenta ha sido actualizada.")
    print("Su nuevo Balance es de: ", balancee[indice])