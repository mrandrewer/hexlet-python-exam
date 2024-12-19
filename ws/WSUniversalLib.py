from enum import Enum
import math


class WSUniversal(object):
    class ProductType(Enum):
        Type1 = 1
        Type2 = 2
        Type3 = 3

    class MaterialType(Enum):
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
    def calculate_materials(
        count: int,
        width: int,
        length: int,
        product_type: ProductType,
        material_type: MaterialType,
    ):
        if count <= 0 or width <= 0 or length <= 0:
            return -1
        square = width * length
        material_amount = count * square \
            * WSUniversal.product_type_coef[product_type]
        print(material_amount)
        defect_amount = material_amount \
            * WSUniversal.material_type_coef[material_type]
        print(defect_amount)
        return math.ceil(material_amount + defect_amount)
