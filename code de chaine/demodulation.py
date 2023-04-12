from PyQt5 import QtCore, QtGui, QtWidgets
from codage_en_ligne import Codage, Filtre_emi, Modulation
from mplcanvas import MplCanvas
from css import styleCss


class Ui_Form(QtCore.QObject):

    sorti_Lrecepteur = QtCore.pyqtSignal(list,int,list)

    def __init__(self,parent=None):
        super().__init__(parent)



    entrez_Mn_canal = []
    Ts = 0
    mode = str
    def setEntrez_MNCanal(self,entrez_Mn_canal, Ts, mode, entrez_Mn_Filtre):
        self.mode = mode
        self.Ts = Ts
        self.entrez_Mn_canal = entrez_Mn_canal
        self.entrez_Mn_Filtre = entrez_Mn_Filtre

        self.emit_recpteur()

    def getEntrez_MNCanal(self):
        return self.entrez_Mn_canal

    def getEntrez_MNfiltre(self):
        return self.entrez_Mn_Filtre


    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(588, 601)
        Form.setMinimumSize(QtCore.QSize(588, 601))
        Form.setMaximumSize(QtCore.QSize(588, 601))
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
        self.widget_demodu_bruit = MplCanvas(self.frame_4)
        self.widget_demodu_bruit.setGeometry(QtCore.QRect(30, 0, 511, 210))
        self.widget_demodu_bruit.setMinimumSize(QtCore.QSize(0, 210))
        self.widget_demodu_bruit.setObjectName("widget_demodu_bruit")
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_7 = QtWidgets.QFrame(self.frame)
        self.frame_7.setMinimumSize(QtCore.QSize(0, 212))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.widget_demodulation = MplCanvas(self.frame_7)
        self.widget_demodulation.setGeometry(QtCore.QRect(30, 0, 511, 210))
        self.widget_demodulation.setMinimumSize(QtCore.QSize(0, 210))
        self.widget_demodulation.setObjectName("widget_demodulation")
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

        Form.setWindowTitle("demodulation")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "demodulation"))
        self.pushButton_exit.setText(_translate("Form", "exit"))


        self.pushButton_exit.clicked.connect(Form.close)   #************************************************




    def emit_recpteur(self):
        entre_code = self.getEntrez_MNCanal() 
        entre_code_demodu = list(Modulation().demodulation(self.getEntrez_MNfiltre()))

        self.widget_demodu_bruit.plot_name(entre_code, self.mode+" + "+"bruit " )
        self.widget_demodulation.plot_name(entre_code_demodu, "demodulation")
        
        self.sorti_Lrecepteur.emit(entre_code_demodu, self.Ts, self.getEntrez_MNfiltre())
