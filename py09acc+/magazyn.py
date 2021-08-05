# ACCOUNTANT v2.0_on_classes
# -*- coding: UTF-8 -*-
# Plik 'magazyn.py' zwraca informację o stanach magazynowych
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
from acc import manager, actions
from acc_lib.acc_class import *
from acc_lib.acc_extras import *
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #


clearscreen()
line_banner('Procedure "MAGAZYN" was started')
try:
    manager.process()
    manager.post_process("magazyn", actions)
except NoActionException('Probably mismatch in operating parameters!\n'
                         'Procedure "MAGAZYN" not performed.'):
    raise
else:
    print('-= The procedure was completed successfully =-')
finally:
    manager.close_actions()
