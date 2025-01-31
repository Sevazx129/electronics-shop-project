import pytest
file = 'items.csv'
from src.item import Item
from src.phone import Phone
from src.keyboard import KeyBoard
from src.item import Item, CSVNotFoundError, InstantiateCSVError
item1 = Item('Samsung', 10000, 23)
Item.pay_rate = 0.8
def test_init():
    assert item1.name == 'Samsung'
    assert item1.price == 10000
    assert item1.quantity == 23

def test_calculate_total_price():
    assert item1.calculate_total_price() == 230000

item1.apply_discount()
def test_apply_discount():
    assert item1.price == 8000

def test_instantiate_from_csv():
    Item.instantiate_from_csv(file)
    assert Item.all[0].name == "Смартфон"
    assert Item.all[0].price == 100
    assert Item.all[0].quantity == 1

def test_string_to_number():
    assert Item.string_to_number('2') == 2
    assert Item.string_to_number('12.98') == 12

def test_Item():
    item = Item("Смартфон", 10000, 20)
    assert repr(item) == "Item('Смартфон', 10000, 20)"
    assert str(item) == 'Смартфон'

def test_Phone():

    # Проверяем новый класс
    phone1 = Phone("iPhone 14", 120000, 5, 2)
    # Проверяем методы
    assert str(phone1) == 'iPhone 14'
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"
    assert phone1.number_of_sim == 2

    # Еще один класс для проверки
    item1 = Item("Смартфон", 10000, 20)
    # Проверяем сложение - правильно
    assert item1 + phone1 == 25
    # Проверяем сложение - нельзя складывать
    assert phone1 + phone1 == 10

    with pytest.raises(ValueError):
        phone1.number_of_sim = 0

def test_keyboard():
    # Создаем экземпляр класса для проверки
    kb = KeyBoard('DarkKD87A', 9600, 5)
    assert str(kb) == "DarkKD87A"
    # Проверяем язык по умолчанию
    assert str(kb.language) == "EN"
    # Проверяем язык
    kb.change_lang()
    assert str(kb.language) == "RU"

    kb.change_lang().change_lang()
    assert str(kb.language) == "RU"

def test_instantiate_csv():
    # Проверка ошибок
    # Тест ошибки "Нет файла"
    with pytest.raises(CSVNotFoundError):
        Item.instantiate_csv('../src/items2.csv')
    # Тест ошибки "файл поврежден"
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_csv('../src/items3.csv')



