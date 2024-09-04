from PyQt6.QtGui import QColor, QPalette, QFont, QFocusEvent
from PyQt6.QtCore import QEasingCurve, QMargins
from PyQt6.QtTest import QTest
from pytestqt.qt_compat import qt_api
from src.pyqt_phone_input.phone_line_edit import PhoneLineEdit
from src.pyqt_phone_input.country_dropdown import CountryDropdown


def test_initial_values(qtbot):
    """Test initial values after instantiating"""

    phone_line_edit = PhoneLineEdit()
    qtbot.addWidget(phone_line_edit)

    assert phone_line_edit.getCountryDropdown() is None
    assert phone_line_edit.getCurrentBorderColor() is None
    assert phone_line_edit.getBorderWidth() == 0


def test_set_country_dropdown(qtbot):
    phone_line_edit = PhoneLineEdit()
    qtbot.addWidget(phone_line_edit)

    country_dropdown = CountryDropdown()
    phone_line_edit.setCountryDropdown(country_dropdown)
    assert phone_line_edit.getCountryDropdown() == country_dropdown


def test_setCurrentBorderColor(qtbot):
    phone_line_edit = PhoneLineEdit()
    qtbot.addWidget(phone_line_edit)

    color = QColor(255, 0, 0)
    phone_line_edit.setCurrentBorderColor(color)
    assert phone_line_edit.getCurrentBorderColor() == color


def test_set_border_width(qtbot):
    phone_line_edit = PhoneLineEdit()
    qtbot.addWidget(phone_line_edit)

    phone_line_edit.setBorderWidth(5)
    assert phone_line_edit.getBorderWidth() == 5
