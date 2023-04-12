from PyQt5 import QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

class MplCanvas(QtWidgets.QWidget):
    def __init__(self,parent = None):
        super(MplCanvas, self).__init__(parent)

        # CREATE FIGURE AND SETTINGS
        self.figure = plt.figure()
        self.figure.patch.set_facecolor("None")
        self.canvas = FigureCanvas(self.figure)
        self.axes = self.figure.add_subplot(111)
        self.axes.patch.set_alpha(0.3)
        self.axes.spines['left'].set_color('white')
        self.axes.spines['bottom'].set_color('white')
        self.axes.tick_params(axis='x', colors='white')
        self.axes.tick_params(axis='y', colors='white')


        ###### Make the background of the canvas transparent
        self.canvas.setStyleSheet("background-color:transparent;")


        self.setLayout(QtWidgets.QVBoxLayout())
        self.layout().addWidget(self.canvas,1)

    def getAxes(self):
        print("test axes .")
        return self.axes
    
    def plot(self,vect):
        self.axes.cla()
        self.axes.plot(vect)
        self.canvas.draw()
        plt.close('all')

    def plot2(self,t,vect,title):
        self.axes.cla()
        self.axes.plot(t,vect)
        self.axes.set_title(title)

        self.canvas.draw()
        plt.close('all')

    def plot_name(self,vect,title):
        self.axes.cla()
        self.axes.plot(vect)
        # self.axes.set_xlabel(xlablel)
        # self.axes.set_ylabel(ylabel)
        self.axes.set_title(title)

        self.canvas.draw()
        plt.close('all')   

    def plot_name1(self,t,vect,title):
        self.axes.cla()
        self.axes.plot(t,vect)
        # self.axes.set_xlabel(xlablel)
        # self.axes.set_ylabel(ylabel)
        self.axes.set_title(title)

        self.canvas.draw()
        plt.close('all')   


