# KSIĘGOWY-MAGAZYN v1.0
# -*- coding: UTF-8 -*-
import sys
# import argparse

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

askHistory: list = []
argvCurrent: list = []
stockStatus: dict = {"jetson": 0, "raspberry": 0, "arduino": 0}
accountBalance = 0
operation = 0
# take: list = []

while 1:
    # take = [input("Podaj kolejne instrukcję: ")]
    inData = str(sys.argv[1])  # pobieram nazwę operacji
    fileIn = open("in.txt", "r+", encoding="utf8")
    fileOut = open("out.txt", "w+", encoding="utf8")

    for i in range(1, len(sys.argv)):  # >>> ARGV
        argvCurrent.append(sys.argv[i])

    if inData == "saldo" and len(sys.argv) == 4:
        accountBalance += int(sys.argv[2])  # >>> SALDO
        fileOut.write("{}\n".format(accountBalance))  # >>> out.txt
        print("{}\n".format(accountBalance))

    elif (inData == "zakup" or inData == "sprzedaż") and len(sys.argv) == 4:
        idName = str(sys.argv[2])
        price = int(sys.argv[3])
        quantity = int(sys.argv[4])
        if price < 0 or quantity <= 0:
            print("Błąd ceny lub ilości!")  # interrupt
            break
        if inData == "zakup":
            if accountBalance < (price * quantity):
                print("Brak środków!")  # interrupt
                break
            else:
                accountBalance -= (price * quantity)  # >>> SALDO
                if stockStatus.get(idName, False):
                    stockStatus[idName] += quantity  # >>> MAGAZYN
                else:
                    stockStatus[idName] = quantity  # +item
        elif inData == "sprzedaż":
            if stockStatus[idName] < quantity:
                print("Brak w magazynie!")  # interrupt
                break
            else:
                accountBalance += (price * quantity)  # >>> SALDO
                stockStatus[idName] -= quantity  # >>> MAGAZYN
                # if stockStatus[idName] == 0:
                #    del stockStatus[idName]  # -item
        for i in range(len(sys.argv) - 1):  # >>> out.txt
            fileOut.write("{}\n".format(argvCurrent))

    if inData == "saldo" or inData == "zakup" or inData == "sprzedaż":
        askHistory.append(argvCurrent)  # >>> HISTORIA
        stopLine = fileIn.readlines()
        eof = len(stopLine)
        del stopLine[eof-1]
        fileIn.seek(0)
        fileIn.writelines(stopLine)
        fileIn.truncate()
        for i in range(len(sys.argv) - 1):  # >>> in.txt
            fileIn.write("{}\n".format(argvCurrent[i]))
        fileIn.write("stop\n")
        fileIn.close()
        fileOut.close()
        operation += 1
        #break

    elif inData == "stop":
        if operation > 0:
            step = len(askHistory) - operation
            for i in range(operation):
                for j in range(4):
                    print("{}\n".format(askHistory[step + 1 + i][j]))
            operation = 0
        else:
            print("STOP")
            break

    elif inData == "konto" and len(sys.argv) == 2:
        fileOut.write("{}\n".format(accountBalance))  # >>> out.txt
        print("{}\n".format(accountBalance))
        print("{}\n".format(stockStatus.items()))
        break

    elif inData == "magazyn" and len(sys.argv) > 1:
        for i in range(2, len(sys.argv)):
            for k, v in stockStatus.items():
                if str(sys.argv[i]) == stockStatus.get(k):  # interrupt
                    print("{}: {}\n".format(k, v))
                    fileOut.write("{}: {}\n".format(k, v))  # >>> out.txt
        #break

    if inData == "przegląd":
        for i in range(int(sys.argv[2]), int(sys.argv[3]) + 1):  # >>> out.txt
            for j in range(len(askHistory[i])):
                print("{}\n".format(askHistory[i][j]))
                fileOut.write("{}\n".format(askHistory[i][j]))
        #break
    break

'''
argv = argparse.ArgumentParser(description="Pobranie argumentów z konsoli")
argv.add_argument('', '--1', help="Wartość argv[1]",
                  type=str, required=False)
argv.add_argument('', '--2', help="Wartość argv[2]",
                  type=str, required=False)
argv.add_argument('', '--3', help="Wartość argv[3]",
                  type=str, required=False)
args = argv.parse_args()
'''