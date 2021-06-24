# KSIĘGOWY-MAGAZYN v2.0_on_classes
# -*- coding: UTF-8 -*-
import os, sys, pickle, msvcrt
from ..library.dodatki import clear_screen, title_line, TPL_FORMAT_table3
from ..library.py05pliki import\
    dict_to_file, dict_to_file_obj, dict_from_file,\
    get_data_from_file, get_data_from_terminal,\
    print_info_argv2, print_info_argv2_obj,\
    print_info_argv234, print_info_argv234_obj
from ..library.py05klasy import groups_dict, group_objects,\
    make_group, make_group_obj,\
    Pupil, Teacher, Educator,\
    if_class, if_class_obj,\
    if_pupil, if_pupil_obj,\
    if_teacher, if_teacher_obj,\
    if_educator, if_educator_obj
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
path_in: str = "in.txt"
path_balance: str = "saldo.py"
path_buy: str = "zakup.py"
path_sale: str = "sprzedaz.py"
path_account: str = "konto.py"
path_stock: str = "magazyn.py"
path_overview: str = "przeglad.py"


askHistory: list = []
argvCurrent: list = []
stockStatus: dict = {}
inData = ""
accountBalance, operation, openProgram, i = 0, 0, 1, 0

while inData != "stop":
    takeData = input("--Wprowadź--operację--> ")
    argvCurrent = takeData.split()
    inData = str(argvCurrent[0])

    if openProgram == 1:
        with open(pathHis, "r", encoding="utf8") as fileHis:  # <<< askHistory
            fileLine = pickle.dumps(fileHis.readlines())
            for line in fileLine:
                askHistory.append(pickle.loads(line.split("\n")))
            if askHistory:
                accountBalance = int(askHistory[-1])
            else:
                accountBalance = 0
            askHistory.pop()

        with open(pathSts, "r", encoding="utf8") as fileSts:  # <<< stockStatus
            fileLine = fileSts.readlines()
            for line in fileLine:
                pair = line.split(":")
                val = pair[1].rstrip()
                key = pair[0]
                stockStatus[key] = int(val)
        openProgram = 0

    if inData == "saldo":
        if len(argvCurrent) != 3:
            print("Nieprawidłowa liczba argumentów!\n")
            continue
        account = int(argvCurrent[1])
        accountBalance += account
        with open(pathOut, "w+", encoding="utf8") as fileOut:
            fileOut.write("{}\n".format(accountBalance))  # >>> out.txt

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
                    stockStatus[idName] += quantity  # >>> MAGAZYN+
                else:
                    stockStatus[idName] = quantity
        elif inData == "sprzedaż":
            if idName not in stockStatus:
                print("* {}: brak produktu!".format(idName))
                continue
            elif int(stockStatus.get(idName)) < quantity:
                print("* {}: za mały asortyment!".format(idName))
                continue
            else:
                accountBalance += (price * quantity)
                stockStatus[idName] -= quantity  # >>> MAGAZYN-
                if stockStatus[idName] == 0:
                    del [stockStatus[idName]]
                    print("* {}: produkt wyprzedany!".format(idName))
        with open(pathOut, "w+", encoding="utf8") as fileOut:
            for i in range(len(argvCurrent)):  # >>> out.txt
                fileOut.write("{}\n".format(argvCurrent[i]))

    if inData == "saldo" or inData == "zakup" or inData == "sprzedaż":
        askHistory.append(argvCurrent)  # >>> HISTORIA
        with open(pathIn, "r+", encoding="utf8") as fileIn:
            newFile = fileIn.readlines()
            fileIn.seek(0)
            for line in newFile:
                if line != "stop\n":
                    fileIn.write(line)
            fileIn.truncate()
            for line in argvCurrent:  # >>> in.txt
                fileIn.write("{}\n".format(line))
            fileIn.write("stop\n")
        operation += 1

    if inData == "konto":
        if len(argvCurrent) != 1:
            print("Nieprawidłowa liczba argumentów!\n")
            continue
        with open(pathOut, "w+", encoding="utf8") as fileOut:
            fileOut.write("{}\n".format(accountBalance))  # >>> out.txt
        print("======== STAN KONTA {0: 9d} gr =======".format(accountBalance))

    elif inData == "magazyn":
        with open(pathOut, "w+", encoding="utf8") as fileOut:
            for line in argvCurrent[1:]:
                if line in stockStatus:
                    print("* {}: {}".format(line, stockStatus[line]))
                    fileOut.write(
                        "{}: {}\n".format(line, stockStatus[line]))  # >>> out.txt
                else:
                    print("* {0:12s}: brak asortymentu!".format(argvCurrent[i]))

    elif inData == "przegląd":
        if len(argvCurrent) != 3:
            print("Nieprawidłowa liczba argumentów!\n")
            continue
        with open(pathOut, "r+", encoding="utf8") as fileOut:
            for i in range(int(argvCurrent[1]), int(argvCurrent[2]) + 1):  # out
                print("Archiwum(ID.{}) {}".format(i, askHistory[i]))
                fileOut.write("{}\n".format(askHistory[i]))

else:
    if operation > 0:
        position = len(askHistory) - operation
        for i in range(position, len(askHistory)):
            name = "| "
            for j in range(len(askHistory[i])):
                name += str(askHistory[i][j]) + " | "
            print("Dzisiaj(ID.{}) {}".format(i, name))
        operation = 0
        print("Zakończono operacje na koncie.\n")
    else:
        print("Koniec. Brak operacji.\n")

    with open(pathHis, "w+", encoding="utf8") as fileHis:  # >>> askHistory.txt
        askHistory.append(accountBalance)
        for line in askHistory:
            fileHis.write("{}\n".format(line))

    with open(pathSts, "w+", encoding="utf8") as fileSts:  # >>> stockStatus.txt
        for k, v in stockStatus.items():
            fileSts.write("{}:{}\n".format(k, v))

exit()

