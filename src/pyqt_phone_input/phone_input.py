from qtpy.QtWidgets import QWidget, QLineEdit, QComboBox


class PhoneInput(QWidget):

    def __init__(self, parent=None):
        super(PhoneInput, self).__init__(parent)

        self.__line_edit = QLineEdit(self)
        self.__line_edit.setFixedSize(self.width(), self.height())

        self.__combo_box = QComboBox(self)
        self.__combo_box.setFixedSize(self.width() // 3, self.height() - 2)
        self.__combo_box.move(1, 1)
