import os
from qtpy.QtCore import QMargins, Signal
from qtpy.QtGui import QColor, QPalette, QIcon, QFont
from qtpy.QtWidgets import QWidget
from .country_dropdown import CountryDropdown
from .phone_line_edit import PhoneLineEdit
from .countries import countries


class PhoneInput(QWidget):

    # Events
    country_changed = Signal()
    number_changed = Signal()

    def __init__(self, parent=None):
        """Create a new PhoneInput instance

        :param parent: the parent widget
        """

        super(PhoneInput, self).__init__(parent)

        # Styling options
        self.__color = QColor(0, 0, 0)
        self.__background_color = QColor(255, 255, 255)
        self.__border_color = self.palette().color(QPalette.ColorRole.Shadow)
        self.__border_width = 1
        self.__border_radius = 3
        self.__padding = QMargins(2, 0, 0, 0)
        self.__selection_foreground_color = None
        self.__selection_background_color = self.palette().color(QPalette.ColorRole.Highlight)
        self.__focused_color = None
        self.__focused_background_color = None
        self.__focused_border_color = self.palette().color(QPalette.ColorRole.Highlight)
        self.__disabled_color = None
        self.__disabled_background_color = None
        self.__disabled_border_color = None
        self.__dropdown_item_height_dynamic = True
        self.__dropdown_item_height = 25
        self.__dropdown_item_selection_color = QColor(255, 255, 255)
        self.__dropdown_item_selection_background_color = self.palette().color(QPalette.ColorRole.Highlight)
        self.__dropdown_border_color = None

        # LineEdit
        self.__phone_line_edit = PhoneLineEdit(self)
        self.__phone_line_edit.setBorderWidth(self.__border_width)

        # Dropdown
        self.__country_dropdown = CountryDropdown(self)
        self.__country_dropdown.setBorderWidth(self.__border_width)
        self.__country_dropdown.currentIndexChanged.connect(self.__handle_country_changed)
        self.__country_dropdown.show_popup.connect(self.__handle_popup_opened)
        self.__country_dropdown.hide_popup.connect(self.__handle_popup_closed)
        self.__country_dropdown.geometry_changed.connect(self.__update_line_edit_style_sheet)

        # Add all countries to dropdown
        self.__directory = os.path.dirname(os.path.realpath(__file__))
        for country in countries:
            self.__country_dropdown.addItem(
                QIcon(self.__directory + '/flag_icons/{}.png'.format(country)),
                '{} ({})'.format(countries[country][0], countries[country][1]))

        # Set up LineEdit
        self.__phone_line_edit.setCountryDropdown(self.__country_dropdown)
        self.__phone_line_edit.textChanged.connect(self.__handle_number_changed)
        self.__phone_line_edit.focus_in.connect(self.__handle_focus_in)
        self.__phone_line_edit.focus_out.connect(self.__handle_focus_out)

        # Update geometry and style sheets
        self.__calculate_geometry()
        self.__update_line_edit_style_sheet()
        self.__update_combobox_style_sheet()

    def __calculate_geometry(self):
        """Calculates everything related to widget geometry"""

        self.__phone_line_edit.setFixedSize(self.width(), self.height())
        self.__country_dropdown.setFixedHeight(self.height())
        self.__country_dropdown.view().setFixedWidth(self.__country_dropdown.minimumSizeHint().width())

    def __handle_country_changed(self):
        """Emits country_changed event when dropdown index changes"""

        self.country_changed.emit()

    def __handle_number_changed(self):
        """Emits number_changed event when LineEdit text changes"""

        self.number_changed.emit()

    def __handle_popup_opened(self):
        """Handles dropdown popup being opened"""

        selection_foreground_color = None
        if self.__selection_foreground_color:
            selection_foreground_color = self.__selection_foreground_color
        elif self.__focused_color:
            selection_foreground_color = self.__focused_color
        else:
            selection_foreground_color = self.__color

        self.__phone_line_edit.setStyleSheet('QLineEdit {'
                           'color: %s;'
                           'background-color: %s;'
                           'border: %dpx solid %s;'
                           'border-radius: %dpx;'
                           'padding: %d %d %d %dpx;'
                           'selection-color: %s;'
                           'selection-background-color: %s;'
                           '}'
                           % (self.__color.name() if self.__focused_color is None else self.__focused_color.name(),
                              self.__background_color.name() if self.__focused_background_color is None else self.__focused_background_color.name(),
                              self.__border_width,
                              self.__border_color.name() if self.__focused_border_color is None else self.__focused_border_color.name(),
                              self.__border_radius,
                              self.__padding.top(),
                              self.__padding.right(),
                              self.__padding.bottom(),
                              self.__padding.left() + self.__country_dropdown.width() + self.__border_width * 2,
                              selection_foreground_color.name(),
                              self.__selection_background_color.name()))

        self.__phone_line_edit.setCurrentBorderColor(
            self.__border_color if self.__focused_border_color is None else self.__focused_border_color)

    def __handle_popup_closed(self):
        """Handles dropdown popup being closed"""

        self.__update_line_edit_style_sheet()
        if not self.__phone_line_edit.hasFocus():
            self.__phone_line_edit.setCurrentBorderColor(self.__border_color)

    def __handle_focus_in(self):
        """Handles LineEdit being focused"""

        self.__phone_line_edit.setCurrentBorderColor(
            self.__border_color if self.__focused_border_color is None else self.__focused_border_color)

    def __handle_focus_out(self):
        """Handles LineEdit losing focus"""

        if not self.__country_dropdown.popup_open:
            self.__phone_line_edit.setCurrentBorderColor(self.__border_color)

    def __update_line_edit_style_sheet(self):
        """Updates the LineEdit stylesheet according to the current values"""

        selection_foreground_color = None
        if self.__selection_foreground_color:
            selection_foreground_color = self.__selection_foreground_color
        elif self.__focused_color:
            selection_foreground_color = self.__focused_color
        else:
            selection_foreground_color = self.__color

        self.__phone_line_edit.setStyleSheet('QLineEdit {'
                           'color: %s;'
                           'background-color: %s;'
                           'border: %dpx solid %s;'
                           'border-radius: %dpx;'
                           'padding: %d %d %d %dpx;'
                           'selection-color: %s;'
                           'selection-background-color: %s;'
                           '}'
                           'QLineEdit:focus {'
                           'color: %s;'
                           'background-color: %s;'
                           'border: %dpx solid %s;'
                           '}'
                           'QLineEdit:disabled {'
                           'color: %s;'
                           'background-color: %s;'
                           'border: %dpx solid %s;'
                           '}'
                           % (self.__color.name(),
                              self.__background_color.name(),
                              self.__border_width,
                              self.__border_color.name(),
                              self.__border_radius,
                              self.__padding.top(),
                              self.__padding.right(),
                              self.__padding.bottom(),
                              self.__padding.left() + self.__country_dropdown.width() + self.__border_width * 2,
                              selection_foreground_color.name(),
                              self.__selection_background_color.name(),
                              self.__color.name() if self.__focused_color is None else self.__focused_color.name(),
                              self.__background_color.name() if self.__focused_background_color is None else self.__focused_background_color.name(),
                              self.__border_width,
                              self.__border_color.name() if self.__focused_border_color is None else self.__focused_border_color.name(),
                              self.__color.name() if self.__disabled_color is None else self.__disabled_color.name(),
                              self.__background_color.name() if self.__disabled_background_color is None else self.__disabled_background_color.name(),
                              self.__border_width,
                              self.__border_color.name() if self.__disabled_border_color is None else self.__disabled_border_color.name()))

    def __update_combobox_style_sheet(self):
        """Updates the dropdown stylesheet according to the current values"""

        dropdown_item_selection_color = None
        if self.__dropdown_item_selection_color:
            dropdown_item_selection_color = self.__dropdown_item_selection_color
        elif self.__focused_color:
            dropdown_item_selection_color = self.__focused_color
        else:
            dropdown_item_selection_color = self.__color

        dropdown_border_color = None
        if self.__dropdown_border_color:
            dropdown_border_color = self.__dropdown_border_color
        elif self.__focused_border_color:
            dropdown_border_color = self.__focused_border_color
        else:
            dropdown_border_color = self.__border_color

        self.__country_dropdown.setStyleSheet('QComboBox QAbstractItemView {'
                                       'outline: none;'
                                       'border: %dpx solid %s;'
                                       '}'
                                       'QListView::item {'
                                       'height: %dpx;'
                                       'color: %s;'
                                       'background-color: %s;'
                                       'border: none;'
                                       '}'
                                       'QListView::item:focus {'
                                       'height: %dpx;'
                                       'color: %s;'
                                       'background-color: %s;'
                                       'border: none;'
                                       '}'
                                       % (self.__border_width,
                                          dropdown_border_color.name(),
                                          self.height() if self.__dropdown_item_height_dynamic else self.__dropdown_item_height,
                                          self.__color.name() if self.__focused_color is None else self.__focused_color.name(),
                                          self.__background_color.name() if self.__focused_background_color is None else self.__focused_background_color.name(),
                                          self.height() if self.__dropdown_item_height_dynamic else self.__dropdown_item_height,
                                          dropdown_item_selection_color.name(),
                                          self.__dropdown_item_selection_background_color.name()))

    def resizeEvent(self, event):
        """Method that gets called every time the widget is resized

        :param event: event sent by PyQt
        """

        self.__calculate_geometry()
        self.__update_line_edit_style_sheet()
        self.__update_combobox_style_sheet()

    def getCountry(self) -> str:
        """Get the current country

        :return: country code (i.e. 'us')
        """

        return self.__country_dropdown.getCountry()

    def getCountryPhoneCode(self) -> str:
        """Get the phone code of the current country

        :return: phone code (i.e. '+1')
        """

        return self.__country_dropdown.getCountryPhoneCode()

    def setCountry(self, country: str):
        """Set the country

        :param country: new country
        """

        self.__country_dropdown.setCountry(country)

    def getPhoneNumber(self) -> str:
        """Get the current phone number (no blank spaces)

        :return: phone number
        """

        return self.getCountryPhoneCode() + self.__phone_line_edit.text().replace(' ', '')

    def setInput(self, input_number: str):
        """Set the LineEdit's input

        :param input_number: new input
        """

        self.__phone_line_edit.setText(input_number)

    def getPlaceholderText(self) -> str:
        """Get the current placeholder text

        :return: placeholder text
        """

        return self.__phone_line_edit.placeholderText()

    def setPlaceholderText(self, text: str):
        """Set the placeholder text

        :param text: new placeholder text
        """

        self.__phone_line_edit.setPlaceholderText(text)

    def getDisabled(self) -> bool:
        """Get whether the widget is disabled

        :return: whether the widget is disabled
        """

        return not self.__country_dropdown.isEnabled()

    def setDisabled(self, disabled: bool):
        """Enable or disable the widget

        :param disabled: whether the widget should be disabled
        """

        self.__phone_line_edit.setDisabled(disabled)
        self.__country_dropdown.setDisabled(disabled)

        if disabled:
            self.__update_line_edit_style_sheet()
            self.__phone_line_edit.setCurrentBorderColor(
                self.__border_color if self.__disabled_border_color is None else self.__disabled_border_color)
        else:
            if self.__phone_line_edit.hasFocus() or self.__country_dropdown.popup_open:
                self.__phone_line_edit.setCurrentBorderColor(
                    self.__border_color if self.__focused_border_color is None else self.__focused_border_color)
            else:
                self.__phone_line_edit.setCurrentBorderColor(self.__border_color)

    def getColor(self) -> QColor:
        """Get the current text color

        :return: text color
        """

        return self.__color

    def setColor(self, color: QColor):
        """Set the text color

        :param color: new text color
        """

        self.__color = color
        self.__update_line_edit_style_sheet()
        self.__update_combobox_style_sheet()

    def getBackgroundColor(self) -> QColor:
        """Get the current background color

        :return: background color
        """

        return self.__background_color

    def setBackgroundColor(self, color: QColor):
        """Set the background color

        :param color: new background color
        """

        self.__background_color = color
        self.__update_line_edit_style_sheet()
        self.__update_combobox_style_sheet()

    def getBorderColor(self) -> QColor:
        """Get the current border color

        :return: border color
        """

        return self.__border_color

    def setBorderColor(self, color: QColor):
        """Set the border color

        :param color: new border color
        """

        self.__border_color = color
        self.__update_line_edit_style_sheet()
        self.__update_combobox_style_sheet()

    def getBorderWidth(self) -> int:
        """Get the current border width

        :return: border width
        """

        return self.__border_width

    def setBorderWidth(self, width: int):
        """Set the border width

        :param width: new border width
        """

        self.__border_width = width
        self.__phone_line_edit.setBorderWidth(width)
        self.__country_dropdown.setBorderWidth(width)
        self.__update_line_edit_style_sheet()
        self.__update_combobox_style_sheet()

    def getBorderRadius(self) -> int:
        """Get the current border radius

        :return: border radius
        """

        return self.__border_radius

    def setBorderRadius(self, radius: int):
        """Set the border radius

        :param radius: new border radius
        """

        self.__border_radius = radius
        self.__update_line_edit_style_sheet()
        self.__update_combobox_style_sheet()

    def getPadding(self) -> QMargins:
        """Get the current padding of the LineEdit

        :return: current padding of the LineEdit
        """

        return self.__padding

    def setPadding(self, padding: QMargins):
        """Set the padding of the LineEdit

        :param padding: new padding of the LineEdit
        """

        self.__padding = padding
        self.__update_line_edit_style_sheet()
        self.__update_combobox_style_sheet()

    def getFocusedColor(self) -> QColor:
        """Get the current focused text color

        :return: focused text color
        """

        return self.__focused_color

    def setFocusedColor(self, color: QColor):
        """Set the focused text color

        :param color: new focused text color
        """

        self.__focused_color = color
        self.__update_line_edit_style_sheet()
        self.__update_combobox_style_sheet()

    def getFocusedBackgroundColor(self) -> QColor:
        """Get the current focused background color

        :return: focused background color
        """

        return self.__focused_background_color

    def setFocusedBackgroundColor(self, color: QColor):
        """Set the focused background color

        :param color: new focused background color
        """

        self.__focused_background_color = color
        self.__update_line_edit_style_sheet()
        self.__update_combobox_style_sheet()

    def getFocusedBorderColor(self) -> QColor:
        """Get the current focused border color

        :return: focused border color
        """

        return self.__focused_border_color

    def setFocusedBorderColor(self, color: QColor):
        """Set the focused border color

        :param color: new focused border color
        """

        self.__focused_border_color = color
        self.__update_line_edit_style_sheet()
        self.__update_combobox_style_sheet()

    def getDisabledColor(self) -> QColor:
        """Get the current disabled text color

        :return: disabled text color
        """

        return self.__disabled_color

    def setDisabledColor(self, color: QColor):
        """Set the disabled text color

        :param color: new disabled text color
        """

        self.__disabled_color = color
        self.__update_line_edit_style_sheet()
        self.__update_combobox_style_sheet()

    def getDisabledBackgroundColor(self) -> QColor:
        """Get the current disabled background color

        :return: disabled background color
        """

        return self.__disabled_background_color

    def setDisabledBackgroundColor(self, color: QColor):
        """Set the disabled background color

        :param color: new disabled background color
        """

        self.__disabled_background_color = color
        self.__update_line_edit_style_sheet()
        self.__update_combobox_style_sheet()

    def getDisabledBorderColor(self) -> QColor:
        """Get the current disabled border color

        :return: disabled border color
        """

        return self.__disabled_border_color

    def setDisabledBorderColor(self, color: QColor):
        """Set the disabled border color

        :param color: new disabled border color
        """

        self.__disabled_border_color = color
        self.__update_line_edit_style_sheet()
        self.__update_combobox_style_sheet()

    def getTextSelectionForegroundColor(self) -> QColor:
        """Get the current text selection foreground color

        :return: text selection foreground color
        """

        return self.__selection_foreground_color

    def setTextSelectionForegroundColor(self, color: QColor):
        """Set the text selection foreground color

        :param color: new text selection foreground color
        """

        self.__selection_foreground_color = color
        self.__update_line_edit_style_sheet()

    def getTextSelectionBackgroundColor(self) -> QColor:
        """Get the current text selection background color

        :return: text selection background color
        """

        return self.__selection_background_color

    def setTextSelectionBackgroundColor(self, color: QColor):
        """Set the text selection background color

        :param color: new text selection background color
        """

        self.__selection_background_color = color
        self.__update_line_edit_style_sheet()

    def getDropdownItemHeightDynamic(self) -> bool:
        """Get whether the dropdown item height is always as high as the widget

        :return: whether the dropdown item height is always as high as the widget
        """

        return self.__dropdown_item_height_dynamic

    def setDropdownItemHeightDynamic(self, dynamic: bool):
        """Set whether the dropdown item height should always be as high as the widget

        :param dynamic: whether the dropdown item height should always be as high as the widget
        """

        self.__dropdown_item_height_dynamic = dynamic

    def getDropdownItemHeight(self) -> int:
        """Get the current dropdown item height

        :return: dropdown item height
        """

        return self.__dropdown_item_height

    def setDropdownItemHeight(self, height: int):
        """Set the dropdown item height

        :param height: new dropdown item height
        """

        self.__dropdown_item_height = height

    def getDropdownItemSelectionForegroundColor(self) -> QColor:
        """Get the current dropdown item selection foreground color

        :return: dropdown item selection foreground color
        """

        return self.__dropdown_item_selection_color

    def setDropdownItemSelectionForegroundColor(self, color: QColor):
        """Set the dropdown item selection foreground color

        :param color: new dropdown item selection foreground color
        """

        self.__dropdown_item_selection_color = color

    def getDropdownItemSelectionBackgroundColor(self) -> QColor:
        """Get the current dropdown item selection background color

        :return: dropdown item selection background color
        """

        return self.__dropdown_item_selection_background_color

    def setDropdownItemSelectionBackgroundColor(self, color: QColor):
        """Set the current dropdown item selection background color

        :param color: new dropdown item selection background color
        """

        self.__dropdown_item_selection_background_color = color

    def getDropdownBorderColor(self) -> QColor:
        """Get the current dropdown border color

        :return: dropdown border color
        """

        return self.__dropdown_border_color

    def setDropdownBorderColor(self, color: QColor):
        """Set the dropdown border color

        :param color: new dropdown border color
        """

        self.__dropdown_border_color = color

    def getFont(self) -> QFont:
        """Get the current font used for LineEdit text and dropdown selected item

        :return: font used for LineEdit text and dropdown selected item
        """

        return self.__phone_line_edit.font()

    def setFont(self, font: QFont):
        """Set the font used for LineEdit text and dropdown selected item

        :param font: new font used for LineEdit text and dropdown selected item
        """

        self.__phone_line_edit.setFont(font)
        self.__country_dropdown.setInputFont(font)

    def getDropdownFont(self) -> QFont:
        """Get the current font used for dropdown items

        :return: font used for dropdown items
        """

        return self.__country_dropdown.font()

    def setDropdownFont(self, font: QFont):
        """Set the font used for dropdown items

        :param font: new font used for dropdown items
        """

        self.__country_dropdown.setFont(font)
