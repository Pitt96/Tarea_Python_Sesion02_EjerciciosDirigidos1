from functools import total_ordering
import sys
from PyQt6.QtWidgets import QMainWindow,QApplication
from PyQt6 import uic
import Funciones as operaciones
class Ejercicio03(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("Formulario3.ui",self)
        self.initUi()

    def initUi(self):
        self.bnuevo.clicked.connect(self.nuevo)
        self.bsalir.clicked.connect(self.salir)
        self.bcalcular.clicked.connect(self.calcular)

    def nuevo(self):
        self.tcurso.setText("")
        self.tnota1.setText("")
        self.tnota2.setText("")
        self.tnota3.setText("")
        self.tnota4.setText("")
        self.tnota5.setText("")
        self.tnota6.setText("")
        self.lblarea.setText("")
        self.tcurso.setFocus()
    
    def calcular(self):
        curso=self.tcurso.text()
        curso=curso.upper()
        n1=float(self.tnota1.text())
        n2=float(self.tnota2.text())
        n3=float(self.tnota3.text())
        n4=float(self.tnota4.text())
        n5=float(self.tnota5.text())
        n6=float(self.tnota6.text())
        prom=operaciones.promedio(n1,n2,n3,n4,n5,n6)
        mensaje=operaciones.Mostrar(curso,n1,n2,n3,n4,n5,n6,prom)
        self.lblarea.setText(mensaje)
    def salir(self):
        self.close()

if __name__=='__main__':
    app=QApplication(sys.argv)
    ventana_3=Ejercicio03()
    ventana_3.show()
    sys.exit(app.exec())