# ACCOUNTANT v2.0_on_classes
# -*- coding: UTF-8 -*-
# Plik 'przeglad.py' zwraca informacje o archiwalnych transakcjach
import os
import sys
from sys import stdout
from acc_lib.acc_additives import cls, title_line
from acc_lib.acc_classes import Accountant
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
err_argv = '\n===== File does not exist or wrong number of arguments! =====\n'
cls()
title_line(' Program księgowo-magazynowy "przeglad.py" ')
logs_file = sys.argv[1]
command_list: list = []

while True:
    if not os.path.exists(logs_file) or len(sys.argv) != 4:
        stdout.write(err_argv)
        break
    else:
        stockStatus = Accountant()
        stockStatus.about_logs(int(sys.argv[2]), int(sys.argv[3]))
