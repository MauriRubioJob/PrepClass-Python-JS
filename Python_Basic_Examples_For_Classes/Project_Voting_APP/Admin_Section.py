# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Admin_Section.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!



from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql      # To be able to use DB

# Lo de aquí abajo de ahora es mi main, y ahí voy a declara una erie de funciones pa poder utilizarlas
class Ui_MainWindow(object):
    # function for DB connection
    def DB_Connection(self):
        Connection = pymysql.connect(host="localhost", user="root", password="", db="voting_db")
        return Connection

    # Function for showing votes number
    def Show_Total_Vote(self):
        Connection = self.DB_Connection()

        SelectQ1 = "select * from votes where Voter_Party='PTI'"
        cursor = Connection.cursor()
        cursor.execute(SelectQ1)
        PTI_Total_Votes = cursor.rowcount
        self.label_2.setNum(PTI_Total_Votes)

        SelectQ2 = "select * from votes where Voter_Party='PMLN'"
        cursor = Connection.cursor()
        cursor.execute(SelectQ2)
        PMLN_Total_Votes = cursor.rowcount
        self.label_4.setNum(PMLN_Total_Votes)

        SelectQ3 = "select * from votes where Voter_Party='PPP'"
        cursor = Connection.cursor()
        cursor.execute(SelectQ3)
        PPP_Total_Votes = cursor.rowcount
        self.label_5.setNum(PPP_Total_Votes)

        Connection.commit()
        Connection.close()

    #Function for message
    def Message(self,title,msg):
        window=QtWidgets.QMessageBox()
        window.setWindowTitle(title)
        window.setText(msg)
        window.setStandardButtons(QtWidgets.QMessageBox.Ok)
        window.exec_()

    # Function for voter register
    def registerVoter(self):
        Connection = self.DB_Connection()
        Voter_Name = self.lineEdit.text()
        Voter_ID = self.lineEdit_2.text()
        Query = "insert into voters(Voter_Name,Voter_ID_Card) values(%s,%s)"
        cursor = Connection.cursor()
        run = cursor.execute(Query, (Voter_Name, Voter_ID))
        if run:
            self.Message("Success", "Voter Registered successfully.")
        Connection.commit()
        Connection.close()
    def registerParty(self):
        Connection=self.DB_Connection()
        Party_Name=self.lineEdit_3.text()
        Party_Char=self.lineEdit_4.text()
        Query="insert into party_db(Party_Name,PartyChar) values(%s,%s)"
        cursor=Connection.cursor()
        run=cursor.execute(Query,(Party_Name,Party_Char))
        if run:
            self.Message("Success","Party Registered successfully.")
        Connection.commit()
        Connection.close()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 410)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet("background-color: rgb(255, 176, 107);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 50, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(212, 187, 255);\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 50, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(212, 187, 255);\n"
"color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(230, 50, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(212, 187, 255);\n"
"color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(360, 50, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(212, 187, 255);\n"
"color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(540, 50, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(212, 187, 255);\n"
"color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(430, 50, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(212, 187, 255);\n"
"color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 90, 591, 20))
        self.line.setStyleSheet("background-color: rgb(255, 163, 70);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(50, 160, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgb(212, 187, 255);\n"
"color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(50, 220, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: rgb(212, 187, 255);\n"
"color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(50, 290, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color: rgb(212, 187, 255);\n"
"color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(170, 220, 161, 22))
        self.lineEdit.setStyleSheet("background-color: rgb(194, 224, 255);\n"
"color: rgb(255, 141, 47);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 290, 161, 22))
        self.lineEdit_2.setStyleSheet("background-color: rgb(194, 224, 255);\n"
"color: rgb(255, 141, 47);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 360, 181, 24))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 179);\n"
"color: rgb(85, 0, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.registerVoter)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(360, 150, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background-color: rgb(212, 187, 255);\n"
"color: rgb(255, 255, 255);")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(360, 210, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background-color: rgb(212, 187, 255);\n"
"color: rgb(255, 255, 255);")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(360, 280, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("background-color: rgb(212, 187, 255);\n"
"color: rgb(255, 255, 255);")
        self.label_12.setObjectName("label_12")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(500, 210, 121, 22))
        self.lineEdit_3.setStyleSheet("background-color: rgb(194, 224, 255);\n"
"color: rgb(255, 141, 47);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(500, 290, 121, 22))
        self.lineEdit_4.setStyleSheet("background-color: rgb(194, 224, 255);\n"
"color: rgb(255, 141, 47);")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(410, 360, 181, 24))
        self.pushButton_2.clicked.connect(self.registerParty)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 179);\n"
"color: rgb(85, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 10, 81, 24))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 179);\n"
"color: rgb(85, 0, 0);")
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Admin Section - Version 1.2.1"))
        self.label.setText(_translate("MainWindow", " PTI :"))
        self.label_2.setText(_translate("MainWindow", " 0"))
        self.label_3.setText(_translate("MainWindow", " PMLN :"))
        self.label_4.setText(_translate("MainWindow", " 0"))
        self.label_5.setText(_translate("MainWindow", " 0"))
        self.label_6.setText(_translate("MainWindow", " PPP :"))
        self.label_7.setText(_translate("MainWindow", " Add Voter"))
        self.label_8.setText(_translate("MainWindow", " Name :"))
        self.label_9.setText(_translate("MainWindow", " ID Card # :"))
        self.pushButton.setText(_translate("MainWindow", "Register Voter"))
        self.label_10.setText(_translate("MainWindow", " Add Party"))
        self.label_11.setText(_translate("MainWindow", " Party Name :"))
        self.label_12.setText(_translate("MainWindow", " Party Head :"))
        self.pushButton_2.setText(_translate("MainWindow", "Register Party"))
        self.pushButton_3.setText(_translate("MainWindow", "Show Results"))
        self.pushButton_3.clicked.connect(self.Show_Total_Vote)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
