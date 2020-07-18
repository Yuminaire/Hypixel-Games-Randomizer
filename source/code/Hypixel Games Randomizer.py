# This Python file uses the following encoding: utf-8
import sys
import os
import random

from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QCheckBox, QPushButton, QComboBox, QDialog, QDialogButtonBox, QLabel, QAbstractButton
from PySide2.QtCore import QFile, Qt, QTimer
from PySide2.QtUiTools import QUiLoader
from PySide2.QtGui import QIcon, QFont


class Dialog(QDialog):
    def __init__(self, game, parent):
        super(Dialog, self).__init__(parent)
        self.Parent = parent
        self.setWindowTitle('Hypixel Games Randomizer')
        self.setWindowIcon(QIcon(self.Parent.windowIcon()))
        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignHCenter)
        font = QFont()
        font.setPointSize(14)
        font.setFamily('Roboto Th')
        self.label.setFont(font)
        self.label.setText('The wheel of games has chosen and\ndecided that you will now play')
        self.game = QLabel(self)
        self.game.setText(game)
        self.game.setAlignment(Qt.AlignHCenter)
        font.setPointSize(16)
        font.setFamily('Roboto Th')
        font.setBold(True)
        self.game.setFont(font)
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.addWidget(self.label)
        self.verticalLayout.addWidget(self.game)
        self.verticalLayout.addWidget(self.buttonBox)
        self.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.close)


class ErrorDialog(QDialog):
    def __init__(self, parent):
        super(ErrorDialog, self).__init__(parent)
        self.Parent = parent
        self.setWindowTitle('Hypixel Games Randomizer')
        self.setWindowIcon(QIcon(self.Parent.windowIcon()))
        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Retry)
        self.buttonBox.setCenterButtons(True)
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignHCenter)
        font = QFont()
        font.setPointSize(14)
        font.setFamily('Roboto Th')
        self.label.setFont(font)
        self.label.setText('You must choose at least one game\nto be able randomize.')
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.addWidget(self.label)
        self.verticalLayout.addWidget(self.buttonBox)
        self.buttonBox.button(QDialogButtonBox.Retry).clicked.connect(self.close)

