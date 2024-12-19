from PyQt5.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QLineEdit,
    QComboBox
)
from Materials import MaterialsListView
from controls.MaterialsWidget import MaterialsWidget
from model.Material import Material


class MainWindow(QMainWindow):

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setWindowTitle('Список материалов')

        widget = QWidget(self)
        main_layout = QVBoxLayout()
        header_layout = QHBoxLayout()
        search_box = QLineEdit(parent=widget)
        header_layout.addWidget(search_box)
        sort_box = QComboBox(parent=widget)
        header_layout.addWidget(sort_box)
        filter_box = QComboBox(parent=widget)
        header_layout.addWidget(filter_box)
        main_layout.addLayout(header_layout)

        material = Material()
        material.type = "Нитки"
        material.name = "Нитки какие-то 2х2"
        material.min_amount = 20
        material.inventory = 100
        material.suppliers = "Рога и копыта"
        material.image = "picture.png"

        materialWidget = MaterialsWidget(material, self)
        main_layout.addWidget(materialWidget)

        materials_view = MaterialsListView(widget)
        main_layout.addWidget(materials_view)
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)
