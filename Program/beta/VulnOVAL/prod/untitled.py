# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1280, 720)
        Form.setStyleSheet(u"/*Copyright (c) DevSec Studio. All rights reserved.\n"
"\n"
"MIT License\n"
"\n"
"Permission is hereby granted, free of charge, to any person obtaining a copy\n"
"of this software and associated documentation files (the \"Software\"), to deal\n"
"in the Software without restriction, including without limitation the rights\n"
"to use, copy, modify, merge, publish, distribute, sublicense, and/or sell\n"
"copies of the Software, and to permit persons to whom the Software is\n"
"furnished to do so, subject to the following conditions:\n"
"\n"
"The above copyright notice and this permission notice shall be included in all\n"
"copies or substantial portions of the Software.\n"
"\n"
"THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n"
"IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n"
"FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\n"
"AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n"
"LIABILITY, WHETHER IN AN ACT"
                        "ION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\n"
"OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n"
"*/\n"
"\n"
"/*-----QWidget-----*/\n"
"QWidget\n"
"{\n"
"	background-color: #242424;\n"
"	color: #fff;\n"
"	selection-background-color: #fff;\n"
"	selection-color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QLabel-----*/\n"
"QLabel\n"
"{\n"
"	background-color: transparent;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QMenuBar-----*/\n"
"QMenuBar \n"
"{\n"
"	background-color: #4a5157;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::item \n"
"{\n"
"	background-color: transparent;\n"
"	border-left: 1px solid #003333;\n"
"	padding: 5px;\n"
"	padding-left: 15px;\n"
"	padding-right: 15px;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::item:selected \n"
"{\n"
"	background-color: #003333;\n"
"	border: 1px solid #006666;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::item:pressed \n"
"{\n"
"	background-color: #006666;\n"
"	border: 1px solid #006666;\n"
"	color: #fff;\n"
"\n"
"}"
                        "\n"
"\n"
"\n"
"/*-----QMenu-----*/\n"
"QMenu\n"
"{\n"
"    background-color: #4a5157;\n"
"    border: 1px solid #4a5157;\n"
"    padding: 10px;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::item\n"
"{\n"
"    background-color: transparent;\n"
"    padding: 2px 20px 2px 20px;\n"
"	min-width: 200px;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::separator\n"
"{\n"
"   	background-color: #242424;\n"
"	height: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::item:disabled\n"
"{\n"
"    color: #555;\n"
"    background-color: transparent;\n"
"    padding: 2px 20px 2px 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"	background-color: #003333;\n"
"	border: 1px solid #006666;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QToolButton-----*/\n"
"QToolButton \n"
"{\n"
"	background-color: transparent;\n"
"	color: #fff;\n"
"	padding: 3px;\n"
"	margin-left: 1px;\n"
"}\n"
"\n"
"\n"
"QToolButton:hover\n"
"{\n"
"	background-color: rgba(70,162,218,50%);\n"
"	border: 1px solid #46a2da;\n"
"	color: #000;\n"
"	\n"
"}\n"
"\n"
"\n"
"QToo"
                        "lButton:pressed\n"
"{\n"
"	background-color: #727272;\n"
"	border: 1px solid #46a2da;\n"
"\n"
"}\n"
"\n"
"\n"
"QToolButton:checked\n"
"{\n"
"	background-color: #727272;\n"
"	border: 1px solid #222;\n"
"}\n"
"\n"
"\n"
"/*-----QPushButton-----*/\n"
"QPushButton\n"
"{\n"
"	background-color: #4891b4;\n"
"	color: #fff;\n"
"	min-width: 80px;\n"
"	border-radius: 4px;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::flat\n"
"{\n"
"	background-color: transparent;\n"
"	border: none;\n"
"	color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::disabled\n"
"{\n"
"	background-color: #606060;\n"
"	color: #959595;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::hover\n"
"{\n"
"	background-color: #54aad3;\n"
"	border: 1px solid #46a2da;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"	background-color: #2385b4;\n"
"	border: 1px solid #46a2da;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::checked\n"
"{\n"
"	background-color: #bd5355;\n"
"	border: 1px solid #bd5355;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QLineEdit"
                        "-----*/\n"
"QLineEdit\n"
"{\n"
"	background-color: #242424;\n"
"	color : #fff;\n"
"	border: 1px solid #1d1d1d;\n"
"	padding: 3px;\n"
"	padding-left: 5px;\n"
"	border-radius: 4px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QPlainTExtEdit-----*/\n"
"QPlainTextEdit\n"
"{\n"
"	background-color: #242424;\n"
"	color : #fff;\n"
"	border: 1px solid #1d1d1d;\n"
"	padding: 3px;\n"
"	padding-left: 5px;\n"
"	border-radius: 4px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QToolBox-----*/\n"
"QToolBox\n"
"{\n"
"	background-color: transparent;\n"
"	border: 1px solid #1d1d1d;\n"
"\n"
"}\n"
"\n"
"\n"
"QToolBox::tab\n"
"{\n"
"	background-color: #002b2b;\n"
"	border: 1px solid #1d1d1d;\n"
"\n"
"}\n"
"\n"
"\n"
"QToolBox::tab:hover\n"
"{\n"
"	background-color: #006d6d;\n"
"	border: 1px solid #1d1d1d;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QComboBox-----*/\n"
"QComboBox\n"
"{\n"
"    background-color: #4a5157;\n"
"    padding-left: 6px;\n"
"    color: #fff;\n"
"    height: 20px;\n"
"	border-radius: 4px;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox::disabled\n"
"{\n"
"	ba"
                        "ckground-color: #404040;\n"
"	color: #656565;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox:on\n"
"{\n"
"    background-color: #4a5157;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    background-color: #4a5157;\n"
"    color: #fff;\n"
"    selection-background-color: #002b2b;\n"
"	selection-color: #fff;\n"
"    outline: 0;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"	background-color: #4a5157;\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"	border-radius: 4px;\n"
"    width: 15px;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"    image: url(://arrow-down.png);\n"
"    width: 8px;\n"
"    height: 8px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QDoubleSpinBox & QCalendarWidget-----*/\n"
"QDoubleSpinBox,\n"
"QCalendarWidget QSpinBox \n"
"{\n"
"	background-color: #242424;\n"
"	color : #fff;\n"
"	border: 1px solid #1d1d1d;\n"
"	border-radius: 4px;\n"
"	padding: 3px;\n"
"	padding-left: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QDo"
                        "ubleSpinBox::up-button, \n"
"QCalendarWidget QSpinBox::up-button\n"
"{\n"
"	background-color: #4a5157;\n"
"    width: 16px; \n"
"	border-top-right-radius: 4px;\n"
"    border-width: 1px;\n"
"	border-color: #1d1d1d;\n"
"\n"
"}\n"
"\n"
"\n"
"QDoubleSpinBox::up-button:hover, \n"
"QCalendarWidget QSpinBox::up-button:hover\n"
"{\n"
"	background-color: #585858;\n"
"\n"
"}\n"
"\n"
"\n"
"QDoubleSpinBox::up-button:pressed, \n"
"QCalendarWidget QSpinBox::up-button:pressed\n"
"{\n"
"	background-color: #252525;\n"
"    width: 16px; \n"
"    border-width: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QDoubleSpinBox::up-arrow,\n"
"QCalendarWidget QSpinBox::up-arrow\n"
"{\n"
"    image: url(://arrow-up.png);\n"
"    width: 7px;\n"
"    height: 7px;\n"
"\n"
"}\n"
"\n"
"\n"
"QDoubleSpinBox::down-button, \n"
"QCalendarWidget QSpinBox::down-button\n"
"{\n"
"	background-color: #4a5157;\n"
"    width: 16px; \n"
"    border-width: 1px;\n"
"	border-bottom-right-radius: 4px;\n"
"	border-color: #1d1d1d;\n"
"\n"
"}\n"
"\n"
"\n"
"QDoubleSpinBox::down-b"
                        "utton:hover, \n"
"QCalendarWidget QSpinBox::down-button:hover\n"
"{\n"
"	background-color: #585858;\n"
"\n"
"}\n"
"\n"
"\n"
"QDoubleSpinBox::down-button:pressed, \n"
"QCalendarWidget QSpinBox::down-button:pressed\n"
"{\n"
"	background-color: #252525;\n"
"    width: 16px; \n"
"    border-width: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QDoubleSpinBox::down-arrow,\n"
"QCalendarWidget QSpinBox::down-arrow\n"
"{\n"
"    image: url(://arrow-down.png);\n"
"    width: 7px;\n"
"    height: 7px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QGroupBox-----*/\n"
"QGroupBox \n"
"{\n"
"    border: 1px solid;\n"
"    border-color: #1d1d1d;\n"
"	border-radius: 4px;\n"
"    margin-top: 23px;\n"
"\n"
"}\n"
"\n"
"\n"
"QGroupBox::title  \n"
"{\n"
"    background-color: #002b2b;\n"
"    color: #fff;\n"
"	subcontrol-position: top left;\n"
"    subcontrol-origin: margin;\n"
"    padding: 5px;\n"
"	min-width: 100px;\n"
"	border: 1px solid #1d1d1d;\n"
"	border-top-left-radius: 4px;\n"
"	border-top-right-radius: 4px;\n"
"	border-bottom: none;\n"
"\n"
"}\n"
"\n"
""
                        "\n"
"/*-----QHeaderView-----*/\n"
"QHeaderView::section\n"
"{\n"
"    background-color: #4a5157;\n"
"	border: none;\n"
"    color: #fff;\n"
"	padding: 4px;\n"
"	\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:disabled\n"
"{\n"
"    background-color: #525251;\n"
"    color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:checked\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(227, 227, 227, 255),stop:1 rgba(187, 187, 187, 255));\n"
"    color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::vertical::first,\n"
"QHeaderView::section::vertical::only-one\n"
"{\n"
"    border-left: 1px solid #003333;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::vertical\n"
"{\n"
"    border-left: 1px solid #003333;\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::horizontal::first,\n"
"QHeaderView::section::horizontal::only-one\n"
"{\n"
"    border-left: 1px solid #003333;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::horizontal\n"
"{\n"
"    border-left: 1px solid #003333;\n"
"\n"
""
                        "}\n"
"\n"
"\n"
"QTableCornerButton::section\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(227, 227, 227, 255),stop:1 rgba(187, 187, 187, 255));\n"
"	border: 1px solid #000;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QCalendarWidget-----*/\n"
"QCalendarWidget QToolButton\n"
"{\n"
"  	background-color: transparent;\n"
"  	color: white;\n"
"\n"
"}\n"
"\n"
"\n"
"QCalendarWidget QToolButton::hover\n"
"{\n"
"	background-color: #006666;\n"
"	border: 1px solid #006666;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QCalendarWidget QMenu \n"
"{\n"
"	width: 120px;\n"
"	left: 20px;\n"
"	color: white;\n"
"\n"
"}\n"
"\n"
"\n"
"QCalendarWidget QWidget \n"
"{ \n"
"	alternate-background-color: #4a5157; \n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QCalendarWidget QAbstractItemView:enabled \n"
"{\n"
"	color: #fff;  \n"
"	background-color: #242424;  \n"
"	selection-background-color: #002b2b; \n"
"	selection-color: #fff; \n"
"\n"
"}\n"
"\n"
"\n"
"QCalendarWidget QAbstractI"
                        "temView:disabled \n"
"{ \n"
"	color: #404040; \n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QTreeWidget-----*/\n"
"QTreeView\n"
"{\n"
"	show-decoration-selected: 0;\n"
"	alternate-background-color: transparent;\n"
"	background-color: transparent;\n"
"   	border: none;\n"
"	color: #fff;\n"
"	font: 8pt;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::item:selected\n"
"{\n"
"	color:#fff;\n"
"	background-color: #002b2b;\n"
"	border-radius: 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::item:!selected:hover\n"
"{\n"
"    background-color: #5e5e5e;\n"
"    border: none;\n"
"    color: white;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed,\n"
"QTreeView::branch:closed:has-children:has-siblings \n"
"{\n"
"	image: url(://tree-closed.png);\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::branch:open:has-children:!has-siblings,\n"
"QTreeView::branch:open:has-children:has-siblings  \n"
"{\n"
"	image: url(://tree-open.png);\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QListView-----*/\n"
"QListView \n"
"{\n"
"	background-color: transparent;\n"
"	alt"
                        "ernate-background-color: transparent;\n"
"    border : none;\n"
"    color: #fff;\n"
"    show-decoration-selected: 1; \n"
"    outline: 0;\n"
"   	border: 1px solid #1d1d1d;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::disabled \n"
"{\n"
"	background-color: #656565;\n"
"	color: #1b1b1b;\n"
"    border: 1px solid #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item \n"
"{\n"
"	background-color: transparent;\n"
"    padding: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:selected \n"
"{\n"
"	background-color: #002b2b;\n"
"	border: 1px solid #002b2b;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:selected:!active \n"
"{\n"
"	background-color: #002b2b;\n"
"	border: 1px solid #002b2b;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:selected:active \n"
"{\n"
"	background-color: #002b2b;\n"
"	border: 1px solid #002b2b;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:hover {\n"
"    background-color: #5e5e5e;\n"
"    border: none;\n"
"    color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QCheckBox----"
                        "-*/\n"
"QCheckBox\n"
"{\n"
"	background-color: transparent;\n"
"    color: #fff;\n"
"	border: none;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator\n"
"{\n"
"    background-color: lightgray;\n"
"    border: 1px solid #000;\n"
"    width: 12px;\n"
"    height: 12px;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    image:url(\"./ressources/check.png\");\n"
"	background-color: #002b2b;\n"
"    border: 1px solid #3a546e;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:unchecked:hover\n"
"{\n"
"	border: 1px solid #46a2da; \n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::disabled\n"
"{\n"
"	color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:disabled\n"
"{\n"
"	background-color: #656565;\n"
"	color: #656565;\n"
"    border: 1px solid #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QRadioButton-----*/\n"
"QRadioButton \n"
"{\n"
"	color: #fff;\n"
"	background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator::unchecked:hover \n"
"{\n"
"	background-color: #d3d3d3;\n"
"	border: 2px solid #002b2b"
                        ";\n"
"	border-radius: 6px;\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator::checked \n"
"{\n"
"	border: 2px solid #52beff;\n"
"	border-radius: 6px;\n"
"	background-color: #002b2b;  \n"
"	width: 9px; \n"
"	height: 9px; \n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QScrollBar-----*/\n"
"QScrollBar:vertical \n"
"{\n"
"   border: none;\n"
"   width: 12px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:vertical \n"
"{\n"
"   border: none;\n"
"   border-radius : 0px;\n"
"   background-color: #7a7a7a;\n"
"   min-height: 80px;\n"
"   width : 12px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:vertical:pressed\n"
"{\n"
"   background-color: #5d5f60; \n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"   border: none;\n"
"   background: transparent;\n"
"   height: 0px;\n"
"   subcontrol-position: bottom;\n"
"   subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical:hover \n"
"{\n"
"   background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical:pressed \n"
"{\n"
"   background"
                        "-color: #3f3f3f;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"   border: none;\n"
"   background: transparent;\n"
"   height: 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:vertical:hover \n"
"{\n"
"   background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:vertical:pressed \n"
"{\n"
"   background-color: #3f3f3f;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:vertical\n"
"{\n"
"   width: 0px;\n"
"   height: 0px;\n"
"   background: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::down-arrow:vertical \n"
"{\n"
"   width: 0px;\n"
"   height: 0px;\n"
"   background: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"   background-color: #222222;\n"
"	\n"
"}\n"
"\n"
"\n"
"QScrollBar:horizontal \n"
"{\n"
"   border: none;\n"
"   height: 12px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:horizontal \n"
"{\n"
"   border: none;\n"
"   border-radius : 0px;\n"
"   background-color: #7a7a7a;\n"
"   min-height: 80px;\n"
""
                        "   height : 12px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:horizontal:pressed\n"
"{\n"
"   background-color: #5d5f60; \n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:horizontal\n"
"{\n"
"   border: none;\n"
"   background: transparent;\n"
"   height: 0px;\n"
"   subcontrol-position: bottom;\n"
"   subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:horizontal:hover \n"
"{\n"
"   background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:horizontal:pressed \n"
"{\n"
"   background-color: #3f3f3f;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:horizontal\n"
"{\n"
"   border: none;\n"
"   background: transparent;\n"
"   height: 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:horizontal:hover \n"
"{\n"
"   background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:horizontal:pressed \n"
"{\n"
"   background-color: #3f3f3f;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:horizontal\n"
"{\n"
"   width: 0px;\n"
"   height: 0px;\n"
"   background: transparent;"
                        "\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::down-arrow:horizontal \n"
"{\n"
"   width: 0px;\n"
"   height: 0px;\n"
"   background: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"   background-color: #222222;\n"
"	\n"
"}\n"
"\n"
"\n"
"/*-----QProgressBar-----*/\n"
"QProgressBar\n"
"{\n"
"	border: 1px solid #1d1d1d;\n"
"    text-align: center;\n"
"	border-radius: 10px;\n"
"	color: #fff;\n"
"	font-weight: bold;\n"
"\n"
"}\n"
"\n"
"\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: #3b86ae;\n"
"	border-radius: 9px;\n"
"    margin: 0.5px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QStatusBar-----*/\n"
"QStatusBar\n"
"{\n"
"	background-color: #4a5157;\n"
"	color: #ffffff;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QSizeGrip-----*/\n"
"QSizeGrip \n"
"{\n"
"	background-color: image(\"./ressources/sizegrip.png\"); /*To replace*/\n"
"	border: none;\n"
"\n"
"}\n"
"")
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget_with_menus = QWidget(Form)
        self.widget_with_menus.setObjectName(u"widget_with_menus")
        self.verticalLayout = QVBoxLayout(self.widget_with_menus)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget_with_menus)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setTextFormat(Qt.TextFormat.RichText)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setWordWrap(False)

        self.verticalLayout.addWidget(self.label)

        self.bt_OVAL_page = QPushButton(self.widget_with_menus)
        self.bt_OVAL_page.setObjectName(u"bt_OVAL_page")
        sizePolicy.setHeightForWidth(self.bt_OVAL_page.sizePolicy().hasHeightForWidth())
        self.bt_OVAL_page.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(False)
        self.bt_OVAL_page.setFont(font1)

        self.verticalLayout.addWidget(self.bt_OVAL_page)

        self.bt_XCCDF_page = QPushButton(self.widget_with_menus)
        self.bt_XCCDF_page.setObjectName(u"bt_XCCDF_page")
        sizePolicy.setHeightForWidth(self.bt_XCCDF_page.sizePolicy().hasHeightForWidth())
        self.bt_XCCDF_page.setSizePolicy(sizePolicy)
        self.bt_XCCDF_page.setFont(font1)

        self.verticalLayout.addWidget(self.bt_XCCDF_page)

        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 4)
        self.verticalLayout.setStretch(2, 4)

        self.gridLayout.addWidget(self.widget_with_menus, 0, 0, 1, 1)

        self.stackedWidget = QStackedWidget(Form)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.OVAL_page = QWidget()
        self.OVAL_page.setObjectName(u"OVAL_page")
        self.verticalLayout_2 = QVBoxLayout(self.OVAL_page)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Widget_withOVALlabel = QWidget(self.OVAL_page)
        self.Widget_withOVALlabel.setObjectName(u"Widget_withOVALlabel")
        self.horizontalLayout = QHBoxLayout(self.Widget_withOVALlabel)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_OVAL = QLabel(self.Widget_withOVALlabel)
        self.label_OVAL.setObjectName(u"label_OVAL")
        font2 = QFont()
        font2.setPointSize(52)
        font2.setBold(True)
        self.label_OVAL.setFont(font2)

        self.horizontalLayout.addWidget(self.label_OVAL)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addWidget(self.Widget_withOVALlabel)

        self.Widget_withOVALchoose = QWidget(self.OVAL_page)
        self.Widget_withOVALchoose.setObjectName(u"Widget_withOVALchoose")
        self.horizontalLayout_2 = QHBoxLayout(self.Widget_withOVALchoose)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_OS = QLabel(self.Widget_withOVALchoose)
        self.label_OS.setObjectName(u"label_OS")
        font3 = QFont()
        font3.setPointSize(9)
        self.label_OS.setFont(font3)

        self.horizontalLayout_2.addWidget(self.label_OS)

        self.Cb_chooseos = QComboBox(self.Widget_withOVALchoose)
        self.Cb_chooseos.addItem("")
        self.Cb_chooseos.addItem("")
        self.Cb_chooseos.addItem("")
        self.Cb_chooseos.addItem("")
        self.Cb_chooseos.addItem("")
        self.Cb_chooseos.setObjectName(u"Cb_chooseos")

        self.horizontalLayout_2.addWidget(self.Cb_chooseos)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.bt_OVALcheck = QPushButton(self.Widget_withOVALchoose)
        self.bt_OVALcheck.setObjectName(u"bt_OVALcheck")
        font4 = QFont()
        font4.setPointSize(8)
        self.bt_OVALcheck.setFont(font4)

        self.horizontalLayout_2.addWidget(self.bt_OVALcheck)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 4)
        self.horizontalLayout_2.setStretch(2, 8)
        self.horizontalLayout_2.setStretch(3, 4)

        self.verticalLayout_2.addWidget(self.Widget_withOVALchoose)

        self.table_OVAL_results = QTableWidget(self.OVAL_page)
        if (self.table_OVAL_results.columnCount() < 3):
            self.table_OVAL_results.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_OVAL_results.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_OVAL_results.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_OVAL_results.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.table_OVAL_results.setObjectName(u"table_OVAL_results")
        self.table_OVAL_results.setSortingEnabled(True)
        self.table_OVAL_results.setColumnCount(3)
        self.table_OVAL_results.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_2.addWidget(self.table_OVAL_results)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 8)
        self.stackedWidget.addWidget(self.OVAL_page)
        self.XCCDF_page = QWidget()
        self.XCCDF_page.setObjectName(u"XCCDF_page")
        self.verticalLayout_3 = QVBoxLayout(self.XCCDF_page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.Widget_withXCCDFlabel = QWidget(self.XCCDF_page)
        self.Widget_withXCCDFlabel.setObjectName(u"Widget_withXCCDFlabel")
        self.horizontalLayout_3 = QHBoxLayout(self.Widget_withXCCDFlabel)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.label_XCCDF = QLabel(self.Widget_withXCCDFlabel)
        self.label_XCCDF.setObjectName(u"label_XCCDF")
        self.label_XCCDF.setFont(font2)

        self.horizontalLayout_3.addWidget(self.label_XCCDF)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)


        self.verticalLayout_3.addWidget(self.Widget_withXCCDFlabel)

        self.Widget_withXCCDFchoose = QWidget(self.XCCDF_page)
        self.Widget_withXCCDFchoose.setObjectName(u"Widget_withXCCDFchoose")
        self.horizontalLayout_4 = QHBoxLayout(self.Widget_withXCCDFchoose)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_OS_2 = QLabel(self.Widget_withXCCDFchoose)
        self.label_OS_2.setObjectName(u"label_OS_2")
        self.label_OS_2.setFont(font3)

        self.horizontalLayout_4.addWidget(self.label_OS_2)

        self.Cb_chooseos_2 = QComboBox(self.Widget_withXCCDFchoose)
        self.Cb_chooseos_2.addItem("")
        self.Cb_chooseos_2.addItem("")
        self.Cb_chooseos_2.addItem("")
        self.Cb_chooseos_2.addItem("")
        self.Cb_chooseos_2.addItem("")
        self.Cb_chooseos_2.setObjectName(u"Cb_chooseos_2")

        self.horizontalLayout_4.addWidget(self.Cb_chooseos_2)

        self.ssh_checkbox = QCheckBox(self.Widget_withXCCDFchoose)
        self.ssh_checkbox.setObjectName(u"ssh_checkbox")

        self.horizontalLayout_4.addWidget(self.ssh_checkbox)

        self.label_2 = QLabel(self.Widget_withXCCDFchoose)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.login_edit = QPlainTextEdit(self.Widget_withXCCDFchoose)
        self.login_edit.setObjectName(u"login_edit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.login_edit.sizePolicy().hasHeightForWidth())
        self.login_edit.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.login_edit)

        self.label_3 = QLabel(self.Widget_withXCCDFchoose)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.pass_edit = QPlainTextEdit(self.Widget_withXCCDFchoose)
        self.pass_edit.setObjectName(u"pass_edit")
        sizePolicy1.setHeightForWidth(self.pass_edit.sizePolicy().hasHeightForWidth())
        self.pass_edit.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.pass_edit)

        self.label_4 = QLabel(self.Widget_withXCCDFchoose)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.ip_edit = QPlainTextEdit(self.Widget_withXCCDFchoose)
        self.ip_edit.setObjectName(u"ip_edit")
        sizePolicy1.setHeightForWidth(self.ip_edit.sizePolicy().hasHeightForWidth())
        self.ip_edit.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.ip_edit)

        self.label_5 = QLabel(self.Widget_withXCCDFchoose)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_4.addWidget(self.label_5)

        self.port_edit = QPlainTextEdit(self.Widget_withXCCDFchoose)
        self.port_edit.setObjectName(u"port_edit")
        sizePolicy1.setHeightForWidth(self.port_edit.sizePolicy().hasHeightForWidth())
        self.port_edit.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.port_edit)

        self.checkb_remediation = QCheckBox(self.Widget_withXCCDFchoose)
        self.checkb_remediation.setObjectName(u"checkb_remediation")

        self.horizontalLayout_4.addWidget(self.checkb_remediation)

        self.bt_XCCDFcheck = QPushButton(self.Widget_withXCCDFchoose)
        self.bt_XCCDFcheck.setObjectName(u"bt_XCCDFcheck")
        self.bt_XCCDFcheck.setFont(font4)

        self.horizontalLayout_4.addWidget(self.bt_XCCDFcheck)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 2)
        self.horizontalLayout_4.setStretch(2, 1)
        self.horizontalLayout_4.setStretch(3, 1)
        self.horizontalLayout_4.setStretch(4, 5)
        self.horizontalLayout_4.setStretch(5, 1)
        self.horizontalLayout_4.setStretch(6, 5)
        self.horizontalLayout_4.setStretch(7, 1)
        self.horizontalLayout_4.setStretch(8, 5)
        self.horizontalLayout_4.setStretch(9, 1)
        self.horizontalLayout_4.setStretch(10, 5)
        self.horizontalLayout_4.setStretch(11, 8)
        self.horizontalLayout_4.setStretch(12, 11)

        self.verticalLayout_3.addWidget(self.Widget_withXCCDFchoose)

        self.table_XCCDF_results = QTableWidget(self.XCCDF_page)
        if (self.table_XCCDF_results.columnCount() < 4):
            self.table_XCCDF_results.setColumnCount(4)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_XCCDF_results.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_XCCDF_results.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_XCCDF_results.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_XCCDF_results.setHorizontalHeaderItem(3, __qtablewidgetitem6)
        self.table_XCCDF_results.setObjectName(u"table_XCCDF_results")
        self.table_XCCDF_results.setSortingEnabled(True)
        self.table_XCCDF_results.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_3.addWidget(self.table_XCCDF_results)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 1)
        self.verticalLayout_3.setStretch(2, 8)
        self.stackedWidget.addWidget(self.XCCDF_page)

        self.gridLayout.addWidget(self.stackedWidget, 0, 1, 1, 1)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 5)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"<p style=\"line-height: 0.5;\">\n"
