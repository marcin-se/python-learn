# Biblioteka z funkcjami zapisu i odczytu w plikach CSV | JSON | PICKLE |
from csv_lib.csv_ext import *
import csv
import json
import pickle
import os


class ModifyFile:
    def __init__(self):
        self.jiff_list = []

    def open_file(self, file_name):
        """ method of opening indicated file """
        if os.path.exists(file_name):
            if os.path.splitext(file_name)[1] == ".csv":
                self.read_csvfile(file_name)
            elif os.path.splitext(file_name)[1] == ".json":
                self.read_jsonfile(file_name)
            elif os.path.splitext(file_name)[1] == ".pickle":
                self.read_picklefile(file_name)
            else:
                raise ErrorExtentionException()
            return True, print(f'SRC-FILE: {file_name}\nData loaded correctly.')
        raise FileExistErrorException()

    def save_file(self, file_name):
        """ method of saving data to indicated file """
        if os.path.splitext(file_name)[1] == ".csv":
            self.save_csvfile(file_name)
        elif os.path.splitext(file_name)[1] == ".json":
            self.save_jsonfile(file_name)
        elif os.path.splitext(file_name)[1] == ".pickle":
            self.save_picklefile(file_name)
        else:
            raise ErrorExtentionException()
        return True, print(f'DST-FILE: {file_name}\nData saved correctly.')

    def read_csvfile(self, file_name):
        """ method of reading data from CSV """
        with open(file_name, 'r', newline='', encoding='utf-8') as file:
            reader_csv = self.clean_csvdata(csv.reader(file))
            for line in reader_csv:
                if not line:
                    break
                else:
                    self.jiff_list.append(line)
        return True

    def read_jsonfile(self, file_name):
        """ method of reading data from JSON """
        with open(file_name, 'r', newline='', encoding='utf-8') as file:
            reader_json = self.clean_csvdata(json.load(file))
            for line in reader_json:
                if not line:
                    break
                else:
                    self.jiff_list.append(line)
        return True

    def read_picklefile(self, file_name):
        """ method of reading data from PICKLE """
        with open(file_name, 'rb') as file:
            reader_pickle = self.clean_csvdata(pickle.load(file))
            for line in reader_pickle:
                if not line:
                    break
                else:
                    self.jiff_list.append(line)
        return True

    def save_csvfile(self, file_name):
        """ method of saving data to CSV """
        with open(file_name, "w", newline="") as file:
            writer_csv = csv.writer(file)
            for line in self.jiff_list:
                writer_csv.writerow(line)
        return True

    def save_jsonfile(self, file_name):
        """ method of saving data to JSON """
        with open(file_name, "w", newline="") as file:
            json.dump(self.jiff_list, file)
        return True

    def save_picklefile(self, file_name):
        """ method of saving data to PICKLE """
        with open(file_name, 'wb') as file:
            pickle.dump(self.jiff_list, file)
        return True

    def clean_csvdata(self, csvdata):
        """ method of cleaning data in CSV """
        # reader_csv = csv.reader(csvdata)
        clean_list: list = []
        for line in csvdata:
            for i in range(len(line)):
                line[i] = line[i].strip(' ')
            clean_list.append(list(line))
        return clean_list

    def change_csvdata(self, change_data):
        """ method of changing data in file """
        change_list = list(change_data.split(","))
        if change_list[0] and change_list[1]:
            self.jiff_list[int(change_list[0])][int(change_list[1]) - 1]\
                    = str(change_list[2])
        else:
            raise IncorrectDataException()
        return True

    def print_data(self):
        """ method of printing data from file """
        for line in self.jiff_list:
            print('{:20}'.format("\t ".join(line)))
        return True

    @staticmethod
    def print_argvchanges(change_data):
        """ method of printing changes """
        change_list = list(change_data.split(","))
        print(TPL_FORMAT_argv.format(
                    int(change_list[0]),
                    int(change_list[1]),
                    str(change_list[2])))
        return True


class ErrorExtentionException(Exception):
    pass # print('Error: Wrong file extension!')


class FileExistErrorException(Exception):
    pass # print('Error: Wrong path or file does not exist!')


class IncorrectDataException(Exception):
    pass # print("Error: Incorrect data references!")
