import sys
from PySide6.QtGui import QFont, QColor
from PySide6.QtWidgets import QMainWindow, QApplication
from src.pyqt_phone_input import PhoneInput


class Window(QMainWindow):

    def __init__(self):
        super().__init__(parent=None)

        # Window settings
        self.setWindowTitle('Example')
        self.setFixedSize(300, 165)

        # Phone input
        self.phone_input = PhoneInput(self)
        self.phone_input.setGeometry(62, 55, 175, 36)
        self.phone_input.setFont(QFont('Arial', 11))
        self.phone_input.setBorderRadius(5)
        self.phone_input.setDropdownBorderColor(QColor(150, 150, 150))
        self.phone_input.setDropdownItemHeightDynamic(False)
        self.phone_input.setDropdownItemHeight(20)
        self.phone_input.setCountry('us')
        self.phone_input.setPlaceholderText('Phone number')


# Run the example
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()
