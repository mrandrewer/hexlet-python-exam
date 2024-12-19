from WSUniversalLib import WSUniversal


def test_success():
    amount = WSUniversal.calculate_materials(
        15,
        20,
        45,
        WSUniversal.ProductType.Type3,
        WSUniversal.MaterialType.Type1)
    assert amount == 114147
