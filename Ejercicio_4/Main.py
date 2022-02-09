#se importa el modulo sys
import sys

from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import uic

import ModuloD as operacionD

class cuotas_ejercicio4(QMainWindow):
    #Constructor de la clase
    #self ---> Hace referencia a la clase: Ejemplo01
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("interfazEjecicio4.ui", self)

        #Inicializar los objetos
        self.initUi()

    def initUi(self):
        self.bnuevo.clicked.connect(self.nuevo)
        self.bcalcular.clicked.connect(self.calcular)
        self.bsalir.clicked.connect(self.salir)


    def nuevo(self):
        self.t_precio.setText("")
        self.t_cantidad.setText("")
        self.t_interes.setText("")
        self.lbl_pagocuotas.setText("")
        self.lbl_pagoneto.setText("")
        self.lbl_diferencia.setText("")

        self.t_precio.setFocus()

    def calcular(self):
        valor_precio_producto=float(self.t_precio.text())
        valor_cantidad_cuotas=float(self.t_cantidad.text())
        valor_interes=float(self.t_interes.text())
        self.lbl_pagocuotas.setText(str(operacionD.PagoPorCuotas(valor_precio_producto,valor_cantidad_cuotas,valor_interes)))



        valor_cuotas=float(self.lbl_pagocuotas.text())
        self.lbl_pagoneto.setText(str(operacionD.PagoNeto(valor_cuotas,valor_cantidad_cuotas)))

        valor_neto=float(self.lbl_pagoneto.text())
        self.lbl_diferencia.setText(str(operacionD.Diferencia(valor_neto,valor_precio_producto)))


        

    def salir(self):
        self.close()


if __name__=="__main__":
    #Se crea una instacia para iniciar la aplicacion
    app=QApplication(sys.argv)

    #Se crea ventana01 de tipo clase: Ejemplo01
    ventana01=cuotas_ejercicio4()
    #Se muestra el ejemplo formulario
    ventana01.show()
    sys.exit(app.exec())

