import mysql.connector
from app.login import Login
from app.alumnoManager import AlumnoManager
from app.instructorManager import InstructorManager
from app.actividadManager import ActividadManager
from app.reporte import Reporte

db_connection = mysql.connector.connect(
    host="127.0.0.1",     # cambiar según MySQL en PC
    user="root",          # cambiar según MySQL en PC
    password="5000",      # cambiar según MySQL en PC
    database="escuela_deportes",  
    port=3306             
)

login_manager = Login(db_connection)
alumno_manager = AlumnoManager(db_connection)
instructor_manager = InstructorManager(db_connection)
actividad_manager = ActividadManager(db_connection)
reporte = Reporte(db_connection)

# Ejemplo de iniciar sesión
correo = input("Correo: ")
contraseña = input("Contraseña: ")
if login_manager.authenticate(correo, contraseña):
    print("Sesión iniciada con éxito.")
else:
    print("Credenciales incorrectas.")