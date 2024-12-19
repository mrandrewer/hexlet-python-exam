from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QTextEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QListView
)
from PyQt5.QtSql import QSqlRecord


class MaterialsWidget(QWidget):
    def __init__(self, material_type, name, parent=None):
        super(MaterialsWidget, self).__init__(parent)

        hbox = QHBoxLayout()
        hbox.addWidget(QLabel(material_type))
        hbox.addWidget(QLabel(name))
        self.setLayout(hbox)
