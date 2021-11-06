from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        MainWindow.setMinimumSize(QtCore.QSize(200, 200))
        MainWindow.setWindowOpacity(1.0)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.comboBox_distribution = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_distribution.setObjectName("comboBox_distribution")
        self.comboBox_distribution.addItem("")
        self.comboBox_distribution.addItem("")
        self.gridLayout_3.addWidget(self.comboBox_distribution, 4, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_3.addWidget(self.progressBar, 6, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.slider_n = QtWidgets.QSlider(self.centralwidget)
        self.slider_n.setOrientation(QtCore.Qt.Horizontal)
        self.slider_n.setObjectName("slider_n")
        self.gridLayout_2.addWidget(self.slider_n, 1, 0, 1, 1)
        self.label_n = QtWidgets.QLabel(self.centralwidget)
        self.label_n.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_n.setObjectName("label_n")
        self.gridLayout_2.addWidget(self.label_n, 0, 0, 1, 1)
        self.spinBox_n = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_n.setObjectName("spinBox_n")
        self.gridLayout_2.addWidget(self.spinBox_n, 1, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 0, 1, 2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_m = QtWidgets.QLabel(self.centralwidget)
        self.label_m.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_m.setObjectName("label_m")
        self.gridLayout.addWidget(self.label_m, 0, 0, 1, 1)
        self.slider_m = QtWidgets.QSlider(self.centralwidget)
        self.slider_m.setOrientation(QtCore.Qt.Horizontal)
        self.slider_m.setObjectName("slider_m")
        self.gridLayout.addWidget(self.slider_m, 1, 0, 1, 1)
        self.spinBox_m = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_m.setSuffix("")
        self.spinBox_m.setObjectName("spinBox_m")
        self.gridLayout.addWidget(self.spinBox_m, 1, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 2)
        self.label_distribution = QtWidgets.QLabel(self.centralwidget)
        self.label_distribution.setObjectName("label_distribution")
        self.gridLayout_3.addWidget(self.label_distribution, 3, 0, 1, 1)
        self.radioButton_N_const = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_N_const.setChecked(True)
        self.radioButton_N_const.setObjectName("radioButton_N_const")
        self.gridLayout_3.addWidget(self.radioButton_N_const, 2, 0, 1, 1)
        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start.setObjectName("pushButton_start")
        self.gridLayout_3.addWidget(self.pushButton_start, 6, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 5, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionQuit_2 = QtWidgets.QAction(MainWindow)
        self.actionQuit_2.setObjectName("actionQuit_2")


        self.pushButton_start.clicked.connect(self.start)
        self.slider_m.valueChanged.connect(self.spinBox_m.setValue)
        self.spinBox_m.valueChanged.connect(self.slider_m.setValue)
        self.slider_n.valueChanged.connect(self.spinBox_n.setValue)
        self.spinBox_n.valueChanged.connect(self.slider_n.setValue)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox_distribution.setItemText(0, _translate("MainWindow", "Normal"))
        self.comboBox_distribution.setItemText(1, _translate("MainWindow", "Poisson"))
        self.label_n.setText(_translate("MainWindow", "N - elemente in subretea"))
        self.label_m.setText(_translate("MainWindow", "M - subretele"))
        self.label_distribution.setText(_translate("MainWindow", "Distribution type:"))
        self.radioButton_N_const.setText(_translate("MainWindow", "N - constant"))
        self.pushButton_start.setText(_translate("MainWindow", "Start"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionQuit_2.setText(_translate("MainWindow", "Quit"))

    def start(self):
        print("running")




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
