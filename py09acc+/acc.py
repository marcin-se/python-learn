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
from acc_lib.acc_class import *
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
actions = sys.argv[2:]


reader = Reader(db_path)
manager = Manager(reader)

@manager.action("saldo", 2)
def saldo(manager, rows):
    price = float(rows[0])
    manager.modify_account(price)

@manager.action("zakup", 3)
def zakup(manager, rows):
    name_item = rows[0]
    price = float(rows[1])
    qty = float(rows[2])
    manager.modify_account(-price*qty)
    manager.modify_stock(name_item, qty)

@manager.action('sprzedaż', 3)
def sprzedaz(manager, rows):
    name_item = rows[0]
    price_item = float(rows[1])
    qty = float(rows[2])
    manager.modify_stock(name_item, -qty)
    manager.modify_account(price_item * qty)

@manager.action("przegląd", 2)
def przeglad(manager, rows):
    manager.view_history(rows[0], rows[1])

@manager.action("magazyn", 3)
def magazyn(manager, rows):
    manager.view_stock(rows)
