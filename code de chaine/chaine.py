from PyQt5 import QtCore, QtGui, QtWidgets
import code_code
import Sequence_emit
import modulation_modulation
import Filtre_Filtre
import canal_bruit
import demodulation
import recepteur
import horloge
import decision
import Sequence_recus

from css import styleCss

class Ui_Form(object):

    def __init__(self):
        self.initComponents()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1000, 600)
        Form.setMinimumSize(QtCore.QSize(1000, 600))
        Form.setMaximumSize(QtCore.QSize(1000, 600))
        Form.setStyleSheet(styleCss)

        self.frame = QtWidgets.QFrame(Form)

        self.frame.setGeometry(QtCore.QRect(0, 10, 998, 581))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_15 = QtWidgets.QFrame(self.frame)
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.frame_15)
        self.gridLayout_11.setObjectName("gridLayout_11")
        spacerItem = QtWidgets.QSpacerItem(190, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.frame_15)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_11.addWidget(self.label, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(190, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem1, 0, 2, 1, 1)
        self.verticalLayout.addWidget(self.frame_15)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_8 = QtWidgets.QFrame(self.frame_2)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_8)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_sbe = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_sbe.setObjectName("pushButton_sbe")
        self.gridLayout.addWidget(self.pushButton_sbe, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.frame_8)
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_code = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_code.setObjectName("pushButton_code")
        self.gridLayout_2.addWidget(self.pushButton_code, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_fd = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_fd.setObjectName("pushButton_fd")
        self.gridLayout_3.addWidget(self.pushButton_fd, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(self.frame_2)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_7)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.pushButton_modulation = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_modulation.setObjectName("pushButton_modulation")
        self.gridLayout_5.addWidget(self.pushButton_modulation, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.frame_7)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(652, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.frame_9 = QtWidgets.QFrame(self.frame_3)
        self.frame_9.setMinimumSize(QtCore.QSize(300, 0))
        self.frame_9.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_9)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pushButton_canal = QtWidgets.QPushButton(self.frame_9)
        self.pushButton_canal.setMinimumSize(QtCore.QSize(52, 0))
        self.pushButton_canal.setMaximumSize(QtCore.QSize(250, 16777215))
        self.pushButton_canal.setObjectName("pushButton_canal")
        self.gridLayout_4.addWidget(self.pushButton_canal, 0, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.frame_9)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_10 = QtWidgets.QFrame(self.frame_4)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_10)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame_10)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout_6.addWidget(self.pushButton_10, 0, 0, 1, 1)
        self.horizontalLayout_3.addWidget(self.frame_10)
        self.frame_11 = QtWidgets.QFrame(self.frame_4)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_11)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.pushButton_decision = QtWidgets.QPushButton(self.frame_11)
        self.pushButton_decision.setObjectName("pushButton_decision")
        self.gridLayout_7.addWidget(self.pushButton_decision, 0, 0, 1, 1)
        self.horizontalLayout_3.addWidget(self.frame_11)
        self.frame_12 = QtWidgets.QFrame(self.frame_4)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame_12)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.pushButton_horloge = QtWidgets.QPushButton(self.frame_12)
        self.pushButton_horloge.setObjectName("pushButton_horloge")
        self.gridLayout_8.addWidget(self.pushButton_horloge, 0, 0, 1, 1)
        self.horizontalLayout_3.addWidget(self.frame_12)
        self.frame_14 = QtWidgets.QFrame(self.frame_4)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.frame_14)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.pushButton_fr = QtWidgets.QPushButton(self.frame_14)
        self.pushButton_fr.setObjectName("pushButton_fr")
        self.gridLayout_10.addWidget(self.pushButton_fr, 0, 0, 1, 1)
        self.horizontalLayout_3.addWidget(self.frame_14)
        self.frame_13 = QtWidgets.QFrame(self.frame_4)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.frame_13)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.pushButton_demodilation = QtWidgets.QPushButton(self.frame_13)
        self.pushButton_demodilation.setObjectName("pushButton_demodilation")
        self.gridLayout_9.addWidget(self.pushButton_demodilation, 0, 0, 1, 1)
        self.horizontalLayout_3.addWidget(self.frame_13)
        self.verticalLayout.addWidget(self.frame_4)


        Form.setWindowTitle("Simulation d'un chaine de transmission")


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Simulation d'un chaine de transmission "))
        self.pushButton_sbe.setText(_translate("Form", "Sequence binaire emis"))
        self.pushButton_code.setText(_translate("Form", " Code en ligne "))
        self.pushButton_fd.setText(_translate("Form", "Filtre d\'émission"))
        self.pushButton_modulation.setText(_translate("Form", "Modulation "))
        self.pushButton_canal.setText(_translate("Form", "Canal de Propagation(avec Bruit)"))
        self.pushButton_10.setText(_translate("Form", "Sequence binaire recus"))
        self.pushButton_decision.setText(_translate("Form", "decision"))
        self.pushButton_horloge.setText(_translate("Form", "Horloge"))
        self.pushButton_fr.setText(_translate("Form", "Filtre de Reception"))
        self.pushButton_demodilation.setText(_translate("Form", "Demodulation"))

