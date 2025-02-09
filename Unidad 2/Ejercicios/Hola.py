import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "Hola.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Conectar múltiples funciones al mismo botón
        #self.btn_accion.clicked.connect(self.mostrar_mensaje)

        # Conectar btn_accion para copiar texto de txt_1 a txt_2
        self.btn_accion.clicked.connect(self.copiar_texto)

    def mostrar_mensaje(self):
        m = QtWidgets.QMessageBox()
        m.setText("¡Hola, PyQt5!")
        m.exec_()

    def copiar_texto(self):
        texto = self.txt_1.text()  # Obtener texto de txt_1
        self.txt_2.setText(texto)  # Pasarlo a txt_2

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


