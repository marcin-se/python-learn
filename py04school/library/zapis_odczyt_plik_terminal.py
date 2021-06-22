# Biblioteka z funkcjami zapisu i odczytu w plikach *.txt #

from library.klasy_metody_funkcje import groups_dict, group_objects,\
    make_group, make_group_obj,\
    Pupil, Teacher, Educator,\
    if_class, if_class_obj,\
    if_pupil, if_pupil_obj,\
    if_teacher, if_teacher_obj,\
    if_educator, if_educator_obj

# funkcja pobierająca dane słownikowe z pliku
def dict_from_file(file_path):
    dictionary = {}
    with open(file_path, encoding="utf-8") as file:
        while True:
            read_key = file.readline().strip()
            if not read_key:
                break
            read_value = file.readline().strip()
            dictionary[read_key] = read_value
        return dictionary


# funkcja zapisująca dane słownikowe do pliku
def dict_to_file(file_path, dictionary):
    with open(file_path, "w+", encoding="utf-8") as file:
        for key, val in dictionary.items():
            file.write(str(key) + "\n")
            file.write(str(val) + "\n")


# funkcja zapisująca dane słownikowo-obiektowe do pliku
def dict_to_file_obj(file_path, dictionary_name):
    with open(file_path, "w+", encoding="utf-8") as file:
        for key, val in dictionary_name.items():
            file.write(str(key) + "\n")
            file.write(str(val) + "\n")


# funkcja pobierająca 'otwarte' dane z pliku *.txt
def get_data_from_file(file_path):
    dictionary: dict = {}
    with open(file_path, encoding="utf-8") as file:
        seek(0)
        while True:
            get_data = str.lower(file.readline().strip())
            if not get_data:
                continue
            if get_data == "koniec":
                break
            if get_data == "uczeń":
                new_pupil = str.title(file.readline().strip())
                new_group = str.lower(file.readline().strip())
                dictionary.update(make_group(new_group, dictionary))
                dictionary[new_group]["pupils"].append(new_pupil)
                # new_pupil_obj = Pupil(new_pupil)
                # new_group_obj = make_group_obj(new_group, dictionary)
                # new_group_obj["pupils"].append(new_pupil)
                # new_pupil_obj.set_group(new_group)
                continue
            if get_data == "nauczyciel":
                new_teacher = str.title(file.readline().strip())
                new_subject = str.lower(file.readline().strip())
                while 1:
                    new_group = str.lower(file.readline().strip())
                    if new_group:
                        dictionary.update(make_group(new_group, dictionary))
                        dictionary[new_group]["teachers"][new_subject] \
                            = new_teacher
                        # new_teacher_obj = Teacher(new_teacher)
                        # new_teacher_obj.set_groups(new_group)
                        # new_group_obj = make_group_obj(new_group, group_objects)
                        # new_group_obj.teachers[new_subject] = new_teacher_obj
                    else:
                        break
                continue
            if get_data == "wychowawca":
                new_educator = str.title(file.readline().strip())
                while 1:
                    new_group = str.lower(file.readline().strip())
                    if new_group:
                        dictionary.update(make_group(new_group, dictionary))
                        dictionary[new_group]["educator"] = new_educator
                        # new_educator_obj = Educator(new_educator)
                        # new_educator_obj.set_groups(new_group)
                        # new_group_obj = make_group_obj(new_group, group_objects)
                        # new_group_obj.educator = new_educator_obj
                    else:
                        break
                continue
    return dictionary


# funkcja pobierająca dane otwarte z terminala
def get_data_from_terminal():
    while 1:
        print("Podaj stanowisko (lub 'koniec'): ", end="")
        get_data = str.lower(input().strip())
        if get_data == "koniec":
            break
        if get_data == "uczeń":
            full_name = str.title(input("Imię Nazwisko: ").strip())
            new_pupil_obj = Pupil(full_name)
            new_group = str.lower(input("Klasa: ").strip())
            groups_dict.update(make_group(new_group, groups_dict))
            groups_dict[new_group]["pupils"].append(full_name)
            # new_group_obj = make_group_obj(new_group, group_objects)
            # new_pupil_obj.set_group(new_group)
            # new_group_obj.pupils.append(new_pupil_obj)
            continue
        if get_data == "nauczyciel":
            full_name = str.title(input("Imię Nazwisko: ").strip())
            new_teacher_obj = Teacher(full_name)
            new_subject = str.lower(input("Przedmiot: ").strip())
            new_teacher_obj.set_subject(new_subject)
            while 1:
                new_group = str.lower(input("Klasa: ").strip())
                if new_group:
                    groups_dict.update(make_group(new_group, groups_dict))
                    groups_dict[new_group]["teachers"][new_subject]\
                        = full_name
                    # new_group_obj = make_group_obj(new_group, group_objects)
                    # new_teacher_obj.set_groups(new_group)
                    # new_group_obj.teachers[new_subject] = new_teacher_obj
                else:
                    break
            continue
        if get_data == "wychowawca":
            full_name = str.title(input("Imię Nazwisko: ").strip())
            new_educator_obj = Educator(full_name)
            while 1:
                new_group = str.lower(input("Klasa: ").strip())
                if new_group:
                    groups_dict.update(make_group(new_group, groups_dict))
                    groups_dict[new_group]["educator"] = full_name
                    # new_group_obj = make_group_obj(new_group, group_objects)
                    # new_educator_obj.set_groups(new_group)
                    # new_group_obj.educator = new_educator_obj
                else:
                    break
            continue


# funkcja zwracająca dane przy 2. argumencie argv
def print_info_argv2(argv2, dict_name):
    if argv2 in dict_name:
        if_class(argv2, dict_name)
        # group_objects[get_data].if_class_obj()
    else:
        print("Brak podanej klasy w bazie danych!")


# funkcja zwracająca dane przy 2. 3. 4. argumencie argv
def print_info_argv234(argv234, dict_name):
    if argv234 in dict_name:
        # for key in dict_name:
        if_pupil(argv234, dict_name)
        # group_objects[full_name].if_pupil_obj()
    elif argv234 in dict_name:
        # for key in dict_name:
        if_teacher(argv234, dict_name)
        # group_objects[full_name].if_teacher_obj()
    elif argv234 in dict_name:
        # for key in dict_name:
        if_educator(argv234, dict_name)
        # group_objects[full_name].if_educator_obj()
    else:
        print("Brak podanej osoby w bazie danych!")
