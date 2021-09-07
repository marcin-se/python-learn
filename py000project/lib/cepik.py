# Biblioteka z modułem 'requests' do obsługi API
# CEPIK - baza pojazdów
# -*- coding: utf-8 -*-
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
from os.path import getmtime, exists
import requests
import datetime
import json
import csv
import os
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#


class CepikAPIcars:
    '''
        Class gets database from sites:
        https://api.cepik.gov.pl/slowniki/
        https://api.cepik.gov.pl/slowniki/rodzaj-pojazdu
    '''
    def __init__(self):
        self.response_marks = {}
        self.response_types = {}
        self.db_marks = {}
        self.db_types = {}
        self.db_csv = []
        self.counter = 0

    def get_response(self):
        ''' Method sends inquiries to the server '''
        url_marks = 'https://api.cepik.gov.pl/slowniki/marka'
        url_types = 'https://api.cepik.gov.pl/slowniki/rodzaj-pojazdu'
        self.response_marks = requests.request('GET', url_marks).json()
        self.response_types = requests.request('GET', url_types).json()

    def load_db(self, file_marks, file_types):
        ''' Load databases from native sites '''
        if not exists(file_marks) or not exists(file_types):
            self.get_response()
            self.save_db(file_marks, file_types)
            self.reference_db()
            return print('The files have been created correctly.')
        file_time = getmtime(file_marks)
        now_time = datetime.datetime.now().timestamp()
        if now_time - file_time < 60 * 60 * 24:
            with open(file_marks, "r") as file:
                self.response_marks = json.load(file)
            with open(file_types, "r") as file:
                self.response_types = json.load(file)
        else:
            self.get_response()
            self.save_db(file_marks, file_types)
            self.reference_db()
        return print('The data was loaded correctly.')

    def save_db(self, file_marks, file_types):
        ''' Save databases to json files '''
        with open(file_marks, mode='w') as file:
            new_file = json.dumps(self.response_marks)
            file.write(new_file)
        with open(file_types, mode='w') as file:
            new_file = json.dumps(self.response_types)
            file.write(new_file)
        return print('The data was written correctly.')

    def transfer_db(self, file_src, file_dst):
        ''' Load databases from native sites '''
        if os.path.isfile(file_src):
            with open(file_src, "r", encoding='utf-8') as file:
                reader_csv = csv.reader(file)
                for line in reader_csv:
                    if not line:
                        break
                    else:
                        self.db_csv.append(line)
        if os.path.isfile(file_dst):
            with open(file_dst, "w") as file:
                file.write(json.dumps(self.db_csv, indent=4))
        return print('The data was transferred correctly.')

    def reference_db(self):
        for key, val in self.response_marks.items():
            key_marks = self.response_marks['data']['attributes'][
                'dostepne-rekordy-slownika'][key]['klucz-slownika']
            val_marks = self.response_marks['data']['attributes'][
                'dostepne-rekordy-slownika'][val]['liczba-wystapien']
            self.db_marks[key_marks] = val_marks
        for key, val in self.response_types.items():
            key_types = self.response_types['data']['attributes'][
                'dostepne-rekordy-slownika'][key]['klucz-slownika']
            val_types = self.response_types['data']['attributes'][
                'dostepne-rekordy-slownika'][val]['liczba-wystapien']
            self.db_types[key_types] = val_types
        return True

    def get_info(self):
        ''' Get answer from database '''
        db_cpt_marks = self.response_marks['data']['attributes']\
                ['ilosc-rekordow-slownika']
        db_date_marks = self.response_marks['meta']['sy:updateBase']
        db_cpt_types = self.response_types['data']['attributes'][
            'ilosc-rekordow-slownika']
        db_date_types = self.response_types['meta']['sy:updateBase']
        print('\n*** VEHICLE BRANDS ***\n----------------------')
        print(f"Today ({db_date_marks}) the vehicle brand database "
              f"contains '{db_cpt_marks}' items.")
        print('\n*** VEHICLE TYPES ***\n----------------------')
        print(f"Today ({db_date_types}) the database of vehicle types "
              f"contains '{db_cpt_types}' items.\n")

    def items(self):
        self.db_marks.items()

    def __getitem__(self, item):
        ''' Method checks item in the database '''
        item = item.upper()
        if item not in self.db_marks:
            return print(f'No, "{item}" does not exist in the database.')
        else:
            return print(f'Yes, "{item}" exists in the database.')

    def __iter__(self):
        self.counter = 0
        return self

    def __next__(self):
        if len(self.db_marks) <= self.counter:
            raise StopIteration
        num_count = list(self.db_marks)[self.counter]
        self.counter += 1
        return num_count
