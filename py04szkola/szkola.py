# SZKOŁA v1.0
# -*- coding: UTF-8 -*-
import sys
import os

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
fileIn = open("in.txt", "a+", encoding="utf8")
fileOut = open("out.txt", "w+", encoding="utf8")

pupils: dict = { name: (clas) }
teachers: dict = { name: [subject, ([clas]) ]}
educators: dict = { name: ([clas]) } 

classes: tuple = (1a, 1b, 1c, 1d, 2a, 2b, 2c, 2d, 3a, 3b, 3c, 3d)
clas: set = ([])
subjects: tuple = (polski, angielski, matematyka, geografia, fizyka,
                    biologia, chemia, w-f)
subject: set = ([])

ucz{„Janek Brzęch”: (klasa,)}
naucz{ „Jan Brzechwa”: [przedmiot, ([klasa]) }
wych{ „John Breschfa”: ([clas]) }

subject = subject.lower()
name = name.title()
clases.append(1b)   # dodaj na koniec listy
clases.add(1b)   # dodaj na koniec zbioru
clases.sort()   # sorowanie

pupils: list = [(name, {"klasa": clas})] 
teachers: list = [(name, {"przedmiot": subject, "uczy": sort{classes})]
educators: list = [(name, {"wychowuje": sort{classes})]




while input_data != strip("koniec"):
    
    if len(sys.argv) == 1:
        
        # wprowadzanie uczniów i belfrów
    
        if inputData == "saldo" and len(sys.argv) == 4:           # saldo >>> hist
            accountBalance += int(sys.argv[2])
            print("{}\n".format(accountBalance))
            fileOut.write("{}\n".format(accountBalance))
    
        elif (inputData == "zakup" or inputData == "sprzedaż") and len(sys.argv) == 4:
            productID = str(sys.argv[2])
            unitPrice = int(sys.argv[3])
            quantity = int(sys.argv[4])
            if unitPrice < 0 or quantity <= 0:
                print("Błąd ceny lub ilości!")
                break
            if inputData == "zakup":
                if accountBalance < (unitPrice * quantity):
                    print("Brak środków!")
                    continue
                else:
                    accountBalance -= (unitPrice * quantity)
                    for i in range(1, len(sys.argv)):    # zakup/sprzedaż >>> hist
                        argvCurrent.append(sys.argv[i])
                    askHistory.append(argvCurrent)
    
            elif inputData == "sprzedaż":
                if True:   # sprawdz, czy nie ma w magazynie?
                    print("Brak w magazynie")
            continue
                else:
                    pass    # jak jest, sprzedajemy!
                accountBalance += (unitPrice * quantity)
                warehouse.append([inputData, productID, unitPrice, quantity])
            dataHistory.append([inputData, productID, unitPrice, quantity])
    
    
    
        for i in range(0, len(askHistory)):                           # <<< in.txt
            for j in range(len(sys.argv)-1):
                print("{}\n".format(askHistory[i][j]))
                fileIn.write("{}\n".format(askHistory[i][j]))
    
        askRange = [1, 2]
        for i in range(askRange[0], askRange[1]+1):                  # >>> out.txt
            for j in range(len(askHistory)):
                print("{}\n".format(askHistory[i][j]))
                fileOut.write("{}\n".format(askHistory[i][j]))
    
    
        print(askHistory[:])
        break
    
    
        inputData = str(sys.argv[1])                            # wczytuję argv 1
        if inputData == "saldo" and len(sys.argv) == 4:
            changeValue = int(sys.argv[2])
            comment = str(sys.argv[3])
            accountBalance += changeValue
            historyTuple.append([inputData, accountBalance, comment])
            fileHist.write("{}".format(historyTuple[(len(historyTuple)) - 1]))
    
        elif (inputData == "zakup" or inputData == "sprzedaż") and len(sys.argv) == 4:
            productID = str(sys.argv[2])
            unitPrice = int(sys.argv[3])
            quantity = int(sys.argv[4])
            if unitPrice < 0 or quantity <= 0:
                print(" Błędna cena lub ilość.")
                break
            if inputData == "zakup":
                if accountBalance < (unitPrice * quantity):
                    print(" Za mało kasy! Brakuje {} gr".format(
                                    int(accountBalance - (unitPrice * quantity)))
                continue
                else:
                    accountBalance -= (unitPrice * quantity)
            elif inputData == "sprzedaż":
                if True:   # sprawdz, czy nie ma w magazynie?
                    print(" Za mało asortymentu.")
            continue
                else:
                    pass    # jak jest, sprzedajemy!
                accountBalance += (unitPrice * quantity)
                warehouseDict.append([inputData, productID, unitPrice, quantity])
            historyTuple.append([inputData, productID, unitPrice, quantity])
    
    if len(sys.argv) == 2:
        in_class = str(sys.argv[2]).strip()
        if in_class in classes
           ... 
    
    if len(sys.argv) == 3:
        firstname = str(sys.argv[2])
        surname = str(sys.argv[3])
        name = str(strip(firstname) + " " + strip(surname)).title()


    else:
        print("Podano nieprawidłowe parametry!")
        continue

pupil_list = [x+1 for x in range(len(pupil)) if pupil["klasa"] == ] # listowanie uczniów 
