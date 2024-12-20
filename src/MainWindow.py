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
from PyQt5.QtWidgets import QApplication


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
        materials_view = MaterialsListView(widget)
        main_layout.addWidget(materials_view)
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)
        self.setMinimumSize(700, 500)
        self.center()

    def center(self):
        frameGm = self.frameGeometry()
        screen = QApplication.desktop() \
            .screenNumber(QApplication.desktop().cursor().pos())
        centerPoint = QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())
