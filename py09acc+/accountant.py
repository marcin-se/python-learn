# ACCOUNTANT+ v.1.0
# .
# .
# .

from manager import Reader, Manager, NotEnoughDataException

reader = Reader('in.txt')
manager = Manager(reader)

@manager.action("saldo", 2)
def saldo(manager, rows):
    price = float(rows[0])
    manager.modify_account(price)


@manager.action("zakup", 3)
def zakup(manager, rows):
    name = rows[0]
    price = float(rows[1])
    qty = float(rows[2])
    manager.modify_account(-price*qty)
    manager.modify_stock(name, qty)
try:
   manager.process()
except NotEnoughDataException as exc:
    print(exc)
