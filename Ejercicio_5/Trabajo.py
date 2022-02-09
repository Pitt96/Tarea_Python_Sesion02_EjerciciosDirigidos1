import sys
from PyQt6.QtWidgets import QMainWindow,QApplication
from PyQt6 import uic
import Funciones as operaciones
class Ejercicio05(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("Formulario5.ui",self)
        self.initUi()

    def initUi(self):
        self.bnuevo.clicked.connect(self.nuevo)
        self.bsalir.clicked.connect(self.salir)
        self.bcalcular.clicked.connect(self.calcular)

    def nuevo(self):
        self.thoras.setText("")
        self.thorasextras.setText("")
        self.tpagohoras.setText("")
        self.lblarea.setText("")
        self.thoras.setFocus()

    def calcular(self):
        horas=int(self.thoras.text())
        horasExtras=int(self.thorasextras.text())
        pagoHoras=float(self.tpagohoras.text())
        sueldoB=operaciones.sueldoBasico(horas,pagoHoras)
        sueldoE=operaciones.sueldoExtra(horasExtras,pagoHoras)
        desc=operaciones.descuento(sueldoB)
        sueldoN=operaciones.sueldoNeto(sueldoB,sueldoE,desc)
        mensaje=operaciones.mostrar(sueldoB,sueldoE,desc,sueldoN)
        self.lblarea.setText(mensaje)
    def salir(self):
        self.close()

if __name__=='__main__':
    app=QApplication(sys.argv)
    ventana_5=Ejercicio05()
    ventana_5.show()
    sys.exit(app.exec())