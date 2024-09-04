from PyQt6.QtCore import QRect
from PyQt6.QtGui import QFont, QPaintEvent
from PyQt6.QtTest import QTest
from pytestqt.qt_compat import qt_api
from src.pyqt_phone_input.country_dropdown import CountryDropdown


def test_initial_values(qtbot):
    """Test initial values after instantiating"""

    country_dropdown = CountryDropdown()
    qtbot.addWidget(country_dropdown)

    assert country_dropdown.getBorderWidth() == 0
    assert not country_dropdown.isDropdownOpen()
    assert country_dropdown.getCountry() == 'af'
    assert country_dropdown.getCountryPhoneCode() == '+93'


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


def test_set_input_font(qtbot):
    """Test setting the input font"""

    country_dropdown = CountryDropdown()
    qtbot.addWidget(country_dropdown)

    font = QFont('Arial', 14)
    country_dropdown.setInputFont(font)
    assert country_dropdown.getInputFont() == font


def test_paint_event(qtbot):
    """Test the paint event"""

    country_dropdown = CountryDropdown()
    qtbot.addWidget(country_dropdown)

    country_dropdown.setCountry('us')

    # Simulate paint event and wait for event to be handled
    paint_event = QPaintEvent(QRect(0, 0, 0, 0))
    qt_api.QtWidgets.QApplication.instance().postEvent(country_dropdown, paint_event)
    QTest.qWait(250)
    width_us = country_dropdown.width()

    country_dropdown.setCountry('de')

    # Simulate paint event and wait for event to be handled
    paint_event = QPaintEvent(QRect(0, 0, 0, 0))
    qt_api.QtWidgets.QApplication.instance().postEvent(country_dropdown, paint_event)
    QTest.qWait(250)
    width_de = country_dropdown.width()

    # US phone code (+1) is shorter than DE (+49), so the widget should be larger with DE selected
    assert width_de > width_us
