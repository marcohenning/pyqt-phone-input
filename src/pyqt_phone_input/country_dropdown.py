from qtpy import QtCore
from qtpy.QtCore import Signal
from PyQt6.QtGui import QPainter
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
        self.popup_open = False

    def paintEvent(self, event):
        painter = QPainter(self)
        if self.count() > 0:
            painter.drawPixmap(5, (self.height() - 24) // 2, self.itemIcon(self.currentIndex()).pixmap(24, 24))

    def showPopup(self):
        super().showPopup()
        self.show_popup.emit()
        self.popup_open = True
        
    def hidePopup(self):
        super().hidePopup()
        self.hide_popup.emit()
        self.popup_open = False

    def getPreferredWidth(self) -> int:
        return self.__preferred_width
