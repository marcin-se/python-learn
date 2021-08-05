# ACCOUNTANT v2.0_on_classes
# -*- coding: UTF-8 -*-
# Biblioteka z funkcjami dodatkowymi ###
import os
import time
from math import ceil


# * * * * * * * * *  C L E A R  S C R E E N  * * * * * * * * #
def clearscreen():
    if os.name == 'posix':  # dla mac i linux
        _ = os.system('clear')
    else:
        _ = os.system('cls')  # dla windows
    return


# * * * * * * * * *  L I N E   O F   S I G N S  * * * * * * * * #
def line_division(stamp="-", width=60):
    return stamp * width


# * * * * * *  H I G H L I G H T E D  L I N E  * * * * * * * * #
def line_hilight(text='', width=60):
    ''' Pojedyncza linia znaków z tekstem (upper) '''
    mytext = text.upper().strip()
    mywidth = ceil((width - len(mytext) - 2) / 4)
    print(f"{'* ' * mywidth} {mytext} {' *' * int(mywidth)}")


# +''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''+
# |             T I T L E   B A N N E R   L I N E              |
# +............................................................+
def line_banner(text='', width=60):  # width = 30, 40, 50, 60,...
    ''' Potrójny baner myślników z tekstem (upper) w środku '''
    mytext = text.upper().strip()
    mywidth = ceil((width - len(mytext) - 3) / 2)
    width += 1 if (width-len(mytext)-2) % 2 == 0 else width
    print('+{}+'.format(line_division("'", width)))
    print(f"|{' ' * mywidth} {mytext} {' ' * int(mywidth+1)}|")
    print('+{}+'.format(line_division('.', width)))


# - - - - - - -  E F F E C T I V E   P R I N T  - - - - - - - - #
def effective_print(text='', delay=0.1):
    ''' Zwraca ciąg znaków po jednym znaku z opóźnieniem '''
    for i in range(len(text)):
        time.sleep(delay)
        yield f'{text[i]}'


# - - - - - - - -  F O R M A T - P R I N T E R - - - - - - - - - #
TPL_FORMAT_argv = 'Wiersz: {:2d}, Kolumna: {:2d}, Wartość: {:5s}'
TPL_FORMAT_csv = '{:3s} | {:10s} | {:7s} | {:7s} | {:9s} |'

