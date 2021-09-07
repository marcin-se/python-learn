# Biblioteka z klasami głównymi do projektu
# # -*- coding: utf-8 -*-#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
import os

brand_on_sale = 'Opel'
instances = [
    'Ford:Fiesta:True:True:True:False',
    'Opel:Corsa:True:True:True:True',
    'Renault:Megane:True:True:False:False'
]


class Car:

    def __init__(self, brand, model, is_airbag_ok, is_painting_ok,
                 is_mechanic_ok, ios):
        self.brand = brand
        self.model = model
        self.is_airbag_ok = is_airbag_ok
        self.is_painting_ok = is_painting_ok
        self.is_mechanic_ok = is_mechanic_ok
        self.__ios = ios

    def is_damaged(self):
        return not (self.is_airbag_ok and self.is_painting_ok and
                    self.is_mechanic_ok)

    def get_car_info(self):
        print('\n{} {}'.format(self.brand, self.model).upper())
        print('Air Bag  - ok? -      {}'.format(self.is_airbag_ok))
        print('Painting - ok? -      {}'.format(self.is_painting_ok))
        print('Mechanic - ok? -      {}'.format(self.is_mechanic_ok))
        print('IS ON SALE?           {}'.format(self.__ios))
        print('-' * 30)

    def __get_ios(self):
        return self.__ios

    def __set_ios(self, new_ios_status):
        if self.brand == brand_on_sale:
            self.__ios = new_ios_status
            print('Changing status "ios" to {} for {}'.
                  format(new_ios_status, self.brand))
        else:
            print('Cannot change status "ios". Sale valid only for {}'.
                  format(brand_on_sale))

    ios = property(__get_ios, __set_ios, None,
                   'If set to "True", the car is available in sale/promo.')

    @classmethod
    def read_from_text(cls, car_text):
        new_car = cls(*car_text.split(':'))
        return new_car

    @staticmethod
    def convert_to_kw(km):
        return km * 0.735

    @staticmethod
    def convert_to_km(kw):
        return kw * 1.36

    @staticmethod
    def read_apikey(file_name):
        ''' funkcja pobierająca klucz API z pliku *.api '''
        if os.path.isfile(file_name):
            if os.path.splitext(file_name)[1] == ".api":
                with open(file_name) as file:
                    return file.readline().strip()
        print('Error: File not found!')
        raise FileNotFoundError

