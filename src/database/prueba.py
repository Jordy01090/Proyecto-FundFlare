import oracledb
class Conexion2():

    connection=oracledb.connect (
        user='C##jordy',
        password='Jordy0109',
        dsn='localhost:1521/xe',
        encoding = 'UTF-8'
    )
    
    cur = connection.cursor()

    nombre_tabla = 'USUARIOS'
    cur.execute("SELECT * FROM usuarios WHERE usuario = 'jordy' AND contraseña = 'jordy2004'")
    result = cur.fetchone()

    if result:
        print(f" existe.")
    else:
        print(f"no existe.")
    cur.close()
    connection.close()
    

    
 
        
# Consultar en all_tables para verificar la existencia de la tabla

# Obtener los resultados


# Verificar si la tabla existe

# Cerrar el cursor y la conexión

