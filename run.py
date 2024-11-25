import mysql.connector
from app.login import Login
from app.alumnoManager import AlumnoManager
from app.instructorManager import InstructorManager
from app.actividadesManager import ActividadesManager
from app.reporte import Reporte

db_connection = mysql.connector.connect(
    host="127.0.0.1",       # Dirección IP del servidor MySQL en PC
    user="root",            # Nombre de usuario de MySQL en PC
    password="5000",        # Contraseña del usuario MySQL en PC
    database="escuela_deportes"  
)

login_manager = Login(db_connection)
alumno_manager = AlumnoManager(db_connection)
instructor_manager = InstructorManager(db_connection)
actividad_manager = ActividadesManager(db_connection)
reporte = Reporte(db_connection)

# Ejemplo de autenticación
correo = input("Correo: ")
contraseña = input("Contraseña: ")

if login_manager.authenticate(correo, contraseña):
    print("Sesión iniciada con éxito.")
    
    action = input("¿Qué acción deseas realizar? (1: Agregar Alumno, 2: Mostrar Alumnos, 3: Salir): ")
    
    if action == "1":
        ci = input("CI del alumno: ")
        nombre = input("Nombre del alumno: ")
        apellido = input("Apellido del alumno: ")
        fecha_nacimiento = input("Fecha de nacimiento (YYYY-MM-DD): ")
        telefono = input("Teléfono: ")
        correo_electronico = input("Correo electrónico: ")
        alumno_manager.alta_alumno(ci, nombre, apellido, fecha_nacimiento, telefono, correo_electronico)
    elif action == "2":
        ci = input("CI del alumno a mostrar: ")
        alumno = alumno_manager.obtener_alumno(ci)
        if alumno:
            print(alumno)
    else:
        print("Saliendo...")
else:
    print("Credenciales incorrectas.")