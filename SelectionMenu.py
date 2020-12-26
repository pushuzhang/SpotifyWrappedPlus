from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
from PyQt5.QtCore import QDate


class SelectionWindow(object):
    def __init__(self):
        self.topACount = 100
        self.topAAll = False;
        self.topSCount = 100
        self.topSAll = False;
        self.topSFromA = 1

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(380, 370)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Finish Button
        self.FinishB = QtWidgets.QPushButton(self.centralwidget)
        self.FinishB.setGeometry(QtCore.QRect(160, 320, 75, 23))
        self.FinishB.setObjectName("FinishB")
        self.FinishB.clicked.connect(self.clicked)
        self.fLabel = QtWidgets.QLabel(self.centralwidget)
        self.fLabel.setText("")
        self.fLabel.setObjectName("fLabel")
        self.fLabel.setGeometry(60,293,260,23)

        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 20, 361, 268))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.topA = QtWidgets.QCheckBox(self.widget)
        self.topA.setObjectName("topA")
        self.verticalLayout_2.addWidget(self.topA)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.aTop10 = QtWidgets.QCheckBox(self.widget)
        self.aTop10.setObjectName("aTop10")
        self.horizontalLayout_2.addWidget(self.aTop10)
        self.aTop100 = QtWidgets.QCheckBox(self.widget)
        self.aTop100.setObjectName("aTop100")
        self.horizontalLayout_2.addWidget(self.aTop100)
        self.aAll = QtWidgets.QCheckBox(self.widget)
        self.aAll.setObjectName("aAll")
        self.horizontalLayout_2.addWidget(self.aAll)

        regex = QtCore.QRegExp("[1-9][0-9]*")  # regular expression for filtering custom user input

        self.aCustom = QtWidgets.QLineEdit(self.widget)
        self.aCustom.setObjectName("aCustom")
        input_validatorA = QtGui.QRegExpValidator(regex, self.aCustom)
        self.aCustom.setValidator(input_validatorA)
        self.horizontalLayout_2.addWidget(self.aCustom)

        self.aLabel = QtWidgets.QLabel(self.widget)
        self.aLabel.setObjectName("aLabel")
        self.horizontalLayout_2.addWidget(self.aLabel)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.aMPD = QtWidgets.QCheckBox(self.widget)
        self.aMPD.setObjectName("aMPD")
        self.verticalLayout_2.addWidget(self.aMPD)

        self.aByMonth = QtWidgets.QCheckBox(self.widget)
        self.aByMonth.setObjectName("aByMonth")
        self.verticalLayout_2.addWidget(self.aByMonth)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.aTopSongs = QtWidgets.QCheckBox(self.widget)
        self.aTopSongs.setObjectName("aTopSongs")
        self.horizontalLayout.addWidget(self.aTopSongs)
        self.asTop1 = QtWidgets.QCheckBox(self.widget)
        self.asTop1.setObjectName("asTop1")
        self.horizontalLayout.addWidget(self.asTop1)
        self.asTop3 = QtWidgets.QCheckBox(self.widget)
        self.asTop3.setObjectName("asTop3")
        self.horizontalLayout.addWidget(self.asTop3)
        self.asTop5 = QtWidgets.QCheckBox(self.widget)
        self.asTop5.setObjectName("asTop5")
        self.horizontalLayout.addWidget(self.asTop5)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.topS = QtWidgets.QCheckBox(self.widget)
        self.topS.setObjectName("topS")
        self.verticalLayout_2.addWidget(self.topS)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.sTop10 = QtWidgets.QCheckBox(self.widget)
        self.sTop10.setObjectName("sTop10")
        self.horizontalLayout_3.addWidget(self.sTop10)
        self.sTop100 = QtWidgets.QCheckBox(self.widget)
        self.sTop100.setObjectName("sTop100")
        self.horizontalLayout_3.addWidget(self.sTop100)
        self.sAll = QtWidgets.QCheckBox(self.widget)
        self.sAll.setObjectName("sAll")
        self.horizontalLayout_3.addWidget(self.sAll)

        self.sCustom = QtWidgets.QLineEdit(self.widget)
        self.sCustom.setObjectName("sCustom")
        input_validatorS = QtGui.QRegExpValidator(regex, self.sCustom)
        self.sCustom.setValidator(input_validatorS)
        self.horizontalLayout_3.addWidget(self.sCustom)

        self.sLabel = QtWidgets.QLabel(self.widget)
        self.sLabel.setObjectName("sLabel")
        self.horizontalLayout_3.addWidget(self.sLabel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.sMDL = QtWidgets.QCheckBox(self.widget)
        self.sMDL.setObjectName("sMDL")
        self.verticalLayout_2.addWidget(self.sMDL)
        self.sByMonth = QtWidgets.QCheckBox(self.widget)
        self.sByMonth.setObjectName("sByMonth")
        self.verticalLayout_2.addWidget(self.sByMonth)
        self.line_2 = QtWidgets.QFrame(self.widget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.setTime = QtWidgets.QCheckBox(self.widget)
        self.setTime.setObjectName("setTime")
        self.horizontalLayout_4.addWidget(self.setTime)
        self.startTime = QtWidgets.QDateEdit(self.widget)
        self.startTime.setObjectName("startTime")
        today = datetime.datetime.now()
        sd = QDate(today.year, 1, 1)
        self.startTime.setDate(sd)
        self.horizontalLayout_4.addWidget(self.startTime)
        self.telda = QtWidgets.QLabel(self.widget)
        self.telda.setObjectName("telda")
        self.horizontalLayout_4.addWidget(self.telda)
        self.endTime = QtWidgets.QDateEdit(self.widget)
        self.endTime.setObjectName("endTime")
        ed = QDate(today.year, today.month, today.day)
        self.endTime.setDate(ed)
        self.horizontalLayout_4.addWidget(self.endTime)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 380, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.FinishB.setText(_translate("MainWindow", "Finish"))
        self.topA.setText(_translate("MainWindow", "Top Artists"))
        self.aTop10.setText(_translate("MainWindow", "Top10"))
        self.aTop100.setText(_translate("MainWindow", "Top100"))
        self.aAll.setText(_translate("MainWindow", "All"))
        self.aLabel.setText(_translate("MainWindow", "Custom"))
        self.aMPD.setText(_translate("MainWindow", "Show most listened day and minutes played"))
        self.aByMonth.setText(_translate("MainWindow", "Rank By Month"))
        self.aTopSongs.setText(_translate("MainWindow", "Show top song(s) from each Artists"))
        self.asTop1.setText(_translate("MainWindow", "Top1"))
        self.asTop3.setText(_translate("MainWindow", "Top3"))
        self.asTop5.setText(_translate("MainWindow", "Top5"))
        self.topS.setText(_translate("MainWindow", "Top Songs"))
        self.sTop10.setText(_translate("MainWindow", "Top10"))
        self.sTop100.setText(_translate("MainWindow", "Top100"))
        self.sAll.setText(_translate("MainWindow", "All"))
        self.sLabel.setText(_translate("MainWindow", "Custom"))
        self.sMDL.setText(_translate("MainWindow", "Show most listened day and times listened"))
        self.sByMonth.setText(_translate("MainWindow", "Rank By Month"))
        self.setTime.setText(_translate("MainWindow", "Set Time Frame"))
        self.telda.setText(_translate("MainWindow", "          ~"))

    def clicked(self):

        if self.aTop10.isChecked():
            self.topACount = 10
        if self.aTop100.isChecked():
            self.topACount = 100
        if self.aAll.isChecked():
            self.topAAll = True
        if self.aCustom.text() != '':
            self.topACount = int(self.aCustom.text())

        if self.sTop10.isChecked():
            self.topSCount = 10
        if self.sTop100.isChecked():
            self.topSCount = 100
        if self.sAll.isChecked():
            self.topSAll = True
        if self.sCustom.text() != '':
            self.topSCount = int(self.sCustom.text())
        if self.aTopSongs.isChecked():
            if self.asTop1.isChecked():
                self.topSFromA = 1;
            if self.asTop3.isChecked():
                self.topSFromA = 3;
            if self.asTop5.isChecked():
                self.topSFromA = 5;

        print(self.topACount, self.topSCount, self.topSFromA)

        self.fLabel.setText("Success...Close this window to generate your History")