import sys
from PyQt5 import uic, QtWidgets
# qtCreatorFile = "P00_Introduccion.ui"  # Nombre del archivo aquí.
# Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

import P4_ChecarPuedeVotar as interfaz

class MyApp(QtWidgets.QMainWindow, interfaz.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        interfaz.Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.Bcomprobar.clicked.connect(self.comprobar)


    # Área de los Slots
    def comprobar (self):
        edad = int(self.Tedad.text())
        if edad >= 18:
            self.msj("Puedes votar")
        else:
            self.msj("No puedes votar")

    def msj(self,mensaje):
        m = QtWidgets.QMessageBox()
        m.setText(mensaje)
        m.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

    # cd Archivos,  una vez en el proyecto
    # pyrcc5 Recursos.qrc -o Recursos_rc.py
    # Los archivos generados siempre son nombre_rc.py,  en caso de problema ponerle ese nombre y pasarlo a la misma carpeta el .py
