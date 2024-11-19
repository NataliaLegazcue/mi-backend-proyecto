class Reporte:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def reporte_actividades_mas_ingresos(self):
        
        try:
            cursor = self.db_connection.cursor(dictionary=True)
            query = """
                SELECT a.descripcion, SUM(a.costo + IFNULL(e.costo, 0)) AS total_ingreso
                FROM actividades a
                LEFT JOIN equipamiento e ON a.id = e.id_actividad
                GROUP BY a.id
                ORDER BY total_ingreso DESC
            """
            cursor.execute(query)
            resultados = cursor.fetchall()

            print("\nReporte de Actividades con Más Ingresos:")
            for row in resultados:
                print(f"Actividad: {row['descripcion']}, Ingreso Total: {row['total_ingreso']}")
        except Exception as e:
            print(f"Error al generar el reporte de ingresos: {e}")

    def reporte_actividades_con_mas_alumnos(self):
        
        try:
            cursor = self.db_connection.cursor(dictionary=True)
            query = """
                SELECT a.descripcion, COUNT(ac.ci_alumno) AS total_alumnos
                FROM actividades a
                JOIN clase c ON a.id = c.id_actividad
                JOIN alumno_clase ac ON c.id = ac.id_clase
                GROUP BY a.id
                ORDER BY total_alumnos DESC
            """
            cursor.execute(query)
            resultados = cursor.fetchall()

            print("\nReporte de Actividades con Más Alumnos:")
            for row in resultados:
                print(f"Actividad: {row['descripcion']}, Total Alumnos: {row['total_alumnos']}")
        except Exception as e:
            print(f"Error al generar el reporte de alumnos: {e}")

    def reporte_turnos_con_mas_clases_dictadas(self):
        
        try:
            cursor = self.db_connection.cursor(dictionary=True)
            query = """
                SELECT t.id, t.hora_inicio, t.hora_fin, COUNT(c.id) AS total_clases
                FROM turnos t
                JOIN clase c ON t.id = c.id_turno
                WHERE c.dictada = TRUE
                GROUP BY t.id
                ORDER BY total_clases DESC
            """
            cursor.execute(query)
            resultados = cursor.fetchall()

            print("\nReporte de Turnos con Más Clases Dictadas:")
            for row in resultados:
                print(f"Turno: {row['id']}, Inicio: {row['hora_inicio']}, Fin: {row['hora_fin']}, Clases Dictadas: {row['total_clases']}")
        except Exception as e:
            print(f"Error al generar el reporte de turnos: {e}")