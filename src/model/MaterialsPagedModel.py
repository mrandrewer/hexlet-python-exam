from math import ceil
from PyQt5.QtCore import QObject, QSortFilterProxyModel


class MaterialsPagedModel(QSortFilterProxyModel):
    def __init__(self, page_size, parent: QObject | None = ...):
        super().__init__(parent)
        self.page_size = page_size
        self.page_num = 0

    def set_page_num(self, page_num):
        self.page_num = page_num
        self.invalidateFilter()

    def get_page_count(self):
        return ceil(float(self.sourceModel().rowCount()) / self.page_size)

    def filterAcceptsRow(self, source_row, source_parent):
        page_start = self.page_size * self.page_num
        page_end = self.page_size * (self.page_num + 1)
        if source_row >= page_start and source_row < page_end:
            return True
        return False
