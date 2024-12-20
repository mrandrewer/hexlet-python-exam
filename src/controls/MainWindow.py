import os
from PyQt5.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QLineEdit,
    QComboBox
)
from PyQt5.QtCore import QSortFilterProxyModel 
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
from controls.MaterialsListView import MaterialsListView
from model.MaterialsModel import MaterialsModel


class MainWindow(QMainWindow):

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setWindowTitle('Список материалов')
        self.create_model()
        widget = QWidget(self)
        main_layout = QVBoxLayout()
        header_layout = QHBoxLayout()
        self.search_box = QLineEdit(parent=widget)
        self.search_box.textChanged.connect(self.on_search_filter_changed)
        header_layout.addWidget(self.search_box)
        self.sort_box = self.create_sort_filter(parent)
        header_layout.addWidget(self.sort_box)
        self.filter_box = self.create_type_filter(widget)
        header_layout.addWidget(self.filter_box)
        main_layout.addLayout(header_layout)
        materials_view = MaterialsListView(self.filter_model, widget)
        main_layout.addWidget(materials_view)
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)
        self.setMinimumSize(700, 500)
        icon_path = os.path.normpath(
            os.path.dirname(
                os.path.dirname(
                    os.path.abspath(__file__)
                )
            ) + "/resources/Большая пачка.png"
        )
        self.setWindowIcon(QIcon(icon_path))
        self.center()

    def center(self):
        frameGm = self.frameGeometry()
        screen = QApplication.desktop() \
            .screenNumber(QApplication.desktop().cursor().pos())
        centerPoint = QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

    def create_model(self):
        self.model = MaterialsModel(self)
        self.filter_model = QSortFilterProxyModel(self)
        self.filter_model.setSourceModel(self.model)

    def create_type_filter(self, parent):
        filter_box = QComboBox(parent)
        types = self.model.get_types()
        filter_box.addItem("Все типы", None)
        for id, name in types.items():
            filter_box.addItem(name, id)
        filter_box.currentIndexChanged.connect(self.on_type_filter_changed)
        return filter_box

    def create_sort_filter(self, parent):
        sort_box = QComboBox(parent)
        sort_box.addItem("Без сортировки", None)
        sort_box.addItem("Наименование (возр.)", 1)
        sort_box.addItem("Наименование (убыв.)", 2)
        sort_box.addItem("Остаток (возр.)", 3)
        sort_box.addItem("Остаток (убыв.)", 4)
        sort_box.addItem("Стоимость (возр.)", 5)
        sort_box.addItem("Стоимость (убыв.)", 6)
        sort_box.currentIndexChanged.connect(self.on_sort_filter_changed)
        return sort_box

    def apply_filter(self):
        search_filter = self.search_box.text()
        type_filter = self.filter_box.currentData()
        sort_type = self.sort_box.currentData()
        self.filter_model.sort

    def on_sort_filter_changed(self, value):
        self.apply_filter()

    def on_type_filter_changed(self, value):
        self.apply_filter()

    def on_search_filter_changed(self, value):
        self.apply_filter()
