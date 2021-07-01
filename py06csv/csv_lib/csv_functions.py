'''Biblioteka z funkcjami zapisu i odczytu w plikach CSV | JSON | PICKLE |'''
import os
import csv
import json
import pickle
from csv_lib.csv_additives import TPL_FORMAT_csv, TPL_FORMAT_argv


# ---READ---READ---READ---READ---READ---READ---READ---READ---


def read_csv_to_csv(working_list, file_name):
    '''funkcja zapisująca dane z listy do pliku CSV'''
    if os.path.exists(file_name):
        with open(file_name, 'r', newline='', encoding='utf-8') as file:
            read_csv = csv.reader(file, delimiter=',')
            # working_list.encode("utf-8")
            working_list.append(read_csv)
        return working_list
    else:
        print('Error: Błąd pliku!')
        return False


def read_csv_to_list(working_list, file_name):
    '''funkcja pobierająca dane ze źródłowego pliku *.csv'''
    if os.path.exists(file_name):
        with open(file_name, 'r', newline='', encoding='utf-8') as file:
            read_csv = csv.reader(file, delimiter=',')
            # working_list.encode("utf-8")
            for line in read_csv:
                working_list.append(line)
        return working_list
    else:
        print('Error: Błąd pliku!')
        return False


def read_json_to_list(working_list, file_name):
    '''funkcja pobierająca dane ze źródłowego pliku csv 'JSON' '''
    if os.path.exists(file_name):
        with open(file_name, 'r', newline='', encoding='utf-8') as file:
            read_json = json.load(file)
            for line in read_json:
                working_list.append(line)
        return working_list
    else:
        print('Error: Błąd pliku!')
        return False


def read_pickle_to_list(working_list, file_name):
    '''funkcja pobierająca dane ze źródłowego pliku csv 'JSON' '''
    if os.path.exists(file_name):
        with open(file_name, 'rb', newline='', encoding='utf-8') as file:
            read_pickle = pickle.load(file)
            for line in read_pickle:
                working_list.append(line)
        return working_list
    else:
        print('Error: Błąd pliku!')
        return False


def read_dict_from_csv(working_dict, file_name):
    if os.path.exists(file_name):
        with open(file_name, 'r', newline='') as file:
            reader_csv = csv.DictReader(file, fieldnames='')
            for row in reader_csv:
                for key, val in row.items():
                    working_dict[key] = val
        return working_dict
    else:
        print('Error: Błąd pliku!')
        return False


# ---SAVE---SAVE---SAVE---SAVE---SAVE---SAVE---SAVE---SAVE---


def save_csv_to_csv(working_list, file_name):
    '''funkcja zapisująca dane CSV do pliku CSV'''
    with open(file_name, 'w', newline='\n', encoding='utf-8') as file:
        file.write(str(working_list))
        return True


def save_list_to_csv(working_list, file_name):
    '''funkcja zapisująca dane z listy do pliku CSV'''
    with open(file_name, 'w', newline='\n', encoding='utf-8') as file:
        writer_csv = csv.writer(file)
        for line in working_list:
            writer_csv.writerow(line)
    return True


def save_list_to_json(working_list, file_name):
    '''funkcja zapisująca dane z listy do pliku CSV 'JSON' '''
    with open(file_name, 'w', newline='\n', encoding='utf-8') as file:
        json.dump(working_list, file)
    return True


def save_list_to_pickle(working_list, file_name):
    '''funkcja zapisująca dane z listy do pliku CSV 'PICKLE' '''
    with open(file_name, 'wb') as file:
        pickle.dump(working_list, file)
    return True


def save_list_to_csv_as_dict(working_list, file_name):
    with open(file_name, 'w', newline='\n', encoding='utf-8') as file:
        fieldnames = working_list[0]
        writer_csv = csv.DictWriter(file, fieldnames=fieldnames)
        writer_csv.writeheader()
        for x in range(len(working_list[0])):
            for i in range(1, len(working_list)):
                writer_csv.writerow({fieldnames[x]: working_list[i][x]})
        return True


