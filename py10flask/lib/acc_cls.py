# ACCOUNTANT v3.0 online                                                       #
# "accountant" obiektowo, wyłącznie z obsługą plików we/wy                     #
# -*- coding: UTF-8 -*-
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#


class NotEnoughMoneyException(Exception):
    ''' niewystarczające środki na koncie '''
    pass


class NotEnoughDataException(Exception):
    ''' niewystarczająca ilość danych '''
    pass


class NotEnoughStockException(Exception):
    ''' niewystarczająca ilość asortymentu '''
    pass


class NoAssortmentException(Exception):
    ''' brak asortymentu w magazynie '''
    pass


class NoActionException(Exception):
    ''' niezgodna liczba parametrów '''
    pass


class OutOfRangeException(Exception):
    ''' przekroczono dostępny zakres wywołania '''
    pass


class FileReadErrorException(Exception):
    ''' błąd odczytu pliku '''
    pass


class FileSaveErrorException(Exception):
    ''' błąd zapisu do pliku '''
    pass


class Reader:
    ''' klasa - odczyt danych z pliku '''

    def __init__(self, filepath):
        self.path = filepath
        self.file = open(filepath)

    def get_line(self, count=1):
        ''' metoda pobiera dane z pliku, zwraca listę '''
        countlist = []
        for i in range(count):
            fileline = self.file.readline()
            if not fileline:
                raise NotEnoughDataException('No data to read!')
            countlist.append(fileline.strip())
        return countlist

    def put_line(self, actions):
        ''' metoda dopisuje jedną linię do pliku '''
        self.open_file_read()
        filelines = self.file.readlines()
        if not filelines:
            raise NotEnoughDataException('No data to read!')
        filelines.insert(-1, (str(actions) + "\n"))
        joinlines = "".join(filelines)
        self.open_file_write()
        self.file.write(joinlines)
        self.file.close()

    def export_data(self, exp_data):
        ''' metoda zapisuje dane w pliku '''
        self.open_file_write()
        for line in exp_data:
            for pos in line:
                self.file.write("\n".join(pos) + "\n")
        self.file.write('stop\n')
        self.file.close()

    def open_file_read(self):
        self.file.close()
        self.file = open(self.path, mode='r', encoding='utf-8')

    def open_file_write(self):
        self.file.close()
        self.file = open(self.path, mode='w', encoding='utf-8')


class Manager:
    ''' główna klasa ogsługi magazynowo-księgowej '''

    def __init__(self, reader):
        self.reader = reader
        self.history = []
        self.account = 0
        self.stock = {}
        self.actions = {}  # {"akcja": (param, callback)}

    def action(self, my_action, params):
        ''' metoda modyfikuje słownik i zwraca funkcję '''
        def action_in(callback):
            self.actions[my_action] = (params, callback)
        return action_in

    def process(self):
        ''' metoda sprawdza akcję, pobiera parametry, zwraca callback '''
        while True:
            my_action = self.reader.get_line()[0]
            if my_action == "stop":
                break
            if my_action not in self.actions:
                raise NoActionException('Mismatch action parameters!\n'
                                        'Procedure not performed.')
            param, callback = self.actions[my_action]
            rows = self.reader.get_line(param)
            callback(self, rows)
        return True

    def post_process(self, my_action, rows):
        ''' metoda dodaje akcję do słownika, uzupełnia historię '''
        parameters, callback = self.actions[my_action]
        if len(rows) != parameters:
            raise NoActionException('Mismatch action parameters!\n'
                                    'Procedure not performed.')
        if callback(self, rows):
            self.add_history([my_action] + rows)
        return True

    def add_history(self, position):
        ''' metoda dodaje akcję do historii '''
        self.history.append(position)
        return True

    def view_history(self, start, stop):
        ''' metoda wyświetla wybrane wiersze z historii '''
        if start <= stop:
            if stop <= len(self.history) - 1:
                for row in self.history[int(start): int(stop)]:
                    print('(ArchID.{}) {}'.format(row, self.history[row]))
        else:
            raise OutOfRangeException('Position range exceeded.\n'
                                      'The last position: {}.'.format(
                                      len(self.history) - 1))
        return True

    def modify_account(self, value):
        ''' metoda modyfikuje stan konta '''
        if self.account + value < 0:
            raise NotEnoughMoneyException('Insufficient financial resources!')
        self.account += value
        return True

    def modify_stock(self, item, qty):
        ''' metoda modyfikuje stany magazynowe '''
        if item not in self.stock:
            self.stock[item] = 0
        if self.stock[item] + qty < 0:
            raise NotEnoughStockException('Insufficient quantity in stock!')
        else:
            self.stock[item] += qty
        return True

    def view_stock(self, items):
        ''' metoda wyświetla stany magazynowe wybranego asortymentu '''
        for item in items:
            if item not in self.stock:
                raise NoAssortmentException(f'No assortment in stock.')
        for item, qty in self.stock.items():
            print("* {}: {}".format(item, qty))
        return True

    def export_to_file(self):
        ''' metoda eksportuje historię do archiwizacji '''
        self.reader.export_data(self.history)
        return True

    def close_actions(self):
        ''' metoda kończy pracę programu '''
        # sys.exit('-= ZAKOŃCZENIE PROGRAMU =-')
