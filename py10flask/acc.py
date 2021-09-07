# ACCOUNTANT v2.0 on classes
# -*- coding: UTF-8 -*-                                                        #
# "accountant" obiektowo, wyłącznie z obsługą plików we/wy                     #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  #
'''
- rozszerzenie programu księgowego
- program czyta i zapisuje do podanego pliku
- niedozwolone są żadne zmienne globalne
- dane przechowywane wewnątrz obiektu "Manager"
'''
from acc_lib.acc_class import Reader, Manager
import sys
# - - - - - - - E X A M P L E S - - - - - - - - E X A M P L E S - - - - - - - -#
'''EXAMPLE1>>>  saldo.py    export.txt  123000  pożyczka                     '''
'''EXAMPLE2>>>  sprzedaz.py export.txt  raspberry  120 5                     '''
'''EXAMPLE3>>>  zakup.py    export.txt  jetson 99.90  15                     '''
'''EXAMPLE4>>>  konto.py    export.txt                                       '''
'''EXAMPLE5>>>  magazyn.py  export.txt  raspberry  jetson  arduino           '''
'''EXAMPLE6>>>  przeglad.py export.txt  8  9                                 '''
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#

db_path = sys.argv[1]
actions = sys.argv[1:]

reader = Reader(db_path)
director = Manager(reader)


@director.action("saldo", 2)
def saldo(director, rows):
    price = float(rows[0])
    director.modify_account(price)


@director.action("zakup", 3)
def zakup(director, rows):
    name_item = rows[0]
    price = float(rows[1])
    qty = float(rows[2])
    director.modify_account(-price * qty)
    director.modify_stock(name_item, qty)


@director.action('sprzedaż', 3)
def sprzedaz(director, rows):
    name_item = rows[0]
    price_item = float(rows[1])
    qty = float(rows[2])
    director.modify_stock(name_item, -qty)
    director.modify_account(price_item * qty)


@director.action("przegląd", 2)
def przeglad(director, rows):
    director.view_history(rows[0], rows[1])


@director.action("magazyn", 3)
def magazyn(director, rows):
    director.view_stock(rows)
