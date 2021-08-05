# ACCOUNTANT v2.0_on_classes
# -*- coding: UTF-8 -*-
# Plik 'saldo.py' obsługuje polecenie zmiany salda konta finansowego
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
from acc import manager, actions
from acc_lib.acc_class import *
from acc_lib.acc_extras import *
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #


clearscreen()
line_banner('Procedure "SALDO" was started')
try:
    manager.process()
    manager.post_process("saldo", actions)
except NoActionException('Probably mismatch in operating parameters!\n'
                         'Procedure "SALDO" not performed.'):
    raise
else:
    print('-= The procedure was completed successfully =-')
    print(f'***** Current account status: {manager.account} *****')
    try:
        manager.export_to_file()
    except FileSaveErrorException('Error occurred while writing to the file!'):
        raise
    else:
        print(f'The action was successfully exported to a file.')
    finally:
        manager.close_actions()
