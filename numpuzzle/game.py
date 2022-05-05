# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'game.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from glob import glob
from operator import truediv
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox



all_buttons = []
buttons = []
class Start(object):
    global Form
    def setupUi(self, Form):
        Form.setObjectName("Form")
        font = QtGui.QFont()
        font.setPointSize(30)
        Form.setFont(font)
        Form.setStyleSheet("background:#4AB8C2")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setWindowTitle("Num Puzzle")
        self.frame.setGeometry(QtCore.QRect(-10, -30, 901, 661))
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(240, 60, 141, 131))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background:#F8D24A")
        self.pushButton.setObjectName("pushButton")
        
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 60, 141, 131))
        font = QtGui.QFont()
        font.setPointSize(30)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background:#F8D24A")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(520, 60, 141, 131))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background:#F8D24A")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(240, 190, 141, 131))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background:#F8D24A")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(380, 190, 141, 131))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background:#F8D24A")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(520, 190, 141, 131))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background:#F8D24A")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(240, 320, 141, 131))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("background:#F8D24A")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setGeometry(QtCore.QRect(380, 320, 141, 131))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("background:#F8D24A")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame)
        self.pushButton_9.setGeometry(QtCore.QRect(520, 320, 141, 131))
        self.pushButton_9.setStyleSheet("background:#F8D24A;")
        self.pushButton_9.setText("")
        self.pushButton_9.setObjectName("pushButton_9")
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton_9.setFont(font)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.add_function()

   


    def add_function(self):
        self.pushButton.clicked.connect(lambda : self.move(self.pushButton.text()))
        self.pushButton_2.clicked.connect(lambda : self.move(self.pushButton_2.text()))
        self.pushButton_3.clicked.connect(lambda : self.move(self.pushButton_3.text()))
        self.pushButton_4.clicked.connect(lambda : self.move(self.pushButton_4.text()))
        self.pushButton_5.clicked.connect(lambda : self.move(self.pushButton_5.text()))
        self.pushButton_6.clicked.connect(lambda : self.move(self.pushButton_6.text()))
        self.pushButton_7.clicked.connect(lambda : self.move(self.pushButton_7.text()))
        self.pushButton_8.clicked.connect(lambda : self.move(self.pushButton_8.text()))
        self.pushButton_9.clicked.connect(lambda : self.move(self.pushButton_9.text()))

    def win_window(self,arr):
        for i in range(0,len(arr) - 2):
            if arr[i] == "" or arr[i + 1] == "":
                return False
            if int(arr[i]) != int(arr[i + 1]) - 1:
                return False
        self.pushButton_9.setText("9")
        
        return True



    def move(self,number):
        global buttons

        arr = []
        for i in buttons:
            for j in i:
                arr.append(j)

        
        row = 0
        if number == '':
            return False
        for i in buttons:
            col = 0
            for j in i:
                if j == number:
                    if row + 1 < 3 and buttons[row + 1][col] == '':
                        buttons_tmp = buttons
                        buttons_tmp[row][col],buttons_tmp[row + 1][col] = buttons_tmp[row + 1][col],buttons_tmp[row][col]
                        count = 1
                        buttons_text_arr = []
                        for i in buttons:
                            for j in i:
                                buttons_text_arr.append(j)
                        for i in all_buttons:
                            i.setText(buttons_text_arr[count - 1])
                            count += 1
                            #print("Buttons value now is - " , i.text())
                        buttons = []
                        buttons.append(buttons_text_arr[0:3])
                        buttons.append(buttons_text_arr[3:6])
                        buttons.append(buttons_text_arr[6:])
                        if self.win_window(buttons_text_arr) == True:
                            win = QMessageBox()
                            win.setWindowTitle("Num Puzzle")
                            win.setText("Congratulations, You Win!!!")
                            win.setStandardButtons(QMessageBox.Ok)
                            win.exec_()
                            quit()

                        return True
                    elif row - 1 >= 0 and buttons[row - 1][col] == '':
                        buttons[row][col],buttons[row - 1][col] = buttons[row - 1][col],buttons[row][col]
                        count = 0
                        buttons_text_arr = []
                        for i in buttons:
                            for j in i:
                                buttons_text_arr.append(j)
                        for i in all_buttons:
                            i.setText(buttons_text_arr[count])
                            count += 1
                        buttons = []
                        buttons.append(buttons_text_arr[0:3])
                        buttons.append(buttons_text_arr[3:6])
                        buttons.append(buttons_text_arr[6:])
                        if self.win_window(buttons_text_arr) == True:
                            win = QMessageBox()
                            win.setWindowTitle("Num Puzzle")
                            win.setText("Congratulations, You Win!!!")
                            win.setStandardButtons(QMessageBox.Ok)
                            win.exec_()
                            quit()
                        return True
                    elif col + 1 < 3 and buttons[row][col + 1] == '':
                        buttons[row][col],buttons[row][col + 1] = buttons[row][col + 1],buttons[row][col]
                        count = 0
                        buttons_text_arr = []
                        for i in buttons:
                            for j in i:
                                buttons_text_arr.append(j)
                        for i in all_buttons:
                            i.setText(buttons_text_arr[count])
                            count += 1
                        buttons = []
                        buttons.append(buttons_text_arr[0:3])
                        buttons.append(buttons_text_arr[3:6])
                        buttons.append(buttons_text_arr[6:])
                        if self.win_window(buttons_text_arr) == True:
                            win = QMessageBox()
                            win.setWindowTitle("Num Puzzle")
                            win.setText("Congratulations, You Win!!!")
                            win.setStandardButtons(QMessageBox.Ok)
                            win.exec_()
                            quit()
                        return True

                    elif col - 1 >= 0 and buttons[row][col - 1] == '':
                        buttons[row][col],buttons[row][col - 1] = buttons[row][col - 1],buttons[row][col]
                        count = 0

                        buttons_text_arr = []
                        for i in buttons:
                            for j in i:
                                buttons_text_arr.append(j)

                        for i in all_buttons:
                            i.setText(buttons_text_arr[count])
                            count += 1

                        buttons = []
                        buttons.append(buttons_text_arr[0:3])
                        buttons.append(buttons_text_arr[3:6])
                        buttons.append(buttons_text_arr[6:])
                        if self.win_window(buttons_text_arr) == True:
                            win = QMessageBox()
                            win.setWindowTitle("Num Puzzle")
                            win.setText("Congratulations, You Win!!!")
                            win.setStandardButtons(QMessageBox.Ok)
                            win.exec_()
                            quit()
                            
                        return True


                col += 1
            row += 1

    


    




    def retranslateUi(self, Form):
        global all_buttons
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "2"))
        all_buttons.append(self.pushButton)
        self.pushButton_2.setText(_translate("Form", "8"))
        all_buttons.append(self.pushButton_2)
        self.pushButton_3.setText(_translate("Form", "6"))
        all_buttons.append(self.pushButton_3)
        self.pushButton_4.setText(_translate("Form", "1"))
        all_buttons.append(self.pushButton_4)
        self.pushButton_5.setText(_translate("Form", "5"))
        all_buttons.append(self.pushButton_5)
        self.pushButton_6.setText(_translate("Form", "7"))
        all_buttons.append(self.pushButton_6) 
        self.pushButton_7.setText(_translate("Form", "4"))
        all_buttons.append(self.pushButton_7)
        self.pushButton_8.setText(_translate("Form", "3"))
        all_buttons.append(self.pushButton_8)
        all_buttons.append(self.pushButton_9)
        buttons_tmp = []
        buttons_tmp.append(self.pushButton.text())
        buttons_tmp.append(self.pushButton_2.text())
        buttons_tmp.append(self.pushButton_3.text())
        buttons.append(buttons_tmp)
        buttons_tmp = []
        buttons_tmp.append(self.pushButton_4.text())
        buttons_tmp.append(self.pushButton_5.text())
        buttons_tmp.append(self.pushButton_6.text())
        buttons.append(buttons_tmp)
        buttons_tmp = []
        buttons_tmp.append(self.pushButton_7.text())
        buttons_tmp.append(self.pushButton_8.text())
        buttons_tmp.append(self.pushButton_9.text())
        buttons.append(buttons_tmp)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Start()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())