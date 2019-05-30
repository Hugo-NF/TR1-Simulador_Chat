# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'connect.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import time

class Ui_connectionDialog(object):
    def setupUi(self, connectionDialog):
        connectionDialog.setObjectName("connectionDialog")
        connectionDialog.resize(518, 80)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(connectionDialog)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.linesLayout = QtWidgets.QVBoxLayout()
        self.linesLayout.setObjectName("linesLayout")
        self.hostLayout = QtWidgets.QHBoxLayout()
        self.hostLayout.setObjectName("hostLayout")
        self.hostLabel = QtWidgets.QLabel(connectionDialog)
        self.hostLabel.setObjectName("hostLabel")
        self.hostLayout.addWidget(self.hostLabel)
        self.hostEdit = QtWidgets.QLineEdit(connectionDialog)
        self.hostEdit.setText("")
        self.hostEdit.setObjectName("hostEdit")
        self.hostLayout.addWidget(self.hostEdit)
        self.linesLayout.addLayout(self.hostLayout)
        self.portLayout = QtWidgets.QHBoxLayout()
        self.portLayout.setObjectName("portLayout")
        self.portLabel = QtWidgets.QLabel(connectionDialog)
        self.portLabel.setObjectName("portLabel")
        self.portLayout.addWidget(self.portLabel)
        self.portEdit = QtWidgets.QLineEdit(connectionDialog)
        self.portEdit.setObjectName("portEdit")
        self.portLayout.addWidget(self.portEdit)
        self.linesLayout.addLayout(self.portLayout)
        self.horizontalLayout_3.addLayout(self.linesLayout)
        self.serverLayout = QtWidgets.QVBoxLayout()
        self.serverLayout.setObjectName("serverLayout")
        self.tcpRadioButton = QtWidgets.QRadioButton(connectionDialog)
        self.tcpRadioButton.setObjectName("tcpRadioButton")
        self.serverLayout.addWidget(self.tcpRadioButton)
        self.udpRadioButton = QtWidgets.QRadioButton(connectionDialog)
        self.udpRadioButton.setObjectName("udpRadioButton")
        self.serverLayout.addWidget(self.udpRadioButton)
        self.horizontalLayout_3.addLayout(self.serverLayout)
        self.progressLayout = QtWidgets.QVBoxLayout()
        self.progressLayout.setObjectName("progressLayout")
        self.connectionProgress = QtWidgets.QProgressBar(connectionDialog)
        self.connectionProgress.setProperty("value", 0)
        self.connectionProgress.setObjectName("connectionProgress")
        self.progressLayout.addWidget(self.connectionProgress)
        self.horizontalLayout_3.addLayout(self.progressLayout)
        self.connectButton = QtWidgets.QPushButton(connectionDialog)
        self.connectButton.setObjectName("connectButton")
        self.horizontalLayout_3.addWidget(self.connectButton)

        self.retranslateUi(connectionDialog)
        QtCore.QMetaObject.connectSlotsByName(connectionDialog)

    def retranslateUi(self, connectionDialog):
        _translate = QtCore.QCoreApplication.translate
        connectionDialog.setWindowTitle(_translate("connectionDialog", "Connection Properties"))
        self.hostLabel.setText(_translate("connectionDialog", "Host Address:"))
        self.hostEdit.setPlaceholderText(_translate("connectionDialog", "127.0.0.1"))
        self.portLabel.setText(_translate("connectionDialog", "Port:"))
        self.portEdit.setPlaceholderText(_translate("connectionDialog", "8080"))
        self.tcpRadioButton.setText(_translate("connectionDialog", "TCP"))
        self.udpRadioButton.setText(_translate("connectionDialog", "UDP"))
        self.connectionProgress.setFormat(_translate("connectionDialog", "Disconnected"))
        self.connectButton.setText(_translate("connectionDialog", "Connect"))

    def connect_animation(self):
        self.connectionProgress.show()
        self.connectionProgress.setFormat("Connecting...")

        for i in range(30):
            self.connectionProgress.setInvertedAppearance(False)
            for value in range(0,101):
                time.sleep(1)
                self.connectionProgress.setValue(value)
            self.connectionProgress.setInvertedAppearance(True)
            for value in range(101, -1, -1):
                time.sleep(1)
                self.connectionProgress.setValue(value)

