from csv import DictReader

file = 'items.csv'
class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.
        """
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.name}'


    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, add_name: str):
        if len(add_name) >= 20:
            raise Exception('Длина наименования товара превышает 20 символов')
        else:
            self.__name = add_name

    @classmethod
    def instantiate_from_csv(cls, file):
        cls.all.clear()

        with open(file, newline='') as f:
            DictReader_obj = DictReader(f)
            for row in DictReader_obj:
               cls.all.append(cls(row['name'], int(row['price']), int(row['quantity'])))

    @staticmethod
    def string_to_number(line):
        a = float(line)
        return int(a)
