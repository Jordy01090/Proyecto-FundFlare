from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox
from src.gui.registrarLogin import RegistrationWindow
from src.gui.main import MainWindow
from src.database.data_user import UsuarioData

from src.model.user import Usuario


#Clase Login para trabajar en la interfáz de inicio de sesión en la app
class Login():
    #Constructor que se conecta la interfáz con la aplicación
    def __init__(self):
        self.login = uic.loadUi("C:/Users/avila/OneDrive/Escritorio/Python_conexion/src/gui/login.ui")
        self.login.lblError.setText("")
        self.initGUI()
        self.login.show()
    #Método para validar usuario y contraseña
    def ingresar(self):
        if len(self.login.txtUsuario.text()) < 2:
            self.login.lblError.setText("Ingrese un usuario válido")
            self.login.txtUsuario.setFocus()#El cursor se pocisiona automaticamente en el siguiente al dar enter
        elif len(self.login.txtClave.text()) < 3:
            self.login.lblError.setText("Ingrese una contraseña válida")
            self.login.txtClave.setFocus()
        else:
            self.login.lblError.setText("")
            usu = Usuario(usuario=self.login.txtUsuario.text(),contraseña=self.login.txtClave.text())
            print(usu._usuario)
            usuData = UsuarioData()
            res = usuData.login(usu)
            if res:
                self.main = MainWindow()
                self.login.hide()
            else:
                self.login.lblError.setText("Datos de usuario incorrectos")
    def registrarLogin(self):
        self.registro = RegistrationWindow()
    #Método para dar paso a la validación de usuario y contraseña
    def initGUI(self):
        self.login.btnAcceder.clicked.connect(self.ingresar)
        self.login.btnRegistrar.clicked.connect(self.registrarLogin)
    