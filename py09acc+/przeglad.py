# ACCOUNTANT v2.0_on_classes
# -*- coding: UTF-8 -*-
# Plik 'przeglad.py' zwraca informacje o archiwalnych transakcjach
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
from acc import manager, actions
from acc_lib.acc_class import *
from acc_lib.acc_extras import *
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #


clearscreen()
line_banner('Procedure "PRZEGLĄD" was started')
try:
    manager.process()
    manager.post_process("przegląd", actions)
except NoActionException('Probably mismatch in operating parameters!\n'
                         'Procedure "PRZEGLĄD" not performed.'):
    raise
else:
    print('-= The procedure was completed successfully =-')
finally:
    manager.close_actions()
