import sys
from PyQt5 import uic, QtWidgets, QtGui,QtCore
qtCreatorFile = "P15_RadioButton.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.rb_batman.clicked.connect(self.personaje)
        self.rb_john.clicked.connect(self.personaje)
        self.rb_iron.clicked.connect(self.personaje)

        self.rb_azul.toggled.connect(self.color)
        self.rb_rojo.toggled.connect(self.color)
        self.rb_verde.toggled.connect(self.color)

    def personaje(self):
        obj = self.sender()
        valor = obj.isChecked()
        if valor:
         print("Personaje - Obj: ", obj.text() , ":", valor)
    def color(self):
        obj = self.sender()
        valor = obj.isChecked()
        if valor:
            print("Color-Obj: ", obj.text(), ":", valor)








if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())