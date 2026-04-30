def calculate_total(items, tax_rate):
    if tax_rate < 0 or tax_rate > 1:
        raise ValueError("Tax rate must be between 0 and 1.")

    total = 0
    for price in items:
        if price < 0:
            raise ValueError("Price cannot be negative, please check it.")
        else:
            total = price + total

    final_amount = total + (total * tax_rate)
    return final_amount
