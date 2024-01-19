import re
from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox, QTableWidgetItem
from historialProyectos import HistorialData
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
        self.main.btnVer_Proyectos.triggered.connect(self.abrirHistorial) 
        self.nuevoP = uic.loadUi("C:/Users/avila/OneDrive/Escritorio/Proyecto_Crowdfunding/src/gui/crearProyecto.ui") 
        self.historial = uic.loadUi("C:/Users/avila/OneDrive/Escritorio/Proyecto_Crowdfunding/src/gui/historialProyectos.ui")
    def abrirNuevoProyecto(self):
        self.nuevoP.show()
        self.nuevoP.btnCrear.clicked.connect(self.registrarProyecto)
###############   Crear  Proyecto ##########################################################
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
            self.limpiarCreacionProyecto()
        else:
            mBox.setText("Proyecto no registrado")
        mBox.exec()
    def limpiarCreacionProyecto(self):
        self.nuevoP.txtNombreP.setText("")
        self.nuevoP.txtDescripcionP.setText("")
        self.nuevoP.txtObjetivoF.setText("0")
################ Historial Proyectos ########################################################
    def abrirHistorial(self):
        self.historial.btnBuscar.clicked.connect(self.buscar)
        self.historial.tblHistorial.setColumnWidth(0,100)
        self.historial.tblHistorial.setColumnWidth(1,200)
        self.historial.tblHistorial.setColumnWidth(2,250)
        self.historial.tblHistorial.setColumnWidth(3,150)
        self.historial.tblHistorial.setColumnWidth(6,150)

        self.historial.show()
        self.llenarTablasHistorial()
    
    def buscar(self):
        his = HistorialData()
        fechaDesde = self.historial.txtFechaDesde.date().toString("dd/MM/yyyy")
        fechaHasta = self.historial.txtFechaHasta.date().toString("dd/MM/yyyy")
        data = his.buscarPorFecha(fechaDesde,fechaHasta,
                           self.historial.txtNombreP.text())
        print(data)
        fila = 0
        self.historial.tblHistorial.setRowCount(len(data))
        for item in data:
            self.historial.tblHistorial.setItem(fila,0,QTableWidgetItem(str(item[0])))
            self.historial.tblHistorial.setItem(fila,1,QTableWidgetItem(str(item[1])))
            self.historial.tblHistorial.setItem(fila,2,QTableWidgetItem(str(item[2])))
            self.historial.tblHistorial.setItem(fila,3,QTableWidgetItem(str(item[3])))
            self.historial.tblHistorial.setItem(fila,4,QTableWidgetItem(str(item[4])))
            self.historial.tblHistorial.setItem(fila,5,QTableWidgetItem(str(item[5])))
            self.historial.tblHistorial.setItem(fila,6,QTableWidgetItem(str(item[6])))
            self.historial.tblHistorial.setItem(fila,7,QTableWidgetItem(str(item[7])))
            fila=fila+1
        
    def llenarTablasHistorial(self):
        pass
 