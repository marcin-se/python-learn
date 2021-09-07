# Biblioteka z modułem 'requests' do obsługi API
# GRATKA - baza pojazdów
# -*- coding: utf-8 -*-
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
import os
import winsound
from os.path import getmtime, exists
import requests
import datetime
import json
import time
from bs4 import BeautifulSoup
# - - - - - - - - - - - - - g r a t k a . p l - - - - - - - - - - - - - - - - -#


def parse_otomoto_offers(samoA):
    ''' method requests offers from site: "otomoto.pl" '''
    for a in samoA:
        offer = None
        yield offer
    raise ImportError('Error: Retrieving data from the network has failed!')


def parse_gratka_offers(samoA):
    ''' method requests offers from site: "gratka.pl" '''
    for a in samoA:
        offer = None
        yield offer
    raise ImportError('Error: Retrieving data from the network has failed!')


def parse_otomoto_brands():
    ''' method requests brand of cars from site: "gratka.pl" '''
    brand_dict: dict = {}
    mod_list:   list = []
    model:      list = []
    count       = 0
    brands_file = 'CARS_DB/brands.json'
    bramod_file = 'CARS_DB/OTOMOTO/brands_model.json'
    main_page   = 'https://www.otomoto.pl/osobowe/'
    for brand in brand_generator(brands_file):
        brand_dict.clear()
        mod_list.clear()
        model.clear()
        count += 1
        url = main_page + brand
        try:
            requests.get(url).status_code != 200
        except ConnectionError as ex:
            print(f' *** The server returned an error for task #{count}. ***'
                  f'\n *** Possibly some component of the url was incorrect.'
                  f' ***\n *** Error: {ex}. ***')
            continue
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        print(f' (({count}))\t.....parsing page in progress.....')
        brand_dict[brand] = {'models': [], 'pages': None}
        time.sleep(15)
        try:
            for base in soup.find_all('div', class_='seoInternalLinks panel-group'):
                for off in base.find_all('ul', class_='links collapse in panel'
                                         '-body modelsLinks'):
                    for br in off.text.split('\n'):
                        model.append(br.strip().split('(')[0]) if \
                                                br.find('(') != -1 else \
                                                model.append(br.strip())
                for mod in model:
                    if mod:
                        mod_list.append(' '.join(mod.strip().split(' ')[1:]))
                        mod_list.sort()
            brand_dict[brand]['models'] = mod_list
        except AttributeError as atr:
            print(f'Error for task #{count}.: {atr}.')
            continue
        add_data(bramod_file, brand_dict)
    print(' *** The data has been processed successfully! ***\n')
    return True


def parse_otomoto_pages():
    ''' method requests brand of cars from site: "gratka.pl" '''
    brand_dict:     dict = {}
    pager:          list = []
    count           = 0
    brands_file     = 'CARS_DB/brands.json'
    maxnum_file     = 'CARS_DB/OTOMOTO/maxNumPage.json'
    main_page       = 'https://www.otomoto.pl/osobowe/'
    suffix1         = '/?search%5Border%5D=created_at_first%3Adesc'
    for brand in brand_generator(brands_file):
        brand_dict.clear()
        pager.clear()
        count += 1
        url = main_page + brand + suffix1
        try:
            page = requests.get(url)                      # status_code == 200
        except ConnectionError as ex:
            print(f' *** The server returned an error for task #{count}. ***'
                  f'\n *** Possibly some component of the url was incorrect.'
                  f' ***\n *** Error: {ex}. ***')
            continue
        soup = BeautifulSoup(page.content, 'html.parser')
        print(f' (({count}))\t.....parsing page in progress.....')
        brand_dict[brand] = {'pages': None}
        time.sleep(15)
        try:
            for base in soup.find_all('script', type='text/javascript'):
                for bas in base.find('script'):
                    print(bas.text)
                    input('uuooo!')
            else:
                print(f' *** The server did not return an url error for ta'
                      f'sk #{count}. ***\n *** There is only one url. ***')
                brand_dict[brand]['pages'] = 1
            print(f'\t---{brand} : {pager}---')
        except AttributeError as atr:
            print(f'Error for task #{count}.: {atr}.')
            continue
        add_data(maxnum_file, brand_dict)
    print(' *** The data has been processed successfully! ***\n')
    return True


