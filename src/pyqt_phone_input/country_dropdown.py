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

        self.__icon_size = 0
        self.__preferred_width = 0
        self.popup_open = False

        self.__calculate_icon_size()

    def paintEvent(self, event):
        painter = QPainter(self)
        if self.count() > 0:
            painter.drawPixmap((self.height() - self.__icon_size) // 2 + self.__border_width - 1,
                               (self.height() - self.__icon_size) // 2,
                               self.itemIcon(self.currentIndex()).pixmap(
                                   self.__icon_size, self.__icon_size))

    def showPopup(self):
        super().showPopup()
        self.show_popup.emit()
        self.popup_open = True
        
    def hidePopup(self):
        super().hidePopup()
        self.hide_popup.emit()
        self.popup_open = False

    def resizeEvent(self, event):
        self.__calculate_icon_size()

    def getPreferredWidth(self) -> int:
        return self.__preferred_width

    def setBorderWidth(self, width: int):
        self.__border_width = width

    def __calculate_icon_size(self):
        self.__icon_size = int(self.height() * 0.7)
        self.__preferred_width = self.height()
        self.setFixedWidth(self.height())
