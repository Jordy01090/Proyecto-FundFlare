from conexion_oracle import Conexion
from data_user import UsuarioData
from proyecto import Proyecto
from datetime import datetime
#Clase que nos ayuda a crear la conexion con nuestra base de datos
class ProyectData():  
    def __init__(self) -> None:
        table_name = 'proyectos'
        if not self.tablaExiste(table_name):
            try:
                self.db = Conexion.conectar(Conexion())
                self.cursor = self.db.cursor()
                sql_create_proyectos = """CREATE TABLE PROYECTOS (
                    id NUMBER PRIMARY KEY,
                    nombre VARCHAR2(255),
                    descripcion VARCHAR2(255),
                    objetivo VARCHAR2(220),
                    fechaInicio VARCHAR2(255),
                    fechaFin VARCHAR2(255),
                    fecha_registro TIMESTAMP,
                    verificado NUMBER(1,0) DEFAULT 0
                )"""
                
                self.cursor.execute(sql_create_proyectos)
                self.cursor.close()
                self.db.commit()
                self.db.close()
                print("Tabla Proyectos creada.")
            except Exception as ex:
                print("Error al crear la tabla de proyectos:", ex)
        else:
            print(f"La tabla {table_name} ya existe.")
        
    def registrarProyecto(self,info: Proyecto):
        fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.db = Conexion.conectar(Conexion())
        self.cursor = self.db.cursor()
        info._fechaInicio = info._fechaInicio.toString("dd/MM/yyyy")
        info._fechaFin = info._fechaFin.toString("dd/MM/yyyy")
        sql_insert = """INSERT INTO proyectos (id, nombre, descripcion, objetivo, fechaInicio, fechaFin, fecha_Registro, verificado) 
                                VALUES (proyectos_seq.NEXTVAL, '{}', '{}', '{}', '{}', '{}',TO_TIMESTAMP('{}', 'DD/MM/YYYY HH24:MI:SS'), '{}')""".format(
                                 info._nombre, info._descripcion, info._objetivo, info._fechaInicio, info._fechaFin,fecha,0)
        print("SQL Statement:", sql_insert)
        self.cursor.execute(sql_insert)
        self.db.commit()
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
    #Metodo que sirve para verificar si la tabla a crear existe o no
    def tablaExiste(self, nombre_tabla):
        self.db = Conexion.conectar(Conexion())
        self.cursor = self.db.cursor()
        self.cursor.execute(f"SELECT table_name FROM all_tables WHERE table_name = '{nombre_tabla.upper()}'")
        resultado = self.cursor.fetchone()
        self.cursor.close()
        return resultado is not None