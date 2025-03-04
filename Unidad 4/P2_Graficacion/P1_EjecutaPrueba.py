import sys
from PyQt5 import uic, QtWidgets
# qtCreatorFile = "P0.ui"  # Nombre del archivo aquí.
# Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
#pyuic5 -x archivo.ui -o archivo.py

import Plantilla_Grafica as interfaz
import matplotlib.pyplot as plt

class MyApp(QtWidgets.QMainWindow, interfaz.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        interfaz.Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los Signals
        self.Bgraficar.clicked.connect(self.graficar)

        #VALORES POR DEFECTO
        self.configuracion = {
            "estilo": ":",
            "color_linea": "black",
            "ancho_linea":1
        }
        self.limite = {
            "x": [1,10,10], #min, max, divisiones
            "y": [1, 10,10], #min, max, divisiones
        }



    # Área de los Slots
    def graficar (self):
        polinomio = self.Tpolinomio.text()
        polinomio = polinomio.replace("^","**")


        X = [i for i in range(self.limite["x"][0], self.limite["x"][1] )]#Lista de comprension{on
        print("Valores de X: ")
        print(X)
        #y = polinomio.replace("x","*(" + str(x) + ")") #2*(X[0]** 2 + 3 * (X[0]) +4
        # 3x^2
        y = [eval(polinomio.replace("x","*(" + str(x) + ")")) for x in X]
        #y = [eval(polinomio.replace("x", str(x))) for x in X]

        print("Valores de Y: ")
        print(y)


        self.sx.plot(X,y,
                     linestyle = self.configuracion["estilo"], #: - -- -.
                     color = self.configuracion["color_linea"], #color de la linea
                     linewidth = self.configuracion["ancho_linea"], #Tamaño de la linea
                     marker=".", # o . * x 1
                     markersize = 4,
                     markerfacecolor = "yellow", # color interno del marcador
                     markeredgewidth = 1, #tamaño del borde del marcador
                     markeredgecolor = "blue", #color del borde del marcador
                     dash_capstyle = "butt",  # dash or solid: "butt" "round" "projecting"
                     dash_joinstyle = "miter" # dash or solid: "miter" "round" "bevel"
                     )


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

    # cd Archivos,  una vez en el proyecto
    # pyrcc5 Recursos.qrc -o Recursos_rc.py
    # Los archivos generados siempre son nombre_rc.py,  en caso de problema ponerle ese nombre y pasarlo a la misma carpeta el .py
