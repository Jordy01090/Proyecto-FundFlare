import oracledb
class Conexion():
    #Creando la conexion
    def __init__(self):
        try:
            self.connection=oracledb.connect (
                user='C##jordy',
                password='Jordy0109',
                dsn='localhost:1521/xe',
                encoding = 'UTF-8'
            )    
            #self.crearAdmin()
            #self.crearTablas()   
             
        except Exception as ex:
            print(ex)
    #Metodo que sirve para verificar si la tabla a crear existe o no
    def tablaExiste(self, nombre_tabla):
        cur = self.connection.cursor()
        cur.execute(f"SELECT table_name FROM all_tables WHERE table_name = '{nombre_tabla.upper()}'")
        resultado = cur.fetchone()
        cur.close()
        return resultado is not None
    #Metodo para crear una nueva tabla
    def crearTablas(self):
        table_name = 'usuarios'
        if not self.tablaExiste(table_name):
            try:
                sql_create_table = """CREATE TABLE USUARIOS (
                    id NUMBER PRIMARY KEY,
                    nombre VARCHAR2(255),
                    apellido VARCHAR2(255),
                    usuario VARCHAR2(255) UNIQUE,
                    contraseña VARCHAR2(255),
                    email VARCHAR2(255),
                    rol VARCHAR2(155)
                )"""
                cur = self.connection.cursor()
                cur.execute(sql_create_table)
                cur.close()
                self.crearAdmin()
            except Exception as ex:
                print("Error al crear la tabla de usuarios:", ex)
        else:
            print(f"La tabla {table_name} ya existe.")
    #Creando usuario admin
    def crearAdmin(self):
        try:
            sql_insert = """INSERT INTO usuarios (id, nombre, apellido, usuario, contraseña, email, rol) 
                            VALUES (usuarios_seq.NEXTVAL, 'Jordy', 'Avila', 'jordy', 'jordy2004', 'avilajordy71@gmail.com', 'Administador')"""
            cur = self.connection.cursor()
            cur.execute(sql_insert)
            self.connection.commit()
        except Exception as ex:
            print("Error al crear el usuario Admin", ex)
 
    #Metodo que retorna una instancia de la conexion
    def conectar(self):
        return self.connection
#con = Conexion()