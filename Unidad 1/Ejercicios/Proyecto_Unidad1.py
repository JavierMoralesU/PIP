import statistics
import sys
import os
from statistics import variance, stdev

#import mean
from PyQt5 import uic, QtWidgets

qtCreatorFile = "Proyecto_Unidad1.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #ingresa los numeros
        self.btn_aceptar.clicked.connect(self.aceptar)
        self.btn_cancelar.clicked.connect(self.cancelar)

        #Lista de numeros
        self.btn_reiniciar.clicked.connect(self.reiniciar)
        self.btn_calcular.clicked.connect(self.calcular)

        #Tendencia central y medidas de dispersion
        self.btn_guardar.clicked.connect(self.guardar)
        self.btn_cargar.clicked.connect(self.cargar)
        self.btn_salir.clicked.connect(self.salir)
        self.numeros = []

        self.ruta_archivo_Numeros= "../../Archivos/numerosAnalisis.csv"
        self.ruta_archivo_Resultados= "../../Archivos/resultadosAnalisis.txt"
        self.guardado = True
    def aceptar(self):
        num_texto=self.txt_numero.text().strip()

        try:
            num=float(num_texto)
            self.numeros.append(num)
            self.txt_numero.clear()
            self.mostrar_numeros()
            self.guardado = False
            self.cambiar_boton_guardar()

        except ValueError:
            QtWidgets.QMessageBox.warning(self, "ERROR", "Ingresa un numero valido")

    #ListaNumeros (CUADRO)
    def mostrar_numeros(self):
            self.txt_listaNumeros.setText(str(self.numeros))


    def cancelar(self):
         self.numeros.pop()
         self.txt_numero.clear()
         self.mostrar_numeros()
         self.guardado = False
         self.msj("correcto", f"Ultimo numero eliminado")


    def reiniciar(self):
        self.numeros=[]
        self.txt_listaNumeros.clear()
        self.txt_media.clear(), self.txt_mediana.clear(), self.txt_moda.clear()
        self.txt_valorMenor.clear(), self.txt_valorMayor.clear(), self.txt_varianza.clear(), self.txt_desviacionEstandar.clear()
        self.guardado = False
        self.msj("Correcto", f"Lista reiniciada...")

    def calcular(self):
        #Tendencia central
        media=statistics.mean(self.numeros) #CALCULA LA MEDIA ARITMETICA
        self.txt_media.setText(str(media))

        mediana=statistics.median(self.numeros) #cacula mediana
        self.txt_mediana.setText(str(mediana))

        moda=statistics.mode(self.numeros) #CALCULA LA MODA
        self.txt_moda.setText(str(moda))

        #Medidas de dispersion
        valorMenor1=min(self.numeros)
        self.txt_valorMenor.setText(str(valorMenor1))

        valorMayor1=max(self.numeros)
        self.txt_valorMayor.setText(str(valorMayor1))

        varianza=variance(self.numeros)
        self.txt_varianza.setText(str(varianza))

        desviacionE=stdev(self.numeros)
        self.txt_desviacionEstandar.setText(str(desviacionE))
        self.msj("Correcto", f"Valores calculados.")

    def guardar(self):
        archivo = open(self.ruta_archivo_Numeros, "w")  # "w"=write (escritura / "a" = append
        for num in self.numeros:
            archivo.write(str(num) + "\n")
        archivo.flush()
        archivo.close()
        self.msj("Correcto", f"Archivo guardado correctamente.")
        self.guardado = True
        self.cambiar_boton_guardar()

        # Guardado de los resultados
        Narchivo = open(self.ruta_archivo_Resultados, "w")
        Narchivo.write("Para la serie de numeros:\n")
        Narchivo.write(f"{self.numeros}\n\n")
        Narchivo.write("Los resultados son los siguientes:\n")
        media   = self.txt_media.toPlainText().strip()
        mediana = self.txt_mediana.toPlainText().strip()
        moda    = self.txt_moda.toPlainText().strip()
        Vmenor = self.txt_valorMenor.toPlainText().strip()
        Vmayor = self.txt_valorMayor.toPlainText().strip()
        varianza = self.txt_varianza.toPlainText().strip()
        desviacion = self.txt_desviacionEstandar.toPlainText().strip()
        Narchivo.write(f"Media = {media}\n")
        Narchivo.write(f"Mediana = {mediana}\n")
        Narchivo.write(f"Moda = {moda}\n")
        Narchivo.write(f"Valor Menor = {Vmenor}\n")
        Narchivo.write(f"Valor Mayor = {Vmayor}\n")
        Narchivo.write(f"Varianza = {varianza}\n")
        Narchivo.write(f"Desviacion Estandar = {desviacion}\n")
        Narchivo.flush()
        Narchivo.close()

    def cargar(self):
        archivo = open(self.ruta_archivo_Numeros)
        contenido = archivo.readlines()  # lee el archivo completo

        nums=[]
        for i in contenido:
            nums.append(float(i))

        print(nums)
        self.numeros=nums
        self.msj("Correcto", f"Archivo cargado.")
        self.calcular()
        self.txt_listaNumeros.setText(str(self.numeros))
        self.guardado = True
        self.cambiar_boton_guardar()


    def salir(self):
        self.close()

    def msj(self, title, txt):
        m = QtWidgets.QMessageBox()
        m.setIcon(QtWidgets.QMessageBox.Information)
        m.setWindowTitle(title)
        m.setText(txt)
        m.exec_()

    def cambiar_boton_guardar(self):
        if self.guardado:
            self.btn_guardar.setStyleSheet(""" background-color: #16A085;  border-radius: 13px;color: rgb(255, 255, 255); """)

        else:
            self.btn_guardar.setStyleSheet(""" background-color: #D10A5A; border-radius: 15px;color: rgb(255, 255, 255);""")



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
