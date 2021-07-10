### Biblioteka z funkcjami dodatkowymi ###
import os
import time
from math import floor
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
def dividing_line(stamp="-", repeat=61):
    print("+" + stamp * (repeat+1) + "+")



# EFFECTIVE PRINT
def effective_print(text):
    for i in range(len(text)):
        stdout.write(f'{text[i]}')
        time.sleep(0.07)
    print('')



# ------------------------------------------------------------- #
# ---------------------- TITLE BANNER ------------------------- #
# ------------------------------------------------------------- #
def title_line(text="none"):
    repeat = 61
    textline = str(text.upper())
    dividing_line("-", repeat)
    lenght = floor((repeat - 1 - len(text)) / 2)
    if not len(text) % 2:
        print("|{} {} {}|".format("-"*lenght, textline, "-"*lenght))
    else:
        print("|{} {} {}|".format("-" * lenght, textline, "-" * (lenght+1)))
    dividing_line("-", repeat)
    return True



# PRINT FORMAT - CSV, FILES, WEATHER
# ------------------------------------------------------------- #
TPL_FORMAT_argv = 'Wiersz: {:2d}, Kolumna: {:2d}, Wartość: {:5s}'
TPL_FORMAT_csv = '{:3s} | {:10s} | {:7s} | {:7s} | {:9s} |'
TPL_FORMAT_weather = '| {:11s} | {:12s} | {:7s} | {:16s} |'
