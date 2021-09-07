# THE_CARS v1.0                                                                #
# project calculating the cost of the selected car model                       #
# -*- coding: UTF-8 -*-                                                        #
from lib.lib_files import *
from lib.gratka import *
# from lib.lib_cls import Car, instances, read_apikey
from lib.cepik import CepikAPIcars
from lib.back4app import Back4appAPIcars
import requests
import time
import json
import sys
from bs4 import BeautifulSoup

# - - - - - - - - - - - P R O J E C T  C O N T E N T - - - - - - - - - - - - - #
clear_screen()

'''apikey = read_apikey('lib//apikey.api')

car_01 = Car.read_from_text(instances[0])
car_02 = Car.read_from_text(instances[1])
car_03 = Car.read_from_text(instances[2])

car_01.get_car_info()
car_02.get_car_info()
car_03.get_car_info()'''

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
# cepik (database)
dividing_line()


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
# back4app (database)
dividing_line()


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
# parse gratka.pl

'''
footer_list:        list = []
brand_dict:         dict = {}
brands_file         = 'CARS_DB/brands.json'
parsed_file         = 'CARS_DB/GRATKA/parsed_offers.json'
brands_model_file   = 'CARS_DB/GRATKA/brands_model.json'
main_page           = 'https://gratka.pl/motoryzacja/osobowe/'
newest              = '?sort=newest'

dividing_line()
count = 0
for value in read_brand(brands_file):
    brand_dict.clear()
    footer_list.clear()
    url = main_page + value + newest
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    # for base in soup.find_all('div', class_='listingWrapper'):
    for base in soup.find_all('ul', class_='seobox__linkList'):
        for offer in base.find_all('li', class_='seobox__listItem'):
            footer = offer.find('a', class_='seobox__link').get_text().strip()
            footer_list.append(footer)
    brand_dict[value] = footer_list
    count += 1
    print(f' {count} saving parsed html in progress.....')
    add_data(brands_model_file, brand_dict)
    time.sleep(60)

            # info_portal = row.find('a', class_='breadcrumbs__link').get_text().strip()
            # info_trade= row.find('a', class_='breadcrumbs__link').get_text().strip()
            # info_type = row.find('a', class_='breadcrumbs__link').get_text().strip()
            # info_brand = row.find('a', class_='breadcrumbs__link').get_text().strip()
            # info_model = row.find('a', class_='breadcrumbs__link').get_text().strip()
            # print(info_portal, info_trade, info_type, info_brand, info_model)

# input('\n < Yeah! >')
'''';a'

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
# parse otomoto.pl

foo_list:       list = []
brand_dict:     dict = {}
brands_file     = 'CARS_DB/brands.json'
parsed_file     = 'CARS_DB/OTOMOTO/parsed_offers.json'
bramod_file     = 'CARS_DB/OTOMOTO/brands_model.json'
main_page       = 'https://www.otomoto.pl/osobowe/'
suffix1         = '?search%5Border%5D=created_at_first%3Adesc'
suffix2         = '&page='
# max_page        = take_numpages()

dividing_line()
# parse_otomoto_brands()
parse_otomoto_pages()