# ---PRINT---PRINT---PRINT---PRINT---PRINT---PRINT---PRINT---PRINT---


def print_argv_changes(change_data):
    '''funkcja wyświetlająca treść zmian pobranych z SYS.ARGV[]'''
    change_list = change_data.split(',')
    print(TPL_FORMAT_argv.format(
        int(change_list[0]), int(change_list[1]), str(change_list[2])))


def print_alldata_from_csvfile(file_name):
    '''funkcja wyświetlająca wszystkie dane z pliku CSV'''
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as file:
            read_csv = csv.reader(file, delimiter=',')
            num_line = 0
            for line in read_csv:
                print(TPL_FORMAT_csv.format(str(num_line).rjust(3), line[0],
                    line[1].rjust(7), line[2].rjust(7), line[3].rjust(7)))
                num_line += 1
            print('\t<<<  Ogółem wierszy: {}.  >>>'.format(num_line))
            return True
    else:
        print('Error: Błąd pliku!')
    return False

def print_alldata_from_jsonfile(file_name):
    '''funkcja wyświetlająca wszystkie dane z pliku CSV/JSON'''
    if os.path.exists(file_name):
        num_line = 0
        with open(file_name, 'r', encoding='utf-8') as file:
            read_json = json.load(file)
            for line in read_json:
                print(TPL_FORMAT_csv.format(str(num_line).rjust(3),
                    str(line[0]), str(line[1]).rjust(7),
                    str(line[2]).rjust(7), str(line[3]).rjust(7)))
                num_line += 1
            print('\t<<<  Ogółem wierszy: {}.  >>>'.format(num_line))
            return True
    else:
        print('Error: Błąd pliku!')
        return False

def print_alldata_from_picklefile(file_name):
    '''funkcja wyświetlająca wszystkie dane z pliku CSV/PICKLE'''
    if os.path.exists(file_name):
        num_line = 0
        with open(file_name, 'rb') as file:
            read_pickle = pickle.load(file)
            for line in read_pickle:
                print(TPL_FORMAT_csv.format(str(num_line).rjust(3),
                    str(line[0]), str(line[1]).rjust(7),
                    str(line[2]).rjust(7), str(line[3]).rjust(7)))
                num_line += 1
            print('\t<<<  Ogółem wierszy: {}.  >>>'.format(num_line))
            return True
    else:
        print('Error: Błąd pliku!')
        return False

# ---DIFFERENT---DIFFERENT---DIFFERENT---DIFFERENT---DIFFERENT---


def get_line(file_name):
    '''funkcja pobierająca jedną linię pliku'''
    return '{}'.format(file_name.readline().strip())


def clean_csv_file(file_name):
    '''funkcja oczyszczająca dane w pliku *.csv z białych znaków'''
    clean_list: list = []
    if os.path.exists(file_name):
        with open(file_name, 'r', newline='') as file:
            read_csv = csv.reader(file)
            for line in read_csv:
                for i in range(len(line)):
                    line[i] = line[i].strip(' ')
                clean_list.append(list(line))
        save_list_to_csv(clean_list, file_name)
        return True
    else:
        print('Error: Błąd pliku!')
        return False


def change_data_from_argv(working_list, change_data):
    '''funkcja zmieniająca dane pobrane z argv[] w pliku *.csv'''
    change_list = change_data.split(",")
    if len(change_list) == 3:
        if int(change_list[1])-1 == 1 or int(change_list[1])-1 == 3:
            working_list[int(change_list[0])][int(change_list[1])-1] \
                = round(float(change_list[2]), 1)
        else:
            working_list[int(change_list[0])][int(change_list[1])-1] \
                = int(round(float(change_list[2])))
        return working_list
    else:
        print('Nieprawidłowe odwołania!')
        return False
