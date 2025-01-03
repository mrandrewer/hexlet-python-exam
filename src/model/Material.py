import decimal


class Material:
    id: int
    type_id: int
    type: str
    name: str
    inventory: int
    min_amount: int
    suppliers: str
    image: str
    price: decimal
    package_amount: int
    unit_id: int
