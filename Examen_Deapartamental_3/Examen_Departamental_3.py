import random

import sys
from PyQt5 import uic, QtWidgets, QtCore
import Recursos_rc
import serial as placa

qtCreatorFile = "Examen_Departamental_3.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        puertos_comunes = ["COM3", "COM4", "COM5", "COM6", "COM7", "COM8"]
        self.CBpuertos.addItems(puertos_comunes)
        # Área de los Signals
        self.arduino = None
        self.segundoPlano = QtCore.QTimer()

        self.prueba_verdadera = True  #Para saber si se estara usando el arduino real o no
        # self.Bconectar.clicked.connect(self.conectar)
        # self.segundoPlano.timeout.connect(self.lecturas)
        self.Bconectar.clicked.connect(self.conectar_fake)
        self.segundoPlano.timeout.connect(self.lecturas_fake)

        self.BmostrarLecturas.clicked.connect(self.ActualizarLista)
        self.Babrir.clicked.connect(self.AbrirBarrera)


    # Área de los Slots
    def conectar(self):
        try:
            texto = self.Bconectar.text()
            if texto == "CONECTAR": #Inicia la comunicacion y la apertura
                com = self.CBpuertos.currentText()
                self.arduino = placa.Serial(com,baudrate=9600,timeout=1)
                self.segundoPlano.start(100)
                self.Bconectar.setText("DESCONECTAR")
            elif texto == "DESCONECTAR": #cierra la comunicacion
                self.Bconectar.setText("RECONECTAR")
                self.segundoPlano.stop()
                self.arduino.close()
            else: #Reapertura comunicacion
                self.Bconectar.setText("DESCONECTAR")
                self.arduino.open()
                self.segundoPlano.start(100)
        except Exception as error:
            print(error)

    def lecturas(self):
        if self.arduino.isOpen():
            if self.arduino.inWaiting():
                try:
                    self.lectura = self.arduino.readline().decode().strip()
                except UnicodeDecodeError: return

                if self.lectura != "":
                    print(self.lectura)  # marca error sin el
                    ######
                    # PROCESAMIENTO DE LOS DATOS
                    self.lectura = self.lectura.split("@")
                    self.lectura = self.lectura[:-1]
                    print(self.lectura)  # marca error sin el
                    self.lectura = [int(i) for i in self.lectura if i.strip().isdigit()] #esto devuelve una lista de int
                    #####
                    if self.BmostrarLecturas.text() == "APAGAR":
                        valor = self.lectura[0]
                        self.deteccion_de_vehiculo(valor)
                        self.lista_datos.addItem(str(valor))
                        self.lista_datos.setCurrentRow(self.lista_datos.count() - 1)

        else:
            print("Arduino no conectado")

    def ActualizarLista(self):
        boton = self.BmostrarLecturas
        texto = boton.text()
        if texto == "PRENDER":
            boton.setText("APAGAR")
        else:
            boton.setText("PRENDER")

    def AbrirBarrera(self):
        try:
            if (self.Bconectar.text() != "DESCONECTAR" and self.prueba_verdadera == True): return
            boton = self.sender()  # Detectamos qué botón se presionó
            boton.setEnabled(False)
            if boton.text() == "¿ABRIR?":
                valor = 180
                boton.setText("¿CERRAR?")
                boton.setStyleSheet("""
                    border: 2px solid black;
                    border-radius: 5px;
                    padding: 5px;
                    background-color: rgb(255, 203, 204);
                """)
                self.Lbarrera.setText("La barrera esta abierta ¿Desea cerrarla?")
                self.aumentarContador()
            else:
                valor = 90
                boton.setText("¿ABRIR?")
                boton.setStyleSheet("""
                                    border: 2px solid black;
                                    border-radius: 5px;
                                    padding: 5px;
                                    background-color: rgb(174, 255, 195);
                                """)
                self.Lbarrera.setText("La barrera esta cerrada ¿Desea abrirla?")
                self.ActualizarLista()
            #Mandar comando a arduino
            print("Comando a enviar:", valor)
            if (self.prueba_verdadera == True):
                comando = f"@{valor}\n"
                self.arduino.write(comando.encode())
                self.arduino.flush()
            #Desactiva el boton por 2 segundos
            QtCore.QTimer.singleShot(1000, lambda: self.reactivar_boton(boton))  # 2000 ms = 2 segundos
        except Exception as e:
            print("Error al activar el actuador:", e)

    def aumentarContador(self):
        try:
            texto = self.Lcontador.text()
            Numero = int(texto)
            Numero += 1
            self.Lcontador.setText(str(Numero))
        except Exception as e:
            print(f"Error inesperado en aumentarContador: {e}")

    def deteccion_de_vehiculo(self, valor):
        if valor <= 20:
           self.Lvehiculo.setText("SI")
           self.Lvehiculo.setStyleSheet("color: green;")
           self.ActualizarLista()
        else:
           self.Lvehiculo.setText("NO")
           self.Lvehiculo.setStyleSheet("color: red;")

    def reactivar_boton(self, boton):
        boton.setEnabled(True)

    #Metodos de prueba con datos simulados:
    def conectar_fake(self):
        self.prueba_verdadera = False
        texto = self.Bconectar.text()
        if texto == "CONECTAR":
            self.segundoPlano.start(100)
            self.Bconectar.setText("DESCONECTAR")
        elif texto == "DESCONECTAR":
            self.segundoPlano.stop()
            self.Bconectar.setText("RECONECTAR")
        else:
            self.segundoPlano.start(100)
            self.Bconectar.setText("DESCONECTAR")
    def lecturas_fake(self):
        valor_simulado = random.randint(0, 400)
        print(f"{valor_simulado}@")
        self.lectura = [valor_simulado]

        if self.BmostrarLecturas.text() == "APAGAR":
            self.deteccion_de_vehiculo(valor_simulado)
            self.lista_datos.addItem(str(valor_simulado))
            self.lista_datos.setCurrentRow(self.lista_datos.count() - 1)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())