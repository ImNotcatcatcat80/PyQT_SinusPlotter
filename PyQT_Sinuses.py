import sys
from PyQt4 import QtCore, QtGui
import traceback
import numpy as np
import matplotlib.pyplot as ppl
from scipy import integrate
import threading
'''
from PyQt4 import uic
uiFile = "PyQT_sinuses.ui"  # ui file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(uiFile)
'''
from UIsinuses import Ui_MainWindow
from UIdialogSin import Ui_MainWindowDialog
from UIinfoSin import Ui_DialogInfo


wtH2 = 0
wtH3 = 0
wtH4 = 0
wtH5 = 0
wtH6 = 0
wtH7 = 0
wtH8 = 0
wtH9 = 0
style_selected = None
plot_black = True
offset_pi = 0
dialogWindowList = []  # Creates a reference to dialog window instances to avoid garbage collection
strayItems = []


class QTSinDialog(QtGui.QMainWindow, Ui_MainWindowDialog):
    def __init__(self, parent="default"):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.pushButtonInDialog.clicked.connect(self.button_clicked)
        self.labelThisW.setText("This won't update progressBarDummy.")
        if parent != "default":
            self.setWindowTitle(parent)
        
    def button_clicked(self):
        if self.pushButtonInDialog.text() == "H":
            self.pushButtonInDialog.setText("Q")
        else:
            self.pushButtonInDialog.setText("H")
        clicks = self.lcdNumberClicks.value()
        clicks += 1
        self.lcdNumberClicks.display(clicks)

        
class QTSinDialogMod(QTSinDialog):
    def __init__(self, parent_title, parent_window):
        super(QTSinDialogMod, self).__init__(parent_title)
        self.parent_window = parent_window
        self.labelThisW.setText("This will update progressBarDummy!")
        self.lcdNumberClicks.display(100)
        
    def button_clicked(self, dont_update_progress):
        super(QTSinDialogMod, self).button_clicked()
        # windowMain.update_progress_bar()  # static reference
        if not dont_update_progress:       
            self.parent_window.update_progress_bar()  # dynamic reference

class QTSinDialogInfo(QtGui.QDialog, Ui_DialogInfo):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        Ui_DialogInfo.__init__(self)
        self.setupUi(self)
        self.labelInfoTitle.setToolTip("Pota!")

