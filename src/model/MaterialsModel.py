import decimal
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
        self.setHeaderData(6, Qt.Horizontal, "Стоимость")

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
                price,
                m.image,
                m.type_id,
                m.package_amount,
                m.unit_id
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
        material.price = self.data(self.index(rowId, 6))
        material.image = self.data(self.index(rowId, 7))
        material.type_id = self.data(self.index(rowId, 8))
        material.package_amount = self.data(self.index(rowId, 9))
        material.unit_id = self.data(self.index(rowId, 10))
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

    def add(self, material: Material):
        add_query = QSqlQuery()
        sql = '''
            INSERT INTO materials (name, type_id, price, inventory, min_amount, package_amount, unit_id ) VALUES
            ( :name, :type_id, :price, :inventory, :min_amount, :package_amount, :unit_id);
        '''
        add_query.prepare(sql)
        add_query.bindValue(':name', material.name[:50])
        add_query.bindValue(':type_id', material.type_id)
        add_query.bindValue(':price', material.price)
        add_query.bindValue(':inventory', material.inventory)
        add_query.bindValue(':min_amount', material.min_amount)
        add_query.bindValue(':package_amount', material.package_amount)
        add_query.bindValue(':unit_id', None if material.unit_id < 0 else material.unit_id)
        add_query.exec_()
        self.refresh_data()

    def update(self, material: Material):
        add_query = QSqlQuery()
        sql = '''
            update materials set
                name = :name,
                type_id = :type_id,
                price = :price,
                inventory = :inventory,
                min_amount = :min_amount,
                package_amount = :package_amount,
                unit_id = :unit_id
            where id = :id;
        '''
        add_query.prepare(sql)
        add_query.bindValue(':id', material.id)
        add_query.bindValue(':name', material.name[:50])
        add_query.bindValue(':type_id', material.type_id)
        add_query.bindValue(':price', material.price)
        add_query.bindValue(':inventory', material.inventory)
        add_query.bindValue(':min_amount', material.min_amount)
        add_query.bindValue(':package_amount', material.package_amount)
        add_query.bindValue(':unit_id', None if material.unit_id < 0 else material.unit_id)
        add_query.exec_()
        self.refresh_data()
