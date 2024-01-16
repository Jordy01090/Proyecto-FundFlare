from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox
from correo import Correo
import re
from database.data_user import UsuarioData

from src.model.user import Usuario

#Clase Login para trabajar en la interfáz de inicio de sesión en la app
class RegistrationWindow():
    
    #Constructor que se conecta la interfáz con la aplicación
    def __init__(self):
        
        self.registro = uic.loadUi("C:/Users/avila/OneDrive/Escritorio/Python_conexion/src/gui/registrarLogin.ui")
        
        #self.initGUI()
        self.registro.lblError.setText("")
        self.initGUI()
        self.registro.show()
    def validation(self):
            
            if len(self.registro.txtNombre.text()) < 2:
                self.registro.lblError.setText("Ingrese nombre válido")
                self.registro.txtNombre.setFocus()#El cursor se pocisiona automaticamente en el siguiente al dar enter
            elif len(self.registro.txtApellido.text()) == 0:
                self.registro.lblError.setText("Ingrese apellido válido")
                self.registro.txtApellido.setFocus()
            elif len(self.registro.txtUsuario.text()) == 0:
                self.registro.lblError.setText("Ingrese una nombre de usuario válido")
                self.registro.txtUsuario.setFocus()
            elif len(self.registro.txtEmail.text()) == 0:
                self.registro.lblError.setText("Ingrese un email válida")
                self.registro.txtEmail.setFocus()
            elif len( self.registro.txtPassword.text()) == 0:
                self.registro.lblError.setText("Ingrese una contraseña válida")
                self.registro.txtPassword.setFocus()
            elif len(self.registro.txtConfPass.text()) == 0:
                self.registro.lblError.setText("Por favor, confirme su contraseña")
                self.registro.txtConfPass.setFocus()
            elif self.registro.txtPassword.text() != self.registro.txtConfPass.text():
                self.registro.lblError.setText("La confirmación de contraseña no coincide")
                self.registro.txtConfPass.setFocus()
            elif self.registro.cmbRol.currentIndex() == 0:
                self.registro.lblError.setText("Seleccione su Rol")
                self.registro.cmbRol.setFocus()
            elif not self.registro.cbTerminos.isChecked():
                self.registro.lblError.setText("Debe aceptar los términos y condiciones")
                self.registro.cbTerminos.setFocus()
            elif not self.validar_correo(self.registro.txtEmail.text()):
                self.registro.lblError.setText('Porfavor ingrese una dirección de correo válida.')
            else:
                usu = Usuario(nombre=self.registro.txtNombre.text(),apellido=self.registro.txtApellido.text(),
                              usuario=self.registro.txtUsuario.text(),contraseña=self.registro.txtPassword.text(),email=self.registro.txtEmail.text(),
                              rol=self.registro.cmbRol.currentText())
                usuData = UsuarioData()
                res = usuData.registro(usu)
                if res:
                    correo = Correo()
                    correo.enviar_correo_confirmacion(self.registro.txtEmail.text())
                    self.registro.lblError.setText("Usuario registrado exitosamente")
                else:
                    #self.registro.lblError.setText(UsuarioData.registro)

                    self.registro.lblError.setText(usuData.msj)
    def validar_correo(self,correo):
        # Expresión regular para validar direcciones de correo electrónico
        patron_correo = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        
        # Intenta hacer coincidir la dirección de correo con el patrón
        if re.match(patron_correo, correo):
            return True
        else:
            return False

    def initGUI(self):
        self.registro.btnRegistrarme.clicked.connect(self.validation)    
        