from qtpy import QtCore
from qtpy.QtCore import Signal
from PyQt6.QtGui import QPainter, QColor
from qtpy.QtWidgets import QComboBox, QStyleOptionComboBox


class CountryDropdown(QComboBox):

    show_popup = Signal()
    hide_popup = Signal()

    def __init__(self, parent=None):
        super(CountryDropdown, self).__init__(parent)

        self.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.__style_option = QStyleOptionComboBox()
        self.initStyleOption(self.__style_option)
        self.__style_option.currentText = ''

        self.__preferred_width = 24 + 12

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QColor(100, 100, 100))
        painter.drawPixmap(5, (self.height() - 24) // 2, self.itemIcon(self.currentIndex()).pixmap(24, 24))
        painter.drawLine(self.width() - 1, 0, self.width() - 1, self.height())

    def showPopup(self):
        super().showPopup()
        self.show_popup.emit()
        
    def hidePopup(self):
        super().hidePopup()
        self.hide_popup.emit()

    def getPreferredWidth(self):
        return self.__preferred_width
