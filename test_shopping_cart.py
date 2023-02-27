from shopping_cart import ShoppingCart
from data_base_empty_pattern import ItemDataBase
import pytest
from unittest.mock import Mock


@pytest.fixture
def cart():
    # All set-up lines that not need to be copied X times in all test functions
    cart = ShoppingCart(5)
    return cart

def test_adding_item_into_cart(cart):
    assert cart.size() == 0
    item = 'apple'
    cart.add('apple')
    assert cart.size() == 1

def test_if_item_in_cart(cart):
    item = 'apple'
    cart.add(item)
    assert 'apple' in cart.get_items()

def test_max_size_of_cart(cart):
    item = 'apple'

    for _ in range(5):
        cart.add(item)

    # If OverflowError exception occur then test will PASS, if exception does NOT occur then test will FAIL
    with pytest.raises(OverflowError):
        cart.add(item)

def test_if_cart_can_return_total_price(cart):
    cart.add('apple')
    cart.add('orange')

    price_map = {'apple': 1, 'orange': 2}

    assert cart.get_total_price(price_map) == 3

def test_if_cart_can_return_total_price_with_mock(cart):
    cart.add('apple')
    cart.add('orange')

    item_data_base = ItemDataBase()

    def mock_get_item(item: str) -> float:
        if item == 'apple':
            return 1.0
        if item == 'orange':
            return 2.0

    #item_data_base.get = Mock(return_value=1.0)
    item_data_base.get = Mock(side_effect=mock_get_item)

    assert cart.get_total_price(item_data_base) == 3





