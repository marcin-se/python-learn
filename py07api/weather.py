# WEATHER v1.0
# -*- coding: UTF-8 -*-
# Skrypt z odczytu danych pogodowych z API (danych z serwera)
import os
import sys
import csv
import time
import json
import msvcrt
import requests
import datetime
from sys import stdin, stdout, stderr
from csv_lib.csv_additives import clear_screen, title_line
# from csv_lib.csv_functions import \

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
'''sprawdź, czy podano datę, czy nie'''
'''jeżeli podano, to czy data past, czy future'''
'''pobierz pakiety pip i zapisz ich listę do pliku ./requirements.txt'''
'''pobierz dane pogodowe api z serwera i zapisz je do pliku ./db_forecast.csv'''
'''dokonaj odczytu prognozowanej lub archiwalnej pogody'''
'''wyświetl odpowiedź'''
'''zapytaj, czy ponowić, czy wyjść'''
# BIBLIOTEKA 'REQUESTS':  >>> https://requests.readthedocs.io/en/master/
# RAPID API:              >>> https://rapidapi.com/collection/top-weather-apis/
# JSON PARSER ONLINE      >>> https://json.parser.online.fr/
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #


class Weather:
    def __init__(self):
        self.response = []
        self.url = ''

    def read_apikey(self, file_name):
        '''metoda pobierająca klucz API z pliku'''
        if os.path.exists(file_name):
            with open(key_file) as file:
                for num in file:
                    return num.strip()
        else:
            return False

    def get_response(self, url_address, place):
        '''metoda pobierająca dane pogodowe z serwera (API)'''
        self.url = url_address
        querystring = {'q': place}
        headers = {
            'x-rapidapi-key': self.read_apikey(key_file),
            'x-rapidapi-host': 'community-open-weather-map.p.rapidapi.com'
        }
        self.response = requests.request(
            'GET', self.url, headers=headers, params=querystring).json()
        return self.response

    def save_response(self, file_name):
        pass

    def save_forecast_csv(self, file_name):
        '''metoda zapisująca dobowe dane pogodowe do pliku (CSV-JSON)'''
        with open(file_name, "w+", newline="", encoding='utf-8') as file:
            weather_csv = csv.writer(file)
            json.dump(weather_csv, file)
        return True

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
'''EXAMPLE0>>>   python weather.py <<klucz_api>> <<YYYY-MM-DD>>             '''
'''EXAMPLE1>>>   python weather.py 3456789345678                                  '''
'''EXAMPLE2>>>   python weather.py 3456789345678 2021-06-30                       '''
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
url = 'https://community-open-weather-map.p.rapidapi.com/forecast'
forecast_place = 'machupickchu'
db_file = 'db_forecast.csv'
pipfreeze_file = 'requirements.txt'
key_file = 'APIKEY.1ST'
weather = 'Nie wiem'
this_day = datetime.datetime.now() #.utcfromtimestamp()
what_day = this_day

clear_screen()
'''while True:
    if len(sys.argv) == 2:
        what_day = sys.argv[2]
    if len(sys.argv) == 1:
        what_day = this_day + 1
    else:
        sys.stdout.write('Nieprawidłowa liczba argumentów!')
        break'''

while True:
    title_line(' Prognoza na dzień: {} to: {}'.format(what_day, weather))

    if requests.get(url):
        print(requests.get(url).text)
    else:
        break
    if 'Rain' == 'Rain':
        weather = 'Będzie padać'
    else:
        weather = 'Nie będzie padać'

    stdin.write("")