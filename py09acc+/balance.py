# ACCOUNTANT v2.0_on_classes
# -*- coding: UTF-8 -*-
# Plik 'saldo.py' obsługuje polecenie zmiany salda konta finansowego
import os
import sys
from sys import stdout
from acc_lib.acc_additives import cls, title_line
from acc_lib.acc_classes import Accountant
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
err_argv = '\n===== File does not exist or wrong number of arguments! =====\n'
cls()
title_line(' Program księgowo-magazynowy "saldo.py" ')
logs_file = sys.argv[1]
command_list: list = []

while True:
    if not os.path.exists(logs_file) or len(sys.argv) != 4:
        stdout.write(err_argv)
        break
    else:
        stockStatus = Accountant()
        command_list.append(['saldo', int(sys.argv[2]), str(sys.argv[3])])
        stockStatus.change_budget(int(sys.argv[2]), str(sys.argv[3]))
        stockStatus.write_to_file(logs_file, command_list)
