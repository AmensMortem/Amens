# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainDesignWVDoDc.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QMetaObject, QRect, QSize, Qt)
from PyQt5.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(448, 390)
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.label_2, 2, 1, 1, 2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.mapOut = QLabel(Form)
        self.mapOut.setObjectName(u"mapOut")

        self.gridLayout.addWidget(self.mapOut, 0, 0, 1, 1)

        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(100, 100))

        self.radio_schema = QRadioButton(self.groupBox)
        self.radio_schema.setChecked(True)
        self.radio_schema.setGeometry(QRect(10, 30, 82, 17))

        self.radio_satellite = QRadioButton(self.groupBox)
        self.radio_satellite.setGeometry(QRect(10, 50, 82, 17))

        self.radio_hybrid = QRadioButton(self.groupBox)
        self.radio_hybrid.setGeometry(QRect(10, 70, 82, 17))

        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 1, Qt.AlignRight | Qt.AlignBottom)

        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 3)

        self.outButton = QPushButton(Form)
        self.outButton.setObjectName(u"outButton")

        self.gridLayout_2.addWidget(self.outButton, 4, 0, 1, 3)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 2, 2, 1, 1)

        self.yInput = QDoubleSpinBox(Form)
        self.yInput.setObjectName(u"yInput")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.yInput.sizePolicy().hasHeightForWidth())
        self.yInput.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.yInput, 3, 2, 1, 1)

        self.xInput = QDoubleSpinBox(Form)
        self.xInput.setObjectName(u"xInput")
        sizePolicy1.setHeightForWidth(self.xInput.sizePolicy().hasHeightForWidth())
        self.xInput.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.xInput, 3, 1, 1, 1)

        self.scaleInput = QSpinBox(Form)
        self.scaleInput.setObjectName(u"scaleInput")

        self.gridLayout_2.addWidget(self.scaleInput, 3, 0, 1, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u041a\u0430\u0440\u0442\u0430", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"X:", None))
        self.mapOut.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u0421\u043b\u043e\u0438", None))
        self.radio_schema.setText(QCoreApplication.translate("Form", u"\u0421\u0445\u0435\u043c\u0430", None))
        self.radio_satellite.setText(
            QCoreApplication.translate("Form", u"\u0421\u043f\u0443\u0442\u043d\u0438\u043a", None))
        self.radio_hybrid.setText(QCoreApplication.translate("Form", u"\u0413\u0438\u0431\u0440\u0438\u0434", None))
        self.outButton.setText(QCoreApplication.translate("Form", u"Output", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u041c\u0430\u0441\u0448\u0442\u0430\u0431:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Y:", None))
    # retranslateUi
