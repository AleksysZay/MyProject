from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
SERVER_NAME = 'DESKTOP-SB4T1AO\SQLEXPRESS'
DATABASE_NAME = 'WSAppDB'


def Conn():  # function for connect to db
    connString = f'DRIVER={{SQL Server}};' \
                 f'SERVER={SERVER_NAME};' \
                 f'DATABASE={DATABASE_NAME}'
    global db
    db = QSqlDatabase.addDatabase('QODBC')
    db.setDatabaseName(connString)
    if db.open():
        print('Connected to SQL Server successfully')
        return True
    else:
        print('Connection failed')
        return False


# --------------------------------------------------------


def Query(sqlQuery):  # function for fulfill sqlQuery
    query = QSqlQuery(db)
    query.prepare(sqlQuery)
    query.exec()
# --------------------------------------------------------


class Ui_Reg(object):
    def setupUi(self, Dialog):
        Dialog.resize(1200, 720)
        self.Name = QtWidgets.QLineEdit(Dialog)
        self.Name.setGeometry(QtCore.QRect(450, 40, 300, 50))
        self.DOB = QtWidgets.QLineEdit(Dialog)
        self.DOB.setGeometry(QtCore.QRect(450, 100, 300, 50))
        self.Age = QtWidgets.QLineEdit(Dialog)
        self.Age.setGeometry(QtCore.QRect(450, 160, 300, 50))
        self.NumbPhone = QtWidgets.QLineEdit(Dialog)
        self.NumbPhone.setGeometry(QtCore.QRect(450, 220, 300, 50))
        self.Login = QtWidgets.QLineEdit(Dialog)
        self.Login.setGeometry(QtCore.QRect(450, 280, 300, 50))
        self.Password = QtWidgets.QLineEdit(Dialog)
        self.Password.setGeometry(QtCore.QRect(450, 340, 300, 50))
        self.Status = QtWidgets.QLineEdit(Dialog)
        self.Status.setGeometry(QtCore.QRect(450, 400, 300, 50))

        self.signup = QtWidgets.QPushButton(Dialog)
        self.signup.setGeometry(QtCore.QRect(450, 460, 300, 50))



        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Регистрация"))
        self.signup.setText(_translate("Dialog", "Зарегестрироваться"))
