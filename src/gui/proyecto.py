class Proyecto():
    def __init__(self, nombre: str,descripcion:str, objetivo= float, fechaInicio="", fechaFin=""):
        self._nombre = nombre
        self._descripcion = descripcion
        self._objetivo = objetivo
        self._fechaInicio = fechaInicio
        self._fechaFin = fechaFin
        