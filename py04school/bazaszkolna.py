# SZKOLA v1.3
# -*- coding: UTF-8 -*-
import msvcrt, sys
from library.dodatki import clear_screen, title_line
from library.zapis_odczyt_plik_terminal import\
    dict_to_file, dict_to_file_obj, dict_from_file,\
    get_data_from_file, get_data_from_terminal,\
    print_info_argv2, print_info_argv234
from library.klasy_metody_funkcje import groups_dict, group_objects
    # make_group, make_group_obj,\
    # Pupil, Teacher, Educator,\
    # if_class, if_class_obj,\
    # if_pupil, if_pupil_obj,\
    # if_teacher, if_teacher_obj,\
    # if_educator, if_educator_obj

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
pathCast: str = "obsada.txt"
pathBase: str = "baza.txt"
pathBaseObj: str = "baza_obj.txt"
get_data: str = ""

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
clear_screen()
title_line(" Wybór danych wejściowych: ")
print('1) "baza.txt"?\n2) "obsada.txt"?\n')
which_file = int(msvcrt.getch())
if which_file == 1:
    groups_dict.update(dict_from_file(pathBase))
elif which_file == 2:
    groups_dict.update(get_data_from_file(pathCast))
else:
    print("Podano niewłaściwą opcję. Bye!")
    exit()

if len(sys.argv) == 1:
    clear_screen()
    title_line(" (edycja) BAZA-SZKOŁA v1.5 ")
    get_data_from_terminal()

if len(sys.argv) > 1:
    clear_screen()
    title_line(" (przegląd) BAZA-SZKOŁA v1.5 ")
    get_data = str.lower(sys.argv[1])
    while 1:
        if len(sys.argv) == 2:
            print_info_argv2(get_data, groups_dict)
            break
        if len(sys.argv) == 3 or len(sys.argv) == 4:
            full_name = str.title(sys.argv[1]) + " " + str.title(sys.argv[2])
            if len(sys.argv) == 4:
                full_name += " " + str.title(sys.argv[3])
            print_info_argv234(full_name, groups_dict)
            break
        else:
            print("Niewłaściwa liczba argumentów! Bye!")
            break

print("\n\nPress any key to continue...")
msvcrt.getch()
dict_to_file(pathBase, groups_dict)   # save data to <*.txt>
dict_to_file_obj(pathBaseObj, group_objects)   # save data to <*.txt>