# Biblioteka z funkcjami zapisu i odczytu w plikach CSV | JSON | PICKLE |
import csv, json, pickle
import library.dodatki

class ModifyCSV:
    def __init__(self):
        self.working_list = []

    def read_file_csv(self, csv_file_src):
        '''metoda pobierająca dane ze źródłowego pliku *.csv'''
        if os.path.exists(csv_file_src):
            with open(csv_file_src) as file:
                line_num = 0
                read_csv = csv.reader(file)
                for line in read_csv:
                    if not line_num:
                        self.working_list.append(line)
                        # print(f'{", ".join(row)}')
                        # line_num += 1
                    else:
                        self.working_list.append(line)
                        # print(f'\t{line[0]}\t{line[1]}\t{line[2]}\t{line[3]}')
                        # line_num += 1
                print(f"Odczytano z pliku {line_num} wierszy.")
                self.working_list.decode("utf-8")
                return True
        else:
            print("Error: Błędna ścieżka pliku źródłowego.")
        return False

    def print_alldata_csv(self, csv_file_src):
        '''metoda wyświetlająca wszystkie dane z pliku *.csv'''
        if os.path.exists(csv_file_src):
            with open(csv_file_src) as file:
                num_line = 0
                read_csv = csv.reader(file)
                for line in read_csv:
                    if not num_line:
                        print("{:20}".format("\t ".join(line)))
                        num_line += 1
                    else:
                        print(TPL_FORMAT_csv.format(line[0], line[1], 
                            line[2], line[3], line[4], line[4]))
                        num_line += 1
                print(f"<<< Ogółem wierszy: {line_num}.>>>")
                print(TPL_FORMAT_csv.format(
                    int(change_list[0])-1, int(change_list[1])-1, str(change_list[2])))

    def save_file_csv(self, csv_file_dst):
        '''metoda zapisująca dane do docelowego pliku *.csv'''
        with open(csv_file_dst, "w+", newline="") as file:
            write_csv = csv.writer(file)
            self.working_list.encode("utf-8")
            for line in self.working_list:
                write_csv.writerow(line)
        return True

    def read_file_csv_json(self, csv_file_src):
        '''metoda pobierająca dane ze źródłowego pliku csv 'JSON' '''
        if os.path.exists(csv_file_dst):
            with open(csv_file_src) as file:
                read_csv = csv.reader(file)
                for line in read_csv:
                    self.working_list.append(json.loads(line))
            return True
        else:
            print("Error: Błędna ścieżka pliku źródłowego.")
        return False

    def save_file_csv_json(self, csv_file_dst):
        '''metoda zapisująca dane do docelowego pliku csv 'JSON' '''
        with open(csv_file_dst, "w+", newline="") as file:
            json.dump(self.working_list, file)
        return True

    def change_csv_from_argv(self, change_data):
        '''metoda zmieniająca dane pobrane z argv[] w pliku *.csv'''
        for change in change_data:
            change_list = change.split(",")
            if change_list[0] and change_list[1]:
                self.working_list[int(change_list[0])-1][int(change_list[1])-1]\
                    = int(change_list[2])
            else:
                print("")
        return self.working_list

    def print_change_argv(self, change_data):
        '''metoda wyświetlająca zmiany pobrane z argv[] w pliku *.csv'''
        change_list: list = []
        for change in change_data:
            change_list = change.split(",")
        print(TPL_FORMAT_csv3col.format(
            int(change_list[0])-1, int(change_list[1])-1, str(change_list[2])))
