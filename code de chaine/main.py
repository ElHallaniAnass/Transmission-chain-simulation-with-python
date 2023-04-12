from PyQt5 import QtCore, QtGui, QtWidgets
import chaine

class Ui_TelecomSum(object):


    def __init__(self):
        self.initComponents()


    def setupUi(self, TelecomSum):
        TelecomSum.setObjectName("TelecomSum")
        TelecomSum.resize(750, 460)
        TelecomSum.setMinimumSize(QtCore.QSize(750, 460))
        TelecomSum.setMaximumSize(QtCore.QSize(750, 460))
        TelecomSum.setStyleSheet("QDialog{\n"
"    background: rgb(0, 0, 0);\n"
"}")
        self.widget = QtWidgets.QWidget(TelecomSum)
        self.widget.setGeometry(QtCore.QRect(0, 0, 751, 461))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.text = QtWidgets.QFrame(self.widget)
        self.text.setMaximumSize(QtCore.QSize(16777215, 420))
        self.text.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.text.setFrameShadow(QtWidgets.QFrame.Raised)
        self.text.setObjectName("text")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.text)
        self.verticalLayout_2.setContentsMargins(50, 0, 50, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.title = QtWidgets.QFrame(self.text)
        self.title.setMaximumSize(QtCore.QSize(16777215, 150))
        self.title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title.setObjectName("title")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.title)
        self.horizontalLayout_3.setContentsMargins(0, 60, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(199, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.title)
        font = QtGui.QFont()
        font.setPointSize(35)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
"    color: #fff;\n"
"}")
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(198, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_2.addWidget(self.title)
        self.description = QtWidgets.QFrame(self.text)
        self.description.setMaximumSize(QtCore.QSize(16777215, 150))
        self.description.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.description.setFrameShadow(QtWidgets.QFrame.Raised)
        self.description.setObjectName("description")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.description)
        self.horizontalLayout_2.setContentsMargins(0, 14, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.description)
        self.textBrowser.setMaximumSize(QtCore.QSize(550, 150))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setKerning(True)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("QTextBrowser{\n"
"    background: transparent;\n"
"    border: none;\n"
"}")
        self.textBrowser.setAutoFormatting(QtWidgets.QTextEdit.AutoNone)
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout_2.addWidget(self.textBrowser)
        self.verticalLayout_2.addWidget(self.description)
        self.frame = QtWidgets.QFrame(self.text)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 150))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 60)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(121, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.butCommencerSum = QtWidgets.QPushButton(self.frame)
        self.butCommencerSum.setMaximumSize(QtCore.QSize(400, 45))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.butCommencerSum.setFont(font)
        self.butCommencerSum.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.butCommencerSum.setStyleSheet("QPushButton{\n"
"    background: transparent;\n"
"    color: #fff;\n"
"    border-radius: 22px;\n"
"    border: 2px solid #fff;\n"
"    width: 300px;\n"
"}\n"
"QPushButton:hover{\n"
"    color: #000;\n"
"    background: #fff;\n"
"}")
        self.butCommencerSum.setObjectName("butCommencerSum")
        self.horizontalLayout.addWidget(self.butCommencerSum)
        spacerItem3 = QtWidgets.QSpacerItem(120, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout_2.addWidget(self.frame)
        self.verticalLayout.addWidget(self.text)
        self.footer = QtWidgets.QFrame(self.widget)
        self.footer.setMaximumSize(QtCore.QSize(16777215, 40))
        self.footer.setStyleSheet("QFrame{\n"
"    background: #fff;\n"
"}")
        self.footer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.footer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.footer.setObjectName("footer")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.footer)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.footer)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel{\n"
"    color: #000;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.label_3 = QtWidgets.QLabel(self.footer)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel{\n"
"    color: #000;\n"
"}")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.verticalLayout.addWidget(self.footer)

        self.retranslateUi(TelecomSum)
        QtCore.QMetaObject.connectSlotsByName(TelecomSum)

    def retranslateUi(self, TelecomSum):
        _translate = QtCore.QCoreApplication.translate
        TelecomSum.setWindowTitle(_translate("TelecomSum", "Dialog"))
        self.label.setText(_translate("TelecomSum", "Bienvenu!"))
        self.textBrowser.setHtml(_translate("TelecomSum", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
                "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600; font-style:italic; color:#ffffff;\"><br>La chaine représente les différentes étapes de traitement de l’information. Il relie l’émetteur au récepteur par l’intermédiaire d’un canal de transmission</span></p></body></html>"))
        self.butCommencerSum.setText(_translate("TelecomSum", "Commencer la sumilation"))
        self.label_2.setText(_translate("TelecomSum", " IHSSANE BOUTAHAR, OTHMANE ELAZRI, ANASS EL HALLANI, YOUNES EL BELGHITI"))
        # self.label_3.setText(_translate("TelecomSum", "Encadrer par : Pr.JILBAB ABDELILAH"))



        self.butCommencerSum.clicked.connect(self.home.show)
        # self.butCommencerSum.clicked.connect(TelecomSum.close)


    def initComponents(self):
        self.home  = QtWidgets.QWidget()
        self.homenew = chaine.Ui_Form( )
        self.homenew.setupUi(self.home)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TelecomSum = QtWidgets.QDialog()
    ui = Ui_TelecomSum()
    ui.setupUi(TelecomSum)
    TelecomSum.show()
    sys.exit(app.exec_())
