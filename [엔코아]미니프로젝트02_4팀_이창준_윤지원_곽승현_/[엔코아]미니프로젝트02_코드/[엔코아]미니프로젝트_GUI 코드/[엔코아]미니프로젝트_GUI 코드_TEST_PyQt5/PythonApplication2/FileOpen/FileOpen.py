# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FileOpen.ui'
#
# Created: Thu Sep 29 13:38:39 2016
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(523, 83)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 38, 56, 12))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(90, 34, 290, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(394, 32, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # TODO:
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.show_file_open)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "파일오픈 예제", None))
        self.label.setText(_translate("Form", "파일경로", None))
        self.pushButton.setText(_translate("Form", "찾기", None))

    # TODO:
    def show_file_open(self):
        fname = QtGui.QFileDialog.getOpenFileName()
        self.lineEdit.setText(fname)
        


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

