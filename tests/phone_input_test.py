from PyQt6.QtCore import QMargins
from PyQt6.QtGui import QColor, QPalette, QFont
from src.pyqt_phone_input.phone_input import PhoneInput


def test_initial_values(qtbot):
    """Test initial values after instantiating"""

    phone_input = PhoneInput()
    qtbot.addWidget(phone_input)

    assert phone_input.getColor() == QColor(0, 0, 0)
    assert phone_input.getBackgroundColor() == QColor(255, 255, 255)
    assert phone_input.getBorderColor() == phone_input.palette().color(QPalette.ColorRole.Shadow)
    assert phone_input.getBorderWidth() == 1
    assert phone_input.getBorderRadius() == 0
    assert phone_input.getPadding() == QMargins(2, 0, 0, 0)
    assert phone_input.getTextSelectionForegroundColor() is None
    assert phone_input.getTextSelectionBackgroundColor() == phone_input.palette().color(QPalette.ColorRole.Highlight)
    assert phone_input.getFocusedColor() is None
    assert phone_input.getFocusedBackgroundColor() is None
    assert phone_input.getFocusedBorderColor() == phone_input.palette().color(QPalette.ColorRole.Highlight)
    assert phone_input.getDisabledColor() is None
    assert phone_input.getDisabledBackgroundColor() is None
    assert phone_input.getDisabledBorderColor() is None
    assert phone_input.isDropdownItemHeightDynamic()
    assert phone_input.getDropdownItemHeight() == 25
    assert phone_input.getDropdownItemSelectionForegroundColor() == QColor(255, 255, 255)
    assert phone_input.getDropdownItemSelectionBackgroundColor() == phone_input.palette().color(QPalette.ColorRole.Highlight)
    assert phone_input.getDropdownBorderColor() is None
    assert phone_input.getCountry() == 'af'
    assert phone_input.getCountryPhoneCode() == '+93'


def test_set_country_and_input(qtbot):
    """Test setting the country and input text"""

    phone_input = PhoneInput()
    qtbot.addWidget(phone_input)

    phone_input.setCountry('us')
    phone_input.setInput('123456789')

    assert phone_input.getCountry() == 'us'
    assert phone_input.getCountryPhoneCode() == '+1'
    assert phone_input.getPhoneNumber() == '+1123456789'


def test_set_placeholder_text(qtbot):
    """Test setting the placeholder text"""

    phone_input = PhoneInput()
    qtbot.addWidget(phone_input)

    phone_input.setPlaceholderText('Phone number')
    assert phone_input.getPlaceholderText() == 'Phone number'


def test_set_disabled(qtbot):
    """Test enabling and disabling the widget"""

    phone_input = PhoneInput()
    qtbot.addWidget(phone_input)

    phone_input.setDisabled(True)
    assert phone_input.isDisabled()

    phone_input.setDisabled(False)
    assert not phone_input.isDisabled()


def test_set_color(qtbot):
    """Test setting the text color"""

    phone_input = PhoneInput()
    qtbot.addWidget(phone_input)

    color = QColor(255, 0, 0)
    phone_input.setColor(color)
    assert phone_input.getColor() == color


def test_set_background_color(qtbot):
    """Test setting the background color"""

    phone_input = PhoneInput()
    qtbot.addWidget(phone_input)

    color = QColor(255, 0, 0)
    phone_input.setBackgroundColor(color)
    assert phone_input.getBackgroundColor() == color


def test_set_border_color(qtbot):
    """Test setting the border color"""

    phone_input = PhoneInput()
    qtbot.addWidget(phone_input)

    color = QColor(255, 0, 0)
    phone_input.setBorderColor(color)
    assert phone_input.getBorderColor() == color


def test_set_border_width(qtbot):
    """Test setting the border width"""

    phone_input = PhoneInput()
    qtbot.addWidget(phone_input)

    phone_input.setBorderWidth(5)
    assert phone_input.getBorderWidth() == 5


def test_set_border_radius(qtbot):
    """Test setting the border radius"""

    phone_input = PhoneInput()
    qtbot.addWidget(phone_input)

    phone_input.setBorderRadius(5)
    assert phone_input.getBorderRadius() == 5


def test_set_padding(qtbot):
    """Test setting the padding"""

    phone_input = PhoneInput()
    qtbot.addWidget(phone_input)

    padding = QMargins(10, 10, 10, 10)
    phone_input.setPadding(padding)
    assert phone_input.getPadding() == padding


def test_set_focused_color(qtbot):
    """Test setting the focused text color"""

    phone_input = PhoneInput()
    qtbot.addWidget(phone_input)

    color = QColor(255, 0, 0)
    phone_input.setFocusedColor(color)
    assert phone_input.getFocusedColor() == color