#lision deux window

        self.pushButton_sbe.clicked.connect(self.data.show)     #***************************************
        self.pushButton_code.clicked.connect(self.code.show)     #***************************************
        self.pushButton_fd.clicked.connect(self.filtre.show)     #***************************************
        self.pushButton_modulation.clicked.connect(self.modu.show)     #***************************************
        self.pushButton_canal.clicked.connect(self.bruit.show)     #***************************************
        self.pushButton_demodilation.clicked.connect(self.demodu.show) 
        self.pushButton_fr.clicked.connect(self.recept.show) 
        self.pushButton_horloge.clicked.connect(self.horloge.show) 
        self.pushButton_decision.clicked.connect(self.decis.show) 
        self.pushButton_10.clicked.connect(self.recu.show) 




    def initComponents(self):
        self.data  = QtWidgets.QWidget()
        self.datanew = Sequence_emit.Ui_Form( )
        self.datanew.setupUi(self.data)


        self.code  = QtWidgets.QWidget()
        self.codeLine = code_code.Ui_Form( )
        self.codeLine.setupUi(self.code)
        self.datanew.sorti_Lcode.connect(self.codeLine.setEntrez_MnSource)  #***************************************


        self.filtre  = QtWidgets.QWidget()
        self.filtre_emit = Filtre_Filtre.Ui_Form()
        self.filtre_emit.setupUi(self.filtre)
        self.codeLine.sorti_Lfiltre.connect(self.filtre_emit.setEntrez_MNCode)  #***************************************


        self.modu  = QtWidgets.QWidget()
        self.modu_new = modulation_modulation.Ui_Form()
        self.modu_new.setupUi(self.modu)
        self.filtre_emit.sorti_Lmodulation.connect(self.modu_new.setEntrez_MNFiltre)  #***************************************


        self.bruit  = QtWidgets.QWidget()
        self.bruit_add = canal_bruit.Ui_Form()
        self.bruit_add.setupUi(self.bruit)
        self.modu_new.sorti_Lcanal.connect(self.bruit_add.setEntrez_MNModulation)  #***************************************


        self.demodu  = QtWidgets.QWidget()
        self.demodu_new = demodulation.Ui_Form()
        self.demodu_new.setupUi(self.demodu)
        self.bruit_add.sorti_Ldemodulation.connect(self.demodu_new.setEntrez_MNCanal)  #***************************************


        self.recept  = QtWidgets.QWidget()
        self.recepteur_new = recepteur.Ui_Form()
        self.recepteur_new.setupUi(self.recept)
        self.demodu_new.sorti_Lrecepteur.connect(self.recepteur_new.setEntrez_MNDemodulation)  #***************************************

        self.horloge  = QtWidgets.QWidget()
        self.horloge_new = horloge.Ui_Form()
        self.horloge_new.setupUi(self.horloge)
        self.recepteur_new.sorti_Lhorloge.connect(self.horloge_new.setEntrez_MNReception)  #***************************************

        self.decis  = QtWidgets.QWidget()
        self.decis_new = decision.Ui_Form()
        self.decis_new.setupUi(self.decis)
        self.recepteur_new.sorti_Ldecision.connect(self.decis_new.setEntrez_MNRecep_desc)  #***************************************

        # self.horloge_new.sorti_Ldecision.connect(self.decis_new.setEntrez_MNReception)  #***************************************

        self.recu  = QtWidgets.QWidget()
        self.recu_new = Sequence_recus.Ui_Form()
        self.recu_new.setupUi(self.recu)
        self.decis_new.sorti_LseqRecus.connect(self.recu_new.setEntrez_MN_desc)  #***************************************


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())




