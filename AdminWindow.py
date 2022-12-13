from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Admin(object):
    def setupUi(self, Dialog):
        Dialog.resize(1200, 720)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Admin"))