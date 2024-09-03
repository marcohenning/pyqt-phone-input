import os
from qtpy.QtCore import QMargins
from qtpy.QtGui import QColor, QPalette, QIcon, QFont
from qtpy.QtWidgets import QWidget
from .country_dropdown import CountryDropdown
from .phone_line_edit import PhoneLineEdit
from .countries import countries


class PhoneInput(QWidget):

    def __init__(self, parent=None):
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

        # Phone number line edit
        self.__phone_line_edit = PhoneLineEdit(self)
        self.__phone_line_edit.setBorderWidth(self.__border_width)

        # Country dropdown
        self.__country_dropdown = CountryDropdown(self)
        self.__country_dropdown.setBorderWidth(self.__border_width)
        self.__country_dropdown.show_popup.connect(self.__handle_popup_opened)
        self.__country_dropdown.hide_popup.connect(self.__handle_popup_closed)
        self.__country_dropdown.geometry_changed.connect(self.__update_line_edit_style_sheet)

        # Add countries to dropdown
        self.__directory = os.path.dirname(os.path.realpath(__file__))
        for country in countries:
            self.__country_dropdown.addItem(
                QIcon(self.__directory + '/flag_icons/{}.png'.format(country)),
                '{} ({})'.format(countries[country][0], countries[country][1]))

        # Set up phone number line edit
        self.__phone_line_edit.setCountryDropdown(self.__country_dropdown)
        self.__phone_line_edit.focus_in.connect(self.__handle_focus_in)
        self.__phone_line_edit.focus_out.connect(self.__handle_focus_out)

        # Update geometry and stylesheets
        self.__calculate_geometry()
        self.__update_line_edit_style_sheet()
        self.__update_combobox_style_sheet()

    def __calculate_geometry(self):
        self.__phone_line_edit.setFixedSize(self.width(), self.height())
        self.__country_dropdown.setFixedHeight(self.height())
        self.__country_dropdown.view().setFixedWidth(self.__country_dropdown.minimumSizeHint().width())

    def __handle_popup_opened(self):
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
        self.__update_line_edit_style_sheet()
        if not self.__phone_line_edit.hasFocus():
            self.__phone_line_edit.setCurrentBorderColor(self.__border_color)

    def __handle_focus_in(self):
        self.__phone_line_edit.setCurrentBorderColor(
            self.__border_color if self.__focused_border_color is None else self.__focused_border_color)

    def __handle_focus_out(self):
        if not self.__country_dropdown.popup_open:
            self.__phone_line_edit.setCurrentBorderColor(self.__border_color)

    def __update_line_edit_style_sheet(self):
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
        self.__calculate_geometry()
        self.__update_line_edit_style_sheet()
        self.__update_combobox_style_sheet()

    def setDisabled(self, disabled: bool):
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

    def setSelectionForegroundColor(self, color: QColor):
        self.__selection_foreground_color = color
        self.__update_line_edit_style_sheet()

    def setSelectionBackgroundColor(self, color: QColor):
        self.__selection_background_color = color
        self.__update_line_edit_style_sheet()

    def setFont(self, font: QFont):
        self.__phone_line_edit.setFont(font)
        self.__country_dropdown.setInputFont(font)

    def setDropdownFont(self, font: QFont):
        self.__country_dropdown.setFont(font)
