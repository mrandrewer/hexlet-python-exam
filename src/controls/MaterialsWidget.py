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
    def __init__(self, parent=None):
        super(MaterialsWidget, self).__init__(parent)
        self.material_box = QWidget(self)
        self.material_box.setObjectName("material_box")
        hbox = QHBoxLayout()
        image_view = QLabel()
        image_view.setObjectName("image")
        hbox.addWidget(image_view)

        right_box = QVBoxLayout()
        title_box = QHBoxLayout()
        title_label = QLabel()
        title_label.setObjectName("title")
        title_box.addWidget(title_label)
        title_box.addStretch()
        inventory_label = QLabel()
        inventory_label.setObjectName("inventory")
        title_box.addWidget(inventory_label)
        right_box.addLayout(title_box)

        min_amount_label = QLabel()
        min_amount_label.setObjectName("min_amount")
        right_box.addWidget(min_amount_label)

        suppliers_box = QHBoxLayout()
        suppliers_title_label = QLabel("Поставщики:")
        suppliers_title_label.setObjectName("suppiers_title")
        suppliers_box.addWidget(suppliers_title_label, 0)
        suppliers_label = QLabel()
        suppliers_label.setObjectName("suppliers")
        suppliers_label.setWordWrap(True)
        suppliers_box.addWidget(suppliers_label, 1)
        right_box.addLayout(suppliers_box)

        hbox.addLayout(right_box)
        self.material_box.setLayout(hbox)

        outer_box = QHBoxLayout()
        outer_box.addWidget(self.material_box)
        self.setLayout(outer_box)

        self.setStyleSheet("""
            MaterialsWidget {
                background-color:white;
                padding: 0;
            }
            #material_box {
                margin: 0;
                border: 1px solid black;
                background-color:white;
            }
            #material_box_min {
                margin: 0;
                border: 1px solid black;
                background-color: #f19292;
            }
            #material_box_max {
                margin: 0;
                border: 1px solid black;
                background-color: #ffba01;
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
                text-align: left;
            }
        """)
        self.image_view = image_view
        self.title_label = title_label
        self.inventory_label = inventory_label
        self.min_amount_label = min_amount_label
        self.suppliers_label = suppliers_label

    def setMaterial(self, material: Material):
        title = f"{material.type} | {material.name}"
        inventory = f"Остаток: {material.inventory} шт"
        min_amount = f"Минимальное количество: {material.min_amount} шт"
        image_name = "/picture.png" \
            if material.image == '' \
            else material.image.replace('\\', '/')
        image_path = os.path.normpath(
            os.path.dirname(
                os.path.dirname(
                    os.path.abspath(__file__)
                )
            ) + "/resources" + image_name
        )
        self.title_label.setText(title)
        self.inventory_label.setText(inventory)
        self.min_amount_label.setText(min_amount)
        self.suppliers_label.setText(material.suppliers)
        self.image_view.setPixmap(
            QPixmap(image_path).scaled(80, 80, Qt.KeepAspectRatio)
        )
        if material.inventory < material.min_amount:
            self.material_box.setObjectName("material_box_min")
        elif material.inventory > material.min_amount * 3:
            self.material_box.setObjectName("material_box_max")
        else:
            self.material_box.setObjectName("material_box")
        self.setStyleSheet(self.styleSheet())
