'''
    4. Начните работу над проектом «Склад оргтехники». Создайте класс,
    описывающий склад. А также класс «Оргтехника», который будет базовым
    для классов-наследников. Эти классы — конкретные типы оргтехники
    (принтер, сканер, ксерокс). В базовом классе определите параметры,
    общие для приведённых типов. В классах-наследниках реализуйте параметры,
    уникальные для каждого типа оргтехники.
'''
class OfficeEquipStock:
    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount
        self.dict = {'Name': self.name, 'Amount': self.amount, 'Price': self.price}
        self.stock = []

    '''
       5. Продолжить работу над первым заданием. Разработайте методы,
       которые отвечают за приём оргтехники на склад и передачу в определённое
       подразделение компании. Для хранения данных о наименовании и
       количестве единиц оргтехники, а также других данных, можно использовать
       любую подходящую структуру (например, словарь).
        6. Продолжить работу над вторым заданием. Реализуйте механизм валидации
        вводимых пользователем данных. Например, для указания количества принтеров,
        отправленных на склад, нельзя использовать строковый тип данных.
    '''
    def equip_dict(self):
        try:
            eq_name = input("Enter item's name: ")
            eq_amount = int(input("Enter amount of the item: "))
            eq_price = int(input("Enter the price: "))
            eq_dict = {'Name': eq_name, 'Amount': eq_amount, 'Price': eq_price}
            self.dict.update(eq_dict)
            self.stock.append(self.dict)
            print(self.stock)
        except:
            return f'ERROR'
        return OfficeEquipStock.equip_dict(self)


    # @staticmethod
    # def correct(name, price, amount):
    #     if name.isdigit == True:
    #         return f"Enter a valid name"
    #     elif amount.isdigit == False:
    #         return f"Enter a valid amount"
    #     elif price.isdigit == False:
    #         return f"Enter a valid price"
    #     else:
    #         return ''

    def __str__(self):
        return f'Name: {self.name}, Price: {self.price}, Amount: {self.amount}'

class Printer(OfficeEquipStock):
    def print(self):
        return 'printed'

class Scanner(OfficeEquipStock):
    def scan(self):
        return 'scanned'

class Xerox(OfficeEquipStock):
    def copied(self):
        return 'copied'

printer = Printer('samsung', 5000, 10)
scanner = Scanner('samsung', 1000, 5)
xerox = Xerox('Xerox', 4000, 6)
print(printer.equip_dict())
print(printer.print())

