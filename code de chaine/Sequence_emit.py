from PyQt5 import QtCore, QtGui, QtWidgets
from mplcanvas import MplCanvas
from css import styleCss
from data_manipulation import Gestion_data
from codage_en_ligne import Codage


class Ui_Form(QtCore.QObject):

    sorti_Lcode = QtCore.pyqtSignal(list,int)

    def __init__(self,parent=None):
        super().__init__(parent)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(489, 627)
        Form.setMinimumSize(QtCore.QSize(489, 627))
        Form.setMaximumSize(QtCore.QSize(489, 627))
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 491, 681))
        self.frame.setMinimumSize(QtCore.QSize(491, 681))
        self.frame.setMaximumSize(QtCore.QSize(491, 681))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.setStyleSheet(styleCss)  #*****************************************


        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_6.setObjectName("gridLayout_6")
        spacerItem = QtWidgets.QSpacerItem(97, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem, 0, 0, 1, 1)
        self.label_sbe_titre_2 = QtWidgets.QLabel(self.frame_3)
        self.label_sbe_titre_2.setMinimumSize(QtCore.QSize(0, 0))
        self.label_sbe_titre_2.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_sbe_titre_2.setFont(font)
        self.label_sbe_titre_2.setObjectName("label_sbe_titre_2")
        self.gridLayout_6.addWidget(self.label_sbe_titre_2, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(97, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem1, 0, 2, 1, 1)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_13 = QtWidgets.QFrame(self.frame)
        self.frame_13.setMaximumSize(QtCore.QSize(16777215, 35))
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_13)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label = QtWidgets.QLabel(self.frame_13)
        self.label.setMinimumSize(QtCore.QSize(75, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_7.addWidget(self.label, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(224, 12, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem2, 0, 2, 1, 1)
        self.spinBox_Ts = QtWidgets.QSpinBox(self.frame_13)
        self.spinBox_Ts.setMinimumSize(QtCore.QSize(131, 22))
        self.spinBox_Ts.setMinimum(1)
        self.spinBox_Ts.setMaximum(10000)
        self.spinBox_Ts.setProperty("value", 100)
        self.spinBox_Ts.setObjectName("spinBox_Ts")
        self.gridLayout_7.addWidget(self.spinBox_Ts, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame_13)
        self.frame_9 = QtWidgets.QFrame(self.frame)
        self.frame_9.setMaximumSize(QtCore.QSize(123345, 40))
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.pushButton_sbe_data = QtWidgets.QPushButton(self.frame_9)
        self.pushButton_sbe_data.setGeometry(QtCore.QRect(10, 10, 75, 20))
        self.pushButton_sbe_data.setObjectName("pushButton_sbe_data")
        self.lineEdit_sbe_datatest_2 = QtWidgets.QLineEdit(self.frame_9)
        self.lineEdit_sbe_datatest_2.setEnabled(True)
        self.lineEdit_sbe_datatest_2.setGeometry(QtCore.QRect(180, 10, 240, 20))
        self.lineEdit_sbe_datatest_2.setStatusTip("")
        self.lineEdit_sbe_datatest_2.setWhatsThis("")
        self.lineEdit_sbe_datatest_2.setAccessibleName("")
        self.lineEdit_sbe_datatest_2.setAccessibleDescription("")
        self.lineEdit_sbe_datatest_2.setAutoFillBackground(False)
        self.lineEdit_sbe_datatest_2.setStyleSheet("")
        self.lineEdit_sbe_datatest_2.setText("1")
        self.lineEdit_sbe_datatest_2.setObjectName("lineEdit_sbe_datatest_2")
        self.verticalLayout.addWidget(self.frame_9)
        self.frame_10 = QtWidgets.QFrame(self.frame)
        self.frame_10.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame_10)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.pushButton_sbe_generez_2 = QtWidgets.QPushButton(self.frame_10)
        self.pushButton_sbe_generez_2.setObjectName("pushButton_sbe_generez_2")
        self.gridLayout_8.addWidget(self.pushButton_sbe_generez_2, 0, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(291, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem3, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame_10)
        self.frame_11 = QtWidgets.QFrame(self.frame)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.widget_sbe_2 = MplCanvas(self.frame_11)
        self.widget_sbe_2.setGeometry(QtCore.QRect(20, 0, 431, 191))
        self.widget_sbe_2.setObjectName("widget_sbe_2")
        self.frame_12 = QtWidgets.QFrame(self.frame_11)
        self.frame_12.setGeometry(QtCore.QRect(0, 400, 471, 40))
        self.frame_12.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.frame_12)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.pushButton_sbe_exit_2 = QtWidgets.QPushButton(self.frame_12)
        self.pushButton_sbe_exit_2.setObjectName("pushButton_sbe_exit_2")
        self.gridLayout_10.addWidget(self.pushButton_sbe_exit_2, 0, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(291, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem4, 0, 0, 1, 1)
        self.widget_sbe_3 = MplCanvas(self.frame_11)
        self.widget_sbe_3.setGeometry(QtCore.QRect(20, 200, 431, 191))
        self.widget_sbe_3.setObjectName("widget_sbe_3")
        self.verticalLayout.addWidget(self.frame_11)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # connect this button to function get text 
        self.pushButton_sbe_generez_2.clicked.connect(self.getAleatoire)   #************************************************
        self.pushButton_sbe_data.clicked.connect(self.gettext) 
        self.pushButton_sbe_exit_2.clicked.connect(Form.close)   #************************************************
        Form.setWindowTitle("Sequence binaire emise")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_sbe_titre_2.setText(_translate("Form", "Sequence binaire emise"))
        self.label.setText(_translate("Form", "  entrer Ts"))
        self.pushButton_sbe_data.setText(_translate("Form", "entrer data"))
        self.lineEdit_sbe_datatest_2.setPlaceholderText(_translate("Form", "Entrez un signial maxsize=15"))
        self.pushButton_sbe_generez_2.setText(_translate("Form", "aliatoire data"))
        self.pushButton_sbe_exit_2.setText(_translate("Form", "exit"))




    def gettext(self):
        # get text form line edit 
        # plot text 
        self.Ts = self.spinBox_Ts.value() 
        if self.lineEdit_sbe_datatest_2.text() is not None:
            lineEdit_sbe_datatest = [int(input) for input in self.lineEdit_sbe_datatest_2.text()] 
        else:
            lineEdit_sbe_datatest = [1]
        codage = Codage(self.Ts,lineEdit_sbe_datatest,1)
        codeur_normal = codage.normal_coder()
        codeur_clk = codage.CLK()

        self.widget_sbe_2.plot_name(codeur_clk,"horloge")
        self.widget_sbe_3.plot_name(codeur_normal, "Input")

        self.sorti_Lcode.emit(lineEdit_sbe_datatest,self.Ts)


    def getAleatoire(self):

        self.Ts = self.spinBox_Ts.value() 

        lineEdit_sbe_datatest =  Gestion_data.rand_data(10)
        # data = str(Gestion_data().convert(lineEdit_sbe_datatest))
        # print(data)
        data = [str(i) for i in lineEdit_sbe_datatest] 
        res = str("".join(data))  
        self.lineEdit_sbe_datatest_2.setText(res)

        codage = Codage(self.Ts,lineEdit_sbe_datatest,1)
        codeur_normal = codage.normal_coder()
        codeur_clk = codage.CLK()

        self.widget_sbe_2.plot_name(codeur_clk, "horloge")
        self.widget_sbe_3.plot_name(codeur_normal,"Input")

        self.sorti_Lcode.emit(lineEdit_sbe_datatest,self.Ts)

 

