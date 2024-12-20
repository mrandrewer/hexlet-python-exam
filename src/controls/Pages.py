from PyQt5.QtWidgets import QWidget, QHBoxLayout
from PyQt5.QtCore import pyqtSignal
from controls.PageLink import PageLink


class Pages(QWidget):

    pageChanged = pyqtSignal([int])

    def __init__(self, page_count, parent=None):
        super().__init__(parent)
        self.page_count = page_count
        self.cur_page = 1
        self.widgets = []
        self.pagination_layout = QHBoxLayout(self)
        self.setLayout(self.pagination_layout)
        self.update_widgets()

    def update_widgets(self):
        self.setUpdatesEnabled(False)
        for widget in list(self.widgets):
            self.layout().removeWidget(widget)
            widget.deleteLater()
            self.widgets.remove(widget)
        prevPageLink = PageLink(
            "<",
            self.cur_page - 1 if self.cur_page > 1 else 1,
            False,
            parent=self)
        prevPageLink.clicked.connect(self.switch_page)
        self.pagination_layout.addWidget(prevPageLink)
        self.widgets.append(prevPageLink)
        for i in range(1, self.page_count + 1):
            page_link = PageLink(str(i), i, self.cur_page == i, parent=self)
            self.pagination_layout.addWidget(page_link)
            self.widgets.append(page_link)
            page_link.clicked.connect(self.switch_page)
        nextPageLink = PageLink(
            ">",
            self.cur_page + 1 if self.cur_page < self.page_count else self.page_count,
            False,
            parent=self)
        nextPageLink.clicked.connect(self.switch_page)
        self.pagination_layout.addWidget(nextPageLink)
        self.widgets.append(nextPageLink)
        self.setUpdatesEnabled(True)

    def switch_page(self, page_num):
        self.cur_page = page_num
        self.pageChanged.emit(page_num)
        self.update_widgets()

    def set_page_count(self, page_count):
        if self.cur_page > self.page_count:
            self.cur_page = page_count
        self.page_count = page_count
        self.update_widgets()

    def set_cur_page(self, cur_page):
        if cur_page < 1:
            cur_page = 1
        if cur_page > self.page_count:
            cur_page = self.page_count
        self.cur_page = cur_page
        self.update_widgets()