def test_set_focused_background_color(qtbot):
    """Test setting the focused background color"""

    phone_input = PhoneInput()
    qtbot.addWidget(phone_input)

    color = QColor(255, 0, 0)
    phone_input.setFocusedBackgroundColor(color)
    assert phone_input.getFocusedBackgroundColor() == color


def test_set_focused_border_color(qtbot):
    """Test setting the focused border color"""

    phone_input = PhoneInput()
    qtbot.addWidget(phone_input)

    color = QColor(255, 0, 0)
    phone_input.setFocusedBorderColor(color)
    assert phone_input.getFocusedBorderColor() == color


def test_set_disabled_color(qtbot):
    """Test setting the disabled text color"""

    phone_input = PhoneInput()
    qtbot.addWidget(phone_input)

    color = QColor(255, 0, 0)
    phone_input.setDisabledColor(color)
    assert phone_input.getDisabledColor() == color


def test_set_disabled_background_color(qtbot):
    """Test setting the disabled background color"""

    phone_input = PhoneInput()
    qtbot.addWidget(phone_input)

    color = QColor(255, 0, 0)
    phone_input.setDisabledBackgroundColor(color)
    assert phone_input.getDisabledBackgroundColor() == color


def test_set_disabled_border_color(qtbot):
    """Test setting the disabled border color"""

    phone_input = PhoneInput()
    qtbot.addWidget(phone_input)

    color = QColor(255, 0, 0)
    phone_input.setDisabledBorderColor(color)
    assert phone_input.getDisabledBorderColor() == color


def test_set_text_selection_foreground_color(qtbot):
    """Test setting the text selection foreground color"""

    phone_input = PhoneInput()
    qtbot.addWidget(phone_input)

    color = QColor(255, 0, 0)
    phone_input.setTextSelectionForegroundColor(color)
    assert phone_input.getTextSelectionForegroundColor() == color


def test_set_text_selection_background_color(qtbot):
    """Test setting the text selection background color"""

    phone_input = PhoneInput()
    qtbot.addWidget(phone_input)

    color = QColor(255, 0, 0)
    phone_input.setTextSelectionBackgroundColor(color)
    assert phone_input.getTextSelectionBackgroundColor() == color


def test_set_dropdown_item_height_dynamic(qtbot):
    """Test setting the dropdown item height to be dynamic or custom height"""

    phone_input = PhoneInput()
    qtbot.addWidget(phone_input)

    phone_input.setDropdownItemHeightDynamic(False)
    assert not phone_input.isDropdownItemHeightDynamic()

    phone_input.setDropdownItemHeightDynamic(True)
    assert phone_input.isDropdownItemHeightDynamic()


def test_set_dropdown_item_height(qtbot):
    """Test setting the dropdown item height"""

    phone_input = PhoneInput()
    qtbot.addWidget(phone_input)

    phone_input.setDropdownItemHeight(15)
    assert phone_input.getDropdownItemHeight() == 15


def test_set_dropdown_item_selection_foreground_color(qtbot):
    """Test setting the dropdown item selection foreground color"""

    phone_input = PhoneInput()
    qtbot.addWidget(phone_input)

    color = QColor(255, 0, 0)
    phone_input.setDropdownItemSelectionForegroundColor(color)
    assert phone_input.getDropdownItemSelectionForegroundColor() == color


def test_set_dropdown_item_selection_background_color(qtbot):
    """Test setting the dropdown item selection background color"""

    phone_input = PhoneInput()
    qtbot.addWidget(phone_input)

    color = QColor(255, 0, 0)
    phone_input.setDropdownItemSelectionBackgroundColor(color)
    assert phone_input.getDropdownItemSelectionBackgroundColor() == color


def test_set_dropdown_border_color(qtbot):
    """Test setting the dropdown border color"""

    phone_input = PhoneInput()
    qtbot.addWidget(phone_input)

    color = QColor(255, 0, 0)
    phone_input.setDropdownBorderColor(color)
    assert phone_input.getDropdownBorderColor() == color


def test_set_font(qtbot):
    """Test setting the font"""

    phone_input = PhoneInput()
    qtbot.addWidget(phone_input)

    font = QFont('Arial', 14)
    phone_input.setFont(font)
    assert phone_input.getFont() == font


def test_set_dropdown_font(qtbot):
    """Test setting the dropdown font"""

    phone_input = PhoneInput()
    qtbot.addWidget(phone_input)

    font = QFont('Arial', 14)
    phone_input.setDropdownFont(font)
    assert phone_input.getDropdownFont() == font
