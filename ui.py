# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(403, 357)
        MainWindow.setMaximumSize(QSize(403, 357))
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(9, 9, 384, 340))
        self._2 = QGridLayout(self.verticalLayoutWidget)
        self._2.setSpacing(7)
        self._2.setObjectName(u"_2")
        self._2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setFamily(u"\u5b8b\u4f53")
        font.setPointSize(14)
        self.label_3.setFont(font)

        self.horizontalLayout_5.addWidget(self.label_3)

        self.listenaddress = QComboBox(self.verticalLayoutWidget)
        self.listenaddress.setObjectName(u"listenaddress")
        self.listenaddress.setFont(font)
        self.listenaddress.setEditable(True)

        self.horizontalLayout_5.addWidget(self.listenaddress)

        self.horizontalLayout_5.setStretch(0, 2)
        self.horizontalLayout_5.setStretch(1, 5)

        self._2.addLayout(self.horizontalLayout_5, 3, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.connectaddress = QComboBox(self.verticalLayoutWidget)
        self.connectaddress.setObjectName(u"connectaddress")
        self.connectaddress.setFont(font)
        self.connectaddress.setEditable(True)

        self.horizontalLayout_3.addWidget(self.connectaddress)

        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 5)

        self._2.addLayout(self.horizontalLayout_3, 5, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.connectport = QLineEdit(self.verticalLayoutWidget)
        self.connectport.setObjectName(u"connectport")
        self.connectport.setFont(font)

        self.horizontalLayout_4.addWidget(self.connectport)

        self.horizontalLayout_4.setStretch(0, 2)
        self.horizontalLayout_4.setStretch(1, 5)

        self._2.addLayout(self.horizontalLayout_4, 6, 0, 1, 1)

        self.network_list = QListWidget(self.verticalLayoutWidget)
        self.network_list.setObjectName(u"network_list")
        font1 = QFont()
        font1.setFamily(u"Nirmala UI")
        font1.setPointSize(10)
        self.network_list.setFont(font1)
        self.network_list.setContextMenuPolicy(Qt.CustomContextMenu)

        self._2.addWidget(self.network_list, 1, 0, 1, 1)

        self.run = QPushButton(self.verticalLayoutWidget)
        self.run.setObjectName(u"run")
        self.run.setFont(font)
        self.run.setIconSize(QSize(20, 20))

        self._2.addWidget(self.run, 7, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.horizontalLayout_6.addWidget(self.label_5)

        self.listenport = QLineEdit(self.verticalLayoutWidget)
        self.listenport.setObjectName(u"listenport")
        self.listenport.setFont(font)

        self.horizontalLayout_6.addWidget(self.listenport)

        self.horizontalLayout_6.setStretch(0, 2)
        self.horizontalLayout_6.setStretch(1, 5)

        self._2.addLayout(self.horizontalLayout_6, 4, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(7)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.network = QComboBox(self.verticalLayoutWidget)
        self.network.addItem("")
        self.network.addItem("")
        self.network.addItem("")
        self.network.addItem("")
        self.network.setObjectName(u"network")
        self.network.setEnabled(False)
        self.network.setFont(font)
        self.network.setEditable(False)

        self.horizontalLayout.addWidget(self.network)

        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 7)

        self._2.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.run.clicked.connect(MainWindow.start)
        self.network_list.itemDoubleClicked.connect(MainWindow.edit_item)
        self.network_list.customContextMenuRequested.connect(MainWindow.my_listwidget_context)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u76d1\u542c\u5730\u5740", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u8fde\u63a5\u5730\u5740", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u8fde\u63a5\u7aef\u53e3", None))
        self.run.setText(QCoreApplication.translate("MainWindow", u"\u786e\u5b9a", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u76d1\u542c\u7aef\u53e3", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u7f51\u7edc", None))
        self.network.setItemText(0, QCoreApplication.translate("MainWindow", u"v4tov4", None))
        self.network.setItemText(1, QCoreApplication.translate("MainWindow", u"v4tov6", None))
        self.network.setItemText(2, QCoreApplication.translate("MainWindow", u"v6tov4", None))
        self.network.setItemText(3, QCoreApplication.translate("MainWindow", u"v6tov6", None))

        # if QT_CONFIG(tooltip)
        self.network.setToolTip(QCoreApplication.translate("MainWindow",
                                                           u"<html><head/><body><p>\u7531\u4e8eipv6\u4f7f\u7528\u8f83\u5c11\uff0c\u6682\u672a\u652f\u6301ipv6\u7aef\u53e3\u8f6c\u53d1\u8bbe\u7f6e</p></body></html>",
                                                           None))
# endif // QT_CONFIG(tooltip)
# retranslateUi
