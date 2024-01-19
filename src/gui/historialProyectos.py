
from conexion_oracle import Conexion 


class HistorialData():
    
    #def buscarPorFecha(self, fechaDesde, fechaHasta):
    #    con = Conexion()
    #   self.db = con.Conexion().conectar()
    #    self.cursor = self.db.cursor()
    #    sql="""SELECT * FROM proyectos WHERE fecha_registro >= '{}'
    #    and fecha_registro <= '{}'""".format(fechaDesde,fechaHasta)
    #    res = self.cursor.execute(sql)
    #    data = res.fetcall()
    #   return data
    def buscarPorFecha(self, fechaDesde, fechaHasta, nombre):
        con = Conexion()
        self.db = con.conectar()  # Debes llamar a la función conectar() en lugar de Conexion().conectar()
        self.cursor = self.db.cursor()
        sql = """SELECT * FROM proyectos 
                WHERE fecha_registro >= TO_DATE('{}', 'DD/MM/YYYY HH24:MI:SS')
                AND fecha_registro <= TO_DATE('{}', 'DD/MM/YYYY HH24:MI:SS') OR nombre='{}'""".format(fechaDesde, fechaHasta, nombre)
        self.cursor.execute(sql)  # Cambiado res por self.cursor.execute()
        data = self.cursor.fetchall()  # Cambiado res.fetcall() por self.cursor.fetchall()
        return data

