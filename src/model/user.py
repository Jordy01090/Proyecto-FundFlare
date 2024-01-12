#Clase modelo que recibe la informacion de un usuario
class Usuario():
    def __init__(self, nombre="",apellido="", usuario="", contraseña="", email="", rol=""):
        self._nombre = nombre
        self._apellido = apellido
        self._usuario = usuario
        self._contraseña = contraseña
        self._email = email
        self._rol = rol
