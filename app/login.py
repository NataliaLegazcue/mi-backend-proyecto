import mysql.connector

class Login:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def authenticate(self, correo, contraseña):
        try:
            cursor = self.db_connection.cursor(dictionary=True)
            query = "SELECT * FROM login WHERE correo = %s AND contraseña = %s"
            cursor.execute(query, (correo, contraseña))
            user = cursor.fetchone()

            if user:
                cursor.execute("UPDATE login SET Actividad = TRUE WHERE correo = %s", (correo,))
                self.db_connection.commit()
                print("Login exitoso. Bienvenido!")
                return True
            else:
                print("Credenciales incorrectas.")
                return False
        except mysql.connector.Error as err:
            print(f"Error en la base de datos: {err}")
            return False
        finally:
            cursor.close()

    def logout(self, correo):
        try:
            cursor = self.db_connection.cursor()
            query = "UPDATE login SET Actividad = FALSE WHERE correo = %s"
            cursor.execute(query, (correo,))
            self.db_connection.commit()
            print("Sesión cerrada.")
        except mysql.connector.Error as err:
            print(f"Error en la base de datos: {err}")
        finally:
            cursor.close()