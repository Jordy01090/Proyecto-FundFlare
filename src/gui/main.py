import re
from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox
from registrarLogin import RegistrationWindow
from crearProyecto import NuevoProyecto
from data_proyect import ProyectData
from proyecto import Proyecto

#Clase Login para trabajar en la interfáz de inicio de sesión en la app
class MainWindow():
    #Constructor que se conecta la interfáz con la aplicación
    def __init__(self):
        self.main = uic.loadUi("C:/Users/avila/OneDrive/Escritorio/Proyecto_Crowdfunding/src/gui/main.ui")
        self.initGUI()
        self.main.showMaximized()
    def initGUI(self):
        self.main.btnCrear_Proyecto.triggered.connect(self.abrirNuevoProyecto) 
        self.nuevoP = uic.loadUi("C:/Users/avila/OneDrive/Escritorio/Proyecto_Crowdfunding/src/gui/crearProyecto.ui") 

    def abrirNuevoProyecto(self):
        self.nuevoP.show()
        self.nuevoP.btnCrear.clicked.connect(self.registrarProyecto)
    def registrarProyecto(self):
        if len(self.nuevoP.txtNombreP.text()) < 2:
            mBox = QMessageBox()
            mBox.setText("El nombre del proyecto debe contener mas de dos caracteres")
            mBox.exec()
            self.nuevoP.txtNombreP.setFocus()
        elif (len(self.nuevoP.txtDescripcionP.toPlainText()) < 30 | len(self.nuevoP.txtDescripcionP.toPlainText()) > 500):
            mBox = QMessageBox()
            mBox.setText("La descripcion de tu proyecto debe contener mas de 30 caracteres y menos de 500")
            mBox.exec()
            self.nuevoP.txtDescripcionP.setFocus()
        elif not self.nuevoP.txtObjetivoF.text().isnumeric():
            mBox = QMessageBox()
            mBox.setText("El monto debe estar en dolares")
            mBox.exec()
            self.nuevoP.txtObjetivoF.setText("0")
            self.nuevoP.txtObjetivoF.setFocus()
        elif not self.nuevoP.fechaI.date().isValid():
            mBox = QMessageBox()
            mBox.setText("Ingrese una fecha de inicio valida")
            mBox.exec()
            self.nuevoP.fechaI.setFocus()
        elif not self.nuevoP.fechaF.date().isValid():
            mBox = QMessageBox()
            mBox.setText("Ingrese una fecha de finalizacion valida")
            mBox.exec()
            self.nuevoP.tfechaF.setFocus()
        else:
            proyectos = Proyecto(
                nombre=self.nuevoP.txtNombreP.text(),
                descripcion=self.nuevoP.txtDescripcionP.toPlainText(),
                objetivo=float(self.nuevoP.txtObjetivoF.text()),
                fechaInicio=self.nuevoP.fechaI.date(),
                fechaFin=self.nuevoP.fechaF.date()
            )
        objData = ProyectData()
        mBox = QMessageBox()
        if objData.registrarProyecto(info=proyectos):
            mBox.setText("Proyecto Registrado")
        else:
            mBox.setText("Proyecto no registrado")
        mBox.exec()
             
 