import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile = "P08_CarruselImagenes.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los Signals
        self.selectorImagen.valueChanged.connect(self.cambiaValor)
        self.selectorImagen.setMinimum(0)
        self.selectorImagen.setMaximum(2)
        self.selectorImagen.setSingleStep(1)
        self.selectorImagen.setValue(0)

        self.datosImagenes={
        0: [":/Logos/UAT.png", "imagen 1"],
        1: [":/Logos/Castor.jpg", "imagen 2"],
        2: [":/Logos/facultad_ingenieria_tampico.png", "imagen 3"],
        }

    # Área de los Slots
    def cambiaValor(self):
        valor=self.selectorImagen.value()
        imagen_ruta=self.datosImagenes[valor][0]
        self.imagen.setPixMap(QtGui.QPixmap(imagen_ruta))
        print(valor)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())