from re import T
from PyQt5 import QtCore, QtGui, QtWidgets
from codage_en_ligne import Filtre_emi
from mplcanvas import MplCanvas
from css import styleCss

class Ui_Form(QtCore.QObject):

    sorti_Lhorloge = QtCore.pyqtSignal(list, int)
    sorti_Ldecision = QtCore.pyqtSignal(list, int)

    def __init__(self,parent=None):
        super().__init__(parent)



    entrez_Mn_demodulation = []
    Ts = 0
    def setEntrez_MNDemodulation(self,entrez_Mn_demodulation, Ts, entrez_Mn_Filtre):
        self.Ts = Ts
        print("ts_rcepteur",Ts)
        self.entrez_Mn_demodulation = entrez_Mn_demodulation
        self.entrez_Mn_Filtre = entrez_Mn_Filtre

        self.get_demodulation_plot()

    def getEntrez_MNDemodulation(self):
        return self.entrez_Mn_demodulation

    def getEntrez_MNfiltre1(self):
        return self.entrez_Mn_Filtre


    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(587, 599)
        Form.setMinimumSize(QtCore.QSize(587, 599))
        Form.setMaximumSize(QtCore.QSize(587, 599))
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 591, 601))
        self.frame.setMinimumSize(QtCore.QSize(591, 601))
        self.frame.setMaximumSize(QtCore.QSize(591, 601))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.setStyleSheet(styleCss)  #*****************************************

        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(161, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(161, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 2, 1, 1)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 212))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.widget_demodu_reception = MplCanvas(self.frame_4)
        self.widget_demodu_reception.setGeometry(QtCore.QRect(30, 0, 511, 210))
        self.widget_demodu_reception.setMinimumSize(QtCore.QSize(0, 210))
        self.widget_demodu_reception.setObjectName("widget_demodu_reception")
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_7 = QtWidgets.QFrame(self.frame)
        self.frame_7.setMinimumSize(QtCore.QSize(0, 212))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.widget_reception = MplCanvas(self.frame_7)
        self.widget_reception.setGeometry(QtCore.QRect(30, 0, 511, 210))
        self.widget_reception.setMinimumSize(QtCore.QSize(0, 210))
        self.widget_reception.setObjectName("widget_reception")
        self.verticalLayout.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.frame)
        self.frame_8.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_8)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem2 = QtWidgets.QSpacerItem(350, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 0, 1, 1)
        self.pushButton_exit = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.gridLayout.addWidget(self.pushButton_exit, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame_8)

        Form.setWindowTitle("Filtre de reception")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Filtre de reception"))
        self.pushButton_exit.setText(_translate("Form", "exit"))

        self.pushButton_exit.clicked.connect(Form.close)   #************************************************



    def get_demodulation_plot(self):
        entre_code = self.getEntrez_MNDemodulation() 
        self.widget_demodu_reception.plot_name(entre_code, "avant reception")

        entre_code_reception = list(Filtre_emi().filtre_r(self.getEntrez_MNfiltre1()))
        self.widget_reception.plot_name(entre_code_reception, "apres reception")

        self.sorti_Lhorloge.emit(entre_code_reception, self.Ts)
        self.sorti_Ldecision.emit(entre_code_reception, self.Ts)

