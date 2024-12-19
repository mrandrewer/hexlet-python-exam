from PyQt5.QtSql import (
    QSqlTableModel,
    QSqlQuery,
    QSqlRecord
)
from PyQt5.QtCore import (
    QAbstractItemModel,
    QModelIndex,
    QObject,
    QSize,
    pyqtSlot,
    Qt,
    QRect,
)
from PyQt5.QtGui import QPainter, QFontMetrics
from PyQt5.QtWidgets import (
    QTableView,
    QWidget,
    QMessageBox,
    QDialog,
    QLabel,
    QLineEdit,
    QTextEdit,
    QComboBox,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QStyledItemDelegate,
    QStyleOptionViewItem,
    QApplication,
    QStyle
)

from model.Material import Material


class MaterialsItemDelegate(QStyledItemDelegate):

    def __init__(self, parent: QObject | None = ...) -> None:
        super().__init__(parent)

    def sizeHint(self, option, index):
        fm = QFontMetrics(option.font)
        return QSize(150, fm.height() * 5 + fm.leading())

    def paint(
            self,
            painter: QPainter | None,
            option: QStyleOptionViewItem,
            index: QModelIndex) -> None:
        material: Material = index.model().get_row_fields(index.row())
        print(material)
        descrRect = QRect(option.rect)
        painter.drawText(descrRect, Qt.AlignLeading, material.name)
