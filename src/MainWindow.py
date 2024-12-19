from PyQt5.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QLineEdit,
    QComboBox
)


class MainWindow(QMainWindow):

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setWindowTitle('Список материалов')

        widget = QWidget(self)
        main_layout = QVBoxLayout()
        header_layout = QHBoxLayout()
        search_box = QLineEdit(parent=self)
        header_layout.addWidget(search_box)
        sort_box = QComboBox(parent=self)
        header_layout.addWidget(sort_box)
        filter_box = QComboBox(parent=self)
        header_layout.addWidget(filter_box)
        main_layout.addChildLayout(header_layout)
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)
