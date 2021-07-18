### Biblioteka z funkcjami dodatkowymi ###
import os
import sys
import time
from sys import stdout


# CLEAR SCREEN
def clear_screen():
    if os.name == 'posix':  # dla mac i linux
        _ = os.system('clear')
    else:
        _ = os.system('cls')  # dla windows
    return


# LINE OF SIGNS
# ------------------------------------------------------------- #
def dividing_line(stamp="-", repeat=55):
    print("+" + stamp * (repeat+1) + "+")


# ------------------------------------------------------------- #
# ---------------------- TITLE BANNER ------------------------- #
# ------------------------------------------------------------- #
def title_line(text="none"):
    repeat = 55
    textline = str(text.upper())
    dividing_line("-", repeat)
    lenght = round((repeat - 2 - len(text)+1)/2)
    print("|{} {} {}|".format("-"*lenght, textline, "-"*lenght))
    dividing_line("-", repeat)
    return True


# FORMAT - PRINT CSV FILES
# ------------------------------------------------------------- #
TPL_FORMAT_argv = 'Wiersz: {:2d}, Kolumna: {:2d}, Wartość: {:5s}'
TPL_FORMAT_csv = '{:3s} | {:10s} | {:7s} | {:7s} | {:9s} |'




# EFFECTIVE PRINT
def effective_print(text):
    for i in range(len(text)):
        x = str(text[i])
        time.sleep(0.07)
        yield str(x)