class Main(QWidget):
    def __init__(self):
        super(Main, self).__init__()
        self.load_ui()

    def load_ui(self):
        loader = QUiLoader()
        path = os.path.join(os.path.dirname(__file__), 'window.ui')
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        ui_file.close()
        self.setFixedSize(660, 510)
        self.setWindowTitle('Hypixel Games Randomizer')
        self.setWindowIcon(QIcon('icon.jpg'))

        self.soloBW = self.findChild(QCheckBox, 'soloBW')
        self.teamBW = self.findChild(QCheckBox, 'teamBW')
        self.threesBW = self.findChild(QCheckBox, 'threesBW')
        self.foursBW = self.findChild(QCheckBox, 'foursBW')
        self.soloSW = self.findChild(QCheckBox, 'soloSW')
        self.teamSW = self.findChild(QCheckBox, 'teamSW')
        self.sololabSW = self.findChild(QCheckBox, 'labsoloSW')
        self.teamlabSW = self.findChild(QCheckBox, 'labteamSW')
        self.tntrun = self.findChild(QCheckBox, 'tntrun')
        self.pvprun = self.findChild(QCheckBox, 'pvprun')
        self.tnttag = self.findChild(QCheckBox, 'tnttag')
        self.bowspleef = self.findChild(QCheckBox, 'bowspleef')
        self.hypixelsays = self.findChild(QCheckBox, 'hypixelsays')
        self.miniwalls = self.findChild(QCheckBox, 'miniwalls')
        self.partygames = self.findChild(QCheckBox, 'partygames')
        self.solospeedUHC = self.findChild(QCheckBox, 'solospeedUHC')
        self.soloBB = self.findChild(QCheckBox, 'soloBB')
        self.teamBB = self.findChild(QCheckBox, 'teamBB')
        self.gtb = self.findChild(QCheckBox, 'gtb')
        self.classicMM = self.findChild(QCheckBox, 'classicMM')
        self.doubleMM = self.findChild(QCheckBox, 'doubleMM')
        self.infection = self.findChild(QCheckBox, 'infection')
        self.bridge2x4 = self.findChild(QCheckBox, 'bridge2x4')
        self.bridge4x3 = self.findChild(QCheckBox, 'bridge4x3')
        self.uhcdm = self.findChild(QCheckBox, 'uhcdm')

        self.nbPlayers = self.findChild(QComboBox, 'nbPlayers')
        self.randomizeButton = self.findChild(QPushButton, 'randomizeButton')
        self.randomizeButton.clicked.connect(self.randomize)
        self.nbPlayers.currentIndexChanged.connect(self.getPlayers)


    def getPlayers(self):
        modes = (self.soloBW, self.teamBW, self.threesBW, self.foursBW, self.soloSW, self.teamSW, self.sololabSW, self.teamlabSW, self.tntrun, self.pvprun, self.tnttag, self.bowspleef,
                self.hypixelsays, self.miniwalls, self.partygames, self.solospeedUHC, self.soloBB, self.teamBB, self.gtb, self.classicMM, self.doubleMM, self.infection, self.bridge2x4,
                self.bridge4x3, self.uhcdm)
        modes8p = (self.soloBW, self.teamBW, self.threesBW, self.foursBW, self.soloSW, self.sololabSW, self.teamSW, self.teamlabSW, self.tntrun, self.pvprun, self.tnttag, self.bowspleef,
                  self.hypixelsays, self.partygames, self.miniwalls, self.solospeedUHC, self.soloBB, self.teamBB, self.gtb, self.classicMM, self.doubleMM, self.infection, self.bridge2x4,
                  self.bridge4x3, self.uhcdm)
        modes10p = (self.teamBW, self.threesBW, self.foursBW, self.soloSW, self.sololabSW, self.teamSW, self.teamlabSW, self.tntrun, self.pvprun, self.tnttag, self.bowspleef, self.hypixelsays,
                   self.miniwalls, self.solospeedUHC, self.soloBB, self.teamBB, self.gtb, self.classicMM, self.doubleMM, self.infection, self.bridge4x3)
        modes12p = (self.teamBW, self.threesBW, self.foursBW, self.soloSW, self.sololabSW, self.teamSW, self.teamlabSW, self.tntrun, self.pvprun, self.tnttag, self.bowspleef,  self.solospeedUHC,
                   self.miniwalls, self.soloBB, self.teamBB, self.classicMM, self.doubleMM, self.infection, self.bridge4x3)
        modes16p = (self.teamBW, self.foursBW, self.teamSW, self.teamlabSW, self.tntrun, self.pvprun, self.tnttag, self.bowspleef, self.miniwalls, self.soloBB, self.teamBB, self.classicMM,
                   self.doubleMM, self.infection)
        modes24p = (self.teamSW, self.teamlabSW, self.tntrun, self.pvprun, self.tnttag, self.bowspleef, self.teamBB, self.doubleMM)
        modes30p = (self.tnttag, self.teamBB)
        modes32p = (self.teamBB)
        playerToModeDict = {0: modes8p, 1: modes10p, 2: modes12p, 3: modes16p, 4: modes24p, 5: modes30p, 6: modes32p}
        for i in range(len(playerToModeDict)):
            if self.nbPlayers.currentIndex() == list(playerToModeDict.keys())[i]:
                okModes = list(playerToModeDict.values())[i]
        for i in modes:
            if okModes == (self.teamBB):
                for i in modes:
                    i.setEnabled(False)
                    i.setChecked(False)
                self.teamBB.setEnabled(True)
            elif i not in okModes:
                i.setEnabled(False)
                i.setChecked(False)
            else:
                i.setEnabled(True)


    def randomize(self):
        modes = (self.soloBW, self.teamBW, self.threesBW, self.foursBW, self.soloSW, self.teamSW, self.sololabSW, self.teamlabSW, self.tntrun, self.pvprun, self.tnttag, self.bowspleef,
                self.hypixelsays, self.miniwalls, self.partygames, self.solospeedUHC, self.soloBB, self.teamBB, self.gtb, self.classicMM, self.doubleMM, self.infection, self.bridge2x4,
                self.bridge4x3, self.uhcdm)
        checkedModes =[]
        for i in modes:
            if i.isChecked():
                checkedModes.append(i.text())
        if checkedModes == []:
            self.dialog = ErrorDialog(Main())
            self.dialog.exec_()
        else:
            index = random.randint(0, len(checkedModes)-1)
            self.dialog = Dialog(checkedModes[index], Main())
            self.dialog.exec_()

if __name__ == "__main__":
    app = QApplication([])
    widget = Main()
    widget.show()
    sys.exit(app.exec_())
