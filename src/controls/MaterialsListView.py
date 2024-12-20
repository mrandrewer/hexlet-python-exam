from PyQt5.QtWidgets import (
    QWidget,
    QListView
)

from controls.MaterialsItemDelegate import MaterialsItemDelegate


class MaterialsListView(QListView):
    def __init__(self, model, parent: QWidget | None = ...) -> None:
        super().__init__(parent)
        self.setModel(model)
        self.setItemDelegateForRow
        self.setSelectionBehavior(self.SelectRows)
        self.setItemDelegate(MaterialsItemDelegate(self))
