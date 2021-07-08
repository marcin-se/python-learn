# WEATHER v1.0                                     (R) Powered by WeatherAPI.com
# -*- coding: UTF-8 -*-                              https://www.weatherapi.com/
# Skrypt z odczytu danych pogodowych z serwera API                             #
'''
sprawdź, czy podano datę, czy nie
jeżeli podano, to czy data past, czy future
pobierz pakiety pip i zapisz ich listę do pliku ./requirements.txt
pobierz dane pogodowe api z serwera i zapisz je do pliku ./db_weather.json
dokonaj odczytu prognozowanej lub archiwalnej pogody
wyświetl odpowiedź
zapytaj, czy ponowić, czy wyjść
'''
# BIBLIOTEKA 'REQUESTS':  >>> https://requests.readthedocs.io/en/master/
# RAPID API:              >>> https://rapidapi.com/collection/top-weather-apis/
# WEATHER API             >>> https://api.weatherapi.com/
# JSON PARSER ONLINE      >>> https://json.parser.online.fr/

from datetime import datetime, timedelta
from os.path import getmtime
from api_lib.api_extras import clear_screen, dividing_line, title_line
from weatherapi.weatherapi_client import WeatherapiClient
from subprocess import Popen
import jsonpickle
import json
import time
import sys
import os

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
'''EXAMPLE1>>>   python weather.py <<klucz_api>>                            '''
'''EXAMPLE1>>>   python weather.py 3456789345678                            '''
'''EXAMPLE2>>>   python weather.py <<klucz_api>> <<YYYY-MM-DD>>             '''
'''EXAMPLE2>>>   python weather.py 3456789345678 2021-06-30                 '''
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #


def read_apikey(file_name):
    '''metoda pobierająca klucz API z pliku'''
    if os.path.exists(file_name):
        with open(key_file) as file:
            for num in file:
                return num.strip()
    else:
        sys.stderr.write('Błąd pliku!')


def install_requirements(file_name):
    '''funkcja pobierająca dane ze źródłowego pliku csv 'JSON' '''
    file_name = os.path.abspath(file_name)
    if os.path.exists(file_name):
        with open(file_name, 'r', newline='') as file:
            args = ['c:\windows\system32\cmd.exe', 'pip', 'install']
            read_file = file.readline().strip()
            for line in read_file:
                args.append(line)
                Popen(args)
    return False, sys.stderr.write('Błąd pliku!')


def change_date_to_unix(date):
    '''metoda zmieniająca zapis daty'''
    unix_date = int(time.mktime(datetime.strptime(date, '%d-%m-%Y').
        timetuple())) if date[2] == '-' else int(time.mktime(
        datetime.strptime(date, '%Y-%m-%d').timetuple()))
    return unix_date


def change_unix_to_date(unix_date):
    '''metoda zmieniająca zapis daty'''
    date_ymd = str((datetime.utcfromtimestamp(unix_date)).strftime('%Y-%m-%d'))
    return date_ymd


def collect_history(dict_name, date, forecast):
    '''metoda zapisująca dane pogodowe w słowniku '''
    dict_name[date] = forecast
    return True


def get_response_current(q):
    resp = jsonpickle.encode(ap_is_controller.get_realtime_weather(q=q,
            lang='pl'))
    return resp


def get_response_history(q, dt, enddt):
    '''get_history_weather(q, dt, *unixdt, *end_dt, *unixend_dt, *hour, *lang)'''
    resp = jsonpickle.encode(ap_is_controller.get_history_weather(q=q, dt=dt,
            unixdt=None, end_dt=enddt, unixend_dt=None, hour=None, lang='pl'))
    return resp


def get_response_forecast(q, days, unixdt):
    '''get_forecast_weather(q, days, *dt, *unixdt, *hour, *lang)'''
    resp = jsonpickle.encode(ap_is_controller.get_forecast_weather(q=q, days=days,
            dt=None, unixdt=unixdt, hour=None, lang='pl'))
    return resp


def load_forecast(file_name, q, dt, unix_today):
    time_file = getmtime(file_name)
    time_now = datetime.now().timestamp()
    if time_now - time_file < 86400:
        with open(file_name, 'r', newline='', encoding='utf-8') as file:
            dict_name = json.load(file)
    else:
        response_h = ap_is_controller.get_history_weather(q=q, dt=dt,
            unixdt=None, end_dt=None, unixend_dt=unix_today, hour=None,
                                                          lang='pl')
        response_f = ap_is_controller.get_forecast_weather(q=q, days=10,
            dt=None, unixdt=unix_today, hour=None, lang='pl')
        dict_name = response_h | response_f
    save_file(file_name, dict_name)
    return dict_name


def save_file(file_name, dict_name):
    '''metoda zapisująca dobowe dane pogodowe do pliku (JSON)'''
    if os.path.exists(file_name):
        with open(file_name, 'w', newline='\n', encoding='utf-8') as file:
            json.dump(dict_name, file)
        return True
    return False, sys.stderr.write('Błąd pliku!')


