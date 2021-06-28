# CSV v1.0
# -*- coding: UTF-8 -*-
# Skrypt z odczytu, zmiany danych i zapisu w plikach CSV | JSON | PICKLE |
import time
import msvcrt
from sys import argv as argv
from sys import stdin, stdout, stderr
from csv_lib.csv_functions import change_csv_from_argv, clean_file_csv, \
    read_file_csv, read_file_csv_json, read_file_csv_pickle, \
    save_file_csv, save_file_csv_json, save_file_csv_pickle, \
    print_changes_argv, print_alldata_csv
from csv_lib.csv_additives import clear_screen, title_line, effective_print
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
path_csv_src = 'trees1.csv'
path_csv_dst = 'trees2.csv'
place = ''
get_data = ''
working_list: list = []
argv_list: list = []
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

if len(argv) > 1:
    place = 'SYS.ARGV'
    path_csv_src = argv[1]
    clean_file_csv(path_csv_src)
    path_csv_dst = argv[2]
else:
    place = 'TERMINAL'
clear_screen()
effective_print('Wprowadzenie do plików CSV, z obsługą kodowania JSON i PICKLE')
while True:
    clear_screen()
    title_line(f' Dane wejściowe z: {place} ')

    if place == 'SYS.ARGV':
        print_alldata_csv(path_csv_src)
        working_list = read_file_csv(working_list, path_csv_src)
        stdout.write('<<< Zawartość źródłowego pliku: >>>')
        print_alldata_csv(path_csv_src)
        if working_list and len(argv) >= 3:
            for i in range(3, len(argv)):
                print_changes_argv(argv[i])
                working_list = change_csv_from_argv(working_list, argv[i])
        else:
            stderr.write('Brak danych do zmiany.')
            break

    elif place == 'TERMINAL':
        stdout.write('Podaj nazwę pliku źródłowego: ')
        path_csv_src = stdin.readline()[:-1]
        stdout.write('Podaj nazwę pliku docelowego: ')
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
            stderr.write('Brak danych do zmiany.')
            break

while True:
    clear_screen()
    title_line(' Wybierz formę zapisu danych CSV: ')
    stdout.write(f'\t(1) CSV?\t(2) JSON?\t(3) PICKLE?\n')
    which_choice = int(msvcrt.getch())
    if which_choice == 1:
        if save_file_csv(working_list, path_csv_dst):
            stderr.write('Poprawnie zapisano zmiany w pliku. (CSV)')
        else:
            stderr.write('Błąd zapisu do pliku! (CSV)')
        break
    elif which_choice == 2:
        if save_file_csv_json(working_list, path_csv_dst):
            stderr.write('Poprawnie zapisano zmiany w pliku. (JSON)')
        else:
            stderr.write('Błąd zapisu do pliku! (JSON)')
        break
    elif which_choice == 3:
        if save_file_csv_pickle(working_list, path_csv_dst):
            stderr.write('Poprawnie zapisano zmiany w pliku. (PICKLE)')
        else:
            stderr.write('Błąd zapisu do pliku! (PICKLE)')
        break
    else:
        stdout.write('Coś źle wybrałeś, jeszcze raz...')
        continue

stdout.write('<<< Zawartość pliku po zmianach: >>>')
print_alldata_csv(path_csv_dst)

stdout.write('..........Bajo!!!..........')
time.sleep(5)