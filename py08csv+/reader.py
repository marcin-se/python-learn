# CSV+ v1.0                                      (R) Powered by nobody & nothing
# -*- coding: UTF-8 -*-                                                        #
# Skrypt z odczytu CSV, zmiany danych i zapisu w pliku JSON lub PICKLE         #
'''
- sprawdź, czy podany plik <src> (lub ścieżka) istnieje
- jeżeli nie istnieje, wypisz komunikat i wyświetl zawartość katalogu
- jeżeli istnieje, to odczytaj plik, zmień dane i wyświetl je, a
- następnie zapisz te dane w pliku docelowym <dst>
- w takim formacie, jak rozszerzenie pliku (np. *.pickle)
'''
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
import os

'''EXAMPLE1>>>  reader.py <<src>> <<dst>> <<change1>>                        '''
'''EXAMPLE1>>>  reader.py file.csv file.json 16,4,201                        '''
'''EXAMPLE1>>>  reader.py file.csv file.pickle 16,4,201                      '''
'''EXAMPLE2>>>  reader.py <<src>> <<dst>> <<change1>> <<change2>> <<...>>    '''
'''EXAMPLE2>>>  reader.py file.csv file.json 16,4,201 4,2,19.2 22,1,obraz    '''
'''EXAMPLE2>>>  reader.py file.csv file.pickle 16,4,201 4,2,19.2             '''
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
from csv_lib.csv_cls import *
from sys import stdout, stderr
import msvcrt
import time
import sys
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#

src_filename, dst_filename, files_dirs = "", "", os.listdir()
changes_list: list = []

clear_screen()
while True:
    abc = ModifyFile()
    try:
        if len(sys.argv) <= 3:
            stderr.write('\nNo data to change!\n')
            break
        if len(sys.argv) > 3:
            src_filename = str(sys.argv[1])
            dst_filename = str(sys.argv[2])
            changes_list = sys.argv[3:]
            if abc.open_file(src_filename):
                for one_change in changes_list:
                    stdout.write('\n<<< List of changes to the '
                                 'file content: >>>\n')
                    abc.print_argvchanges(one_change)
                    abc.change_csvdata(one_change)
                    time.sleep(0.2)
                abc.save_file(dst_filename)
            else:
                break
            stdout.write('\n<<< File contents after changes: >>>\n')
            abc.print_data()
            break
    except NoFileException:
        print(f'Error: Wrong path or source file does not exist!')
        if len(files_dirs) != 0:
            print(f'(Current directory: {os.getcwd()}\\)\n'
                  f'There are here {len(files_dirs)}. files or directories:')
            abc.listing_files(files_dirs)
        break
    except DirectoryWithoutFilesException:
        print(f'Error: Current directory does not contain files')
        break
    except OpenErrorExtentionException:
        print(f'Error: Wrong source file extension!')
        break
    except SaveErrorExtentionException:
        print(f'Error: Wrong destionation file extension!')
        break
    except IncorrectDataException:
        print(f'Error: Incorrect data references!')
        break

time.sleep(0.5)
stdout.write('\n<<< Press any key... >>>\n\n')
if msvcrt.getch():
    clear_screen()
