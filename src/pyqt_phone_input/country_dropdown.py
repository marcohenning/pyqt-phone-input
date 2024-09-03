import math
from qtpy import QtCore
from qtpy.QtCore import Signal, Qt
from qtpy.QtGui import QPainter, QFont, QFontMetrics
from qtpy.QtWidgets import QComboBox
from .countries import countries


class CountryDropdown(QComboBox):

    show_popup = Signal()
    hide_popup = Signal()
    geometry_changed = Signal()

    def __init__(self, parent=None):
        super(CountryDropdown, self).__init__(parent)

        self.__input_font = self.font()
        self.__font_metrics = QFontMetrics(self.font())
        self.__icon_size = 0
        self.__border_width = 0
        self.popup_open = False
        self.__current_country_code = ''

        self.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.view().setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.currentTextChanged.connect(self.__handle_current_item_changed)

        self.__handle_current_item_changed()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setFont(self.__input_font)

        if self.count() > 0:
            buffer_left = math.ceil((self.height() - self.__icon_size) / 2) + self.__border_width
            x_start = buffer_left + self.__border_width - 1
            painter.drawPixmap(x_start, buffer_left - self.__border_width, self.itemIcon(
                self.currentIndex()).pixmap(self.__icon_size, self.__icon_size))
            painter.drawText(x_start + self.__icon_size + buffer_left // 2,
                             self.height() - int((self.height() - self.__font_metrics.tightBoundingRect(
                                 self.__current_country_code).height()) / 2),
                             self.__current_country_code)

    def showPopup(self):
        super().showPopup()
        self.popup_open = True
        self.show_popup.emit()
        
    def hidePopup(self):
        super().hidePopup()
        self.popup_open = False
        self.hide_popup.emit()

    def resizeEvent(self, event):
        self.__calculate_geometry()

    def getCountry(self) -> str:
        current_country_name = self.currentText().split(' (')[0]

        for country in countries:
            if countries[country][0] == current_country_name:
                return country

    def getCountryCode(self) -> str:
        return self.__current_country_code

    def setCountry(self, new_country: str):
        index = 0
        new_country = new_country.lower()

        for country in countries:
            if country == new_country:
                self.setCurrentIndex(index)
                break
            index += 1

    def getBorderWidth(self) -> int:
        return self.__border_width

    def setBorderWidth(self, width: int):
        self.__border_width = width
        self.__calculate_geometry()
        self.update()

    def getInputFont(self) -> QFont:
        return self.__input_font

    def setInputFont(self, font: QFont):
        self.__input_font = font
        self.__calculate_geometry()
        self.update()

    def __calculate_geometry(self):
        self.__font_metrics = QFontMetrics(self.__input_font)
        self.__icon_size = int(self.height() * 0.7)
        buffer_left = math.ceil((self.height() - self.__icon_size) / 2) + self.__border_width
        self.setFixedWidth(self.height() + self.__font_metrics.tightBoundingRect(self.__current_country_code).width() + buffer_left // 2)
        self.geometry_changed.emit()
        self.update()

    def __update_country_code(self):
        if self.count() > 0:
            self.__current_country_code = self.currentText().split('(')[1].split(')')[0]

    def __handle_current_item_changed(self):
        self.__update_country_code()
        self.__calculate_geometry()
