from PyQt5 import QtCore, QtGui, QtWidgets
from mplcanvas import MplCanvas
from css import styleCss
from codage_en_ligne import Codage 
import numpy as np

class Ui_Form(QtCore.QObject):

    sorti_Lfiltre = QtCore.pyqtSignal(list,int,str)

    def __init__(self,parent=None):
        super().__init__(parent)

    entrez_MnSource = []
    Ts = 0

    def setEntrez_MnSource(self,entrez_MnSource,Ts):
        self.Ts = Ts
        self.entrez_MnSource = entrez_MnSource
        self.choix_Code()

        
    def getEntrez_MnSource(self):
        return self.entrez_MnSource


    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(941, 561)
        Form.setMinimumSize(QtCore.QSize(941, 561))
        Form.setMaximumSize(QtCore.QSize(941, 561))
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, -10, 941, 584))
        self.frame.setMinimumSize(QtCore.QSize(941, 584))
        self.frame.setMaximumSize(QtCore.QSize(941, 584))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        Form.setStyleSheet(styleCss)

        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout.setObjectName("gridLayout")
        self.label_sbe_titre = QtWidgets.QLabel(self.frame_5)
        self.label_sbe_titre.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_sbe_titre.setFont(font)
        self.label_sbe_titre.setObjectName("label_sbe_titre")
        self.gridLayout.addWidget(self.label_sbe_titre, 0, 1, 2, 1)
        spacerItem = QtWidgets.QSpacerItem(300, 14, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(301, 14, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_5)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(97, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 0, 1, 1)
        self.comboBox_cl_choix = QtWidgets.QComboBox(self.frame_3)
        self.comboBox_cl_choix.setObjectName("comboBox_cl_choix")
        self.comboBox_cl_choix.addItem("")
        self.comboBox_cl_choix.addItem("")
        self.comboBox_cl_choix.addItem("")
        self.comboBox_cl_choix.addItem("")
        self.comboBox_cl_choix.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_cl_choix, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(98, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 3, 1, 1)
        self.spinBox_cl_HDBN = QtWidgets.QSpinBox(self.frame_3)
        self.spinBox_cl_HDBN.setMinimumSize(QtCore.QSize(100, 20))
        self.spinBox_cl_HDBN.setMinimum(2)
        self.spinBox_cl_HDBN.setMaximum(100)
        self.spinBox_cl_HDBN.setDisplayIntegerBase(10)
        self.spinBox_cl_HDBN.setObjectName("spinBox_cl_HDBN")
        self.gridLayout_2.addWidget(self.spinBox_cl_HDBN, 0, 4, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(98, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 0, 5, 1, 1)
        self.pushButton_cl_generer = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_cl_generer.setMinimumSize(QtCore.QSize(110, 22))
        self.pushButton_cl_generer.setObjectName("pushButton_cl_generer")
        self.gridLayout_2.addWidget(self.pushButton_cl_generer, 0, 6, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(97, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 0, 7, 1, 1)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 210))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.widget_cl_entrez = MplCanvas(self.frame_2)
        self.widget_cl_entrez.setGeometry(QtCore.QRect(230, -10, 461, 210))
        self.widget_cl_entrez.setMinimumSize(QtCore.QSize(0, 209))
        self.widget_cl_entrez.setObjectName("widget_cl_entrez")
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 210))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.widget_cl_code = MplCanvas(self.frame_4)
        self.widget_cl_code.setGeometry(QtCore.QRect(10, 0, 441, 209))
        self.widget_cl_code.setMinimumSize(QtCore.QSize(0, 209))
        self.widget_cl_code.setObjectName("widget_cl_code")
        self.widget_cl_dsp = MplCanvas(self.frame_4)
        self.widget_cl_dsp.setGeometry(QtCore.QRect(470, 0, 441, 209))
        self.widget_cl_dsp.setMinimumSize(QtCore.QSize(0, 209))
        self.widget_cl_dsp.setObjectName("widget_cl_dsp")
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_6 = QtWidgets.QFrame(self.frame)
        self.frame_6.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem6 = QtWidgets.QSpacerItem(620, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.pushButton_cl_exit = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_cl_exit.setObjectName("pushButton_cl_exit")
        self.horizontalLayout.addWidget(self.pushButton_cl_exit)
        self.verticalLayout.addWidget(self.frame_6)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


        Form.setWindowTitle("Code en ligne")


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_sbe_titre.setText(_translate("Form", " Code en ligne "))
        self.comboBox_cl_choix.setItemText(0, _translate("Form", "RZ"))
        self.comboBox_cl_choix.setItemText(1, _translate("Form", "NRZ"))
        self.comboBox_cl_choix.setItemText(2, _translate("Form", "MILLER"))
        self.comboBox_cl_choix.setItemText(3, _translate("Form", "MANCHISTER"))
        self.comboBox_cl_choix.setItemText(4, _translate("Form", "HDBN"))
        self.label.setText(_translate("Form", "cas de HDBN"))
        self.pushButton_cl_generer.setText(_translate("Form", "generer"))
        self.pushButton_cl_exit.setText(_translate("Form", "exit"))


        self.pushButton_cl_exit.clicked.connect(Form.close)   #************************************************
        self.pushButton_cl_generer.pressed.connect(self.choix_Code) 
        # self.pushButton_cl_generer.clicked.connect(self.entrer_plot) 

        

    # Récupération du texte de l’élément sélectionné dans ComboBox

    def choix_Code(self):   
        entre = self.getEntrez_MnSource() 

        self.hdbn = self.spinBox_cl_HDBN.value() 
        self.content = self.comboBox_cl_choix.currentText() 

        codage = Codage(self.Ts,entre,1)

        codeur_init = codage.normal_coder()
        self.widget_cl_entrez.plot_name(codeur_init, "Input ")

        rz = codage.RZ() 
        nrz = codage.NRZ()            
        miller = codage.miller()        
        manchister = codage.manchester()        
        hdbn = codage.HDBN(self.hdbn)        

        f = np.arange(-20,20,0.001)
        dsp_rz = codage.DSP_RZ(f)
        dsp_nrz = codage.DSP_NRZ(f)
        f1 = np.arange(-0.03,0.03,0.0001)

        dsp_miller = codage.DSP_miller(f)
        dsp_manchister = codage.DSP_manchester(f)
        dsp_hdbn = codage.DSP_HDBN(f)


        if self.content == "RZ" :

            self.widget_cl_code.plot_name(rz, "Codage :"+self.content)
            self.widget_cl_dsp.plot_name1(f,dsp_rz, "DSP")
            self.sorti_Lfiltre.emit(rz, self.Ts,self.content)

        elif self.content == "NRZ" :
            self.widget_cl_code.plot_name(nrz, "Codage :"+self.content)
            self.widget_cl_dsp.plot_name1(f,dsp_nrz, "DSP")
            self.sorti_Lfiltre.emit(nrz, self.Ts,self.content)

        elif self.content == "MILLER" :
            self.widget_cl_code.plot_name(miller, "Codage :"+self.content)
            self.widget_cl_dsp.plot_name1(f,dsp_miller, "DSP")
            self.sorti_Lfiltre.emit(miller, self.Ts,self.content)


        elif self.content == "MANCHISTER" :
            self.widget_cl_code.plot_name(manchister, "Codage :"+self.content)
            self.widget_cl_dsp.plot_name1(f,dsp_manchister,"DSP")
            self.sorti_Lfiltre.emit(manchister, self.Ts, self.content)


        else :
            self.widget_cl_code.plot_name(hdbn,"Codage :"+self.content)
            self.widget_cl_dsp.plot_name1(f,dsp_hdbn, "DSP")
            self.sorti_Lfiltre.emit(hdbn, self.Ts, self.content)



