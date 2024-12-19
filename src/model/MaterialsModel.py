from PyQt5.QtSql import QSqlQueryModel
from PyQt5.QtCore import QObject, Qt


class MaterialsModel(QSqlQueryModel):
    def __init__(self, parent: QObject | None = ...) -> None:
        super().__init__(parent)
        self.refresh_data()
        self.setHeaderData(0, Qt.Horizontal, "Превью")
        self.setHeaderData(1, Qt.Horizontal, "Тип")
        self.setHeaderData(2, Qt.Horizontal, "Наименование")
        self.setHeaderData(3, Qt.Horizontal, "Остаток")
        self.setHeaderData(4, Qt.Horizontal, "Минимальное количество")
        self.setHeaderData(5, Qt.Horizontal, "Поставщики")

    def refresh_data(self):
        sql = '''
            select
                m.id,
                mt.name as material_type,
                m.name,
                m.inventory,
                m.min_amount,
                (
                select string_agg(s.name, ', ')
                from materials_suppliers ms
                    join suppliers s
                        on s.id = ms.supplier_id
                where ms.material_id = m.id) as suppliers,
                m.image
            from materials m
                join material_types as mt
                    on mt.id = m.type_id
        '''
        self.setQuery(sql)
