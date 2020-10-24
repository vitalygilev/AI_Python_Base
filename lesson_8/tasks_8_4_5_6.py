from types import FunctionType
from abc import abstractmethod, ABC


def show_items_menu():
    item_type = 0
    while item_type == 0:
        print(10 * '-')
        print('Select item type:')
        print(10 * '-')
        print(' 1 - Printer.')
        print(' 2 - Copier.')
        print(' 3 - Scanner.')
        print(' 4: Cancel enter.')
        try:
            item_type = int(input("Your choice: "))
            if item_type > 4 or item_type < 1:
                item_type = 0
        except Exception:
            print("Wrong choice! Select 1, 2 or 3!")
            item_type = 0
    return item_type


class TItem:

    def __init__(self, item_=None, quantity=0, address=''):
        self.item = item_
        self.quantity = quantity
        self.address = address

    def input_item(self):
        cur_item = None
        item_type = show_items_menu()
        if item_type != 4:
            if item_type == 1:
                cur_item = TPrinter()
            elif item_type == 2:
                cur_item = TCopier()
            elif item_type == 3:
                cur_item = TScanner()
            if cur_item:
                cur_item.input_good()
                self.item = cur_item
                while self.quantity == 0:
                    try:
                        self.quantity = int(input(f"Enter quantity of {self.item.model}:"))
                        if self.quantity <= 0:
                            print("Enter positive quantity!")
                            self.quantity = 0
                            continue
                        self.address = input(f"Enter address of {self.item.model}:")
                    except ValueError as e_2:
                        print("quantity error ", e_2)
                        self.quantity = 0


class TStore:

    def __init__(self, name):
        self.name = name
        self.goods = []

    def get_balance(self):
        return self.goods

    def op_moving(self, info=False):
        if info:
            return 'Move item'
        else:
            try:
                item_number = int(input(f"Enter item number (use 'Show storage's balance' function) {1} to "
                                        f"{len(self.get_balance())} or 0 for exit:"))
                if item_number > 0:
                    move_quantity = int(input(f"Enter quantity of {self.goods[item_number - 1].item.model} to move:"))
                    if move_quantity > self.goods[item_number - 1].quantity:
                        print(f"There is not enough {self.goods[item_number - 1].item.model} to move! "
                              f"There is only {self.goods[item_number - 1].quantity}.")
                    else:
                        self.goods[item_number - 1].quantity -= move_quantity
                        print(f"{move_quantity} of {self.goods[item_number - 1].item.model} successfully moved.")
                    if self.goods[item_number - 1].quantity == 0:
                        del self.goods[item_number - 1]
            except Exception as e_1:
                print("Wrong item number or quantity! ", e_1)

    def op_receiving(self, info=False, new_item=None):
        if info:
            return 'Receive item'
        else:
            if not new_item:
                new_item = TItem()
                new_item.input_item()
            if new_item.item:
                self.goods.append(new_item)

    def op_show_balance(self, info=False):
        if info:
            return "Show storage's balance"
        else:
            for cur_num, cur_item in enumerate(self.get_balance()):
                print(f"{cur_num + 1}: {cur_item.item.model}, quantity: {cur_item.quantity}, "
                      f"address: {cur_item.address}")

    @classmethod
    def available_operations(cls):
        return [x for x, y in cls.__dict__.items() if type(y) == FunctionType and not str(x).find('op_')]


class OfficeEquipment:

    def __init__(self, model='', manufacturer='', country=''):
        self.model = model
        self.manufacturer = manufacturer
        self.country = country

    @abstractmethod
    def input_good(self):
        pass


class TPrinter(OfficeEquipment, ABC):

    def __init__(self, printer_type='', **kwargs):
        super().__init__(**kwargs)
        self.printer_type = printer_type

    def input_good(self):
        self.model = input('Enter model: ')
        self.manufacturer = input('Enter manufacturer: ')
        self.country = input('Enter country: ')
        self.printer_type = input('Enter printer type: ')


class TCopier(OfficeEquipment, ABC):

    def __init__(self, copier_class='', **kwargs):
        super().__init__(**kwargs)
        self.copier_class = copier_class

    def input_good(self):
        self.model = input('Enter model: ')
        self.manufacturer = input('Enter manufacturer: ')
        self.country = input('Enter country: ')
        self.copier_class = input('Enter copier class: ')


class TScanner(OfficeEquipment, ABC):

    def __init__(self, scanner_mode='', **kwargs):
        super().__init__(**kwargs)
        self.scanner_mode = scanner_mode

    def input_good(self):
        self.model = input('Enter model: ')
        self.manufacturer = input('Enter manufacturer: ')
        self.country = input('Enter country: ')
        self.scanner_mode = input('Enter scanner mode: ')


printer1 = TPrinter(model='EPSON L805', manufacturer='EPSON', country='Philippines', printer_type='Jet')
printer2 = TPrinter(model='PANTUM P3300DN', manufacturer='PANTUM', country='China', printer_type='Laser')
printer3 = TPrinter(model='BQ WitBox 2', manufacturer='BQ', country='China', printer_type='3D')

copier1 = TCopier(model='CANON imageRUNNER C3125i', manufacturer='CANON', country='Thailand', copier_class='NFS')
copier2 = TCopier(model='Ricoh Priport DX 2430', manufacturer='Ricoh', country='Japan', copier_class='Risograph')
copier3 = TCopier(model='Panasonic KX-FL423RUВ', manufacturer='Panasonic', country='Japan', copier_class='Fax')

scanner1 = TScanner(model='Xerox Mobile 497N01316', manufacturer='Xerox', country='China', scanner_mode='Handheld')
scanner2 = TScanner(model='EPSON Perfection V19', manufacturer='EPSON', country='Philippines', scanner_mode='Tablet')
scanner3 = TScanner(model='Honeywell Voyager XP', manufacturer='Honeywell', country='China', scanner_mode='Barcode')

store1 = TStore('Main')
store1.op_receiving(False, TItem(printer1, 10, 'A-1-1-1'))
store1.op_receiving(False, TItem(printer2, 20, 'A-1-1-1'))
store1.op_receiving(False, TItem(printer3, 30, 'A-1-1-1'))
store1.op_receiving(False, TItem(copier1, 40, 'A-1-1-1'))
store1.op_receiving(False, TItem(copier2, 50, 'A-1-1-1'))
store1.op_receiving(False, TItem(copier3, 60, 'A-1-1-1'))
store1.op_receiving(False, TItem(scanner1, 70, 'A-1-1-1'))
store1.op_receiving(False, TItem(scanner2, 80, 'A-1-1-1'))
store1.op_receiving(False, TItem(scanner3, 90, 'A-1-1-1'))

menu_items = store1.available_operations()
while True:
    print(10 * '-')
    print('Main menu:')
    print(10 * '-')
    for i, item in enumerate(menu_items):
        cur_op = store1.__getattribute__(item)
        print(f"{i + 1}. {cur_op(True)}")
    print(f"{len(menu_items) + 1}. Quit")
    try:
        menu_item_selected = int(input("Your choice: "))
        if 0 < menu_item_selected <= len(menu_items):
            cur_op = store1.__getattribute__(menu_items[menu_item_selected - 1])
            cur_op(False)
        elif menu_item_selected == len(menu_items) + 1:
            break
    except Exception as e:
        print(f"Wrong choice! Enter 1 to {len(menu_items) + 1} ({e})")
