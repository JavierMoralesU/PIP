import sys
from PyQt5 import uic, QtWidgets, QtCore
import serial as placa


qtCreatorFile = "Practica4_ArduinoPythonGUI.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los Signals
        # poner 3 en el cuadro


        self.arduino = None
        self.btn_accion.clicked.connect(self.conectar)

        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.lecturas)

        self.btn_control.clicked.connect(self.control)
        self.btn_control2.clicked.connect(self.control)
        self.btn_control3.clicked.connect(self.control)



    # Área de los Slots
    def control(self):
     boton = self.sender()
     if self.arduino.isOpen(): #    if self.arduino and self.arduino.isOpen():
        texto = boton.text()
        if texto == "PRENDER":
            boton.setText("APAGAR")
            self.arduino.write("1".encode())
        else:
            boton.setText("PRENDER")
            self.arduino.write("0".encode())

    def lecturas(self):
        if  self.arduino.isOpen():
            if self.arduino.inWaiting():
                lectura = self.arduino.readline().decode().strip()
                if lectura !="":
                  print(lectura) #marca error sin el
                  ######
                  #PROCESAMIENTO DE LOS DATOS
                  lectura = lectura.split("@")
                  lectura = lectura[:-1]
                  print(lectura) #marca error sin el
                  lectura = [int(i) for i in lectura if i.strip().isdigit()]
                  #####
                  if self.btn_control.text() == "APAGAR":
                   self.lista_datos.addItem(str(lectura[0]))
                   self.lista_datos.setCurrentRow(self.lista_datos.count() - 1)
                  if self.btn_control2.text() == "APAGAR":
                   self.lista_datos2.addItem(str(lectura[1]))
                   self.lista_datos2.setCurrentRow(self.lista_datos2.count() - 1)
                  if self.btn_control3.text() == "APAGAR":
                   self.lista_datos3.addItem(str(lectura[2]))
                   self.lista_datos3.setCurrentRow(self.lista_datos3.count() - 1)



    def conectar(self):
        try:
            texto = self.btn_accion.text()
            if texto == "CONECTAR": #Inicia la comunicacion y la apertura
                com = "COM" + self.txt_com.text() #quitar el 3
                self.btn_accion.setText("DESCONECTAR")
                self.txt_estado.setText("CONECTADO")
                self.arduino = placa.Serial(com,baudrate=9600,timeout=1)
                self.segundoPlano.start(100)

            elif texto == "DESCONECTAR": #cierra la comunicacion
                self.btn_accion.setText("RECONECTAR")
                self.txt_estado.setText("DESCONECTADO")
                self.segundoPlano.stop()
                self.arduino.close()

            else: #Reapertura comunicacion
                self.btn_accion.setText("DESCONECTAR")
                self.txt_estado.setText("RECONECTADO")
                self.arduino.open()
                self.segundoPlano.start(100)
        except Exception as error:
            print(error)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

    # cd Archivos,  una vez en el proyecto
    # pyrcc5 Recursos.qrc -o Recursos_rc.py
    # Los archivos generados siempre son nombre_rc.py,  en caso de problema ponerle ese nombre y pasarlo a la misma carpeta el .py
