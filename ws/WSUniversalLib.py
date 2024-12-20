from enum import IntEnum
import math


class Calculation(object):
    class ProductType(IntEnum):
        Type1 = 1
        Type2 = 2
        Type3 = 3

    class MaterialType(IntEnum):
        Type1 = 1
        Type2 = 2

    product_type_coef = {
        ProductType.Type1: 1.1,
        ProductType.Type2: 2.5,
        ProductType.Type3: 8.43
    }

    material_type_coef = {
        MaterialType.Type1: 0.003,
        MaterialType.Type2: 0.0012
    }

    @staticmethod
    def get_quantity_for_product(
        product_type: int,
        material_type: int,
        count: int,
        width: int,
        length: int,
    ):
        if count <= 0 or width <= 0 or length <= 0:
            return -1
        if product_type not in iter(Calculation.ProductType):
            return -1
        if material_type not in iter(Calculation.MaterialType):
            return -1
        square = width * length
        material_amount = count * square \
            * Calculation.product_type_coef[product_type]
        print(material_amount)
        defect_amount = material_amount \
            * Calculation.material_type_coef[material_type]
        print(defect_amount)
        return math.ceil(material_amount + defect_amount)
