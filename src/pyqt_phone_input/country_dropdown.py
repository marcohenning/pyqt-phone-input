from qtpy import QtCore
from qtpy.QtCore import Signal
from qtpy.QtWidgets import QComboBox


class CountryDropdown(QComboBox):

    show_popup = Signal()
    hide_popup = Signal()

    def __init__(self, parent=None):
        super(CountryDropdown, self).__init__(parent)

        self.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        
    def showPopup(self):
        super().showPopup()
        self.show_popup.emit()
        
    def hidePopup(self):
        super().hidePopup()
        self.hide_popup.emit()
