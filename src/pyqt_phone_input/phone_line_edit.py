from qtpy.QtGui import QPainter, QPalette, QColor
from qtpy.QtCore import Signal
from qtpy.QtWidgets import QLineEdit
from .country_dropdown import CountryDropdown


class PhoneLineEdit(QLineEdit):

    focused = Signal()

    def __init__(self, parent=None):
        super(PhoneLineEdit, self).__init__(parent)

        self.__country_dropdown = None
        self.__border_color = self.palette().color(QPalette.ColorRole.Shadow)
        self.__focused_border_color = self.palette().color(QPalette.ColorRole.Highlight)
        self.__hovered_border_color = QColor(255, 0, 0)
        self.__border_color_current = self.__border_color

    def paintEvent(self, event):
        super().paintEvent(event)
        if self.__country_dropdown:
            painter = QPainter(self)
            painter.setPen(self.__border_color_current)
            painter.drawLine(self.__country_dropdown.width() + 1, 0, self.__country_dropdown.width() + 1, self.height())

    def focusInEvent(self, event):
        super().focusInEvent(event)
        self.focused.emit()
        self.__border_color_current = self.__focused_border_color

    def focusOutEvent(self, event):
        super().focusOutEvent(event)
        self.__border_color_current = self.__border_color

    def setCountryDropdown(self, country_dropdown: CountryDropdown):
        self.__country_dropdown = country_dropdown

    def setCurrentBorderColor(self, color: QColor):
        self.__border_color_current = color
