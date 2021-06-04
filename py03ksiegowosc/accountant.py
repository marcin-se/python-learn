# KSIĘGOWY-MAGAZYN v1.0
# -*- coding: UTF-8 -*-
# imort sys
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
pathIn: str = "in.txt"
pathOut: str = "out.txt"
pathHis: str = "askHistory.txt"
pathSts: str = "stockStatus.txt"

askHistory: list = []
history: list = []
argvCurrent: list = []
stockStatus: dict = {}
inData = ""
accountBalance, operation = 0, 0

while inData != "stop":
    takeData = input()
    argvCurrent = takeData.split()
    inData = str(argvCurrent[0])

    with open(pathHis, "r+") as fileHis:   # <<< askHistory
        fileLine = fileHis.readlines()
        for line in fileLine:
            newLine = line.rstrip('\n')
            askHistory.append(line)
            accountBalance = (askHistory[-1])
        askHistory.pop()

    with open(pathSts, "r+") as fileSts:   # <<< stockStatus
        fileLine = fileSts.readlines()
        for line in fileLine:
            pair = line.split(":")
            val = pair[1].rstrip()
            key = pair[0]
            stockStatus[key] = val

    if inData == "saldo":
        if len(argvCurrent) != 3:
            print("Nieprawidłowa liczba argumentów!\n")
            continue
        account = int(argvCurrent[1])
        accountBalance += account
        with open(pathOut, "w+") as fileOut:
            fileOut.write("{}\n".format(accountBalance))    # >>> out.txt

    elif inData == "zakup" or inData == "sprzedaż":
        if len(argvCurrent) != 4:
            print("Nieprawidłowa liczba argumentów!\n")
            continue
        idName = str(argvCurrent[1])
        price = int(argvCurrent[2])
        quantity = int(argvCurrent[3])
        if price <= 0 or quantity <= 0:
            print("Nieprawidłowa cena lub ilość!")
            continue
        if inData == "zakup":
            if accountBalance < (price * quantity):
                print("Zakup: brak środków na koncie!")
                continue
            else:
                accountBalance -= (price * quantity)
                if idName in stockStatus:
                    stockStatus[idName] += quantity   # >>> MAGAZYN+
                else:
                    stockStatus[idName] = quantity
        elif inData == "sprzedaż":
            if idName not in stockStatus:
                print("{}: brak produktu!".format(idName))
                continue
            elif stockStatus[idName] < quantity:
                print("{}: za mały asortyment!".format(idName))
                continue
            else:
                accountBalance += (price * quantity)
                stockStatus[idName] -= quantity       # >>> MAGAZYN-
                if stockStatus[idName] == 0:
                    del[stockStatus[idName]]
                    print("{}: produkt wyprzedany!".format(idName))
        with open(pathOut, "w+") as fileOut:
            for i in range(len(argvCurrent)):         # >>> out.txt
                fileOut.write("{}\n".format(argvCurrent[i]))

    if inData == "saldo" or inData == "zakup" or inData == "sprzedaż":
        askHistory.append(argvCurrent)               # >>> HISTORIA
        with open(pathIn, "r+") as fileIn:
            newFile = fileIn.readlines()
            fileIn.seek(0)
            for line in newFile:
                if line != "stop"+"\n":
                    fileIn.write(line)
            fileIn.truncate()
            for i in range(len(argvCurrent)):         # >>> in.txt
                fileIn.write("{}\n".format(argvCurrent[i]))
            fileIn.write("stop\n")
        operation += 1

    if inData == "konto":
        if len(argvCurrent) != 1:
            print("Nieprawidłowa liczba argumentów!\n")
            continue
        with open(pathOut, "w+") as fileOut:
            fileOut.write("{}".format(accountBalance))  # >>> out.txt
        print("Stan konta: {} gr".format(accountBalance))

    elif inData == "magazyn":
        with open(pathOut, "w+") as fileOut:
            for i in range(1, len(argvCurrent)):
                if argvCurrent[i] in stockStatus:
                    for k, v in stockStatus.items():
                        if argvCurrent[i] == k:
                            print("{}: {}".format(k, v))
                            fileOut.write("{}: {}\n".format(k, v))  # >>> out.txt
                else:
                    print("{}: brak asortymentu!".format(argvCurrent[i]))

    elif inData == "przegląd":
        if len(argvCurrent) != 3:
            print("Nieprawidłowa liczba argumentów!\n")
            continue
        with open(pathOut, "r+") as fileOut:
            for i in range(int(argvCurrent[1]), int(argvCurrent[2]) + 1):  # out
                for j in range(len(askHistory[i])):
                    print("Operacja({}): {}".format(i, askHistory[i][j]))
                    fileOut.write("{}\n".format(askHistory[i][j]))

else:
    if operation > 0:
        position = len(askHistory) - operation
        for i in range(position, len(askHistory)):
            for j in range(len(askHistory[i])):
                print("Operacja({}): {}\n".format(i, askHistory[i][j]))
        operation = 0
        print("Zakończono operacje na koncie.\n")
    else:
        print("Koniec. Brak operacji.\n")

    with open(pathHis, "w+", encoding="utf8") as fileHis:   # >>> askHistory.txt
        askHistory.append(accountBalance)
        for i in range(len(askHistory)):
            fileHis.write("{}\n".format(askHistory[i]))

    with open(pathSts, "w+", encoding="utf8") as fileSts:   # >>> stockStatus.txt
        for k, v in stockStatus.items():
            fileSts.write("{}:{}\n".format(k, v))