class PyQTSin(QtGui.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.pushButtonPlot.clicked.connect(self.on_plot_button)
        self.dialogWindow = None
        self.infoWindow = None
        self.floatingLabel = None
        self.timerProgBar = QtCore.QBasicTimer()
        self.progBarStep = 0
        self.actionNew_window.triggered.connect(self.open_dialog)
        self.actionInfo.triggered.connect(self.open_info)
        self.actionClose.triggered.connect(self.close_window)
        '''        
        item0 = QtGui.QListWidgetItem("r-")
        item1 = QtGui.QListWidgetItem("b-")
        item2 = QtGui.QListWidgetItem("g-")
        item3 = QtGui.QListWidgetItem("r--")
        item4 = QtGui.QListWidgetItem("b--")
        item5 = QtGui.QListWidgetItem("g--")
        self.listWidgetStyles.addItem(item0)
        self.listWidgetStyles.addItem(item1)
        self.listWidgetStyles.addItem(item2)
        self.listWidgetStyles.addItem(item3)
        self.listWidgetStyles.addItem(item4)
        self.listWidgetStyles.addItem(item5)
        self.listWidgetStyles.setCurrentItem(item0)
        '''
        item_styles = ["r-", "b-", "g-", "r--", "b--", "g--"]
        for s in item_styles:
            item = QtGui.QListWidgetItem("%s" % s)
            self.listWidgetStyles.addItem(item)
        self.listWidgetStyles.itemClicked.connect(self.display_item_styles)
        self.listWidgetStyles.setCurrentRow(0)
        # self.checkBoxA = QtGui.QCheckBox()
        self.checkBoxA.toggled.connect(self.print_a)
        self.comboBoxAngCos.insertItem(0, "Phi")
        self.comboBoxAngCos.insertItem(1, "Cos(Phi)")
        self.comboBoxAngCos.currentIndexChanged.connect(self.on_knob_changed)
        self.labelTopText.setText("Angle")
        self.labelMidText.setText("0°")
        self.Knob0.valueChanged.connect(self.on_knob_changed)
        self.Knob0.setScale(0, 360, 60)
        self.Knob0.setRange(0, 360, 1)
        self.comboBoxCenter.insertItem(0, "Voltage")
        self.comboBoxCenter.insertItem(1, "Current")
        self.comboBoxCenter.insertItem(2, "...")
        self.comboBoxCenter.currentIndexChanged.connect(self.update_combobox_center)
        self.toolButton0.clicked.connect(self.on_tool_button0)
        self.toolButton1.clicked.connect(self.on_tool_button1)
        self.progressBarDummy.setValue(0)
        # self.infoWindow = QTSinDialogInfo()

    def on_plot_button(self):
        global wtH2, wtH3, wtH4, wtH5, wtH6, wtH7, wtH8, wtH9, style_selected, offset_pi, plot_black
        if self.checkBoxA.isChecked():
            plot_black = True
        else:
            plot_black = False
        offset_pi = self.Knob0.value() / 180 * np.pi
        wtH2 = float(self.doubleSpinBoxHarm2.value()) / 100
        wtH3 = float(self.doubleSpinBoxHarm3.value()) / 100
        wtH4 = float(self.doubleSpinBoxHarm4.value()) / 100
        wtH5 = float(self.doubleSpinBoxHarm5.value()) / 100
        wtH6 = float(self.doubleSpinBoxHarm6.value()) / 100
        wtH7 = float(self.doubleSpinBoxHarm7.value()) / 100
        wtH8 = float(self.doubleSpinBoxHarm8.value()) / 100
        wtH9 = float(self.doubleSpinBoxHarm9.value()) / 100
        style_selected = self.listWidgetStyles.currentItem().text()
        print(str(style_selected))
        pth = plot_thread("@ 50Hz")
        pth.run()
        
    def open_dialog(self):  # Creates a unique instance of dialogWindow
        self.dialogWindow = QTSinDialog()
        self.dialogWindow.show()
        
    def open_info(self):
        self.infoWindow = QTSinDialogInfo()
        self.infoWindow.show()

    def print_a(self):
        if self.checkBoxA.isChecked():
            print("a")
        else:
            print("NOT a")
        
    def on_knob_changed(self):
        if self.comboBoxAngCos.currentIndex() == 0:
            self.labelTopText.setText("Angle")
            self.labelMidText.setText(str(self.Knob0.value()) + "°")
        else:
            self.labelTopText.setText("Cos(Phi)")
            self.labelMidText.setText(str(round(np.cos((self.Knob0.value()/180*np.pi)), 2)))
    
    def update_combobox_center(self):
        if self.comboBoxCenter.currentIndex() == 2:
            self.comboBoxCenter.setEditable(True)
        else:
            self.comboBoxCenter.setEditable(False)
            
    def on_tool_button0(self):  # Creates multiple instances of dialogWindow
        global dialogWindowList
        wNumber = len(dialogWindowList)
        dialogWindowMultiple = QTSinDialogMod("From toolButton - Window # " + str(wNumber), self)
        dialogWindowMultiple.show()
        dialogWindowList.append(dialogWindowMultiple)
        
    def on_tool_button1(self):
        global dialogWindowList
        for ow in dialogWindowList:
            ow.button_clicked(True)
        
    def display_item_styles(self):
        self.floatingLabel = QtGui.QLabel()
        self.floatingLabel.setText(str(self.listWidgetStyles.currentItem()))
        floatingLabelFont = QtGui.QFont("Fixedsys", 12, QtGui.QFont.Normal)
        self.floatingLabel.setFont(floatingLabelFont)
        self.floatingLabel.show()
        
    def timerEvent(self, event):
        if self.progBarStep >= 100:
            self.timerProgBar.stop()
            return
        else:
            self.progBarStep += 1
            self.progressBarDummy.setValue(self.progBarStep)
        
    def update_progress_bar(self):
        if(self.progressBarDummy.value() < 100):
            if not self.timerProgBar.isActive():
                self.timerProgBar.start(1000, self)
            else:
                self.timerProgBar.stop()
            
    def close_window(self):
        self.close()


def plot_pwn(val):
    global style_selected
    xlistAxisX = []
    ylistAxisX = []
    xlistA = []
    ylistA = []
    xlistB = []
    ylistB = []
    xlistC = []
    ylistC = []
    for n in range(-10000, 10000):
        n2 = n + 10000
        xlistAxisX.append(n/1000)
        ylistAxisX.append(0)
        xlistA.append(n/1000)
        ylistA.append(np.sin(n/1000) + wtH2*np.sin(2*n/1000) + wtH3*np.sin(3*n/1000) + wtH4*np.sin(4*n/1000) + wtH5*np.sin(5*n/1000) + wtH6*np.sin(6*n/1000) + wtH7*np.sin(7*n/1000) + wtH8*np.sin(8*n/1000) + wtH9*np.sin(9*n/1000))
        xlistB.append(n/1000)
        ylistB.append(np.sin(offset_pi + n / 1000))
        xlistC.append(n/1000)
        ylistC.append((np.sin(n/1000) + wtH2*np.sin(2*n/1000) + wtH3*np.sin(3*n/1000) + wtH4*np.sin(4*n/1000) + wtH5*np.sin(5*n/1000) + wtH6*np.sin(6*n/1000) + wtH7*np.sin(7*n/1000) + wtH8*np.sin(8*n/1000) + wtH9*np.sin(9*n/1000)) - (np.sin(offset_pi + n / 1000)))

    print(str(val))

    ppl.clf()
    ppl.plot(xlistAxisX, ylistAxisX, "k-", linewidth = 1)
    ppl.plot(xlistA, ylistA, style_selected, linewidth=3, label="ph A")
    if windowMain.checkBoxA.isChecked():
        ppl.plot(xlistB, ylistB, "k:", linewidth=3, label="ph B")
    if windowMain.checkBoxB.isChecked():
        ppl.plot(xlistC, ylistC, "y--", linewidth=3, label="ph C")
    ppl.plot(0, 0, "k+", markersize=24)

    ppl.axis([-3 * np.pi, 3 * np.pi, -2, 2])
    if windowMain.comboBoxCenter.currentIndex() == 0:
        ppl.ylabel("Voltage (U)")
    elif windowMain.comboBoxCenter.currentIndex() == 1:
        ppl.ylabel("Current (I)")
    else:
        ppl.ylabel(windowMain.comboBoxCenter.currentText())
    ppl.xlabel("Time (t)")
    ppl.show()


class plot_thread(threading.Thread):
    def __init__(self, pgraph):
        super(plot_thread, self).__init__()
        self.pgraph = pgraph

    def run(self):
        plot_pwn(self.pgraph)


if __name__ == "__main__":
    try:
        app = QtGui.QApplication(sys.argv)
        windowMain = PyQTSin()
        windowMain.show()
        sys.exit(app.exec_())
    except:
        traceback.print_exc()
