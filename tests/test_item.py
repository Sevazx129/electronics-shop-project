import pytest
from src.item import Item
item1 = Item('Samsung', 10000, 23)
Item.pay_rate = 0.8
def test_init():
    assert item1.name == 'Samsung'
    assert item1.price == 10000
    assert item1.quantity == 23

def test_calculate_total_price():
    assert item1.calculate_total_price() == 230000

def test_apply_discount():
    assert item1.apply_discount() == 8000
