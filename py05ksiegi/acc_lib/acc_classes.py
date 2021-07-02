# ACCOUNTANT v2.0_on_classes
# -*- coding: UTF-8 -*-
# Biblioteka z klasami i funkcjami księgowości rachunkowo-magazynowej
from sys import stdout


class Accountant:
    ''' klasa obsługująca księgowość rachunkowo-magazynową '''
    def __init__(self):
        self.log_list = self.log_list.append(['None', 0, 0, 0])
        self.stock_status = {}
        self.account_balance = 0

    def change_budget(self, value, comment):
        ''' metoda zmieniająca stan konta finansowego '''
        self.account_balance += value
        self.log_list.append(['saldo', value, comment])
        stdout.write('===== Zmieniono wartość środków na koncie. =====')
        return 1

    def change_buy(self, product_name, price, quantity):
        ''' metoda obsługująca proces zakupów '''
        if price <= 0 or quantity <= 0:
            print('===== Nieprawidłowa cena lub ilość! =====')
            return 0
        elif self.account_balance <= price * quantity:
            print('===== Zakup niemożliwy! Brak środków! =====')
            return 0
        else:
            self.account_balance -= price * quantity
            self.stock_status[product_name] += quantity
            self.log_list.append(['zakup', product_name, price, quantity])
            print('===== Zakup zakończony pomyślnie. =====')
        return 1

    def change_sale(self, product_name, price, quantity):
        ''' metoda obsługująca proces sprzedaży '''
        if product_name not in self.stock_status:
            print('* {}: brak produktu w magazynie!'.format(product_name))
            return 0
        elif self.stock_status[product_name] <= quantity:
            print('* {}: zbyt mały asortyment!'.format(product_name))
            return 0
        else:
            self.account_balance += price * quantity
            self.stock_status[product_name] -= quantity
            if not self.stock_status[product_name]:
                print('* {}: produkt wyprzedany!'.format(product_name))
            self.log_list.append(['sprzedaż', product_name, price, quantity])
            print('===== Sprzedaż zakończona pomyślnie. =====')
            return 1

    def about_account(self):
        ''' metoda zwracająca info o stanie konta finansowego '''
        print('===== Stan konta: {} ====='.format(self.account_balance))
        return self.account_balance

    def about_stock(self, product_name):
        ''' metoda zwracająca info o stanach magazynowych '''
        if product_name in self.stock_status:
            print('* {}: {} szt'.format(
                product_name, self.stock_status[product_name]))
            return 1
        else:
            print('* {}: brak asortymentu w magazynie!'.format(
                product_name))
            return 0

    def about_logs(self, start_range, stop_range):
        ''' metoda zwracająca info o dotychczasowych transakcjach '''
        if start_range <= stop_range:
            if stop_range <= len(self.log_list) - 1:
                for oper in range(start_range, stop_range):
                    stdout.write('Archiwum(ID.{}) {}\n'.format(
                        oper, self.log_list[oper]))
                    return 1
            else:
                print('===== Wartości poza zakresem! =====')
                print('(( Ostatni indeks operacji to {}. ))'.format(
                    len(self.log_list) - 1))
        else:
            print('===== Odwrócone wartości zakresu! =====')
        return 0

    def write_to_file(self, file_name, command_list):
        ''' metoda zapisująca 'otwarte' dane do pliku '''
        with open(file_name, 'r+', encoding='utf-8') as file:
            new_file = file.readlines()
            file.seek(0)
            for line in new_file:
                if line != 'stop\n':
                    file.write(line)
            file.truncate()
            for idx in command_list:
                file.write("{}\n".format(idx))
            file.write('stop\n')
        return 1

    def get_line(self, file_name):
        '''funkcja pobierająca jedną linię pliku'''
        return '{}'.format(file_name.readline().strip())

    def read_from_file_to_list(self, file_name):
        '''funkcja pobierająca 'otwarte' dane z pliku'''
        with open(file_name, 'r', encoding="utf-8") as file:
            command_list: list = []
            file.seek(0)
            while True:
                get_data = self.get_line(file)

                if not get_data or get_data == 'stop':
                    break

                if get_data == 'saldo':
                    value = int(self.get_line(file))
                    comment = str(self.get_line(file))
                    command_list.append(['saldo', value, comment])

                if get_data == 'sprzedaż':
                    product_name = str(self.get_line(file))
                    price = int(self.get_line(file))
                    quantity = int(self.get_line(file))
                    command_list.append(['sprzedaż',
                                         product_name, price, quantity])

                if get_data == 'zakup':
                    product_name = str(self.get_line(file))
                    price = int(self.get_line(file))
                    quantity = int(self.get_line(file))
                    command_list.append(['zakup',
                                         product_name, price, quantity])
        return command_list
