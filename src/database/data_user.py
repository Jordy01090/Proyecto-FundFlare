
from src.database.conexion_oracle import Conexion 
from src.model.user import Usuario
#Clase que nos ayuda a crear la conexion con nuestra base de datos
class UsuarioData():  
    #Metodo que sirve para verificar la existencia de un usuario en la base de datos
    def __init__(self):
        self.msj = None
    def login(self,usuario: Usuario):
        self.db = Conexion.conectar(Conexion())
        self.cursor = self.db.cursor()
        res = self.cursor.execute("SELECT * FROM usuarios WHERE usuario = '{}' AND contraseña = '{}'".format(usuario._usuario, usuario._contraseña))
        
        fila = res.fetchone()
        if fila:
            usuario = Usuario(usuario=fila[1],contraseña=fila[2])
            self.cursor.close()
            self.db.close()
            print(fila)
            return usuario
        else:
            print(fila)
            return None
    def registro(self, usuario):
        if self.usuario_existe(usuario._usuario):
            # El usuario ya existe, realiza las acciones necesarias (por ejemplo, mostrar un mensaje de error)
            mensaje = "El usuario ya existe. Por favor, elija otro nombre de usuario."
            print(mensaje)
            self.msj = mensaje
            return False
            #return False
        elif self.correo_existe(usuario._email):
            # El correo ya existe, realiza las acciones necesarias (por ejemplo, mostrar un mensaje de error)
            mensaje = "El correo ya ha sido registrado. Por favor, utilice otro correo."
            print(mensaje)
            self.msj = mensaje
            return False
            #return False
        else:
            # El usuario no existe, procede con el registro
            try:
                sql_insert = """INSERT INTO usuarios (id, nombre, apellido, usuario, contraseña, email, rol) 
                                VALUES (usuarios_seq.NEXTVAL, '{}', '{}', '{}', '{}', '{}', '{}')""".format(
                                    usuario._nombre, usuario._apellido, usuario._usuario, usuario._contraseña, usuario._email, usuario._rol
                                )
                self.db = Conexion.conectar(Conexion())
                self.cursor = self.db.cursor()
                self.cursor.execute(sql_insert)
                self.db.commit()
                return True
            except Exception as ex:
                print("Error al registrar el usuario:", ex)
                return False
            
    def usuario_existe(self, nombre_usuario):
        self.db = Conexion.conectar(Conexion())
        cur = self.db.cursor()
        cur.execute(f"SELECT COUNT(*) FROM usuarios WHERE usuario = '{nombre_usuario}'")
        resultado = cur.fetchone()
        cur.close()
        return resultado[0] > 0
    def correo_existe(self, correo):
        cur = self.db.cursor()
        cur.execute(f"SELECT COUNT(*) FROM usuarios WHERE email = '{correo}'")
        resultado = cur.fetchone()
        cur.close()
        return resultado[0] > 0
        

