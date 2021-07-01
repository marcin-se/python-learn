# CSV v1.1
# -*- coding: UTF-8 -*-
import os
import sys
import csv
import time
import msvcrt
from sys import argv as argv
from sys import stdin, stdout, stderr
from csv_lib.csv_additives import clear_screen, title_line, effective_print
from csv_lib.csv_functions import read_csv_to_csv, save_csv_to_csv, \
    read_csv_to_list, read_json_to_list, read_pickle_to_list, \
    save_list_to_csv, save_list_to_json, save_list_to_pickle, \
    print_argv_changes, print_alldata_from_csvfile, \
    print_alldata_from_jsonfile, print_alldata_from_picklefile, \
    get_line, clean_csv_file, change_data_from_argv
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
path_csv_src = './trees1.csv'
path_csv_dst = './trees2.csv'
place = ''
get_data = ''
working_list: list = []
argv_list: list = []
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

while True:
    if len(sys.argv) >= 1:
        place = 'SYS.ARGV'
        path_csv_src = str(sys.argv[1])
        path_csv_dst = str(sys.argv[2])
    else:
        place = 'TERMINAL'
# python test.py trees1.csv trees2.csv 22,2,8

    print('------read_csv_to_list')
    input()
    print(read_csv_to_list(working_list, path_csv_src))

    print('------clean_csv_file')
    input()
    clean_csv_file(path_csv_src)

    print('------print_alldata_from_csvfile')
    input()
    print_alldata_from_csvfile(path_csv_src)

    print('------print_argv_changes')
    input()
    print_argv_changes(sys.argv[3])

    print('------change_data_from_argv')
    input()
    change_data_from_argv(working_list, sys.argv[3])

    print('------save_list_to_csv')
    input()
    save_list_to_csv(working_list, path_csv_dst)

    print('------print_alldata_from_csvfile')
    input()
    print_alldata_from_csvfile(path_csv_dst)

    # clean_csv_file(path_csv_src)

    '''if place == 'SYS.ARGV':
        working_list = read_file_csv(working_list, path_csv_src)
        if os.path.exists(path_csv_src):
            stdout.write('<<< Zawartość źródłowego pliku: >>>\n')
            print_alldata_csv(path_csv_src)
        if working_list and len(sys.argv) >= 3:
            for i in range(3, len(sys.argv)):
                print_changes_argv(sys.argv[i])
                working_list = change_csv_from_argv(working_list, sys.argv[i])
        else:
            stderr.write('Brak danych do zmiany.')
            break

    elif place == 'TERMINAL':
        print('Podaj nazwę pliku źródłowego: ')
        path_csv_src = stdin.readline()[:-1]
        print('Podaj nazwę pliku docelowego: ')
        path_csv_dst = stdin.readline()[:-1]
        working_list = read_file_csv(working_list, path_csv_src)
        if working_list:
            while True:
                stdout.write('Podaj dane "Y,X,wartość" lub "stop": ')
                get_data = stdin.readline()[:-1]
                if get_data == 'stop' or get_data == '':
                    break
                else:
                    print_changes_argv(get_data)
                    working_list = change_csv_from_argv(working_list, get_data)
                    continue
        else:
            stderr.write('Brak danych do zmiany.\n')
            break
print(working_list)
while True:
    title_line(' Wybierz formę zapisu danych CSV: ')
    stdout.write(f'\t(1) CSV?\t(2) JSON?\t(3) PICKLE?\n')
    which_choice = int(msvcrt.getch())
    if which_choice == 1:
        if save_file_csv(working_list, path_csv_dst):
            stderr.write('Poprawnie zapisano zmiany w pliku. (CSV)\n')
        else:
            stderr.write('Błąd zapisu do pliku! (CSV)\n')
        break
    elif which_choice == 2:
        if save_file_csv_json(working_list, path_csv_dst):
            stderr.write('Poprawnie zapisano zmiany w pliku. (JSON)\n')
        else:
            stderr.write('Błąd zapisu do pliku! (JSON)\n')
        break
    elif which_choice == 3:
        if save_file_csv_pickle(working_list, path_csv_dst):
            stderr.write('Poprawnie zapisano zmiany w pliku. (PICKLE)\n')
        else:
            stderr.write('Błąd zapisu do pliku! (PICKLE)\n')
        break
    else:
        stdout.write('Coś źle wybrałeś, jeszcze raz...\n')
        continue

stdout.write('<<< Zawartość pliku po zmianach: >>>\n')
print_alldata_csv(path_csv_dst)

stdout.write('..........Bajo!!!..........\n')
time.sleep(5)'''
    break
