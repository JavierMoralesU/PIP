from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QSlider, QDial, QLabel
from PyQt5.QtCore import Qt


class Ventana(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QSlider y QDial Sincronizados")
        self.setGeometry(100, 100, 400, 200)

        # Crear el layout principal (horizontal)
        layout_principal = QHBoxLayout()

        # Layout vertical para el Slider
        layout_slider = QVBoxLayout()
        self.label_slider = QLabel("Slider: 1")
        self.slider = QSlider(Qt.Vertical)  # Vertical para que se vea bien al lado del dial
        self.slider.setRange(1, 100)
        self.slider.setTickPosition(QSlider.TicksBothSides)
        self.slider.setTickInterval(10)
        self.slider.valueChanged.connect(self.actualizar_valor)

        layout_slider.addWidget(self.label_slider)
        layout_slider.addWidget(self.slider)

        # Layout vertical para el Dial
        layout_dial = QVBoxLayout()
        self.label_dial = QLabel("Dial: 1")
        self.dial = QDial()
        self.dial.setRange(1, 100)
        self.dial.setNotchesVisible(True)
        self.dial.valueChanged.connect(self.actualizar_valor)

        layout_dial.addWidget(self.label_dial)
        layout_dial.addWidget(self.dial)

        # Agregar los dos layouts al principal
        layout_principal.addLayout(layout_slider)  # Izquierda
        layout_principal.addLayout(layout_dial)  # Derecha

        self.setLayout(layout_principal)

    def actualizar_valor(self, valor):
        """Sincroniza los valores del Slider y el Dial."""
        self.slider.setValue(valor)
        self.dial.setValue(valor)
        self.label_slider.setText(f"Slider: {valor}")
        self.label_dial.setText(f"Dial: {valor}")


# Ejecutar aplicación
app = QApplication([])
ventana = Ventana()
ventana.show()
app.exec_()