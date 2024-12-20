from PyQt5.QtSql import QSqlQueryModel, QSqlQuery
from PyQt5.QtCore import QObject, Qt
from model.Material import Material


class MaterialsModel(QSqlQueryModel):
    def __init__(self, parent: QObject | None = ...) -> None:
        super().__init__(parent)
        self.refresh_data()
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

    def get_row_fields(self, rowId):
        material = Material()
        material.id = self.data(self.index(rowId, 0))
        material.type = self.data(self.index(rowId, 1))
        material.name = self.data(self.index(rowId, 2))
        material.inventory = self.data(self.index(rowId, 3))
        material.min_amount = self.data(self.index(rowId, 4))
        material.suppliers = self.data(self.index(rowId, 5))
        material.image = self.data(self.index(rowId, 6))
        return material

    def get_types(self):
        sel_query = QSqlQuery()
        sql = '''
            select id, name
            from material_types
            order by name;
        '''
        sel_query.exec_(sql)
        types = {}
        if sel_query.isActive():
            sel_query.first()
            while sel_query.isValid():
                types[sel_query.value('id')] = sel_query.value('name')
                sel_query.next()
        return types

    def get_units(self):
        sel_query = QSqlQuery()
        sql = '''
            select id, name
            from units
            order by name;
        '''
        sel_query.exec_(sql)
        units = {}
        if sel_query.isActive():
            sel_query.first()
            while sel_query.isValid():
                units[sel_query.value('id')] = sel_query.value('name')
                sel_query.next()
        return units
