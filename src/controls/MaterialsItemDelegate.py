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
    Qt
)
from PyQt5.QtGui import QPainter
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

from controls.MaterialsWidget import MaterialsWidget


class MaterialsItemDelegate(QStyledItemDelegate):

    def __init__(self, parent: QObject | None = ...) -> None:
        super().__init__(parent)

    def paint(
            self,
            painter: QPainter | None,
            option: QStyleOptionViewItem,
            index: QModelIndex) -> None:

        record = index.data()
        print(record)

        QApplication \
            .style() \
            .drawControl(QStyle.CE_ItemViewItem, new_option, painter)