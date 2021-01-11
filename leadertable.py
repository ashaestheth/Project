import sys

import ui as ui
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(321, 402)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(30, 40, 261, 331))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label_leaderboard = QtWidgets.QLabel(Dialog)
        self.label_leaderboard.setGeometry(QtCore.QRect(30, 10, 271, 16))
        font = QtGui.QFont()
        font.setFamily("monaco")
        font.setPointSize(12)
        self.label_leaderboard.setFont(font)
        self.label_leaderboard.setObjectName("label_leaderboard")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_leaderboard.setText(_translate("Dialog", "таблица лидеров уровня Любитель"))

    def start_window(self):
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_Dialog()
        ui.setupUi(MainWindow)
        MainWindow.show()
