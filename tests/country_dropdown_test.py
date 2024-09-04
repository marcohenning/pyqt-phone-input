from PyQt6.QtGui import QFont
from src.pyqt_phone_input.country_dropdown import CountryDropdown


def test_initial_values(qtbot):
    """Test initial values after instantiating"""

    country_dropdown = CountryDropdown()
    qtbot.addWidget(country_dropdown)

    assert country_dropdown.getBorderWidth() == 0
    assert not country_dropdown.getPopupOpen()
    assert country_dropdown.getCountry() == 'af'
    assert country_dropdown.getCountryPhoneCode() == '+93'


def test_set_country(qtbot):
    country_dropdown = CountryDropdown()
    qtbot.addWidget(country_dropdown)

    country_dropdown.setCountry('us')

    assert country_dropdown.getCountry() == 'us'
    assert country_dropdown.getCountryPhoneCode() == '+1'


def test_set_border_width(qtbot):
    country_dropdown = CountryDropdown()
    qtbot.addWidget(country_dropdown)

    country_dropdown.setBorderWidth(5)
    assert country_dropdown.getBorderWidth() == 5


def test_set_input_font(qtbot):
    country_dropdown = CountryDropdown()
    qtbot.addWidget(country_dropdown)

    font = QFont('Arial', 14)
    country_dropdown.setInputFont(font)
    assert country_dropdown.getInputFont() == font
