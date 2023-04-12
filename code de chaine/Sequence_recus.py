from PyQt5 import QtCore, QtGui, QtWidgets
from mplcanvas import MplCanvas
from css import styleCss


class Ui_Form(QtCore.QObject):

    def __init__(self,parent=None):
        super().__init__(parent)

    entrez_Mn_decision = []
    Ts = 0

    def setEntrez_MN_desc(self,entrez_Mn_decision, Ts):
        self.entrez_Mn_decision = entrez_Mn_decision
        self.Ts = Ts
        self.get__desc()

    def getEntrez_MN_desc(self):
        return self.entrez_Mn_decision


    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(585, 610)
        Form.setMinimumSize(QtCore.QSize(585, 610))
        Form.setMaximumSize(QtCore.QSize(585, 610))
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 585, 610))
        self.frame.setMinimumSize(QtCore.QSize(585, 610))
        self.frame.setMaximumSize(QtCore.QSize(585, 610))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.setStyleSheet(styleCss)  #*****************************************

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(161, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(161, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 2, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setMinimumSize(QtCore.QSize(0, 212))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.widget_demodu_bruit = MplCanvas(self.frame_5)
        self.widget_demodu_bruit.setGeometry(QtCore.QRect(30, 20, 511, 210))
        self.widget_demodu_bruit.setMinimumSize(QtCore.QSize(0, 210))
        self.widget_demodu_bruit.setObjectName("widget_demodu_bruit")
        self.verticalLayout_2.addWidget(self.frame_5)
        self.frame_7 = QtWidgets.QFrame(self.frame)
        self.frame_7.setMinimumSize(QtCore.QSize(0, 212))
        self.frame_7.setMaximumSize(QtCore.QSize(16777215, 140))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_4 = QtWidgets.QFrame(self.frame_7)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(161, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem2, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_5.addWidget(self.label_3, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(161, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem3, 0, 2, 1, 1)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_2 = QtWidgets.QFrame(self.frame_7)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem4 = QtWidgets.QSpacerItem(257, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)


        self.label.setText("........")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(256, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 0, 2, 1, 1)
        self.verticalLayout.addWidget(self.frame_2)
        self.verticalLayout_2.addWidget(self.frame_7)
        self.frame_9 = QtWidgets.QFrame(self.frame)
        self.frame_9.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_9)
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem6 = QtWidgets.QSpacerItem(350, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem6, 0, 0, 1, 1)
        self.pushButton_exit_2 = QtWidgets.QPushButton(self.frame_9)
        self.pushButton_exit_2.setObjectName("pushButton_exit_2")
        self.gridLayout_4.addWidget(self.pushButton_exit_2, 0, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_9)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Sequence binaire recue"))
        self.label_3.setText(_translate("Form", "Sequence binaire recue apres decision"))
        self.pushButton_exit_2.setText(_translate("Form", "exit"))
        self.pushButton_exit_2.clicked.connect(Form.close) 


    def get__desc(self):
        entre = self.getEntrez_MN_desc() 

        self.widget_demodu_bruit.plot_name(entre, "apres decision")
        data = ""
        l = 0
        for i, n in enumerate(entre):
            if i == l*self.Ts :
                data += str(n)
                l += 1
        self.label.setText(data)
