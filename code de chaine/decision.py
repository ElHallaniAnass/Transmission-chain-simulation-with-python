from PyQt5 import QtCore, QtGui, QtWidgets
from mplcanvas import MplCanvas
from css import styleCss
from codage_en_ligne import Modulation
import numpy as np



class Ui_Form(QtCore.QObject):

    sorti_LseqRecus = QtCore.pyqtSignal(list,int)

    def __init__(self,parent=None):
        super().__init__(parent)


    entrez_Mn_recep_desc = []
    Ts = 0
    def setEntrez_MNRecep_desc(self,entrez_Mn_recep_desc, Ts):
        self.entrez_Mn_recep_desc = entrez_Mn_recep_desc
        self.Ts = Ts
        self.get_rece_desc_plot()

    def getEntrez_MNRecep_desc(self):
        return self.entrez_Mn_recep_desc



    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(588, 600)
        Form.setMinimumSize(QtCore.QSize(588, 600))
        Form.setMaximumSize(QtCore.QSize(588, 600))
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
        self.widget_reception = MplCanvas(self.frame_4)
        self.widget_reception.setGeometry(QtCore.QRect(30, 0, 511, 210))
        self.widget_reception.setMinimumSize(QtCore.QSize(0, 210))
        self.widget_reception.setObjectName("widget_reception")
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_7 = QtWidgets.QFrame(self.frame)
        self.frame_7.setMinimumSize(QtCore.QSize(0, 212))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.widget_Decision = MplCanvas(self.frame_7)
        self.widget_Decision.setGeometry(QtCore.QRect(30, 0, 511, 210))
        self.widget_Decision.setMinimumSize(QtCore.QSize(0, 210))
        self.widget_Decision.setObjectName("widget_Decision")
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

        Form.setWindowTitle("Decision")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Decision"))
        self.pushButton_exit.setText(_translate("Form", "exit"))

        self.pushButton_exit.clicked.connect(Form.close)   #************************************************

    def get_rece_desc_plot(self):
        entre = self.getEntrez_MNRecep_desc() 
        self.widget_reception.plot_name(entre, "avant decision")
        seuil = np.mean(entre)

        entre_decision = Modulation().decision(entre,100,seuil)    
        self.widget_Decision.plot_name(entre_decision, "apres decision")

        self.sorti_LseqRecus.emit(entre_decision, self.Ts)
