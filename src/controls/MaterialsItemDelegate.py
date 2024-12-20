from PyQt5.QtCore import (
    QModelIndex,
    QObject,
    QSize,
)
from PyQt5.QtGui import QPainter, QFontMetrics
from PyQt5.QtWidgets import (
    QStyledItemDelegate,
    QStyleOptionViewItem,
)
from controls.MaterialsWidget import MaterialsWidget
from model.Material import Material


class MaterialsItemDelegate(QStyledItemDelegate):

    def __init__(self, parent: QObject | None = ...) -> None:
        super().__init__(parent)
        self.widget = MaterialsWidget()

    def sizeHint(self, option, index):
        fm = QFontMetrics(option.font)
        return QSize(150, fm.height() * 7 + fm.leading())

    def paint(
            self,
            painter: QPainter | None,
            option: QStyleOptionViewItem,
            index: QModelIndex) -> None:
        material: Material = index.model() \
            .sourceModel().get_row_fields(index.row())
        self.widget.setMaterial(material)
        self.widget.resize(option.rect.size())
        self.widget.render(
            painter,
            self.parent().geometry().topLeft() + option.rect.topLeft())