def read_file(file_name):
    '''funkcja pobierająca dane ze źródłowego pliku csv 'JSON' '''
    if os.path.exists(file_name):
        dict_name: dict = {}
        with open(file_name, 'r', newline='', encoding='utf-8') as file:
            read_json = json.load(file)
            for key, val in read_json.items():
                dict_name[key] = val
            return dict_name
    return False, sys.stderr.write('Błąd pliku!')


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

key_file = 'APIKEY.txt'
db_weather = 'db_weather.json'
db_requests = 'db_requests.json'
pipfreeze_file = r"C:\Users\mksse\PycharmProjects\py07api\
            weatherapi-Python-CodeGen-PY\requirements.txt"
date_today = datetime.now().strftime('%Y-%m-%d')
date_tomorrow = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
date_month = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
forecast_codes = [1063, 1066, 1069, 1072, 1087, 1150, 1153, 1168, 1171, 1183,
            1186, 1189, 1192, 1195, 1198, 1201, 1204, 1207, 1243, 1246, 1273]

# WEATHER PARAMETERS :
url_current = 'https://api.weatherapi.com/v1/current.json'
url_forecast = 'https://api.weatherapi.com/v1/forecast.json'
url_history = 'https://api.weatherapi.com/v1/history.json'
''' print(requests.get(url).text) if requests.get(url) 
                                                else print('Error requests')'''
key = read_apikey(key_file)
q = 'Katowice'
lang = 'pl'
dt = ''              # format: dt = yyyy-MM-dd
unix_date = 0        # format: unixdt = 1490227200
unix_end = 0         # format: unix_end = 1490227200
days = 1             # liczba dni prognozy: 1...10
country, city, local_date = '', '', ''
forecast_code, forecast, temperature, forecast_my = 0, '', 0.0, 'Nie wiem ;/'
response: dict = {}
weather_arch: dict = {}
requests_arch: dict = {}

while True:
    clear_screen()
    if len(sys.argv) == 3 and sys.argv[1] == 'apikey':
        date = sys.argv[2]
    elif len(sys.argv) == 2 and sys.argv[1] == 'apikey':
        date = date_tomorrow
    else:
        sys.stdout.write('Nieprawidłowe dane wejściowe!')
        break

    client = WeatherapiClient(key)
    ap_is_controller = client.ap_is
    ''' obiekt klienta pogodowego klasy: WeatherapiClient(key)'''

    unix_date = change_date_to_unix(date)
    unix_today = change_date_to_unix(date_today)
    unix_tomorrow = change_date_to_unix(date_tomorrow)
    unix_month = change_date_to_unix(date_month)
    ''' konwersja dat na unixtime '''

    install_requirements(pipfreeze_file)
    ''' instalacja pakietów z pliku: "requirements.txt" '''

    weather_arch = load_forecast(file_name=db_weather, q=q, dt=date_month,
                                 unix_today=unix_today)
    ''' aktualizacja pliku "db_weather.json" danymi z "weatherapi.com" '''

    if date in weather_arch:
        forecast_my = 'Będzie padać' if weather_arch[sys.argv[2]] in \
                                        forecast_codes else 'Nie będzie padać'
    else:
        if unix_date == unix_today:
            response = json.loads(get_response_current(q=q))
        elif unix_date < unix_today:
            response = json.loads(get_response_history(q=q,
                                                        dt=date, enddt=None))
        elif unix_date > unix_today:
            response = json.loads(get_response_forecast(q=q, days=days,
                                                            unixdt=unix_date))
    ''' sprawdzanie daty - data implikuje rodzaj zapytania o pogodę '''

    response = json.loads(get_response_forecast(q=q, days=10, unixdt=unix_date))
    save_file(db_weather, response)
    print(response)
    country = response['location']['country']
    city = response['location']['name']
    local_date = change_unix_to_date(response['location']['localtime_epoch'])
    forecast_code = response['current']['condition']['code']
    forecast = response['current']['condition']['text']
    temperature = response['current']['temp_c']

    sys.stdout.write('Country: \t| {}\nCity: \t\t| {}\nLocal time: \t| {}\n'.
        format(country, city, local_date))
    sys.stdout.write('Temperature: \t| {}`C\nForecast: \t| {}\n'
        'Forecast code: \t| {}\n'.format(temperature, forecast, forecast_code))

    for code in forecast_codes:
        forecast_my = 'Będzie padać ;(' if forecast_code == code else \
                                                        'Nie będzie padać ;)'

    title = '{}, {} >>> {}'.format(city, local_date, forecast_my)
    title_line(title)

    collect_history(requests_arch, unix_date, forecast_my)
    ''' zapis "request" w słowniku ("YYYY-MM-DD": "Będzie padać") '''

    save_file(db_requests, requests_arch)
    ''' zapis słownika z "requests" do pliku '''
    break