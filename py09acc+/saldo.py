# ACCOUNTANT v2.0_on_classes
# -*- coding: UTF-8 -*-
# Plik 'saldo.py' obsługuje polecenie zmiany salda konta finansowego
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
from acc import director, actions
from acc_lib.acc_extras import *
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #


clearscreen()
line_banner('Procedure "SALDO" was started')

director.process()
director.post_process("saldo", actions)
print('-= The procedure was completed successfully =-')
print(f'***** Current account status: {director.account} *****')

director.export_to_file()
print(f'The action was successfully exported to a file.')

director.close_actions()
