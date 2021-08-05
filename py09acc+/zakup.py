# ACCOUNTANT v2.0_on_classes
# -*- coding: UTF-8 -*-
# Plik 'zakup.py' obsługuje zakupy magazynowe asortymentu
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
from acc import manager, actions
from acc_lib.acc_class import *
from acc_lib.acc_extras import *
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #


clearscreen()
line_banner('Procedure "ZAKUP" was started')
try:
    manager.process()
    manager.post_process("zakup", actions)
except NoActionException('Probably mismatch in operating parameters!\n'
                         'Procedure "ZAKUP" not performed.'):
    raise
else:
    print('-= The procedure was completed successfully =-')
    try:
        manager.export_to_file()
    except FileSaveErrorException('Error occurred while writing to the file!'):
        raise
    else:
        print('-= The action was successfully exported to a file =-')
    finally:
        manager.close_actions()
