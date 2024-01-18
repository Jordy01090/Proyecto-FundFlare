from conexion_oracle import Conexion
from data_user import UsuarioData
from proyecto import Proyecto
from datetime import datetime
#Clase que nos ayuda a crear la conexion con nuestra base de datos
class ProyectData():  
    def __init__(self) -> None:
        try:
            self.db = Conexion.conectar(Conexion())
            self.cursor = self.db.cursor()
            sql_create_proyectos = """CREATE TABLE PROYECTOS (
                id NUMBER PRIMARY KEY,
                nombre VARCHAR2(255),
                descripcion VARCHAR2(255),
                objetivo VARCHAR2(220),  -- Corrección: Cambiado VARCAHAR2 a VARCHAR2
                fechaInicio VARCHAR2(255),
                fechaFin VARCHAR2(255),
                fecha_registro DATE,
                NUMBER(1,0) DEFAULT 0 
            )"""
            
            self.cursor.execute(sql_create_proyectos)
            self.cursor.close()
            self.db.close()
            print("Tabla Proyectos creada.")
        except Exception as ex:
            print("Tablas Proyectos OK: ", ex)
        
    def registrarProyecto(self,info: Proyecto):
        fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.db = Conexion.conectar(Conexion())
        self.cursor = self.db.cursor()
        
        sql_insert = """INSERT INTO proyectos (id, nombre, descripcion, objetivo, fechaInicio, fechaFin, fechaRegistro, verificado) 
                                VALUES (proyectos_seq.NEXTVAL, '{}', '{}', '{}', '{}', '{}', '{}', '{}')""".format(
                                    info._nombre, info._nombre, info._descripcion, info._objetivo, info._fechaInicio, info._fechaFin,fecha,False)
        self.cursor.execute(sql_insert)
        self.db.commit
        if self.cursor.rowcount == 1:
            return True
        else:
            return False
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