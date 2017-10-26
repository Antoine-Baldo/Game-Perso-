
"Programmed by Antoine BALDO"

import os
import random
import sys
from PyQt4 import QtGui, QtCore
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from pygame import *
from game1 import *

def run():
	app = QtGui.QApplication(sys.argv)
	GUI = Window()
	GUI.show()
	sys.exit(app.exec_())
class Window(QtGui.QDialog):
	def __init__(self, parent=None):
		super(Window, self).__init__(parent)
		self.setGeometry(400,50,500,500)
		self.setWindowTitle('Unicorne Game control!!!')
		self.setWindowIcon(QtGui.QIcon('Media/Graphics/rainbowwin.png'))
		grid = QtGui.QGridLayout()
		self.setLayout(grid)
		Label1 = QtGui.QLabel('\t\t\t'+"Bienvenu dans le jeu de la licorne par Antoine BALDO!")
		Label4 = QtGui.QLabel()
		pixmap = QtGui.QPixmap("Media/Graphics/welcome.jpg")
		Label4.setPixmap(pixmap)
		Label2 = QtGui.QLabel('\t\t\t'+"Choisie le nombre d'ennemies et click sur le bouton START ")
		Label3 = QtGui.QLabel("Evite les mechants et atteint le block arc-en-ciel (comme celui en haut a gauhe de cette fenetre) pour finir le niveau")
		btnQ = QtGui.QPushButton('QUIT', self)
		btnQ.clicked.connect(QtCore.QCoreApplication.instance().quit)
		self.sp = QtGui.QSpinBox(self)
		self.sp.setRange(0, 30)
		self.sp.setSingleStep(1)
		self.sl = QtGui.QSlider(QtCore.Qt.Horizontal, self)
		self.sl.setMinimum(0)
		self.sl.setMaximum(30)
		self.sl.setValue(0)
		self.sl.setTickInterval(5)
		self.sl.setTickPosition(QtGui.QSlider.TicksBelow)
		self.sl.valueChanged.connect(self.sp.setValue)
		self.sp.valueChanged.connect(self.sl.setValue)
		
		def run_game():
			Val_sp = int(self.sp.value())
			game(Val_sp)

		btnS = QtGui.QPushButton("START", self)
		btnS.clicked.connect(run_game)
		grid.addWidget(Label4)
		grid.addWidget(Label1)
		grid.addWidget(self.sp)
		grid.addWidget(self.sl)
		grid.addWidget(Label2)
		grid.addWidget(Label3)
		grid.addWidget(btnS)
		grid.addWidget(btnQ)
run()