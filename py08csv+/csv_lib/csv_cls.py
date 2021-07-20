# Biblioteka z funkcjami zapisu i odczytu w plikach CSV | JSON | PICKLE |
from csv_lib.csv_ext import TPL_FORMAT_csv, TPL_FORMAT_argv
import pickle
import json
import csv
import sys
import os


class ModifyFile:
    def __init__(self):
        self.jiff_list = []

    def clean_csvfile(self, file_name):
        '''funkcja oczyszczająca dane w pliku *.csv z białych znaków'''
        clean_list: list = []
        if os.path.exists(file_name):
            with open(file_name, 'r', newline='') as file:
                read_csv = csv.reader(file)
                for line in read_csv:
                    for i in range(len(line)):
                        line[i] = line[i].strip(' ')
                    clean_list.append(list(line))
            self.save_csvfile(file_name)
            return True
        return False, sys.stderr.write('Błąd rozszerzenia!')

    def read_csvfile(self, file_name):
        '''metoda pobierająca dane ze źródłowego pliku *.csv'''
        if os.path.exists(file_name):
            if os.path.splitext(file_name)[1] == ".csv":
                with open(file_name, 'r', newline='', encoding='utf-8') as file:
                    reader_csv = csv.reader(file)
                    for line in reader_csv:
                        self.jiff_list.append(line)
                return self.jiff_list
            return False, sys.stderr.write('Błąd rozszerzenia!')
        return False, sys.stderr.write('Błąd pliku!')

    def save_csvfile(self, file_name):
        '''metoda zapisująca dane do docelowego pliku *.csv'''
        if os.path.exists(file_name):
            if os.path.splitext(file_name)[1] == ".csv":
                with open(file_name, 'w', newline='\n', encoding='utf-8') as file:
                    writer_csv = csv.writer(file)
                    for line in self.jiff_list:
                        writer_csv.writerow(line)
                return True
            return False, sys.stderr.write('Błąd rozszerzenia!')
        return False, sys.stderr.write('Błąd pliku!')

    def read_jsonfile(self, file_name):
        '''funkcja pobierająca dane ze źródłowego pliku *.json '''
        if os.path.exists(file_name):
            if os.path.splitext(file_name)[1] == ".json":
                with open(file_name, 'r', newline='', encoding='utf-8') as file:
                    reader_json = json.load(file)
                    for line in reader_json:
                        self.jiff_list.append(line)
                return self.jiff_list
            return False, sys.stderr.write('Błąd rozszerzenia!')
        return False, sys.stderr.write('Błąd pliku!')

    def save_jsonfile(self, file_name):
        '''funkcja zapisująca dane z listy do pliku *.json '''
        if os.path.exists(file_name):
            if os.path.splitext(file_name)[1] == ".json":
                with open(file_name, 'w', newline='\n', encoding='utf-8') as file:
                    json.dump(self.jiff_list, file)
                return True
            return False, sys.stderr.write('Błąd rozszerzenia!')
        return False, sys.stderr.write('Błąd pliku!')

    def read_picklefile(self, file_name):
        '''funkcja pobierająca dane ze źródłowego pliku *.pickle '''
        if os.path.exists(file_name):
            if os.path.splitext(file_name)[1] == ".pickle":
                with open(file_name, 'rb', newline='', encoding='utf-8') as file:
                    reader_pickle = pickle.load(file)
                    for line in reader_pickle:
                        self.jiff_list.append(line)
                return self.jiff_list
            return False, sys.stderr.write('Błąd rozszerzenia!')
        return False, sys.stderr.write('Błąd pliku!')

    def save_picklefile(self, file_name):
        '''funkcja zapisująca dane z listy do pliku CSV 'PICKLE' '''
        if os.path.exists(file_name):
            if os.path.splitext(file_name)[1] == ".pickle":
                with open(file_name, 'wb') as file:
                    pickle.dump(self.jiff_list, file)
                return True
            return False, sys.stderr.write('Błąd rozszerzenia!')
        return False, sys.stderr.write('Błąd pliku!')
    ''' Odczyt i zapis - obsługa plików CSV, JSON, PICKLE '''

    def print_csvdata(self, file_name):
        '''metoda wyświetlająca wszystkie dane z pliku *.csv'''
        if os.path.exists(file_name):
            with open(file_name) as file:
                reader_csv = csv.reader(file)
                for line in reader_csv:
                    if line == 0:
                        print("{:20}".format("\t ".join(line)))
                    else:
                        print(TPL_FORMAT_csv.format(line[0], line[1],
                            line[2], line[3], line[4], line[4]))
                print(TPL_FORMAT_csv.format(
                    int(change_list[0])-1, int(change_list[1])-1, str(change_list[2])))

    def print_file(self, file_name):
        '''metoda wyświetlająca zawartość dowolnego pliku '''
        if os.path.exists(file_name):
            with open(file_name) as file:
                reader = file.read()
                for line in reader:
                    if not line:
                        break
                    else:
                        print(line)
        return False, sys.stderr.write('Błąd pliku!')

    @staticmethod
    def print_argvchanges(change_data):
        '''metoda wyświetlająca zmiany pobrane z argv[] w pliku *.csv'''
        change_list: list = []
        for change in change_data:
            change_list = change.split(",")
        print(TPL_FORMAT_argv.format(int(change_list[0])-1,
                                     int(change_list[1])-1,
                                     str(change_list[2])))

    def change_argvchanges(self, change_data):
        '''metoda zmieniająca dane pobrane z argv[] w pliku *.csv'''
        for change in change_data:
            change_list = change.split(",")
            if change_list[0] and change_list[1]:
                self.jiff_list[int(change_list[0]) - 1]\
                              [int(change_list[1]) - 1]\
                              = int(change_list[2])
                return self.jiff_list
            return False, sys.stderr.write('Błąd argumentów!')
