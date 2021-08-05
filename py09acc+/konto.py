# ACCOUNTANT v2.0_on_classes
# -*- coding: UTF-8 -*-
# Plik 'konto.py' zwraca informację o stanie konta finansowego
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
from acc import manager, actions
from acc_lib.acc_class import *
from acc_lib.acc_extras import *
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #


clearscreen()
line_banner('Procedure "KONTO" was started')
try:
    manager.process()
except NoActionException('Probably mismatch in operating parameters!\n'
                         'Procedure "KONTO" not performed.'):
    raise
else:
    print('-= The procedure was completed successfully =-')
    print(f'***** Current account status: {manager.account} *****')
finally:
    manager.close_actions()
