from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt, pyqtSignal


class PageLink(QLabel):

    clicked = pyqtSignal([int])

    def __init__(self, text, page_num, active, parent=None):
        super().__init__(text, parent=parent)
        self.setTextInteractionFlags(Qt.LinksAccessibleByMouse)
        if active:
            self.setStyleSheet("color: #D32B39;")
        else:
            self.setStyleSheet("color: black;")
        self.setCursor(Qt.PointingHandCursor)
        self.page_num = page_num

    def mousePressEvent(self, event):
        self.clicked.emit(self.page_num)
        return super().mousePressEvent(event)
