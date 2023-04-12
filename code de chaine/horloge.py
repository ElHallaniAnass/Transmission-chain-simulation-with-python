from PyQt5 import QtCore, QtGui, QtWidgets
from codage_en_ligne import Codage
from mplcanvas import MplCanvas
from css import styleCss
from data_manipulation import Gestion_data

class Ui_Form(QtCore.QObject):

    sorti_Ldecision = QtCore.pyqtSignal(int)

    def __init__(self,parent=None):
        super().__init__(parent)



    entrez_Mn_reception = []
    Ts = 0
    def setEntrez_MNReception(self,entrez_Mn_reception, Ts):
        self.Ts = Ts
        self.entrez_Mn_reception = entrez_Mn_reception
        self.get_reception_plot()

    def getEntrez_MNReception(self):
        return self.entrez_Mn_reception

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(585, 595)
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
        self.widget_reception_2 = MplCanvas(self.frame_4)
        self.widget_reception_2.setGeometry(QtCore.QRect(30, 0, 511, 210))
        self.widget_reception_2.setMinimumSize(QtCore.QSize(0, 210))
        self.widget_reception_2.setObjectName("widget_reception_2")
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_7 = QtWidgets.QFrame(self.frame)
        self.frame_7.setMinimumSize(QtCore.QSize(0, 212))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.widget_horloge = MplCanvas(self.frame_7)
        self.widget_horloge.setGeometry(QtCore.QRect(30, 0, 511, 210))
        self.widget_horloge.setMinimumSize(QtCore.QSize(0, 210))
        self.widget_horloge.setObjectName("widget_horloge")
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

        Form.setWindowTitle("Récupération d'horloge")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Récupération d\'horloge"))
        self.pushButton_exit.setText(_translate("Form", "exit"))


        self.pushButton_exit.clicked.connect(Form.close)   #************************************************


    def get_reception_plot(self):
        entre = self.getEntrez_MNReception() 
        self.widget_reception_2.plot_name(entre, "apres reception")


        codage = Codage(self.Ts,entre[0:int(len(entre)/self.Ts)],1)
        codeur_clk = codage.CLK()
        self.widget_horloge.plot_name(codeur_clk, "Horloge")

        # self.sorti_Ldecision.emit(self.Ts)
