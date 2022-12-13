from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Auth(object):
    def setupUi(self, Dialog):
        Dialog.resize(1200, 720)
        self.login = QtWidgets.QTextEdit(Dialog)
        self.login.setGeometry(QtCore.QRect(450, 150, 300, 50))
        self.password = QtWidgets.QTextEdit(Dialog)
        self.password.setGeometry(QtCore.QRect(450, 250, 300, 50))
        self.btnMain = QtWidgets.QPushButton(Dialog)
        self.btnMain.setGeometry(QtCore.QRect(450, 350, 300, 50))
        self.btnReg = QtWidgets.QPushButton(Dialog)
        self.btnReg.setGeometry(QtCore.QRect(450, 450, 300, 50))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Авторизация"))
        self.btnReg.setText(_translate("Dialog", "Регистрация"))
        self.btnMain.setText(_translate("Dialog", "Авторизация"))