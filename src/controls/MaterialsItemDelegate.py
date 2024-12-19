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
from PyQt5.QtGui import QPainter, QFontMetrics, QFont
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
        title = f"{material.type} | {material.name}"
        min_amount = f"Минимальное количество: {material.min_amount}шт"
        suppliers = f"Поставщики: {material.suppliers}"

        title_font = QFont(option.font)
        font_metrics = QFontMetrics(title_font)
        padding = font_metrics.lineSpacing() // 2

        title_rect = QRect(option.rect)
        title_rect.setLeft(title_rect.left() + padding)
        title_rect.setTop(title_rect.top() + padding)
        title_rect.setRight(title_rect.right() - padding)
        title_rect.setHeight(font_metrics.lineSpacing())

        amount_rect = QRect(option.rect)
        amount_rect.setLeft(amount_rect.left() + padding)
        amount_rect.setTop(title_rect.bottom())
        amount_rect.setRight(amount_rect.right() - padding)
        amount_rect.setHeight(font_metrics.lineSpacing())

        supplier_rect = QRect(option.rect)
        supplier_rect.setLeft(supplier_rect.left() + padding)
        supplier_rect.setTop(amount_rect.bottom())
        supplier_rect.setRight(supplier_rect.right() - padding)
        supplier_rect.setHeight(font_metrics.lineSpacing())

        painter.drawText(amount_rect, Qt.AlignLeading, min_amount)
        painter.drawText(title_rect, Qt.AlignLeading, title)
        painter.drawText(supplier_rect, Qt.AlignLeading, suppliers)
