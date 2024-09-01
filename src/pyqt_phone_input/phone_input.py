import os
from PyQt6 import QtCore
from qtpy.QtCore import QRegularExpression, QMargins, QSize
from qtpy.QtGui import QRegularExpressionValidator, QColor, QPalette, QIcon
from qtpy.QtWidgets import QWidget, QLineEdit
from .country_dropdown import CountryDropdown
from .countries import countries


class PhoneInput(QWidget):

    def __init__(self, parent=None):
        super(PhoneInput, self).__init__(parent)

        self.__line_edit = QLineEdit(self)
        self.__line_edit.setPlaceholderText('Phone number')
        self.__line_edit.setValidator(QRegularExpressionValidator(QRegularExpression('[0-9]*')))

        self.__combo_box = CountryDropdown(self)
        self.__combo_box.setIconSize(QSize(24, 24))  # TODO: Replace placeholder values
        self.__combo_box.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.__combo_box.show_popup.connect(self.__popup_shown)
        self.__combo_box.hide_popup.connect(self.__popup_hidden)

        # Add countries to dropdown
        self.__directory = os.path.dirname(os.path.realpath(__file__))
        for country in countries:
            self.__combo_box.addItem(
                QIcon(self.__directory + '/flag_icons/{}.png'.format(country)),
                '{} ({})'.format(countries[country][0], countries[country][1]))

        # Styling options
        self.__color = QColor(0, 0, 0)
        self.__background_color = QColor(255, 255, 255)
        self.__border_color = self.palette().color(QPalette.ColorRole.Shadow)
        self.__placeholder_color = self.palette().color(QPalette.ColorRole.Shadow)
        self.__placeholder_color_outside = None
        self.__placeholder_color_current = self.__placeholder_color
        self.__border_width = 1
        self.__border_radius = 5
        self.__padding = QMargins()
        self.__hovered_color = None
        self.__hovered_background_color = None
        self.__hovered_border_color = None
        self.__hovered_border_width = None
        self.__focused_color = None
        self.__focused_background_color = None
        self.__focused_border_color = self.palette().color(QPalette.ColorRole.Highlight)
        self.__focused_border_width = None
        self.__disabled_color = None
        self.__disabled_background_color = None
        self.__disabled_border_color = None
        self.__disabled_border_width = None

        self.__calculate_geometry()
        self.__update_style_sheet()

    def __calculate_geometry(self):
        self.__line_edit.setFixedSize(self.width(), self.height())
        self.__combo_box.setFixedSize(self.__combo_box.getPreferredWidth(), self.height() - self.__border_width * 2)
        self.__combo_box.move(self.__border_width, self.__border_width)
        self.__combo_box.view().setFixedWidth(self.__combo_box.minimumSizeHint().width())

    def __popup_shown(self):
        # TODO: Replace placeholder with real stylesheet
        self.__line_edit.setStyleSheet('border: 1px solid %s; border-radius: %dpx; padding: 0px 0px 0px %dpx' % (self.__focused_border_color.name(), 5, self.__combo_box.width()))

    def __popup_hidden(self):
        self.__update_style_sheet()

    def __update_style_sheet(self):
        self.__line_edit.setStyleSheet('QLineEdit {'
                           'color: %s;'
                           'background-color: %s;'
                           'border: %dpx solid %s;'
                           'border-radius: %dpx;'
                           'padding: %d %d %d %dpx;'
                           '}'
                           'QLineEdit:hover {'
                           'color: %s;'
                           'background-color: %s;'
                           'border: %dpx solid %s;'
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
                              self.__padding.left() + self.__combo_box.width(),
                              self.__color.name() if self.__hovered_color is None else self.__hovered_color.name(),
                              self.__background_color.name() if self.__hovered_background_color is None else self.__hovered_background_color.name(),
                              self.__border_width if self.__hovered_border_width is None else self.__hovered_border_width,
                              self.__border_color.name() if self.__hovered_border_color is None else self.__hovered_border_color.name(),
                              self.__color.name() if self.__focused_color is None else self.__focused_color.name(),
                              self.__background_color.name() if self.__focused_background_color is None else self.__focused_background_color.name(),
                              self.__border_width if self.__focused_border_width is None else self.__focused_border_width,
                              self.__border_color.name() if self.__focused_border_color is None else self.__focused_border_color.name(),
                              self.__color.name() if self.__disabled_color is None else self.__disabled_color.name(),
                              self.__background_color.name() if self.__disabled_background_color is None else self.__disabled_background_color.name(),
                              self.__border_width if self.__disabled_border_width is None else self.__disabled_border_width,
                              self.__border_color.name() if self.__disabled_border_color is None else self.__disabled_border_color.name()))

        self.__combo_box.setStyleSheet('')

    def resizeEvent(self, event):
        self.__calculate_geometry()
        self.__update_style_sheet()
