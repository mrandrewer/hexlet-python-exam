import os
from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
)
from PyQt5.QtGui import (
    QPixmap
)
from PyQt5.QtCore import Qt

from model.Material import Material


class MaterialsWidget(QWidget):
    def __init__(self, material: Material, parent=None):
        super(MaterialsWidget, self).__init__(parent)
        title = f"{material.type} | {material.name}"
        inventory = f"Остаток: {material.min_amount} шт"
        min_amount = f"Минимальное количество: {material.min_amount} шт"
        image_path = os.path.dirname(
            os.path.dirname(
                os.path.abspath(__file__)
            )
        ) + "/resources/" + material.image

        material_box = QWidget(self)
        material_box.setObjectName("material_box")
        hbox = QHBoxLayout()
        image_view = QLabel()
        image_view.setObjectName("image")
        print(image_path)
        image_view.setPixmap(
            QPixmap(image_path).scaled(80, 80, Qt.KeepAspectRatio)
        )
        hbox.addWidget(image_view)

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
        suppliers_title_label = QLabel("Поставщики:")
        suppliers_title_label.setObjectName("suppiers_title")
        suppliers_box.addWidget(suppliers_title_label)
        suppliers_label = QLabel(material.suppliers)
        suppliers_label.setObjectName("suppliers")
        suppliers_label.setWordWrap(True)
        suppliers_box.addWidget(suppliers_label)
        suppliers_box.addStretch()
        right_box.addLayout(suppliers_box)

        hbox.addLayout(right_box)
        material_box.setLayout(hbox)

        outer_box = QHBoxLayout()
        outer_box.addWidget(material_box)
        self.setLayout(outer_box)

        self.setStyleSheet("""
            #material_box{
                border: 1px solid black;
            }
            QLabel {
                font: Verdana;
            }
            QLabel#title{
                font-size: 14pt;
                text-align: left;
            }
            QLabel#suppiers_title{
                font-weight:600;
            }
        """)
