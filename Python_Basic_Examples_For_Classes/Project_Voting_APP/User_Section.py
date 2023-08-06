# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'User_Section.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql      # To be able to use DB

class Ui_MainWindow(object):

    def DB_Connection(self):
        Connection = pymysql.connect(host="localhost", user="root", password="", db="voting_db")
        return Connection

    def Message(self,title,msg):
        window=QtWidgets.QMessageBox()
        window.setWindowTitle(title)
        window.setText(msg)
        window.setStandardButtons(QtWidgets.QMessageBox.Ok)
        window.exec_()

    # Function for vote submitting
    def Submit_Vote(self):
        Connection=self.DB_Connection()
        cursor=Connection.cursor()

        # Storing line edit in variable
        Voter_Name=self.lineEdit.text()
        Voter_ID=self.lineEdit_3.text()

        #Checking Voter dat in voter Table
        checkReg="select * from voters where Voter_ID_Card=%s"
        cursor.execute(checkReg,(Voter_ID))
        countReg=cursor.rowcount

        # Checking voter in votes table
        checkVote="select * from votes where Voter_ID=%s"
        cursor.execute(checkVote,(Voter_ID))
        countVote=cursor.rowcount

        # Checking user registration and vote
        # Also checking readio buttons
        if countReg!=1:
            self.Message("Error","Your data is not present in our DB")
        elif countVote==1:
            self.Message("Error","You have already submitted a vote")
        elif self.radioButton.isChecked():
            vote="PTI"
            insert="insert into votes(Voter_Name,Voter_ID,Voter_Party) values(%s,%s,%s)"
            run=cursor.execute(insert,(Voter_Name,Voter_ID,vote))
            if run:
                self.Message("Submitted Vote","Your vote has been successfully submitted. Thank you.")

        elif self.radioButton_2.isChecked():
            vote = "PMLN"
            insert = "insert into votes(Voter_Name,Voter_ID,Voter_Party) values(%s,%s,%s)"
            run = cursor.execute(insert, (Voter_Name, Voter_ID, vote))
            if run:
                self.Message("Submitted Vote", "Your vote has been successfully submitted. Thank you.")

        elif self.radioButton_3.isChecked():
            vote = "PPP"
            insert = "insert into votes(Voter_Name,Voter_ID,Voter_Party) values(%s,%s,%s)"
            run = cursor.execute(insert, (Voter_Name, Voter_ID, vote))
            if run:
                self.Message("Submitted Vote", "Your vote has been successfully submitted. Thank you.")
        Connection.commit()
        Connection.close()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 370)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(120, 176, 107);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 20, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(212, 187, 255);\n"
"color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(50, 110, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgb(212, 187, 255);\n"
"color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(170, 110, 411, 22))
        self.lineEdit.setStyleSheet("background-color: rgb(194, 224, 255);\n"
"color: rgb(255, 141, 47);")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(290, 320, 181, 24))
        self.pushButton.clicked.connect(self.Submit_Vote)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 179);\n"
"color: rgb(85, 0, 0);")
        self.pushButton.setObjectName("pushButton")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(50, 180, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background-color: rgb(212, 187, 255);\n"
"color: rgb(255, 255, 255);")
        self.label_10.setObjectName("label_10")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(170, 190, 411, 22))
        self.lineEdit_3.setStyleSheet("background-color: rgb(194, 224, 255);\n"
"color: rgb(255, 141, 47);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(50, 260, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background-color: rgb(212, 187, 255);\n"
"color: rgb(255, 255, 255);")
        self.label_11.setObjectName("label_11")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(340, 270, 91, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(480, 270, 91, 20))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(200, 270, 91, 20))
        self.radioButton.setObjectName("radioButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Admin Section - Version 1.2.1"))
        self.label_6.setText(_translate("MainWindow", "Voting Aplication"))
        self.label_7.setText(_translate("MainWindow", " Name :"))
        self.pushButton.setText(_translate("MainWindow", "Submit Vote"))
        self.label_10.setText(_translate("MainWindow", " ID Card # :"))
        self.label_11.setText(_translate("MainWindow", "Select Vote"))
        self.radioButton_2.setText(_translate("MainWindow", "PMLN"))
        self.radioButton_3.setText(_translate("MainWindow", "PPP"))
        self.radioButton.setText(_translate("MainWindow", "PTI"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
