from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox
from correo import Correo
import re
from data_user import UsuarioData

from user import Usuario

#Clase Login para trabajar en la interfáz de inicio de sesión en la app
class NuevoProyecto():
    
    #Constructor que se conecta la interfáz con la aplicación
    def __init__(self):
        
        self.nuevoP = uic.loadUi("C:/Users/avila/OneDrive/Escritorio/Proyecto_Crowdfunding/src/gui/crearProyecto.ui")
        self.nuevoP.show()
     