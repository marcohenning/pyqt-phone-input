# PyQt Phone Input

[![PyPI](https://img.shields.io/badge/pypi-v1.0.0-blue)](https://pypi.org/project/pyqt-phone-input)
[![Python](https://img.shields.io/badge/python-3.7+-blue)](https://github.com/marcohenning/pyqt-phone-input)
[![License](https://img.shields.io/badge/license-MIT-green)](https://github.com/marcohenning/pyqt-phone-input/blob/master/LICENSE)
[![Coverage](https://img.shields.io/badge/coverage-90%25-neon)](https://github.com/marcohenning/pyqt-phone-input)
[![Build](https://img.shields.io/badge/build-passing-neon)](https://github.com/marcohenning/pyqt-phone-input)

A clean and modern phone number input widget for PyQt and PySide.

![Main](https://github.com/user-attachments/assets/b0d91e9a-a38f-45b9-9886-e1422c298b2c)

## About

The widget features a dropdown to select the country and a text field to input a phone number, both of which are highly customizable. The country dropdown offers exactly the same 235 countries / territories that Google's phone inputs do and displays the selected country's flag as well as its phone code. The flag icons used are modified versions of the icons available on [this repository](https://github.com/lipis/flag-icons).

## Installation

```
pip install pyqt-phone-input
```

## Example

```python
from PyQt6.QtWidgets import QMainWindow
from pyqt_phone_input import PhoneInput


class Window(QMainWindow):

    def __init__(self):
        super().__init__(parent=None)

        # Phone input
        self.phone_input = PhoneInput(self)
        self.phone_input.setBorderRadius(5)
        self.phone_input.setCountry('us')
        self.phone_input.setPlaceholderText('Phone number')
```

## Documentation

> **IMPORTANT:** <br>Styling of the widget must not be done by setting the stylesheet manually as the widget calculates the stylesheet itself and overrides it. Use the provided methods such as `setBackgroundColor()`, `setFocusedBackgroundColor()` and `setDisabledBackgroundColor()` instead.

* **Setting the current country:**
```python
phone_input.setCountry('us')  # United States
```

* **Getting the current country:**
```python
phone_input.getCountry()  # 'us'
```

* **Getting the current phone code:**
```python
phone_input.getCountryPhoneCode()  # '+1'
```

* **Getting the phone number:**
```python
# country = 'us', input = '1234567'
phone_input.getPhoneNumber()  # '+11234567'
```

* **Setting the text color:**
```python
phone_input.setColor(QColor(0, 0, 0))
```

* **Setting the background color:**
```python
phone_input.setBackgroundColor(QColor(255, 255, 255))
```

* **Setting the border color:**
```python
phone_input.setBorderColor(QColor(0, 0, 0))
```

* **Setting the border width:**
```python
phone_input.setBorderWidth(1)
```

* **Setting the border radius:**
```python
phone_input.setBorderRadius(5)
```

* **Setting the placeholder text:**
```python
phone_input.setPlaceholderText('Phone number')
```

**<br>All methods:**

| Method                                                         | Description                                                                                   |
|----------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| `getCountry(self)`                                             | Get the country code of the currently selected country                                        |
| `getCountryPhoneCode(self)`                                    | Get the phone code of the currently selected country                                          |
| `setCountry(self, country: str)`                               | Set the current country (by country code)                                                     |
| `getPhoneNumber(self)`                                         | Get the phone number (Returns country code and number from text field without any spaces)     |
| `setInput(self, input_number: str)`                            | Set the text field's input                                                                    |
| `getPlaceholderText(self)`                                     | Get the text field's current placeholder text                                                 |
| `setPlaceholderText(self, text: str)`                          | Set the text field's current placeholder text                                                 |
| `isDisabled(self)`                                             | Get whether the widget is currently disabled                                                  |
| `setDisabled(self, disabled: bool)`                            | Set whether the widget should be disabled                                                     |
| `setColor(self, color: QColor)`                                | Set the regular color of the text                                                             |
| `setBackgroundColor(self, color: QColor)`                      | Set the regular color of the background                                                       |
| `setBorderColor(self, color: QColor)`                          | Set the regular color of the border                                                           |
| `setBorderWidth(self, width: int)`                             | Set the width of the border                                                                   |
| `setBorderRadius(self, radius: int)`                           | Set the radius of the border                                                                  |
| `setPadding(self, padding: QMargins)`                          | Set the padding of the text field                                                             |
| `setFocusedColor(self, color: QColor)`                         | Set the text color for when the widget is focused                                             |
| `setFocusedBackgroundColor(self, color: QColor)`               | Set the background color for when the widget is focused                                       |
| `setFocusedBorderColor(self, color: QColor)`                   | Set the border color for when the widget is focused                                           |
| `setDisabledColor(self, color: QColor)`                        | Set the text color for when the widget is disabled                                            |
| `setDisabledBackgroundColor(self, color: QColor)`              | Set the background color for when the widget is disabled                                      |
| `setDisabledBorderColor(self, color: QColor)`                  | Set the border color for when the widget is disabled                                          |
| `setTextSelectionForegroundColor(self, color: QColor)`         | Set the foreground color of the text field's selection                                        |
| `setTextSelectionBackgroundColor(self, color: QColor)`         | Set the background color of the text field's selection                                        |
| `isDropdownItemHeightDynamic(self)`                            | Get whether the dropdown item height is dynamic (always the same height as the widget)        |
| `setDropdownItemHeightDynamic(self, dynamic: bool)`            | Set whether the dropdown item height should be dynamic (always the same height as the widget) |
| `setDropdownItemHeight(self, height: int)`                     | Set the dropdown item height (will only be used if dynamic height is disabled)                |
| `setDropdownItemSelectionForegroundColor(self, color: QColor)` | Set the foreground color of the selected dropdown item                                        |
| `setDropdownItemSelectionBackgroundColor(self, color: QColor)` | Set the background color of the selected dropdown item                                        |
| `setDropdownBorderColor(self, color: QColor)`                  | Set the border color of the dropdown window                                                   |
| `setFont(self, font: QFont)`                                   | Set the font used by text field and phone code of currently selected country                  |
| `setDropdownFont(self, font: QFont)`                           | Set the font used for the dropdown items                                                      |

## Countries

| Country Code | Country / Territory            | Phone Code |
|--------------|--------------------------------|------------|
| af           | Afghanistan                    | +93        |
| al           | Albania                        | +355       |
| dz           | Algeria                        | +213       |
| as           | American Samoa                 | +1         |
| ad           | Andorra                        | +376       |
| ao           | Angola                         | +244       |
| ai           | Anguilla                       | +1         |
| ag           | Antigua and Barbuda            | +1         |
| ar           | Argentina                      | +54        |
| am           | Armenia                        | +374       |
| aw           | Aruba                          | +297       |
| sh-ac        | Ascension Island               | +247       |
| au           | Australia                      | +61        |
| at           | Austria                        | +43        |
| az           | Azerbaijan                     | +994       |
| bs           | Bahamas                        | +1         |
| bh           | Bahrain                        | +973       |
| bd           | Bangladesh                     | +880       |
| bb           | Barbados                       | +1         |
| by           | Belarus                        | +375       |
| be           | Belgium                        | +32        |
| bz           | Belize                         | +501       |
| bj           | Benin                          | +229       |
| bm           | Bermuda                        | +1         |
| bt           | Bhutan                         | +975       |
| bo           | Bolivia                        | +591       |
| ba           | Bosnia and Herzegovina         | +387       |
| bw           | Botswana                       | +267       |
| br           | Brazil                         | +55        |
| io           | British Indian Ocean Territory | +246       |
| vg           | British Virgin Islands         | +1         |
| bn           | Brunei                         | +673       |
| bg           | Bulgaria                       | +359       |
| bf           | Burkina Faso                   | +226       |
| bi           | Burundi                        | +257       |
| kh           | Cambodia                       | +855       |
| cm           | Cameroon                       | +237       |
| ca           | Canada                         | +1         |
| cv           | Cape Verde                     | +238       |
| bq           | Caribbean Netherlands          | +599       |
| ky           | Cayman Islands                 | +1         |
| cf           | Central African Republic       | +236       |
| td           | Chad                           | +235       |
| cl           | Chile                          | +56        |
| cn           | China                          | +86        |
| co           | Colombia                       | +57        |
| km           | Comoros                        | +269       |
| cg           | Congo - Brazzaville            | +242       |
| cd           | Congo - Kinshasa               | +243       |
| ck           | Cook Islands                   | +682       |
| cr           | Costa Rica                     | +506       |
| ci           | Côte d'Ivoire                  | +225       |
| hr           | Croatia                        | +385       |
| cu           | Cuba                           | +53        |
| cw           | Curaçao                        | +599       |
| cy           | Cyprus                         | +357       |
| cz           | Czechia                        | +420       |
| dk           | Denmark                        | +45        |
| dj           | Djibouti                       | +253       |
| dm           | Dominica                       | +1         |
| do           | Dominican Republic             | +1         |
| ec           | Ecuador                        | +593       |
| eg           | Egypt                          | +20        |
| sv           | El Salvador                    | +503       |
| gq           | Equatorial Guinea              | +240       |
| er           | Eritrea                        | +291       |
| ee           | Estonia                        | +372       |
| sz           | Eswatini                       | +268       |
| et           | Ethiopia                       | +251       |
| fk           | Falkland Islands               | +500       |
| fo           | Faroe Islands                  | +298       |
| fj           | Fiji                           | +679       |
| fi           | Finland                        | +358       |
| fr           | France                         | +33        |
| gf           | French Guiana                  | +594       |
| pf           | French Polynesia               | +689       |
| ga           | Gabon                          | +241       |
| gm           | Gambia                         | +220       |
| ge           | Georgia                        | +995       |
| de           | Germany                        | +49        |
| gh           | Ghana                          | +233       |
| gi           | Gibraltar                      | +350       |
| gr           | Greece                         | +30        |
| gl           | Greenland                      | +299       |
| gd           | Grenada                        | +1         |
| gp           | Guadeloupe                     | +590       |
| gu           | Guam                           | +1         |
| gt           | Guatemala                      | +502       |
| gn           | Guinea                         | +224       |
| gw           | Guinea-Bissau                  | +245       |
| gy           | Guyana                         | +592       |
| ht           | Haiti                          | +509       |
| hn           | Honduras                       | +504       |
| hk           | Hong Kong                      | +852       |
| hu           | Hungary                        | +36        |
| is           | Iceland                        | +354       |
| in           | India                          | +91        |
| id           | Indonesia                      | +62        |
| ir           | Iran                           | +98        |
| iq           | Iraq                           | +964       |
| ie           | Ireland                        | +353       |
| il           | Israel                         | +972       |
| it           | Italy                          | +39        |
| jm           | Jamaica                        | +1         |
| jp           | Japan                          | +81        |
| jo           | Jordan                         | +962       |
| kz           | Kazakhstan                     | +7         |
| ke           | Kenya                          | +254       |
| ki           | Kiribati                       | +686       |
| xk           | Kosovo                         | +383       |
| kw           | Kuwait                         | +965       |
| kg           | Kyrgyzstan                     | +996       |
| la           | Laos                           | +856       |
| lv           | Latvia                         | +371       |
| lb           | Lebanon                        | +961       |
| ls           | Lesotho                        | +266       |
| lr           | Liberia                        | +231       |
| ly           | Libya                          | +218       |
| li           | Liechtenstein                  | +423       |
| lt           | Lithuania                      | +370       |
| lu           | Luxembourg                     | +352       |
| mo           | Macao                          | +853       |
| mg           | Madagascar                     | +261       |
| mw           | Malawi                         | +265       |
| my           | Malaysia                       | +60        |
| mv           | Maldives                       | +960       |
| ml           | Mali                           | +223       |
| mt           | Malta                          | +356       |
| mh           | Marshall Islands               | +692       |
| mq           | Martinique                     | +596       |
| mr           | Mauritania                     | +222       |
| mu           | Mauritius                      | +230       |
| mx           | Mexico                         | +52        |
| fm           | Micronesia                     | +691       |
| md           | Moldova                        | +373       |
| mc           | Monaco                         | +377       |
| mn           | Mongolia                       | +976       |
| me           | Montenegro                     | +382       |
| ms           | Montserrat                     | +1         |
| ma           | Morocco                        | +212       |
| mz           | Mozambique                     | +258       |
| mm           | Myanmar                        | +95        |
| na           | Namibia                        | +264       |
| nr           | Nauru                          | +674       |
| np           | Nepal                          | +977       |
| nl           | Netherlands                    | +31        |
| nc           | New Caledonia                  | +687       |
| nz           | New Zealand                    | +64        |
| ni           | Nicaragua                      | +505       |
| ne           | Niger                          | +227       |
| ng           | Nigeria                        | +234       |
| nu           | Niue                           | +683       |
| nf           | Norfolk Island                 | +672       |
| kp           | North Korea                    | +850       |
| mk           | North Macedonia                | +389       |
| mp           | Northern Mariana Islands       | +1         |
| no           | Norway                         | +47        |
| om           | Oman                           | +968       |
| pk           | Pakistan                       | +92        |
| pw           | Palau                          | +680       |
| ps           | Palestine                      | +970       |
| pa           | Panama                         | +507       |
| pg           | Papua New Guinea               | +675       |
| py           | Paraguay                       | +595       |
| pe           | Peru                           | +51        |
| ph           | Philippines                    | +63        |
| pl           | Poland                         | +48        |
| pt           | Portugal                       | +351       |
| pr           | Puerto Rico                    | +1         |
| qa           | Qatar                          | +974       |
| re           | Réunion                        | +262       |
| ro           | Romania                        | +40        |
| ru           | Russia                         | +7         |
| rw           | Rwanda                         | +250       |
| ws           | Samoa                          | +685       |
| sm           | San Marino                     | +378       |
| st           | São Tomé & Príncipe            | +239       |
| sa           | Saudi Arabia                   | +966       |
| sn           | Senegal                        | +221       |
| rs           | Serbia                         | +381       |
| sc           | Seychelles                     | +248       |
| sl           | Sierra Leone                   | +232       |
| sg           | Singapore                      | +65        |
| sx           | Sint Maarten                   | +1         |
| sk           | Slovakia                       | +421       |
| si           | Slovenia                       | +386       |
| sb           | Solomon Islands                | +677       |
| so           | Somalia                        | +252       |
| za           | South Africa                   | +27        |
| kr           | South Korea                    | +82        |
| ss           | South Sudan                    | +211       |
| es           | Spain                          | +34        |
| lk           | Sri Lanka                      | +94        |
| bl           | St. Barthélemy                 | +590       |
| sh-hl        | St. Helena                     | +290       |
| kn           | St. Kitts & Nevis              | +1         |
| lc           | St. Lucia                      | +1         |
| mf           | St. Martin                     | +590       |
| pm           | St. Pierre & Miquelon          | +508       |
| vc           | St. Vincent & Grenadines       | +1         |
| sd           | Sudan                          | +249       |
| sr           | Suriname                       | +597       |
| se           | Sweden                         | +46        |
| ch           | Switzerland                    | +41        |
| sy           | Syria                          | +963       |
| tw           | Taiwan                         | +886       |
| tj           | Tajikistan                     | +992       |
| tz           | Tanzania                       | +255       |
| th           | Thailand                       | +66        |
| tl           | Timor-Leste                    | +670       |
| tg           | Togo                           | +228       |
| tk           | Tokelau                        | +690       |
| to           | Tonga                          | +676       |
| tt           | Trinidad & Tobago              | +1         |
| tn           | Tunisia                        | +216       |
| tr           | Türkiye                        | +90        |
| tm           | Turkmenistan                   | +993       |
| tc           | Turks & Caicos Islands         | +1         |
| tv           | Tuvalu                         | +688       |
| vi           | U.S. Virgin Islands            | +1         |
| ug           | Uganda                         | +256       |
| ua           | Ukraine                        | +380       |
| ae           | United Arab Emirates           | +971       |
| gb           | United Kingdom                 | +44        |
| us           | United States                  | +1         |
| uy           | Uruguay                        | +598       |
| uz           | Uzbekistan                     | +998       |
| vu           | Vanuatu                        | +678       |
| va           | Vatican City                   | +39        |
| ve           | Venezuela                      | +58        |
| vn           | Vietnam                        | +84        |
| wf           | Wallis & Futuna                | +681       |
| ye           | Yemen                          | +967       |
| zm           | Zambia                         | +260       |
| zw           | Zimbabwe                       | +263       |

## License

This software is licensed under the [MIT license](https://github.com/marcohenning/pyqt-phone-input/blob/master/LICENSE).
