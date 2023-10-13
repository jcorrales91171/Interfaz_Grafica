import sys
import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import (QApplication, QLabel, QWidget, QLineEdit, QPushButton, QMessageBox, QCheckBox,)
                            #QApplicationaplicacio
                            #QLabel se utiliza para mostrar los label en la aplicacion y las imagenes
                            #QWidget nos permite generar la ventana de los ocmponenetes
                            #QLineEdit campos uqe nos permiten ingresar 
                            #Qpushbutton paragenerar botones que podemos presionar
                            #QMessageBox nos permite interactuar con el ususario mostrandole textos emergentes 
                            #QPixmap nos permitira introducir imagenes en nuestros labels
from PyQt6.QtGui import QFont,QPixmap

from registro import RegistrarUsuarioView

class Login(QWidget):

    def __init__(self):
        super().__init__()
        self.inicializar_UI()

    def inicializar_UI(self):
        self.setGeometry(100, 100, 350, 250)
        self.setWindowTitle("login")
        self.generar_formulario()
        self.show()


    def generar_formulario(self):
        self.is_logged = False

        user_label = QLabel(self)
        user_label.setText("usuario")
        user_label.setFont(QFont('Arial', 10))
        user_label.move(20,54)
        

        self.user_input = QLineEdit(self)
        self.user_input.resize(250, 24)
        self.user_input.move(98, 50)

        password_label = QLabel(self)
        password_label.setText("Password:")
        password_label.setFont(QFont('Arial',10))
        password_label.move(20, 86)
        
        self.password_input = QLineEdit(self)
        self.password_input.resize(250,24)
        self.password_input.move(98, 82)
        self.password_input.setEchoMode(
            QLineEdit.EchoMode.Password
        )

        self.check_view_password = QCheckBox(self)
        self.check_view_password.setText("Ver contraseña")
        self.check_view_password.move(90, 110)
        self.check_view_password.toggled.connect(self.mostrar_contrasena)

        login_button = QPushButton(self)
        login_button.setText("Login")
        login_button.resize(320, 34)
        login_button.move(20, 140)
        login_button.clicked.connect(self.Inicializar_mainview)

        Register_button = QPushButton(self)
        Register_button.setText("Registrarse")
        Register_button.resize(320, 34)
        Register_button.move(20, 180)
        Register_button.clicked.connect(self.registrar_usuario)

    def mostrar_contrasena(self, clicked):
        if clicked:
            self.password_input.setEchoMode(
                QLineEdit.EchoMode.Normal
            )
        else:
            self.password_input.setEchoMode(
                QLineEdit.EchoMode.Password
            )

    def Inicializar_mainview():
        pass

    def registrar_usuario():
        new_user_form = RegistrarUsuarioView()
        new_user_form 
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = Login()
    sys.exit(app.exec())
