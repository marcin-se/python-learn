# ACCOUNTANT v2.0_on_classes
# -*- coding: UTF-8 -*-
# Plik 'przeglad.py' zwraca informacje o archiwalnych transakcjach
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
from acc import director, actions
from acc_lib.acc_extras import *
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #


clearscreen()
line_banner('Procedure "PRZEGLAD" was started')

director.process()
director.post_process("przegląd", actions)
print('-= The procedure was completed successfully =-')

director.close_actions()
