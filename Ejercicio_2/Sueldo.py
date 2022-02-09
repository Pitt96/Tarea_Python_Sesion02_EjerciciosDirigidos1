from functools import total_ordering
import sys
from PyQt6.QtWidgets import QMainWindow,QApplication
from PyQt6 import uic
import Metodos as operaciones
class Ejercicio02(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("Formulario2.ui",self)
        self.initUi()

    def initUi(self):
        self.bnuevo.clicked.connect(self.nuevo)
        self.bsalir.clicked.connect(self.salir)
        self.bcalcular.clicked.connect(self.calcular)

    def nuevo(self):
        self.tsueldo.setText("")
        self.lbldetalles.setText("")
        self.tsueldo.setFocus()
    
    def calcular(self):
        sueldo=float(self.tsueldo.text())
        au=operaciones.aumento(sueldo)
        boni=operaciones.bonificacion(au)
        total=operaciones.SueldoTotal(au,boni)
        self.lbldetalles.setText(operaciones.Mostrar(au,boni,total))

    def salir(self):
        self.close()

if __name__=='__main__':
    app=QApplication(sys.argv)
    ventana_2=Ejercicio02()
    ventana_2.show()
    sys.exit(app.exec())