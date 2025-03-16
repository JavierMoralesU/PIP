'''

generar aleatoriamente en caja texto, nombre de imaegen, abajo imagen y slider , aceptar , si coincide la imagen y el texto correcto

simular funcionamiento reloj 24 establecer hora manualmente
'''
import random
from winreg import error

import sys
from PyQt5 import uic, QtWidgets, QtGui, QtCore

qtCreatorFile = "PP2.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los Signals

        self.seg = 0
        self.min = 0
        self.hora = 0

        self.Bempezar.clicked.connect(self.iniciarTempo)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.temporizador)

    def iniciarTempo(self):
        if (self.Bempezar.text() == "Empezar"):
            if (self.Tsegundo.text() != "" and self.Tminuto.text() != "" and self.Thora.text() != ""):
                self.seg = int(self.Tsegundo.text())
                self.min = int(self.Tminuto.text())
                self.hora = int(self.Thora.text())
                self.timer.start(1000)  # Tiempo en milisegundos
                self.Bempezar.setText("Detener")
            else:
                self.msj("Error", "Faltaron especificar datos")
                if (self.Tsegundo.text() == "" ) :self.Tsegundo.setText("0")
                if (self.Tminuto.text() == "" ) :self.Tminuto.setText("0")
                if (self.Thora.text() == "" ) :self.Thora.setText("0")
        else:
            self.timer.stop()
            self.Bempezar.setText("Empezar")

    def temporizador(self):

            self.seg += 1
            self.Tsegundo.setText(str(self.seg))
            if self.seg == 60: #Afecta a segundos y minutos
                self.seg = 0
                self.Tsegundo.setText(str(self.seg))
                self.min += 1
                self.Tminuto.setText(str(self.min))
            if self.min == 60: #Afecta a minutos y horas
                self.min = 0
                self.Tminuto.setText(str(self.min))
                self.hora += 1
                self.Thora.setText(str(self.hora))
            if self.hora == 24:
                self.hora = 0
                self.Thora.setText(str(self.hora))

    def msj(self, title, txt):
        m = QtWidgets.QMessageBox()
        m.setIcon(QtWidgets.QMessageBox.Information)
        m.setWindowTitle(title)
        m.setText(txt)
        m.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())