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
from csv_lib.csv_cls import *
from datetime import datetime, timedelta
from sys import stdin, stdout, stderr
import msvcrt
import time
import sys

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#

path_src = 'trees1.csv'
path_dst = 'trees2.csv'
place = ''
get_data = ''
data_list: list = []
argv_list: list = []


clear_screen()
while True:
    abc = ModifyFile()
    while 1:
        if len(sys.argv) >= 1:
            place = 'SYS.ARGV'
            path_src = str(sys.argv[1])
            path_dst = str(sys.argv[2])
            if os.path.splitext(path_src)[1] == ".csv":
                abc.clean_csvfile(path_src)
        else:
            place = 'TERMINAL'
        title_line(' Pochodzenie zmiany danych:  {} '.format(place))
        time.sleep(1)

        if place == 'SYS.ARGV':
            abc.jiff_list = abc.read_csvfile(path_src)
            if abc.jiff_list and len(sys.argv) >= 3:
                stdout.write('\nWykaz zmian w zawartości pliku:\n')
                for i in range(3, len(sys.argv)):
                    abc.print_argvchanges(sys.argv[i])
                    data_list = abc.change_argvchanges(sys.argv[i])
                time.sleep(1)
            else:
                stderr.write('\nBrak danych do zmiany.\n')
                break
            stdout.write('\n\t<<< Zawartość pliku przed zmianami: >>>\n')
            abc.print_csvdata(path_src)
            time.sleep(1)

        elif place == 'TERMINAL':
            print('\nPodaj nazwę pliku źródłowego: ')
            path_src = stdin.readline()[:-1]
            print('\nPodaj nazwę pliku docelowego: ')
            path_csv_dst = stdin.readline()[:-1]
            data_list = abc.read_csvfile(path_src)
            if data_list:
                while True:
                    stdout.write('\nPodaj dane "Y,X,wartość" lub "stop": ')
                    get_data = stdin.readline()[:-1]
                    if get_data == 'stop' or get_data == '':
                        break
                    else:
                        abc.print_argvchanges(get_data)
                        jiff_list = abc.change_argvchanges(get_data)
                        continue
                time.sleep(1)
            else:
                stderr.write('Brak danych do zmiany.\n')
                break

    if abc.jiff_list:
        while 1:
            title_line(' Wybierz formę zapisu danych CSV: ')
            stdout.write(f'\t(1) CSV?\t(2) JSON?\t(3) PICKLE?\n')
            which_choice = int(msvcrt.getch())
            if which_choice == 1:
                if abc.save_csvfile(path_dst):
                    stderr.write('\nPoprawnie zapisano plik (CSV).\n')
                    stdout.write('\t<<< Zawartość pliku po zmianach: >>>\n')
                    print_alldata_from_csvfile(path_dst)
                else:
                    stderr.write('Błąd zapisu do pliku! (CSV)\n')
                break
            elif which_choice == 2:
                if abc.save_jsonfile(path_dst):
                    stderr.write('\nPoprawnie zapisano plik (JSON).\n')
                    stdout.write('\t<<< Zawartość pliku po zmianach: >>>\n')
                    print_alldata_from_jsonfile(path_dst)
                else:
                    stderr.write('Błąd zapisu do pliku! (JSON)\n')
                break
            elif which_choice == 3:
                if abc.save_picklefile(path_dst):
                    stderr.write('\nPoprawnie zapisano plik (PICKLE).\n')
                    stdout.write('\t<<< Zawartość pliku po zmianach: >>>\n')
                    print_alldata_from_picklefile(path_dst)
                else:
                    stderr.write('\nBłąd zapisu do pliku! (PICKLE)\n')
                break
            else:
                stdout.write('\n\tCoś źle klikasz, jeszcze raz...\n')
                time.sleep(1)
                clear_screen()
                continue
    time.sleep(1)
    stdout.write('\nPress any key...\n')
    if msvcrt.getch():
        clear_screen()
        break
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#