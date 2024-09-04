from PyQt6.QtCore import QRect
from PyQt6.QtGui import QFont, QPaintEvent
from PyQt6.QtWidgets import QLineEdit
from PyQt6.QtTest import QTest
from pytestqt.qt_compat import qt_api
from src.pyqt_phone_input.country_dropdown import CountryDropdown


def test_initial_values(qtbot):
    """Test initial values after instantiating"""

    country_dropdown = CountryDropdown()
    qtbot.addWidget(country_dropdown)

    assert country_dropdown.getPhoneCodeLineEdit() is None
    assert country_dropdown.getBorderWidth() == 0
    assert not country_dropdown.isDropdownOpen()
    assert country_dropdown.getCountry() == 'af'
    assert country_dropdown.getCountryPhoneCode() == '+93'


def test_set_phone_code_line_edit(qtbot):
    """Test setting the phone code LineEdit"""

    country_dropdown = CountryDropdown()
    qtbot.addWidget(country_dropdown)

    phone_code_line_edit = QLineEdit()
    country_dropdown.setPhoneCodeLineEdit(phone_code_line_edit)
    assert country_dropdown.getPhoneCodeLineEdit() == phone_code_line_edit


def test_set_country(qtbot):
    """Test setting the country"""

    country_dropdown = CountryDropdown()
    qtbot.addWidget(country_dropdown)

    country_dropdown.setCountry('us')

    assert country_dropdown.getCountry() == 'us'
    assert country_dropdown.getCountryPhoneCode() == '+1'


def test_set_border_width(qtbot):
    """Test setting the border width"""

    country_dropdown = CountryDropdown()
    qtbot.addWidget(country_dropdown)

    country_dropdown.setBorderWidth(5)
    assert country_dropdown.getBorderWidth() == 5
