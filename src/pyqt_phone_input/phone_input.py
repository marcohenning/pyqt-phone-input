import os
from PyQt6 import QtCore
from qtpy.QtCore import QRegularExpression, QMargins
from qtpy.QtGui import QRegularExpressionValidator, QColor, QPalette, QIcon, QFont
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
        self.__padding = QMargins()
        self.__selection_foreground_color = None
        self.__selection_background_color = QColor(255,0,0)#self.palette().color(QPalette.ColorRole.Highlight)
        self.__focused_color = None
        self.__focused_background_color = None
        self.__focused_border_color = self.palette().color(QPalette.ColorRole.Highlight)
        self.__disabled_color = None
        self.__disabled_background_color = None
        self.__disabled_border_color = None

        # Phone number line edit
        self.__line_edit = PhoneLineEdit(self)
        self.__line_edit.setBorderWidth(self.__border_width)
        self.__line_edit.setPlaceholderText('Phone number')
        self.__line_edit.setValidator(QRegularExpressionValidator(QRegularExpression('[0-9 ]*')))

        # Country dropdown
        self.__combo_box = CountryDropdown(self)
        self.__combo_box.setBorderWidth(self.__border_width)
        self.__combo_box.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.__combo_box.show_popup.connect(self.__popup_shown)
        self.__combo_box.hide_popup.connect(self.__popup_hidden)
        self.__combo_box.geometry_changed.connect(self.__update_style_sheet)

        # Add countries to dropdown
        self.__directory = os.path.dirname(os.path.realpath(__file__))
        for country in countries:
            self.__combo_box.addItem(
                QIcon(self.__directory + '/flag_icons/{}.png'.format(country)),
                '{} ({})'.format(countries[country][0], countries[country][1]))

        self.__line_edit.setCountryDropdown(self.__combo_box)
        self.__line_edit.focus_in.connect(self.__update_line_edit_focus_in)
        self.__line_edit.focus_out.connect(self.__update_line_edit_focus_out)

        self.__calculate_geometry()
        self.__update_style_sheet()

    def __calculate_geometry(self):
        self.__line_edit.setFixedSize(self.width(), self.height())
        self.__combo_box.setFixedHeight(self.height() - self.__border_width * 2)
        self.__combo_box.move(self.__border_width, self.__border_width)
        self.__combo_box.view().setFixedWidth(self.__combo_box.minimumSizeHint().width())

    def __popup_shown(self):
        selection_foreground_color = None
        if self.__selection_foreground_color:
            selection_foreground_color = self.__selection_foreground_color
        elif self.__focused_color:
            selection_foreground_color = self.__focused_color
        else:
            selection_foreground_color = self.__color

        self.__line_edit.setStyleSheet('QLineEdit {'
                           'color: %s;'
                           'background-color: %s;'
                           'border: %dpx solid %s;'
                           'border-radius: %dpx;'
                           'padding: %d %d %d %dpx;'
                           'selection-color: %s;'
                           'selection-background-color: %s;'
                           '}' % (self.__color.name() if self.__focused_color is None else self.__focused_color.name(),
                                  self.__background_color.name() if self.__focused_background_color is None else self.__focused_background_color.name(),
                                  self.__border_width,
                                  self.__border_color.name() if self.__focused_border_color is None else self.__focused_border_color.name(),
                                  self.__border_radius,
                                  self.__padding.top(),
                                  self.__padding.right(),
                                  self.__padding.bottom(),
                                  self.__padding.left() + self.__combo_box.width() + self.__border_width * 2,
                                  selection_foreground_color.name(),
                                  self.__selection_background_color.name()
                                  ))
        self.__line_edit.setCurrentBorderColor(self.__border_color if self.__focused_border_color is None else self.__focused_border_color)

    def __popup_hidden(self):
        self.__update_style_sheet()
        if not self.__line_edit.hasFocus():
            self.__line_edit.setCurrentBorderColor(self.__border_color)

    def __update_line_edit_focus_in(self):
        self.__line_edit.setCurrentBorderColor(self.__border_color if self.__focused_border_color is None else self.__focused_border_color)

    def __update_line_edit_focus_out(self):
        if not self.__combo_box.popup_open:
            self.__line_edit.setCurrentBorderColor(self.__border_color)

    def __update_style_sheet(self):
        selection_foreground_color = None
        if self.__selection_foreground_color:
            selection_foreground_color = self.__selection_foreground_color
        elif self.__focused_color:
            selection_foreground_color = self.__focused_color
        else:
            selection_foreground_color = self.__color

        self.__line_edit.setStyleSheet('QLineEdit {'
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
                              self.__padding.left() + self.__combo_box.width() + self.__border_width * 2,
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

    def resizeEvent(self, event):
        self.__calculate_geometry()
        self.__update_style_sheet()

    def setDisabled(self, disabled: bool):
        self.__line_edit.setDisabled(disabled)
        self.__combo_box.setDisabled(disabled)

        if disabled:
            self.__update_style_sheet()
            self.__line_edit.setCurrentBorderColor(
                self.__border_color if self.__disabled_border_color is None else self.__disabled_border_color)
        else:
            if self.__line_edit.hasFocus() or self.__combo_box.popup_open:
                self.__line_edit.setCurrentBorderColor(
                    self.__border_color if self.__focused_border_color is None else self.__focused_border_color)
            else:
                self.__line_edit.setCurrentBorderColor(self.__border_color)

    def setSelectionForegroundColor(self, color: QColor):
        self.__selection_foreground_color = color
        self.__update_style_sheet()

    def setSelectionBackgroundColor(self, color: QColor):
        self.__selection_background_color = color
        self.__update_style_sheet()

    def setFont(self, font: QFont):
        self.__line_edit.setFont(font)
        self.__combo_box.setInputFont(font)

    def setDropdownFont(self, font: QFont):
        self.__combo_box.setFont(font)
