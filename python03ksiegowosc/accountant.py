# KSIĘGOWY-MAGAZYN v1.0
# -*- coding: UTF-8 -*-
import sys
import os
path_1 = "plikInput.txt"
path_2 = "plikMagazyn.txt"
path_3 = "plikHistoria.txt"

def clear_screen():
    if os.name == 'posix':  # dla mac i linux
        _ = os.system('clear')
    else:
        _ = os.system('cls')  # dla windows
    return

def listingWarehouse():
    for i in range(1, len(warehouse) + 1):
        print("Aktualny stan magazynowy:")
        print(warehouse[i][0], "\n")            # productID
        print(warehouse[i][1], "\n")            # unitPrice
        print(warehouse[i][2], "\n")            # quantity
    return

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
clear_screen()
fileInput = open(path_1, "a+", encoding="utf8")
fileWarhouse = open(path_2, "a+", encoding="utf8")
fileHistory = open(path_3, "a+", encoding="utf8")

dataInput: list = []       # dataInput[i] = (sys.argv[1], sys.argv[2], ...)
warehouse: list = []       # warehouse[i] = (id_produktu, wartość_jedn, ilość)
dataHistory: list = []     # dataHistory[i] = (argument1, argument2, ...)
accountBalance = 1000000

while 1:
    inputData = str(sys.argv[1])
    # for i in range(len(sys.argv) + 1):
        dataInput.append([a][i] = str(sys.argv[i+1])

    fileInput.write(dataInput[len(dataInput)-1], "\n")
    if inputData == "saldo" and len(sys.argv) == 4:
        changeValue = int(sys.argv[2])
        comment = str(sys.argv[3])
        accountBalance += changeValue
        dataHistory.append([inputData, accountBalance, comment])
        fileHistory.write("{}".format(dataHistory[(len(dataHistory))-1]))

    elif (inputData == "zakup" or inputData == "sprzedaż") and len(sys.argv) == 4:
        productID = str(sys.argv[2])
        unitPrice = int(sys.argv[3])
        quantity = int(sys.argv[4])
        if unitPrice < 0 or quantity <= 0:
            print(" Podano absurdalne wartości dla ceny jednostkowej lub ilości.")
            break
        if inputData == "zakup":
            if accountBalance < (unitPrice * quantity):
                print(" Na koncie firmowym pozostało {:8d} gr".format(
                                                         int(accountBalance)))
                print(" To za mało na dokonanie przedmiotowego zakupu.")
            continue
            else:
                accountBalance -= (unitPrice * quantity)
        elif inputData == "sprzedaż":
            if True:   # sprawdz, czy nie ma w magazynie?
                print(" Mamy niewystarczającą ilość asortymentu.")
        continue
            else:
                pass    # jak jest, sprzedajemy!
            accountBalance += (unitPrice * quantity)
            warehouse.append([inputData, productID, unitPrice, quantity])
        dataHistory.append([inputData, productID, unitPrice, quantity])



'''
    elif inputData == "sprzedaż":
        productID = str(sys.argv[2])
        unitPrice = int(sys.argv[3])
        quantity = int(sys.argv[4])
        dataHistory.append([inputData, productID, unitPrice, quantity])
        accountBalance += (unitPrice * quantity)
'''

        if unitPrice < 0 or quantity <= 0:
            print(" Podano nierealne wartości dla ceny jednostkowej lub ilości.")
            break
        elif accountBalance < (unitPrice * quantity):
            print(" Na koncie firmowym pozostało {:8d} gr".format(
                int(accountBalance)))
            print(" To za mało na dokonanie przedmiotowego zakupu.")
        else:
            accountBalance -= (unitPrice * quantity)


    elif inputData == "konto":


    elif inputData == "magazyn":


    elif inputData == "przegląd":


    else:
        print(" Wprowadzono nieprawidłowe dane! Przyjdź, jak się nauczysz :/")
        break
