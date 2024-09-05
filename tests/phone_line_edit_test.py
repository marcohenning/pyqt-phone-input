from PyQt6.QtCore import QRect
from PyQt6.QtGui import QColor, QPaintEvent
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
    """Test setting the country dropdown"""

    phone_line_edit = PhoneLineEdit()
    qtbot.addWidget(phone_line_edit)

    country_dropdown = CountryDropdown()
    phone_line_edit.setCountryDropdown(country_dropdown)
    assert phone_line_edit.getCountryDropdown() == country_dropdown


def test_set_current_border_color(qtbot):
    """Test setting the current border color"""

    phone_line_edit = PhoneLineEdit()
    qtbot.addWidget(phone_line_edit)

    color = QColor(255, 0, 0)
    phone_line_edit.setCurrentBorderColor(color)
    assert phone_line_edit.getCurrentBorderColor() == color


def test_set_border_width(qtbot):
    """Test setting the border width"""

    phone_line_edit = PhoneLineEdit()
    qtbot.addWidget(phone_line_edit)

    phone_line_edit.setBorderWidth(5)
    assert phone_line_edit.getBorderWidth() == 5


def test_paint_event(qtbot):
    """Test the paint event"""

    phone_line_edit = PhoneLineEdit()
    qtbot.addWidget(phone_line_edit)

    country_dropdown = CountryDropdown()
    color = QColor(255, 0, 0)

    phone_line_edit.setCountryDropdown(country_dropdown)
    phone_line_edit.setBorderWidth(5)
    phone_line_edit.setCurrentBorderColor(color)

    # Simulate paint event and wait for event to be handled
    paint_event = QPaintEvent(QRect(0, 0, 0, 0))
    qt_api.QtWidgets.QApplication.instance().postEvent(phone_line_edit, paint_event)
    QTest.qWait(250)

    assert phone_line_edit.getCountryDropdown() == country_dropdown
    assert phone_line_edit.getBorderWidth() == 5
    assert phone_line_edit.getCurrentBorderColor() == color
