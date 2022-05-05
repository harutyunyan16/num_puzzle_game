

from PyQt5 import QtCore, QtGui, QtWidgets
from game import Start

import sys
class Ui_Form(object):
    
    def start_game(self):
        self.window = QtWidgets.QWidget()
        self.ui = Start()
        self.ui.setupUi(self.window)
        Form2.close()
        self.window.show()
        
    def about_game(self):
        from about import Ui_Form
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()



    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(844, 546)
        Form.setStyleSheet("background:#F8D24A;")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(250, 110, 341, 111))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background:black;color:white;border-radius:15")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 320, 341, 111))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background:black;color:white;border-radius:15")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.add_function()

    def add_function(self):
        self.pushButton.clicked.connect(lambda : self.start_game())
        self.pushButton_2.clicked.connect(lambda : self.about_game())


    
    


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "START"))
        self.pushButton_2.setText(_translate("Form", "ABOUT"))






if __name__ == "__main__":
    global Form2
    app = QtWidgets.QApplication(sys.argv)
    Form2 = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form2)
    Form2.show()
    sys.exit(app.exec_())
