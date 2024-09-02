from qtpy.QtCore import Signal
from qtpy.QtGui import QPainter, QPalette, QColor
from qtpy.QtWidgets import QLineEdit
from .country_dropdown import CountryDropdown


class PhoneLineEdit(QLineEdit):

    focus_in = Signal()
    focus_out = Signal()

    def __init__(self, parent=None):
        super(PhoneLineEdit, self).__init__(parent)

        self.__country_dropdown = None

    def paintEvent(self, event):
        super().paintEvent(event)
        if self.__country_dropdown:
            painter = QPainter(self)
            painter.setPen(self.__border_color_current)
            painter.drawLine(self.__country_dropdown.width() + 1, 0, self.__country_dropdown.width() + 1, self.height())

    def focusInEvent(self, event):
        super().focusInEvent(event)
        self.focus_in.emit()

    def focusOutEvent(self, event):
        super().focusOutEvent(event)
        self.focus_out.emit()

    def setCountryDropdown(self, country_dropdown: CountryDropdown):
        self.__country_dropdown = country_dropdown

    def setCurrentBorderColor(self, color: QColor):
        self.__border_color_current = color
