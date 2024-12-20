from WSUniversalLib import Calculation


def test_success():
    amount = Calculation.get_quantity_for_product(
        3,
        1,
        15,
        20,
        45)
    assert amount == 114147


def test_incorrect_count():
    amount = Calculation.get_quantity_for_product(
        3,
        1,
        -1,
        20,
        45)
    assert amount == -1


def test_incorrect_length():
    amount = Calculation.get_quantity_for_product(
        3,
        1,
        1,
        -20,
        45)
    assert amount == -1


def test_incorrect_product():
    amount = Calculation.get_quantity_for_product(
        5,
        1,
        1,
        20,
        45)
    assert amount == -1
    

def test_incorrect_material():
    amount = Calculation.get_quantity_for_product(
        2,
        -1,
        1,
        20,
        45)
    assert amount == -1