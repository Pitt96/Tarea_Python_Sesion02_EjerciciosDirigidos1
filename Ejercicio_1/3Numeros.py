import sys
from PyQt6.QtWidgets import QMainWindow,QApplication
from PyQt6 import uic
import Metodos as operaciones
class Ejercicio01(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("Ejercicio_1.ui",self)
        self.initUi()

    def initUi(self):
        self.bnuevo.clicked.connect(self.nuevo)
        self.bsalir.clicked.connect(self.salir)
        self.bpotencia.clicked.connect(self.potencia)
        self.bsumar.clicked.connect(self.suma)

    def nuevo(self):
        self.tnumero1.setText("")
        self.tnumero2.setText("")
        self.tnumero3.setText("")
        self.lblnum1.setText("")
        self.lblnum2.setText("")
        self.lblnum3.setText("")
        self.lblc1.setText("")
        self.lblc2.setText("")
        self.lblc3.setText("")
        self.lblsuma.setText("")
        self.tnumero1.setFocus()

    def potencia(self):
        numero1=int(self.tnumero1.text())
        self.lblnum1.setText(str(numero1))
        numero2=int(self.tnumero2.text())
        self.lblnum2.setText(str(numero2))
        numero3=int(self.tnumero3.text())
        self.lblnum3.setText(str(numero3))
        pot1=operaciones.Cpotencia(numero1)
        pot2=operaciones.Cpotencia(numero2)
        pot3=operaciones.Cpotencia(numero3)
        self.lblc1.setText(str(pot1))
        self.lblc2.setText(str(pot2))
        self.lblc3.setText(str(pot3))
    def suma(self):
        numero1=int(self.tnumero1.text())
        numero2=int(self.tnumero2.text())
        numero3=int(self.tnumero3.text())
        s=operaciones.Csuma(numero1,numero2,numero3)
        self.lblsuma.setText(str(s))
    
    def salir(self):
        self.close()

if __name__=='__main__':
    app=QApplication(sys.argv)
    ventana_1=Ejercicio01()
    ventana_1.show()
    sys.exit(app.exec())