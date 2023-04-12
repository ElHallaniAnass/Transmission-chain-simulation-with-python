from PyQt5 import QtCore, QtGui, QtWidgets
from codage_en_ligne import Codage, Filtre_emi, Modulation
from mplcanvas import MplCanvas
from css import styleCss
import numpy as np

class Ui_Form(QtCore.QObject):

    sorti_Ldemodulation = QtCore.pyqtSignal(list ,int, str, list)

    def __init__(self,parent=None):
        super().__init__(parent)



    entrez_Mn_modulation, entrez_Mn_Filtre = [], []
    Ts = 0
    mode = str
    def setEntrez_MNModulation(self,entrez_Mn_modulation, Ts, mode, entrez_Mn_Filtre):
        self.mode = mode
        self.Ts = Ts
        self.entrez_Mn_modulation = entrez_Mn_modulation
        self.entrez_Mn_Filtre = entrez_Mn_Filtre

        self.emit_demodulation()

    def getEntrez_MNModulation(self):
        return self.entrez_Mn_modulation

    def getFiltre(self):
        return self.entrez_Mn_Filtre



    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(584, 593)
        Form.setMinimumSize(QtCore.QSize(584, 593))
        Form.setMaximumSize(QtCore.QSize(584, 593))
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 591, 601))
        self.frame.setMinimumSize(QtCore.QSize(591, 601))
        self.frame.setMaximumSize(QtCore.QSize(591, 601))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.setStyleSheet(styleCss)

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
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(69, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame_5)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 1, 1, 1)
        self.doubleSpinBox_sigma = QtWidgets.QDoubleSpinBox(self.frame_5)
        self.doubleSpinBox_sigma.setMinimumSize(QtCore.QSize(100, 0))
        self.doubleSpinBox_sigma.setDecimals(1)
        self.doubleSpinBox_sigma.setMaximum(1.0)
        self.doubleSpinBox_sigma.setSingleStep(0.1)
        self.doubleSpinBox_sigma.setObjectName("doubleSpinBox_sigma")
        self.gridLayout_3.addWidget(self.doubleSpinBox_sigma, 0, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(69, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 0, 3, 1, 1)
        self.pushButton_canal_generer = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_canal_generer.setMinimumSize(QtCore.QSize(100, 0))
        self.pushButton_canal_generer.setObjectName("pushButton_canal_generer")
        self.gridLayout_3.addWidget(self.pushButton_canal_generer, 0, 4, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(69, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 0, 5, 1, 1)
        self.verticalLayout.addWidget(self.frame_5)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 212))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.widget_canal_modu = MplCanvas(self.frame_4)
        self.widget_canal_modu.setGeometry(QtCore.QRect(30, 0, 511, 210))
        self.widget_canal_modu.setMinimumSize(QtCore.QSize(0, 210))
        self.widget_canal_modu.setObjectName("widget_canal_modu")
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_7 = QtWidgets.QFrame(self.frame)
        self.frame_7.setMinimumSize(QtCore.QSize(0, 212))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.widget_canal_bruit = MplCanvas(self.frame_7)
        self.widget_canal_bruit.setGeometry(QtCore.QRect(30, 0, 511, 210))
        self.widget_canal_bruit.setMinimumSize(QtCore.QSize(0, 210))
        self.widget_canal_bruit.setObjectName("widget_canal_bruit")
        self.verticalLayout.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.frame)
        self.frame_8.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_8)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem5 = QtWidgets.QSpacerItem(350, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 0, 0, 1, 1)
        self.pushButton_canal_exit = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_canal_exit.setObjectName("pushButton_canal_exit")
        self.gridLayout.addWidget(self.pushButton_canal_exit, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame_8)

        Form.setWindowTitle("Canal de propagation")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Canal de propagation"))
        self.label_2.setText(_translate("Form", "variance"))
        self.pushButton_canal_generer.setText(_translate("Form", "generer"))
        self.pushButton_canal_exit.setText(_translate("Form", "exit"))



        self.pushButton_canal_exit.clicked.connect(Form.close)   #************************************************
        self.pushButton_canal_generer.pressed.connect(self.emit_demodulation) 



    def emit_demodulation(self):
        sigma = self.doubleSpinBox_sigma.value() 
        entre_modu = self.getEntrez_MNModulation()
    
        entre_modu_br = Modulation().noise_noise(entre_modu,len(entre_modu), sigma)
        entre_modu_bruit = list(entre_modu_br)
        self.widget_canal_modu.plot_name(entre_modu, self.mode )
        self.widget_canal_bruit.plot_name(entre_modu_bruit, self.mode+" + Bruit avec var = "+ str(sigma))

        self.sorti_Ldemodulation.emit(entre_modu_bruit, self.Ts, self.mode, self.getFiltre())
