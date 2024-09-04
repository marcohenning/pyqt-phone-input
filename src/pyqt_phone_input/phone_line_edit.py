from qtpy.QtCore import Signal, QRegularExpression
from qtpy.QtGui import QPainter, QColor, QRegularExpressionValidator
from qtpy.QtWidgets import QLineEdit
from .country_dropdown import CountryDropdown


class PhoneLineEdit(QLineEdit):

    # Events
    focus_in = Signal()
    focus_out = Signal()

    def __init__(self, parent=None):
        """Create a new PhoneLineEdit instance

        :param parent: the parent widget
        """

        super(PhoneLineEdit, self).__init__(parent)

        # Connected country dropdown
        self.__country_dropdown = None
        self.__border_color_current = None
        self.__border_width = 0

        # Set validator to only allow numbers and spaces as input
        self.setValidator(QRegularExpressionValidator(QRegularExpression('[0-9 ]*')))

    def paintEvent(self, event):
        """Method that gets called every time the widget needs to be updated.
        Everything related to widget graphics happens here.

        :param event: event sent by PyQt
        """

        super().paintEvent(event)

        # Draw inside border to separate the LineEdit from connected dropdown
        if self.__country_dropdown and self.__border_color_current:
            painter = QPainter(self)
            painter.setPen(self.__border_color_current)
            x = self.__country_dropdown.width() + self.__border_width * 2

            for i in range(self.__border_width):
                painter.drawLine(x + i, 0, x + i, self.height() - 1)

    def focusInEvent(self, event):
        """Method that gets called every time the widget gains focus

        :param event: event sent by PyQt
        """

        super().focusInEvent(event)
        self.focus_in.emit()

    def focusOutEvent(self, event):
        """Method that gets called every time the widget loses focus

        :param event: event sent by PyQt
        """

        super().focusOutEvent(event)
        self.focus_out.emit()

    def getCountryDropdown(self) -> CountryDropdown:
        """Get the current country dropdown

        :return: country dropdown
        """

        return self.__country_dropdown

    def setCountryDropdown(self, country_dropdown: CountryDropdown):
        """Set the country dropdown

        :param country_dropdown: new country dropdown
        """

        self.__country_dropdown = country_dropdown

    def getCurrentBorderColor(self) -> QColor:
        """Get the current border color

        :return: current border color
        """

        return self.__border_color_current

    def setCurrentBorderColor(self, color: QColor):
        """Set the current border color

        :param color: new border color
        """

        self.__border_color_current = color
        self.update()

    def getBorderWidth(self) -> int:
        """Get the current border width

        :return: current border width
        """

        return self.__border_width

    def setBorderWidth(self, width: int):
        """Set the current border width

        :param width: new border width
        """

        self.__border_width = width
        self.update()
