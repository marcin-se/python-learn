# WEATHER v1.4                                     (R) Powered by WeatherAPI.com
# -*- coding: UTF-8 -*-                              https://www.weatherapi.com/
# Skrypt z odczytu danych pogodowych z serwera API                             #
'''
sprawdź, czy podano datę, czy nie
jeżeli podano, to czy data past, czy future
pobierz pakiety pip i zapisz ich listę do pliku ./requirements.txt
pobierz dane pogodowe api z serwera i zapisz je do pliku ./db_weather.json
dokonaj odczytu prognozowanej lub archiwalnej pogody
wyświetl odpowiedź
zapisz request do pliku
'''
# BIBLIOTEKA 'REQUESTS':  >>> https://requests.readthedocs.io/en/master/
# RAPID API:              >>> https://rapidapi.com/collection/top-weather-apis/
# WEATHER API             >>> https://api.weatherapi.com/
# JSON PARSER ONLINE      >>> https://json.parser.online.fr/
from api_lib.api_extras import clear_screen, dividing_line, title_line
from weatherapi.weatherapi_client import WeatherForecast, forecast_codes
from datetime import datetime, timedelta
from subprocess import Popen
import json
import time
import sys
import os

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
'''EXAMPLE1>>>   python weather.py <<klucz_api>>                            '''
'''EXAMPLE1>>>   python weather.py 3456789345678                            '''
'''EXAMPLE2>>>   python weather.py <<klucz_api>> <<YYYY-MM-DD>>             '''
'''EXAMPLE2>>>   python weather.py 3456789345678 2021-06-30                 '''
'''EXAMPLE3>>>   python weather.py 3456789345678 2021-06-30 Warszawa        '''
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #


def read_apikey(file_name):
    ''' funkcja pobierająca klucz API z pliku '''
    if os.path.exists(file_name):
        with open(key_file) as file:
            for num in file:
                return num.strip()
    return sys.stderr.write('Błąd pliku!')


def install_requirements(file_name):
    ''' funkcja pobierająca dane ze źródłowego pliku csv 'JSON' '''
    file_name = os.path.abspath(file_name)
    if os.path.exists(file_name):
        pass
        with open(file_name, 'r', newline='') as file:
            args = ['pip', 'install']
            read_file = file.readline().strip()
            for line in read_file:
                args.append(line)
                Popen(args)
        return sys.stdout.write('Wymagane biblioteki są zainstalowane.\n')
    return [False, sys.stderr.write('Błąd pliku!')]


def change_date_to_unix(date):
    ''' funkcja zmieniająca zapis daty '''
    unix_date = int(time.mktime(datetime.strptime(date, '%d-%m-%Y').
        timetuple())) if date[2] == '-' else int(time.mktime(
        datetime.strptime(date, '%Y-%m-%d').timetuple()))
    return unix_date


def change_unix_to_date(unix_date):
    ''' funkcja zmieniająca zapis daty '''
    date_ymd = str((datetime.utcfromtimestamp(unix_date)).strftime('%Y-%m-%d'))
    return date_ymd

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# PARAMETERS OF FILES & DATES :
key_file = 'APIKEY.txt'
db_weather = './db_weather.json'
db_requests = 'db_requests.json'
pipfreeze_file = "./requirements.txt"
date_today = datetime.now().strftime('%Y-%m-%d')
date_tomorrow = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
date_month = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')

