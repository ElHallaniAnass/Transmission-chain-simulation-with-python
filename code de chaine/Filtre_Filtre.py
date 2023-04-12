from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
from mplcanvas import MplCanvas
from codage_en_ligne import Codage, Filtre_emi, Modulation
from css import styleCss


class Ui_Form(QtCore.QObject):

    sorti_Lmodulation = QtCore.pyqtSignal(list,int)

    def __init__(self,parent=None):
        super().__init__(parent)



    entrez_Mn_code = []
    Ts = 0
    code = str
    def setEntrez_MNCode(self,entrez_Mn_code,Ts, code):
        self.code = code
        self.Ts = Ts
        self.entrez_Mn_code = entrez_Mn_code
        self.emit_Nyquist()
        
    def getEntrez_MnCode(self):
        return self.entrez_Mn_code




    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(907, 656)
        Form.setMinimumSize(QtCore.QSize(907, 656))
        Form.setMaximumSize(QtCore.QSize(907, 656))
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(-10, -10, 931, 665))
        self.frame.setMinimumSize(QtCore.QSize(931, 665))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.setStyleSheet(styleCss)  #*****************************************

        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 35))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(334, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(333, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 2, 1, 1)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 37))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 35))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(287, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem2, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(287, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem3, 0, 2, 1, 1)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setMinimumSize(QtCore.QSize(0, 210))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.widget_Fb_code = MplCanvas(self.frame_5)
        self.widget_Fb_code.setGeometry(QtCore.QRect(10, 0, 431, 210))
        self.widget_Fb_code.setMinimumSize(QtCore.QSize(0, 210))
        self.widget_Fb_code.setObjectName("widget_Fb_code")
        self.widget_Fb_imp = MplCanvas(self.frame_5)
        self.widget_Fb_imp.setGeometry(QtCore.QRect(470, 0, 431, 210))
        self.widget_Fb_imp.setMinimumSize(QtCore.QSize(0, 210))
        self.widget_Fb_imp.setObjectName("widget_Fb_imp")
        self.verticalLayout.addWidget(self.frame_5)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 35))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem4 = QtWidgets.QSpacerItem(304, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(304, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 0, 2, 1, 1)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_6 = QtWidgets.QFrame(self.frame)
        self.frame_6.setMaximumSize(QtCore.QSize(16777215, 37))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(self.frame_6)
        self.label_4.setMinimumSize(QtCore.QSize(120, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 1, 1, 1)
        self.doubleSpinBox_alpha = QtWidgets.QDoubleSpinBox(self.frame_6)
        self.doubleSpinBox_alpha.setMinimumSize(QtCore.QSize(100, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.doubleSpinBox_alpha.setFont(font)
        self.doubleSpinBox_alpha.setDecimals(1)
        self.doubleSpinBox_alpha.setMaximum(1.0)
        self.doubleSpinBox_alpha.setSingleStep(0.5)
        self.doubleSpinBox_alpha.setProperty("value", 0.0)
        self.doubleSpinBox_alpha.setObjectName("doubleSpinBox_alpha")
        self.gridLayout_2.addWidget(self.doubleSpinBox_alpha, 0, 3, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(118, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem6, 0, 4, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(119, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem7, 0, 6, 1, 1)
        self.pushButton_Fn_generer = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_Fn_generer.setMinimumSize(QtCore.QSize(110, 22))
        self.pushButton_Fn_generer.setObjectName("pushButton_Fn_generer")
        self.gridLayout_2.addWidget(self.pushButton_Fn_generer, 0, 5, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(119, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem8, 0, 0, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem9, 0, 2, 1, 1)
        self.verticalLayout.addWidget(self.frame_6)
        self.frame_9 = QtWidgets.QFrame(self.frame)
        self.frame_9.setMinimumSize(QtCore.QSize(0, 210))
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.widget_Fn_dsp = MplCanvas(self.frame_9)
        self.widget_Fn_dsp.setGeometry(QtCore.QRect(470, 0, 431, 210))
        self.widget_Fn_dsp.setMinimumSize(QtCore.QSize(0, 210))
        self.widget_Fn_dsp.setObjectName("widget_Fn_dsp")
        self.widget_Fn = MplCanvas(self.frame_9)
        self.widget_Fn.setGeometry(QtCore.QRect(10, 0, 431, 210))
        self.widget_Fn.setMinimumSize(QtCore.QSize(0, 210))
        self.widget_Fn.setObjectName("widget_Fn")
        self.verticalLayout.addWidget(self.frame_9)
        self.frame_7 = QtWidgets.QFrame(self.frame)
        self.frame_7.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_7.setMaximumSize(QtCore.QSize(16777215, 35))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_7)
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem10 = QtWidgets.QSpacerItem(620, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem10, 0, 0, 1, 1)
        self.pushButton_Fn_exit = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_Fn_exit.setObjectName("pushButton_Fn_exit")
        self.gridLayout_5.addWidget(self.pushButton_Fn_exit, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame_7)
        self.frame_2.raise_()
        self.frame_3.raise_()
        self.frame_4.raise_()
        self.frame_6.raise_()
        self.frame_7.raise_()
        self.frame_9.raise_()
        self.frame_5.raise_()


        Form.setWindowTitle("Filtre d'émission")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Filtre d\'émission"))
        self.label_2.setText(_translate("Form", "Filtre Blanchissant "))
        self.label_3.setText(_translate("Form", "Filtre de Nyquist"))
        self.label_4.setText(_translate("Form", "             alpha"))
        self.pushButton_Fn_generer.setText(_translate("Form", "generer"))
        self.pushButton_Fn_exit.setText(_translate("Form", "exit"))



        self.pushButton_Fn_exit.clicked.connect(Form.close)   #************************************************
        self.pushButton_Fn_generer.pressed.connect(self.emit_Nyquist) 

        




    def emit_Nyquist(self): 
        self.alpha = self.doubleSpinBox_alpha.value() 

        entre_code = self.getEntrez_MnCode() 
        entre_code_filtre = Filtre_emi().filtre_blanch(entre_code)
        self.widget_Fb_code.plot_name(entre_code, "Codage :"+self.code)
        self.widget_Fb_imp.plot_name(entre_code_filtre, "Filtre blanchissant")


        t = np.linspace(0,len(entre_code_filtre),len(entre_code_filtre))
        filtr_n = list(Filtre_emi().filre_ideal_alpha(entre_code_filtre,self.alpha ,t,2))

        f = np.arange(-20,20,0.1)
        dsp = Filtre_emi().DSP_FE(f,self.Ts,self.alpha )
        self.widget_Fn.plot2(t,filtr_n, " Filtre de Nyquist")
   
        self.widget_Fn_dsp.plot_name1(f,dsp,"DSP")

        self.sorti_Lmodulation.emit(filtr_n,self.Ts)

