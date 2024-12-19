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

from model.Material import Material


class MaterialsWidget(QWidget):
    def __init__(self, material: Material, parent=None):
        super(MaterialsWidget, self).__init__(parent)
        title = f"{material.type} | {material.name}"
        inventory = f"Остаток: {material.min_amount} шт"
        min_amount = f"Минимальное количество: {material.min_amount} шт"

        hbox = QHBoxLayout()
        right_box = QVBoxLayout()
        
        title_box = QHBoxLayout()
        title_label = QLabel(title)
        title_label.setObjectName("title")
        title_box.addWidget(title_label)
        title_box.addStretch()
        inventory_label = QLabel(inventory)
        inventory_label.setObjectName("inventory")
        title_box.addWidget(inventory_label)
        right_box.addLayout(title_box)

        min_amount_label = QLabel(min_amount)
        min_amount_label.setObjectName("min_amount")
        right_box.addWidget(min_amount_label)

        suppliers_box = QHBoxLayout()
        suppliers_title_label = QLabel("Поставщики: ")
        suppliers_title_label.setObjectName("suppiers_title")
        suppliers_box.addWidget(suppliers_title_label)
        suppliers_label = QLabel(material.suppliers)
        suppliers_label.setObjectName("suppliers")
        suppliers_box.addWidget(suppliers_label)
        suppliers_box.addStretch()
        right_box.addLayout(suppliers_box)

        hbox.addLayout(right_box)
        self.setLayout(hbox)
