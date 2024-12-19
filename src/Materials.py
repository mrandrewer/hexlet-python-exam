from PyQt5.QtSql import QSqlQueryModel, QSqlQuery
from PyQt5.QtCore import QObject, pyqtSlot, Qt
from PyQt5.QtWidgets import (
    QTableView,
    QWidget,
    QMessageBox,
    QDialog,
    QLabel,
    QLineEdit,
    QTextEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout
)


class MaterialsModel(QSqlQueryModel):
    def __init__(self, parent: QObject | None = ...) -> None:
        super().__init__(parent)
        self.refresh_data()

    def refresh_data(self):
        sql = '''
            select
                m.image,
                mt.name as material_type,
                m.name,
                m.inventory,
                m.min_amount,
                (
                select string_agg(s.name, ', ')
                from materials_suppliers ms
                    join suppliers s
                        on s.id = ms.supplier_id
                where ms.material_id = m.id) as suppliers
            from materials m
                join material_types as mt
                    on mt.id = m.type_id
        '''
        self.setQuery(sql)


class MaterialsView(QTableView):
    def __init__(self, parent: QWidget | None = ...) -> None:
        super().__init__(parent)
        model = MaterialsModel(self)
        self.setModel(model)
        self.setSelectionBehavior(self.SelectRows)
