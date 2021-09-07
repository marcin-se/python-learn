# Biblioteka z funkcjami dodatkowymi
# # -*- coding: utf-8 -*-#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
from math import floor
import winsound
import time
import os


# CLEAR SCREEN
def clear_screen():
    if os.name == 'posix':  # dla mac i linux
        _ = os.system('clear')
    else:
        _ = os.system('cls')  # dla windows
    return


# LINE OF SIGNS
# ------------------------------------------------------------- #
def dividing_line(stamp="+", repeat=63):
    print("+" + stamp * (repeat+1) + "+")


# ------------------------------------------------------------- #
# ---------------------- TITLE BANNER ------------------------- #
# ------------------------------------------------------------- #
def title_line(text="none"):
    repeat = 63
    textline = str(text.upper())
    dividing_line("-", repeat)
    lenght = floor((repeat - 1 - len(text)) / 2)
    if not len(text) % 2:
        print("|{} {} {}|".format("-"*lenght, textline, "-"*lenght))
    else:
        print("|{} {} {}|".format("-" * lenght, textline, "-" * (lenght+1)))
    dividing_line("-", repeat)
    return True


# FORMAT - PRINT CSV FILES
# ------------------------------------------------------------- #
TPL_FORMAT_argv = 'Wiersz: {:1d},  Kolumna: {:1d},  Wartość: {:3s}\n'
TPL_FORMAT_csv = '{:3s} | {:10s} | {:7s} | {:7s} | {:9s} |'


# EFFECTIVE PRINT
def effective_print(text):
    for i in range(len(text)):
        x = str(text[i])
        time.sleep(0.07)
        yield str(x)


# BEEP SOUND :: # Frequency: 2500 Hz :: # Duration:  1000 ms
def effective_sound(frequency=800, duration=50):
    for i in range(1, 11):
        time.sleep(0.05)
        winsound.Beep(i*100+frequency, duration)
    return

