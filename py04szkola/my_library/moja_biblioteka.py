### Biblioteka własna z klasami i funkcjami ###

# TXT >>> DICT
# data from <*.txt> to dict
def dict_from_file(file_path):
    dictionary = {}
    with open(file_path, "a+", encoding="utf8") as file:
        while True:
            read_key = file.readline()
            if not read_key:
                break
            read_value = file.readline()
            dictionary[read_key] = read_value
    return dictionary

# DICT >>> TXT
# data from dict to <*.txt>
def dict_to_file(file_path, dictionary_name):
    with open(file_path, "w+", encoding="utf8") as file:
        for key, val in dictionary_name.items():
            file.write(str(key) + "\n")
            file.write(str(val) + "\n")
