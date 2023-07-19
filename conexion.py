"""Conectar con SQL"""

import pyodbc
from credenciales import database, password, server, username

def conexion():
    """Conexión a SQL"""
    try:

        cn= pyodbc.connect('DRIVER={SQL Server};SERVER='+server+
                            ';DATABASE='+database+
                            ';UID='+username+
                            ';PWD='+ password)
        print("conexion")
        return cn
    except ImportError:
        print("ERROR A LA CONEXIÓN")
        return None
_=conexion()
