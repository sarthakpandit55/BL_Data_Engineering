import pytest
import source.E_Commerce as ECommerce

def test_valid_item_price():
    items = [100, 0, 200]
    tax_rate = 0.5

    result = ECommerce.calculate_total(items, tax_rate)

    assert result == 450

def test_negative_price():
    items = [-100, 0, 200]
    tax_rate = 0.5

    with pytest.raises(ValueError, match="Price cannot be negative."):
        ECommerce.calculate_total(items, tax_rate)


def test_invalid_tax_rate():
    items = [100, 200, 300]
    tax_rate = 2

    with pytest.raises(ValueError, match="Tax rate must be between 0 and 1."):
        ECommerce.calculate_total(items, tax_rate)