def take_numpages(file_name):
    ''' method loads number of pages for parsed site '''
    if os.path.isfile(file_name):
        with open(file_name, mode='a', newline='\n') as file:
            for a in file:
                numpages = None
                yield numpages
    raise FileNotFoundError('Error: The requested file was not found!')


def parse_gratka_brands(samoA):
    ''' method requests brand of cars from site: "gratka.pl" '''
    for a in samoA:
        numpages = None
        yield numpages
    raise ImportError('Error: Retrieving data from the network has failed!')


def save_data(file_name, body=None):
    """ method of saving data to JSON """
    with open(file_name, mode='w') as file:
        json.dump(body, file)
    return print(' *** The data was downloaded correctly. ***')


def add_data(file_name, body=None):
    """ method of saving data to JSON """
    if os.path.isfile(file_name):
        with open(file_name, mode='a', newline='\n') as file:
            file.write(json.dumps(body, indent=4))
            file.write(',\n\t')
            winsound.Beep(1000, 200)
        return print(' *** The data was added correctly. ***')
    raise FileNotFoundError('Error: The requested file was not found!')


def brand_generator(file_name):
    """ generator - it reads brand name from file """
    if os.path.isfile(file_name):
        with open(file_name, 'r', encoding='utf-8') as file:
            while True:
                read_brand = file.readline().strip()
                if not read_brand:
                    break
                yield read_brand


def load_data(file_name):
    ''' method loads database from file (possibly from the site)'''
    if not exists(file_name):
        read_info = get_data()
        save_data(file_name)
        print(' *** The file has been created correctly. ***')
        return read_info
    file_time = getmtime(file_name)
    now_time = datetime.datetime.now().timestamp()
    if now_time - file_time < 90:
        with open(file_name, "r") as file:
            read_info = json.load(file)
            print(' *** The data was loaded correctly. ***\n')
            return read_info
    else:
        read_info = get_data()
        save_data(file_name)
        print(' *** The data was loaded correctly. ***\n')
    return read_info


def get_data(samoA):
    ''' method loads database from native site '''
    for a in samoA:
        data = None
        yield data
    raise ConnectionError('Error: Connection error with the server!')


'''
def parse_back4app_brands():
    file4app = './/CARS_DB//back4app.json'
    file4app_my = './/CARS_DB//back4app_my.json'
    file_cut = './/CARS_DB//back4app_cut.json'
    que_mod, que_cat = '', ''
    back4app = Back4appAPIcars()
    back4app.load_db(file4app, file4app_my)
    while True:
        clear_screen()
        back4app.get_info()
        dividing_line('.' * 40)
        que_bra = input('\n((((((Enter the brand of the vehicle >> ')
        que_bra = que_bra.title().strip()
        if not que_bra:
            print('You did not enter the vehicle brand...')
            dividing_line('.' * 40)
            que_mod = input('((((((Enter the model of the vehicle >> ')
            que_mod = que_mod.title().strip()
            if not que_mod:
                print('You also did not enter the vehicle model...')
                dividing_line('.' * 40)
                que_cat = input('((((((Enter the vehicle body type  >> ')
                que_cat = que_cat.upper().strip()
        elif any((que_bra, que_mod, que_cat)):
            while True:
                for ans in back4app.get_verse(brand=que_bra,
                                              model=que_mod,
                                              typec=que_cat):
                    back4app.set_ans(ans)
                break
            back4app.save_db(file_cut)
        else:
            print('\nYou have not provided any vehicle parameters!\nBy!...')
            time.sleep(1)
        break
    return


def parse_cepik_brands():
    file_marks = 'CARS_DB/db_marks.json'
    file_types = 'CARS_DB/db_types.json'
    file_csv = 'CEPIK/pojazdy_24_2021-05-02.csv'
    file_json = 'CEPIK/base.json'
    cepik_cars = CepikAPIcars()
    cepik_cars.transfer_db(file_csv, file_json)
    cepik_cars.get_info()
    print(' < OK! >')
    # print(cepik_cars.items())
    return
'''