# WEATHER PARAMETERS :
url_current = 'https://api.weatherapi.com/v1/current.json'
url_forecast = 'https://api.weatherapi.com/v1/forecast.json'
url_history = 'https://api.weatherapi.com/v1/history.json'
key = read_apikey(key_file)
q = 'Katowice,pl'
lang = 'pl'
dt = ''              # format: dt = yyyy-MM-dd
unix_date = 0        # format: unixdt = 1490227200
unix_end = 0         # format: unix_end = 1490227200
days = 2             # liczba dni prognozy: 1...10
country, city, local_date = '', '', ''
forecast_code, forecast, temperature, forecast_my = 0, '', 0.0, 'Nie wiem...'
response: dict = {}
weather_arch: dict = {}
requests_arch: dict = {}
''' print(requests.get(url).text) if requests.get(url) 
                                               else print('Error requests') '''
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
while True:
    clear_screen()
    print()
    if len(sys.argv) == 4 and sys.argv[1] == 'apikey':
        date = sys.argv[2]
        q = sys.argv[3]
    elif len(sys.argv) == 3 and sys.argv[1] == 'apikey':
        date = sys.argv[2]
    elif len(sys.argv) == 2 and sys.argv[1] == 'apikey':
        date = date_tomorrow
    else:
        sys.stdout.write('Nieprawidłowe dane wejściowe!')
        break
    ''' sprawdzenie ilości, kolejności i formatu argumentów "sys.argv" '''

    # install_requirements(pipfreeze_file)
    ''' instalacja pakietów z pliku: "requirements.txt" '''

    wf = WeatherForecast(key)
    wfc = wf.ap_is
    ''' utworzenie obiektu klienta pogodowego klasy: WeatherForecast'''

    weather_arch = wf.load_forecast(file_name=db_weather, q=q)
    ''' aktualizacja pliku "db_weather.json" co 24h '''

    sys.stdout.write('\nMetoda "wf[date]" działa następująco:\n')
    info = wf[date]
    print(date, info)
    sys.stdout.write('\nMetoda "wf.items()" działa następująco:\n')
    for day, forc in wf.items():
        print(day, forc)
    ''' użycie metod, zgodnie z treścią zadania '''

    unix_date = change_date_to_unix(date)
    unix_today = change_date_to_unix(date_today)
    unix_tomorrow = change_date_to_unix(date_tomorrow)
    unix_month = change_date_to_unix(date_month)
    ''' konwersja dat na unixtime '''

    if date in weather_arch:
        local_date = date
        forecast_my = weather_arch[date]
        temperature = '---'
        country = 'Poland'
        city = q
    elif unix_date == unix_today:
        response = json.loads(wf.get_current(q=q))
        country = response['location']['country']
        city = response['location']['name']
        local_date = change_unix_to_date(response['location']['localtime_epoch'])
        forecast_code = response['current']['condition']['code']
        forecast = (response['current']['condition']['text'])
        temperature = response['current']['temp_c']
    elif unix_date < unix_today or unix_date > unix_today:
        if unix_date < unix_today:
            time_now = datetime.now().timestamp()
            if time_now - unix_date > 3600 * 24 * 7:     # 3600 * hours * days
                date = change_unix_to_date(unix_today - 518400)
            response = json.loads(wf.get_history(q=q, dt=date, enddt=None))
        elif unix_date > unix_today:
            response = json.loads(wf.get_forecast(q=q, days=days, dt=None,
                                                        unixdt=unix_date+43200))
        country = response['location']['country']
        city = response['location']['name']
        local_date = response['forecast']['forecastday'][0]['date']
        forecast_code = response['forecast']['forecastday'][0]['day'] \
                                                        ['condition']['code']
        forecast = response['forecast']['forecastday'][0]['day'] \
                                                        ['condition']['text']
        temperature = response['forecast']['forecastday'][0]['day']['avgtemp_c']
        forecast_my = 'Będzie padać!' if forecast_code in forecast_codes \
                                                        else 'Nie będzie padać.'
    ''' sprawdzanie daty - data implikuje rodzaj zapytania o pogodę '''

    dividing_line()
    sys.stdout.write('Kraj: \t\t| {}\nMiasto: \t| {}\nData: \t\t| {}\n'.
        format(country, city, local_date))
    sys.stdout.write(
        'Temperatura: \t| {}`C\nPrognoza({:4}): | {:44}\nInfo: \t\t| {:18}\n'.
                     format(temperature, forecast_code, forecast, forecast_my))
    title_line('{} ({}) ---- {}'.format(city, local_date, forecast_my))
    print('\n\n')
    ''' wyświetlenie pobranych wyników '''

    requests_arch = {date: forecast_my}
    wf.save_dict_to_file(db_requests, requests_arch)
    ''' zapis "request" w słowniku a następnie zapis do pliku '''

    break
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #