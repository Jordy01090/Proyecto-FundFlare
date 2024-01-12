from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox

#Clase Login para trabajar en la interfáz de inicio de sesión en la app
class MainWindow():
    #Constructor que se conecta la interfáz con la aplicación
    def __init__(self):
        self.main = uic.loadUi("C:/Users/avila/OneDrive/Escritorio/Python_conexion/src/gui/main.ui")
        #self.initGUI()
        self.main.showMaximized()

         