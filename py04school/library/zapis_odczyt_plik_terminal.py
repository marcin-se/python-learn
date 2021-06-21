### Biblioteka z funkcjami zapisu i odczytu w plikach *.txt ###


# funkcja pobierająca dane słownikowe z pliku
def dict_from_file(file_path):
    dictionary = {}
    with open(file_path) as file:
        while True:
            read_key = file.readline().strip()
            if not read_key:
                break
            read_value = file.readline().strip()
            dictionary[read_key] = read_value
        return dictionary


# funkcja zapisująca dane słownikowe do pliku
def dict_to_file(file_path, dictionary_name):
    with open(file_path, "w+", encoding="utf8") as file:
        for key, val in dictionary_name.items():
            file.write(str(key) + "\n")
            file.write(str(val) + "\n")
    return

#
# # funkcja pobierająca dane otwarte z pliku
# def get_data_from_file(file_path):
#     with open(file_path) as file:
#         while True:
#
#
#
# # funkcja pobierająca dane otwarte z terminala
# def get_data_from_terminal():
#     get_data = ""
