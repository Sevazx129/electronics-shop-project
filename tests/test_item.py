import pytest
file = 'items.csv'
from src.item import Item
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

def test_item():
    item = Item("Смартфон", 10000, 20)
    assert repr(item) == "Item('Смартфон', 10000, 20)"
    assert str(item) == 'Смартфон'
