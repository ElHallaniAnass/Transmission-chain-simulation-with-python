from PyQt5 import QtCore, QtGui, QtWidgets
from mplcanvas import MplCanvas
from css import styleCss

class Ui_Form(QtCore.QObject):

    sorti_Lcode = QtCore.pyqtSignal(list)

    def __init__(self,parent=None):
        super().__init__(parent)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(497, 515)
        Form.setStyleSheet(styleCss)  #*****************************************

        self.frame = QtWidgets.QFrame(Form)

        self.frame.setGeometry(QtCore.QRect(0, -10, 491, 521))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(97, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.label_sbe_titre = QtWidgets.QLabel(self.frame_3)
        self.label_sbe_titre.setMinimumSize(QtCore.QSize(0, 0))
        self.label_sbe_titre.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_sbe_titre.setFont(font)
        self.label_sbe_titre.setObjectName("label_sbe_titre")
        self.gridLayout.addWidget(self.label_sbe_titre, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(97, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_8 = QtWidgets.QFrame(self.frame)
        self.frame_8.setMaximumSize(QtCore.QSize(123345, 40))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_8)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pushButton_sbe_data = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_sbe_data.setObjectName("pushButton_sbe_data")
        self.gridLayout_4.addWidget(self.pushButton_sbe_data, 0, 0, 1, 1)
        self.lineEdit_sbe_datatest = QtWidgets.QLineEdit(self.frame_8)
        self.lineEdit_sbe_datatest.setEnabled(True)
        self.lineEdit_sbe_datatest.setStatusTip("")
        self.lineEdit_sbe_datatest.setWhatsThis("")
        self.lineEdit_sbe_datatest.setAccessibleName("")
        self.lineEdit_sbe_datatest.setAccessibleDescription("")
        self.lineEdit_sbe_datatest.setAutoFillBackground(False)
        self.lineEdit_sbe_datatest.setStyleSheet("")
        self.lineEdit_sbe_datatest.setText("")
        self.lineEdit_sbe_datatest.setObjectName("lineEdit_sbe_datatest")
        self.gridLayout_4.addWidget(self.lineEdit_sbe_datatest, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(179, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem2, 0, 2, 1, 1)
        self.verticalLayout.addWidget(self.frame_8)
        self.frame_7 = QtWidgets.QFrame(self.frame)
        self.frame_7.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_7)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_sbe_generez = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_sbe_generez.setObjectName("pushButton_sbe_generez")
        self.gridLayout_2.addWidget(self.pushButton_sbe_generez, 0, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(291, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame_7)
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        
        self.widget_sbe = MplCanvas(self.frame_5)
        self.widget_sbe.setGeometry(QtCore.QRect(20, 30, 431, 191))
        self.widget_sbe.setObjectName("widget_sbe")
        self.frame_2 = QtWidgets.QFrame(self.frame_5)
        self.frame_2.setGeometry(QtCore.QRect(0, 290, 471, 40))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem4 = QtWidgets.QSpacerItem(291, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem4, 0, 0, 1, 1)
        self.pushButton_sbe_exit = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_sbe_exit.setObjectName("pushButton_sbe_exit")
        self.gridLayout_5.addWidget(self.pushButton_sbe_exit, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame_5)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)



        # connect this button to function get text 
        self.pushButton_sbe_generez.clicked.connect(self.getAleatoire)   #************************************************
        self.pushButton_sbe_data.clicked.connect(self.gettext) 
        self.pushButton_sbe_exit.clicked.connect(Form.close)   #************************************************
        Form.setWindowTitle("Sequence binaire emise")


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_sbe_titre.setText(_translate("Form", "Sequence binaire emise"))
        self.pushButton_sbe_data.setText(_translate("Form", "entrer data"))
        self.lineEdit_sbe_datatest.setPlaceholderText(_translate("Form", "Entrez un signial maxsize=15"))
        self.pushButton_sbe_generez.setText(_translate("Form", "data aléatoire "))
        self.pushButton_sbe_exit.setText(_translate("Form", "exit"))






    def gettext(self):
        # get text form line edit 
        # plot text 
        lineEdit_sbe_datatest = [int(input) for input in self.lineEdit_sbe_datatest.text()]  
        ax = self.widget_sbe.plot(lineEdit_sbe_datatest)
        self.sorti_Lcode.emit(lineEdit_sbe_datatest)

    def getAleatoire(self):
        # get text form line edit 
        # plot text 
        lineEdit_sbe_datatest =  [1,0,0,0,0,1]
        ax = self.widget_sbe.plot(lineEdit_sbe_datatest)
        self.sorti_Lcode.emit(lineEdit_sbe_datatest)



