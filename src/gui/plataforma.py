
from PyQt6.QtWidgets import QApplication
from login import Login
#Clase plataforma que permite la conexion con del login con PyQt6
class Plataforma():
    def __init__(self):
        self.app = QApplication([])
        self.login = Login()
        self.app.exec()
