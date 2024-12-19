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
    QHBoxLayout,
    QListView
)

from controls.MaterialsItemDelegate import MaterialsItemDelegate
from model.MaterialsModel import MaterialsModel


class MaterialsView(QTableView):
    def __init__(self, parent: QWidget | None = ...) -> None:
        super().__init__(parent)
        model = MaterialsModel(self)
        self.setModel(model)
        self.setSelectionBehavior(self.SelectRows)


class MaterialsListView(QListView):
    def __init__(self, parent: QWidget | None = ...) -> None:
        super().__init__(parent)
        model = MaterialsModel(self)
        self.setModel(model)
        self.setItemDelegateForRow
        self.setSelectionBehavior(self.SelectRows)
        self.setItemDelegate(MaterialsItemDelegate(self))
