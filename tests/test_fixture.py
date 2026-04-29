import pytest

@pytest.fixture
def setup():
    print("Open Browser")
    print("Login")
    print("Browse Products")
    yield
    print("Logout")
    print("Close Browser")


def test_add_item_cart(setup):
    print("Item added to cart")


def test_remove_item_cart():
    print("Item removed from cart")