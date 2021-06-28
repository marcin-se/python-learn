'''Biblioteka z funkcjami zapisu i odczytu w plikach CSV | JSON | PICKLE |'''
import csv, json, pickle
import library.dodatki


def get_line(file):
    '''funkcja pobierająca jedną linię pliku *.csv'''
    return "{}".format(file.readline().strip())


def clean_file_csv(csv_file):
    '''funkcja oczyszczająca dane w pliku *.csv z białych znaków'''
    if os.path.exists(csv_file):
        with open(csv_file, 'r', newline='') as file:
            read_csv = csv.reader(file)
            for line in read_csv:
                clean_row = line.split(",")
                clean_list.append(clean_row.strip())
            save_file_csv(clean_list, csv_file)
            return True
    else:
        print("Plik nie istnieje!")
    return False


def read_file_csv(working_list, csv_file_src):
    '''funkcja pobierająca dane ze źródłowego pliku *.csv'''
    if os.path.exists(csv_file_src):
        with open(csv_file_src, 'r', newline='') as file:
            file.seek(0)
            line_num = 0
            read_csv = csv.reader(file)
            for line in read_csv:
                if line == 'stop':
                    break
                if not line_num:
                    working_list.append(line)
                    # print(f'{", ".join(row)}')
                    line_num += 1
                else:
                    working_list.append(line)
                    # print(f'\t{line[0]}\t{line[1]}\t{line[2]}\t{line[3]}')
                    line_num += 1
            print(f"Odczytano z pliku {line_num} wierszy.")
            working_list.decode("utf-8")
            return working_list
    else:
        print("Error: Błędna ścieżka pliku źródłowego.")
    return False


def save_file_csv(working_list, csv_file):
    '''funkcja zapisująca dane do docelowego pliku *.csv'''
    with open(csv_file, "w+", newline="") as file:
        write_csv = csv.writer(file)
        working_list.encode("utf-8")
        for line in working_list:
            write_csv.writerow(line)
    return True


def read_file_csv_json(working_list, csv_file):
    '''funkcja pobierająca dane ze źródłowego pliku csv 'JSON' '''
    if os.path.exists(csv_file):
        with open(csv_file, "rb", newline='') as file:
            file.seek(0)
            read_csv = csv.reader(file)
            for line in read_csv:
                working_list.append(json.loads(line))
        return True
    else:
        print("Error: Błędna ścieżka pliku źródłowego.")
    return working_list


def save_file_csv_json(working_list, csv_file):
    '''funkcja zapisująca dane do docelowego pliku csv 'JSON' '''
    with open(csv_file, "w+", newline="") as file:
        json.dump(working_list, file)
    return True


def read_file_csv_pickle(working_list, csv_file):
    '''funkcja pobierająca dane ze źródłowego pliku csv 'JSON' '''
    if os.path.exists(csv_file):
        with open(csv_file, "rb", newline='') as file:
            file.seek(0)
            read_csv = csv.reader(file)
            for line in read_csv:
                working_list.append(pickle.loads(line))
        return True
    else:
        print("Error: Błędna ścieżka pliku źródłowego.")
    return working_list


def save_file_csv_pickle(working_list, csv_file):
    '''funkcja zapisująca dane do docelowego pliku csv 'JSON' '''
    with open(csv_file, "w+", newline="") as file:
        pickle.dump(working_list, file)
    return True


def change_csv_from_argv(working_list, change_data):
    '''funkcja zmieniająca dane pobrane z argv[] w pliku *.csv'''
    for change in change_data:
        change_list = change.split(",")
        if change_list[0] and change_list[1]:
            working_list[int(change_list[0])-1][int(change_list[1])-1]\
                = int(change_list[2])
        else:
            print("Nieprawidłowe odwołania.")
    return working_list


def print_changes_argv(change_data):
    '''funkcja wyświetlająca zmiany pobrane z argv[] w pliku *.csv'''
    change_list: list = []
    for change in change_data:
        change_list = change.split(",")
    print('Odczytano następujące zmiany:')
    print(TPL_FORMAT_csv3col.format(
        int(change_list[0])-1, int(change_list[1])-1, str(change_list[2])))


def print_alldata_csv(csv_file_src):
    '''funkcja wyświetlająca wszystkie dane z pliku *.csv'''
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
