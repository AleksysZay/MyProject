
import sys
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5 import QtCore, QtGui, QtWidgets
from AuthWindow import Ui_Auth
from RegWindow import Ui_Reg
from UserWindow import Ui_User
from AdminWindow import Ui_Admin
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

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Auth()
    ui.setupUi(Dialog)
    Dialog.show()

    def openUser():
        global UserWin
        UserWin = QtWidgets.QDialog()
        ui = Ui_User()
        ui.setupUi(UserWin)
        Dialog.close()
        UserWin.show()

    def openAdmin():
        global AdminWin
        AdminWin = QtWidgets.QDialog()
        ui = Ui_Admin()
        ui.setupUi(AdminWin)
        Dialog.close()
        AdminWin.show()




    def openReg():
        global RegWin
        RegWin = QtWidgets.QDialog()
        ui = Ui_Reg()
        ui.setupUi(RegWin)
        Dialog.close()
        RegWin.show()

        def addUser():
            if Conn():
                # QueryAddUser = f"INSERT INTO [USER] VALUES ('{ui.Name.text()}', '{ui.DOB.text()}', '{ui.Age.text()}', '{ui.NumbPhone.text()}', '{ui.Login.text()}', '{ui.Password.text()}', '{ui.Status.text()}') "
                QueryAddUser = f"insert into [User] values('ddd','12-02-3004',19,'1','2','3','4')"
                Query(QueryAddUser)
                print('User was added!')

        def returnWin1():
            RegWin.close()
            Dialog.show()
        ui.signup.clicked.connect(addUser)
        ui.signup.clicked.connect(returnWin1)




    ui.btnReg.clicked.connect(openReg)
    if 10 < 2:
        ui.btnMain.clicked.connect(openUser)
    else:
        ui.btnMain.clicked.connect(openAdmin)
    sys.exit(app.exec_())