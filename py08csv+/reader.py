# CSV+ v1.0                                      (R) Powered by nobody & nothing
# -*- coding: UTF-8 -*-                                                        #
# Skrypt z odczytu CSV, zmiany danych i zapisu w pliku JSON lub PICKLE         #
'''
- sprawdź, czy podany plik <src> (lub ścieżka) istnieje
- jeżeli nie istnieje, wypisz komunikat i wyświetl zawartość katalogu
- jeżeli istnieje, to odczytaj plik, zmień dane i wyświetl je, a
- następnie zapisz te dane w pliku docelowym <dst>
- w takim formacie, jak rozszerzenie pliku (np. *.pickle)
'''
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
'''EXAMPLE1>>>  reader.py <<src>> <<dst>> <<change1>>                        '''
'''EXAMPLE1>>>  reader.py file.csv file.json 16,4,201                        '''
'''EXAMPLE1>>>  reader.py file.csv file.pickle 16,4,201                      '''
'''EXAMPLE2>>>  reader.py <<src>> <<dst>> <<change1>> <<change2>> <<...>>    '''
'''EXAMPLE2>>>  reader.py file.csv file.json 16,4,201 4,2,19.2 22,1,obraz    '''
'''EXAMPLE2>>>  reader.py file.csv file.pickle 16,4,201 4,2,19.2             '''
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
from csv_lib.csv_ext import *
from csv_lib.csv_cls import ModifyFile
from sys import stdout, stderr
import msvcrt
import time
import sys

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#

path_src, path_dst = "", ""
changes_list: list = []

clear_screen()
while True:
    abc = ModifyFile()
    if len(sys.argv) <= 3:
        stderr.write('\nNo data to change!\n')
        break
    if len(sys.argv) > 3:
        path_src = str(sys.argv[1])
        path_dst = str(sys.argv[2])
        changes_list = sys.argv[3:]
        if abc.open_file(path_src):
            stdout.write('\n<<< List of changes to the file content: >>>\n')
            for one_change in changes_list:
                abc.print_argvchanges(one_change)
                abc.change_csvdata(one_change)
                time.sleep(0.5)
            abc.save_file(path_dst)
        else:
            stdout.write('Problem with the source file!')
            stderr.write('\nFiles from the current directory\n')
            break
        stdout.write('\n<<< File contents after changes: >>>\n')
        abc.print_data()
        time.sleep(1)
        break
stdout.write('\n<<< Press any key... >>>\n\n')
if msvcrt.getch():
    clear_screen()
