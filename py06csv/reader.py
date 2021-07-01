# CSV v1.1
# -*- coding: UTF-8 -*-
# Skrypt z odczytu, zmiany danych i zapisu w plikach CSV | JSON | PICKLE |
import os
import sys
import time
import msvcrt
from sys import argv as argv
from sys import stdin, stdout, stderr
from csv_lib.csv_additives import clear_screen, title_line
from csv_lib.csv_functions import \
    read_csv_to_list, read_json_to_list, read_pickle_to_list, \
    save_list_to_csv, save_list_to_json, save_list_to_pickle, \
    print_argv_changes, print_alldata_from_csvfile, \
    print_alldata_from_jsonfile, print_alldata_from_picklefile, \
    clean_csv_file, change_data_from_argv

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
path_csv_src = 'trees1.csv'
path_csv_dst = 'trees2.csv'
place = ''
get_data = ''
working_list: list = []
argv_list: list = []
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
clear_screen()
while True:
    while 1:
        if len(sys.argv) >= 1:
            place = 'SYS.ARGV'
            path_csv_src = str(sys.argv[1])
            clean_csv_file(path_csv_src)
            path_csv_dst = str(sys.argv[2])
        else:
            place = 'TERMINAL'
        title_line(' Pochodzenie zmiany danych:  {} '.format(place))
        time.sleep(2)

        if place == 'SYS.ARGV':
            working_list = read_csv_to_list(working_list, path_csv_src)
            stdout.write('\n\t<<< Zawartość pliku przed zmianami: >>>\n')
            print_alldata_from_csvfile(path_csv_src)
            time.sleep(1)
            if working_list and len(sys.argv) >= 3:
                stdout.write('\nWykaz zmian w zawartości pliku:\n')
                for i in range(3, len(sys.argv)):
                    print_argv_changes(sys.argv[i])
                    working_list = change_data_from_argv(
                        working_list, sys.argv[i])
                time.sleep(2)
                break
            else:
                stderr.write('\nBrak danych do zmiany.\n')
                break


        elif place == 'TERMINAL':
            print('\nPodaj nazwę pliku źródłowego: ')
            path_csv_src = stdin.readline()[:-1]
            print('\nPodaj nazwę pliku docelowego: ')
            path_csv_dst = stdin.readline()[:-1]
            working_list = read_csv_to_list(working_list, path_csv_src)
            if working_list:
                while True:
                    stdout.write('\nPodaj dane "Y,X,wartość" lub "stop": ')
                    get_data = stdin.readline()[:-1]
                    if get_data == 'stop' or get_data == '':
                        break
                    else:
                        print_argv_changes(get_data)
                        working_list = change_data_from_argv(
                            working_list, get_data)
                        continue
                time.sleep(1)
            else:
                stderr.write('Brak danych do zmiany.\n')
                break

    if working_list:
        while 1:
            title_line(' Wybierz formę zapisu danych CSV: ')
            stdout.write(f'\t(1) CSV?\t(2) JSON?\t(3) PICKLE?\n')
            which_choice = int(msvcrt.getch())
            if which_choice == 1:
                if save_list_to_csv(working_list, path_csv_dst):
                    stderr.write('\nPoprawnie zapisano plik (CSV).\n')
                    stdout.write('\t<<< Zawartość pliku po zmianach: >>>\n')
                    print_alldata_from_csvfile(path_csv_dst)
                else:
                    stderr.write('Błąd zapisu do pliku! (CSV)\n')
                break
            elif which_choice == 2:
                if save_list_to_json(working_list, path_csv_dst):
                    stderr.write('\nPoprawnie zapisano plik (JSON).\n')
                    stdout.write('\t<<< Zawartość pliku po zmianach: >>>\n')
                    print_alldata_from_jsonfile(path_csv_dst)
                else:
                    stderr.write('Błąd zapisu do pliku! (JSON)\n')
                break
            elif which_choice == 3:
                if save_list_to_pickle(working_list, path_csv_dst):
                    stderr.write('\nPoprawnie zapisano plik (PICKLE).\n')
                    stdout.write('\t<<< Zawartość pliku po zmianach: >>>\n')
                    print_alldata_from_picklefile(path_csv_dst)
                else:
                    stderr.write('\nBłąd zapisu do pliku! (PICKLE)\n')
                break
            else:
                stdout.write('\n\tCoś źle klikasz, jeszcze raz...\n')
                time.sleep(2)
                clear_screen()
                continue
    time.sleep(2)
    stdout.write('\nPress any key...\n')
    if msvcrt.getch():
        clear_screen()
        break
