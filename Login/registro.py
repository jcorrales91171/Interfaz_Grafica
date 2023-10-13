from PyQt6.QtWidgets import (QDialog, QLabel,
                             QPushButton, QLineEdit,QMessageBox)
from PyQt6.QtGui import QFont,QPixmap

class RegistrarUsuarioView(QDialog):
    def __init__(self):
        super().__init__()
        self.generar_formulario()

    def generar_formulario(self):
        self.setGeometry(100, 100, 350, 250)
        self.setWindowTitle("Ventana de registro")

        user_label = QLabel(self)
        user_label.setText("usuario")
        user_label.setFont(QFont('Arial', 10))
        user_label.move(20,54)