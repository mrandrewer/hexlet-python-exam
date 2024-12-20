from PyQt5.QtWidgets import (
    QWidget,
    QListView
)

from controls.MaterialsItemDelegate import MaterialsItemDelegate
from model.MaterialsModel import MaterialsModel


class MaterialsListView(QListView):
    def __init__(self, parent: QWidget | None = ...) -> None:
        super().__init__(parent)
        model = MaterialsModel(self)
        self.setModel(model)
        self.setItemDelegateForRow
        self.setSelectionBehavior(self.SelectRows)
        self.setItemDelegate(MaterialsItemDelegate(self))
