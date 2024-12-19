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
            select *
            from materials;
        '''
        self.setQuery(sql)


class MaterialsView(QTableView):
    def __init__(self, parent: QWidget | None = ...) -> None:
        super().__init__(parent)
        model = MaterialsModel(self)
        self.setModel(model)
        self.setSelectionBehavior(self.SelectRows)
