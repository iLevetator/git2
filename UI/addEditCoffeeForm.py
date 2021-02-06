# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 200)
        MainWindow.setMinimumSize(QtCore.QSize(500, 200))
        MainWindow.setMaximumSize(QtCore.QSize(500, 200))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(10, 110, 481, 81))
        self.table.setObjectName("table")
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        self.btn_new = QtWidgets.QPushButton(self.centralwidget)
        self.btn_new.setGeometry(QtCore.QRect(10, 10, 481, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_new.setFont(font)
        self.btn_new.setObjectName("btn_new")
        self.btn_edit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_edit.setGeometry(QtCore.QRect(310, 60, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_edit.setFont(font)
        self.btn_edit.setObjectName("btn_edit")
        self.ID = QtWidgets.QSpinBox(self.centralwidget)
        self.ID.setGeometry(QtCore.QRect(51, 60, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ID.setFont(font)
        self.ID.setMinimum(1)
        self.ID.setObjectName("ID")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 70, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btn_load = QtWidgets.QPushButton(self.centralwidget)
        self.btn_load.setGeometry(QtCore.QRect(110, 60, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_load.setFont(font)
        self.btn_load.setObjectName("btn_load")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Капучино"))
        self.btn_new.setText(_translate("MainWindow", "Новая запись"))
        self.btn_edit.setText(_translate("MainWindow", "Сохранить изменения"))
        self.label.setText(_translate("MainWindow", "ID"))
        self.btn_load.setText(_translate("MainWindow", "Отобразить запись"))
