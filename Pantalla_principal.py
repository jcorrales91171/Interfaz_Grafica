import sys
import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QWidget

class VentanaVacia(QWidget):
    def __init__(self):
        super().__init__()      #se define la inicializacion del Qwidget para la ventana
        self.inicializarUI()

    def inicializarUI(self):
        self.setGeometry(100,100,250,250) #
        self.setWindowTitle("Panel solar Fotovoltaica Movil (2023)")
        self.show()

if __name__ =='__main__':
    app = QApplication(sys.argv)        #se encarga de administrar las interacciones que haga el usuario ocn la ventana 
    ventana = VentanaVacia()            #Estancia de la clase 
    sys.exit(app.exec())# se debe organizar para inicializar con la ecendida EJECUCION DEL SISTEMA
    