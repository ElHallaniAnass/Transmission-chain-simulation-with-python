from PyQt5 import QtCore, QtGui, QtWidgets
from mplcanvas import MplCanvas
from css import styleCss
from codage_en_ligne import Modulation
import numpy as np


class Ui_Form(QtCore.QObject):

    sorti_Lcanal = QtCore.pyqtSignal(list,int,str,list)

    def __init__(self,parent=None):
        super().__init__(parent)



    entrez_Mn_Filtre = []
    Ts = 0
    def setEntrez_MNFiltre(self,entrez_Mn_Filtre, Ts):
        self.Ts = Ts
        self.entrez_Mn_Filtre = entrez_Mn_Filtre
        self.emit_canal()

    def getEntrez_MnFiltre(self):
        return self.entrez_Mn_Filtre




    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(814, 600)
        Form.setMinimumSize(QtCore.QSize(814, 601))
        Form.setMaximumSize(QtCore.QSize(814, 601))
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 821, 601))
        self.frame.setMinimumSize(QtCore.QSize(821, 601))
        self.frame.setMaximumSize(QtCore.QSize(821, 601))
        self.frame.setStyleSheet(styleCss)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
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
        font.setPointSize(22)
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
        self.comboBox_Modu_type = QtWidgets.QComboBox(self.frame_5)
        self.comboBox_Modu_type.setMinimumSize(QtCore.QSize(120, 20))
        self.comboBox_Modu_type.setObjectName("comboBox_Modu_type")
        self.comboBox_Modu_type.addItem("")
        self.comboBox_Modu_type.addItem("")
        self.comboBox_Modu_type.addItem("")
        self.gridLayout_3.addWidget(self.comboBox_Modu_type, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(69, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 0, 2, 1, 1)
        self.pushButton_Modu_generer = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_Modu_generer.setObjectName("pushButton_Modu_generer")
        self.gridLayout_3.addWidget(self.pushButton_Modu_generer, 0, 3, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(69, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 0, 4, 1, 1)
        self.verticalLayout.addWidget(self.frame_5)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 212))
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 212))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.widget_modu_Fn = MplCanvas(self.frame_4)
        self.widget_modu_Fn.setGeometry(QtCore.QRect(200, 0, 401, 210))
        self.widget_modu_Fn.setMinimumSize(QtCore.QSize(0, 210))
        self.widget_modu_Fn.setObjectName("widget_modu_Fn")
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 212))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 212))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.widget_modu_dsp_2 = MplCanvas(self.frame_3)
        self.widget_modu_dsp_2.setGeometry(QtCore.QRect(400, 0, 391, 210))
        self.widget_modu_dsp_2.setMinimumSize(QtCore.QSize(0, 210))
        self.widget_modu_dsp_2.setObjectName("widget_modu_dsp_2")
        self.widget_modu = MplCanvas(self.frame_3)
        self.widget_modu.setGeometry(QtCore.QRect(10, 0, 381, 210))
        self.widget_modu.setMinimumSize(QtCore.QSize(0, 210))
        self.widget_modu.setObjectName("widget_modu")
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_8 = QtWidgets.QFrame(self.frame)
        self.frame_8.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_8)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem5 = QtWidgets.QSpacerItem(350, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 0, 0, 1, 1)
        self.pushButton_Modu_exit = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_Modu_exit.setObjectName("pushButton_Modu_exit")
        self.gridLayout.addWidget(self.pushButton_Modu_exit, 0, 2, 1, 1)
        self.widget_modu_dsp = QtWidgets.QWidget(self.frame_8)
        self.widget_modu_dsp.setMinimumSize(QtCore.QSize(0, 210))
        self.widget_modu_dsp.setObjectName("widget_modu_dsp")
        self.gridLayout.addWidget(self.widget_modu_dsp, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame_8)


        Form.setWindowTitle("Modulisation")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Modulisation"))
        self.comboBox_Modu_type.setItemText(0, _translate("Form", "ASK"))
        self.comboBox_Modu_type.setItemText(1, _translate("Form", "PSK"))
        self.comboBox_Modu_type.setItemText(2, _translate("Form", "FSK"))
        self.pushButton_Modu_generer.setText(_translate("Form", "generer"))
        self.pushButton_Modu_exit.setText(_translate("Form", "exit"))

        self.pushButton_Modu_exit.clicked.connect(Form.close)   #************************************************
        self.pushButton_Modu_generer.pressed.connect(self.emit_canal) 
        # self.pushButton_cl_generer.clicked.connect(self.entrer_plot) 

        






    def emit_canal(self):       
        self.content = self.comboBox_Modu_type.currentText()
        self.entre = self.getEntrez_MnFiltre() 
        self.widget_modu_Fn.plot_name(self.entre, "Filtre d'émission")

        t = np.linspace(0,300,1000)
        fAsk, deltaF = 100, 70
        fPsk = 50
        fFsk = 100
        ask = list(Modulation().ASK(fAsk,self.entre,t))
        psk = list(Modulation().PSK(fPsk,self.entre,t))
        fsk = list(Modulation().FSK(fFsk,deltaF,self.entre,t))

        dspAsk = Modulation().DSP_mod(fAsk,t,self.Ts)
        dspPsk = Modulation().DSP_mod(fPsk,t,self.Ts)
        dspFsk = Modulation().DSP_mod(fFsk,t,self.Ts)

        if self.content == "ASK" :
            self.widget_modu.plot_name(ask, self.content )
            self.widget_modu_dsp_2.plot_name1(t, dspAsk, "DSP_ASk" )

            self.sorti_Lcanal.emit(ask, self.Ts, self.content,self.entre)

        elif self.content == "PSK" :
            self.widget_modu.plot_name(psk, self.content )
            self.widget_modu_dsp_2.plot_name1(t, dspPsk, "DSP_PSK" )

            self.sorti_Lcanal.emit(psk, self.Ts, self.content,self.entre)

        else :
            self.widget_modu.plot_name(fsk, self.content )
            self.widget_modu_dsp_2.plot_name1(t, dspFsk, "DSP_FSK" )

            self.sorti_Lcanal.emit(fsk, self.Ts, self.content, self.entre)

        
      
