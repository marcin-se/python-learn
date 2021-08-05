# ACCOUNTANT v2.0_on_classes
# -*- coding: UTF-8 -*-
# Plik 'zakup.py' obsługuje zakupy magazynowe asortymentu
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
from acc import director, actions
from acc_lib.acc_extras import *
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #


clearscreen()
line_banner('Procedure "ZAKUP" was started')

director.process()
director.post_process("zakup", actions)
print('-= The procedure was completed successfully =-')

director.export_to_file()
print('-= The action was successfully exported to a file =-')

director.close_actions()