"<html><head/><body><p>SCAP</p><p>Scan</p></body></html>", None))
        self.bt_OVAL_page.setText(QCoreApplication.translate("Form", u"OVAL", None))
        self.bt_XCCDF_page.setText(QCoreApplication.translate("Form", u"XCCDF", None))
        self.label_OVAL.setText(QCoreApplication.translate("Form", u"OVAL", None))
        self.label_OS.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 OC", None))
        self.Cb_chooseos.setItemText(0, QCoreApplication.translate("Form", u"Debian 11", None))
        self.Cb_chooseos.setItemText(1, QCoreApplication.translate("Form", u"Kali Linux", None))
        self.Cb_chooseos.setItemText(2, QCoreApplication.translate("Form", u"Debian 12", None))
        self.Cb_chooseos.setItemText(3, QCoreApplication.translate("Form", u"Rocky Linux 9", None))
        self.Cb_chooseos.setItemText(4, QCoreApplication.translate("Form", u"RHEL 9", None))

        self.bt_OVALcheck.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c \u043f\u0440\u043e\u0432\u0435\u0440\u043a\u0443 \u043f\u043e OVAL \u0434\u0435\u0444\u0438\u043d\u0438\u0446\u0438\u044f\u043c", None))
        ___qtablewidgetitem = self.table_OVAL_results.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"CVE", None));
        ___qtablewidgetitem1 = self.table_OVAL_results.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"\u0421\u0442\u0430\u0442\u0443\u0441", None));
        ___qtablewidgetitem2 = self.table_OVAL_results.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 CVE", None));
        self.label_XCCDF.setText(QCoreApplication.translate("Form", u"XCCDF", None))
        self.label_OS_2.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 OC", None))
        self.Cb_chooseos_2.setItemText(0, QCoreApplication.translate("Form", u"Debian 11", None))
        self.Cb_chooseos_2.setItemText(1, QCoreApplication.translate("Form", u"Kali Linux", None))
        self.Cb_chooseos_2.setItemText(2, QCoreApplication.translate("Form", u"Debian 12", None))
        self.Cb_chooseos_2.setItemText(3, QCoreApplication.translate("Form", u"Rocky Linux 9", None))
        self.Cb_chooseos_2.setItemText(4, QCoreApplication.translate("Form", u"RHEL 9", None))

        self.ssh_checkbox.setText(QCoreApplication.translate("Form", u"ssh", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"login", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"pass", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"IP", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"port", None))
        self.checkb_remediation.setText(QCoreApplication.translate("Form", u"\u0418\u0441\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0443\u044f\u0437\u0432\u0438\u043c\u043e\u0441\u0442\u0435\u0439", None))
        self.bt_XCCDFcheck.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c \u043f\u0440\u043e\u0432\u0435\u0440\u043a\u0443 \u043f\u043e XCCDF", None))
        ___qtablewidgetitem3 = self.table_XCCDF_results.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u0430\u0432\u0438\u043b\u043e", None));
        ___qtablewidgetitem4 = self.table_XCCDF_results.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"\u0421\u0442\u0430\u0442\u0443\u0441", None));
        ___qtablewidgetitem5 = self.table_XCCDF_results.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"\u0412\u0430\u0436\u043d\u043e\u0441\u0442\u044c", None));
        ___qtablewidgetitem6 = self.table_XCCDF_results.horizontalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"\u0418\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u044f \u043f\u043e \u0438\u0441\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044e", None));
    # retranslateUi

