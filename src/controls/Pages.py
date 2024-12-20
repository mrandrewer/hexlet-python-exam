from PyQt5.QtWidgets import QWidget, QHBoxLayout
from controls.PageLink import PageLink
from PyQt5.QtCore import pyqtSignal


class Pages(QWidget):

    pageChanged = pyqtSignal([int])

    def __init__(self, page_count, parent=None):
        super().__init__(parent)
        self.page_count = page_count
        self.cur_page = 1
        self.update_widgets()

    def update_widgets(self):
        self.setUpdatesEnabled(False)
        pagination_layout = QHBoxLayout(self)
        prevPageLink = PageLink(
            "<",
            self.cur_page - 1 if self.cur_page > 1 else 1,
            False,
            parent=self)
        pagination_layout.addWidget(prevPageLink)
        for i in range(1, self.page_count + 1):
            page_link = PageLink(str(i), i, self.cur_page == i, parent=self)
            pagination_layout.addWidget(page_link)
            page_link.clicked.connect(self.switch_page)
        nextPageLink = PageLink(
            ">",
            self.cur_page + 1 if self.cur_page < self.page_count else self.page_count,
            False,
            parent=self)
        pagination_layout.addWidget(nextPageLink)
        self.setLayout(pagination_layout)
        self.setUpdatesEnabled(True)

    def switch_page(self, page_num):
        self.pageChanged.emit(page_num)
