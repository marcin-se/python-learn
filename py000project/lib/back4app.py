# Biblioteka z modułem 'requests' do obsługi API
# BACK4APP - baza pojazdów
# -*- coding: utf-8 -*-
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
from os.path import getmtime, exists
import requests
import datetime
import urllib
import json
import os
# - - - - - - - - - - - - - b a c k 4 a p p - - - - - - - - - - - - - - - - - -#


class Back4appAPIcars:
    ''' Class gets database from site: https://www.back4app.com/database/ '''
    def __init__(self):
        self.back4app_db = None
        self.back4ref_db = {}
        self.back4list_db = []
        self.when_get_db = ''

    def __str__(self):
        return ' <<< Database from: "www.back4app.com" >>>\n' \
               ' <<< (Current size database: {} items)'.format(
                self.back4app_db["count"])

    def load_db(self, file_name, myfile_name):
        ''' Load database from file (possibly from the site)'''
        if not exists(file_name):
            self.get_db()
            self.save_db(file_name)
            self.ref_db(myfile_name)
            return print(' *** The file has been created correctly. ***')
        file_time = getmtime(file_name)
        now_time = datetime.datetime.now().timestamp()
        if now_time - file_time < 3600 * 6:
            with open(file_name, "r") as file:
                self.back4app_db = json.load(file)
                self.ref_db(myfile_name)
        else:
            self.get_db()
            self.save_db(file_name)
            self.ref_db(myfile_name)
        self.when_get_db = datetime.datetime.\
            utcfromtimestamp(file_time + 7200).strftime('%d. %B %Y (%H:%M)')
        return print(' *** The data was loaded correctly. ***\n')

    def get_db(self):
        ''' Load database from native site '''
        apiapp = self.read_apikey('.//lib//apiapp.api')
        apihead = self.read_apikey('.//lib//apihead.api')
        url = 'https://parseapi.back4app.com/classes/' \
              'Carmodels_Car_Model_List?count=1&limit=300000'
        headers = {
            'X-Parse-Application-Id': apiapp, 'X-Parse-REST-API-Key': apihead}
        self.back4app_db = json.loads(requests.get(url, headers=headers)
                                      .content.decode('utf-8'))

    def save_db(self, file_name, flag=0):
        with open(file_name, mode="w") as file:
            if flag != 0:
                file.write(json.dumps(self.back4app_db, indent=4))
            else:
                self.back4list_db = sorted(self.back4list_db, key=lambda x: x[0])
                file.write(json.dumps(self.back4list_db, indent=4))
        return print(' *** The data was saved correctly. ***\n')

    def ref_db(self, file_name):
        ''' Method truncates database '''
        self.back4ref_db = self.back4app_db["results"]
        for elem in self.back4ref_db:
            del elem["objectId"]
            del elem["Year"]
            del elem["createdAt"]
            del elem["updatedAt"]
            elem["Make"] = str(elem["Make"]).title()
            elem["Model"] = str(elem["Model"]).title()
            elem["Category"] = str(elem["Category"]).upper()
        with open(file_name, mode='w') as filemon:
            filemon.write(json.dumps(self.back4ref_db, indent=4))
        return print(' *** The database has been truncated successfully. ***')

    def get_info(self):
        ''' Get answer from database '''
        db_count = self.back4app_db["count"]
        print(':' * 84)
        print(f"For day <{self.when_get_db}> the vehicle brand database "
              f"contains <{db_count}> items.")
        print(":" * 84)

    def get_verse(self, brand='', model='', typec='', start=0):
        id = start
        for element in self.back4ref_db:
            if brand == element["Make"] or model == element["Model"] or \
                                                typec in element["Category"]:
                id += 1
                yield id, element

    def set_ans(self, ans):
        print('{:4})\tMarka: {:15}\tModel: {:20}\tTyp: {}'.format(ans[0],
                                            str(ans[1]["Make"]).title(),
                                            str(ans[1]["Model"]).title(),
                                            str(ans[1]["Category"]).upper()))
        self.back4list_db.append([str(ans[1]["Make"]).title(),
                                  str(ans[1]["Model"]).title(),
                                  str(ans[1]["Category"]).upper()])
        return True

    @staticmethod
    def read_apikey(file_name):
        ''' funkcja pobierająca z pliku klucz API '''
        if os.path.isfile(file_name):
            if os.path.splitext(file_name)[1] == ".api":
                with open(file_name) as file:
                    return file.readline().strip()
        print('Error: File not found!')
        raise FileNotFoundError()


"""
class Back4appAPIcars:
    ''' Class gets database from site: https://www.back4app.com/database/ '''
    def __init__(self):
        self.back4app_db = {}
        self.reference_db = {}
        self.counter = 0


    def load_db(self, file_name):
        ''' Load databases from file (possibly from the site)'''
        if not exists(file_name):
            self.get_db()
            self.save_db(file_name)
            # self.ref_db()
            return print('The files have been created correctly.')
        file_time = getmtime(file_name)
        now_time = datetime.datetime.now().timestamp()
        if now_time - file_time < 60 * 60 * 24:
            with open(file_name, "r") as file:
                self.back4app_db = json.load(file)
        else:
            self.get_db()
            self.save_db(file_name)
            # self.ref_db()
        return print('The data was loaded correctly.')

    def save_db(self, file_name):
        with open(file_name, "w") as file:
            new_file = json.dumps(self.back4app_db, indent=2)
            file.write(new_file)
        return True

    def get_db(self):
        ''' Load databases from native site '''
        key1 = self.read_apikey(apiapp)
        key2 = self.read_apikey(apihead)
        url = 'https://parseapi.back4app.com/classes/' \
              'Carmodels_Car_Model_List?count=1&limit=1000'
        headers = {'X-Parse-Application-Id': key1, 'X-Parse-REST-API-Key': key2}
        data = json.loads(requests.get(url, headers=headers)
                          .content.decode('utf-8'))
        print(json.dumps(data, indent=2))

    def ref_db(self):
        ''' Method gets items from db '''
        for key, val in self.back4app_db.items():
            key_car = self.back4app_db['data']['attributes'][
                'dostepne-rekordy-slownika'][key]['klucz-slownika']
            val_car = self.back4app_db['data']['attributes'][
                'dostepne-rekordy-slownika'][val]['liczba-wystapien']
            self.reference_db[key_car] = val_car
        return True

    def get_info(self):
        ''' Get answer from database '''
        db_info = self.back4app_db['data']['attributes'] \
            ['ilosc-rekordow-slownika']
        now_time = datetime.datetime.now().timestamp()

        print('\n*** VEHICLE BRANDS ***\n----------------------')
        print(f"Today ({now_time}) the vehicle brand database "
              f"contains '{db_info}' items.")
        print('\n*** end info ***---------------*** end info ***\n')

    def items(self):
        self.reference_db.items()

    def __getitem__(self, item):
        ''' Method checks item in the database '''
        item = item.upper()
        if item not in self.reference_db:
            return print(f'No, "{item}" does not exist in the database.')
        else:
            return print(f'Yes, "{item}" exists in the database.')

    def __iter__(self):
        self.counter = 0
        return self

    def __next__(self):
        if len(self.reference_db) <= self.counter:
            raise StopIteration
        num_count = list(self.reference_db)[self.counter]
        self.counter += 1
        return num_count

    @staticmethod
    def read_apikey(file_name):
        ''' funkcja pobierająca z pliku klucz API '''
        if os.path.isfile(file_name):
            if os.path.splitext(file_name)[1] == ".api":
                with open(file_name) as file:
                    return file.readline().strip()
        print('Error: File not found!')
        raise FileNotFoundError

"""

