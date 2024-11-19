CREATE DATABASE IF NOT EXISTS escuela_deportes;

USE escuela_deportes;

#Tabla para el manejo de usuarios de login
CREATE TABLE login ( 

    correo VARCHAR(60) PRIMARY KEY, 

    contraseña VARCHAR(60) NOT NULL 

); 

#Tabla de actividades, con costo asociado a cada actividad
CREATE TABLE actividades ( 

    id INT AUTO_INCREMENT PRIMARY KEY, 

    descripcion VARCHAR(100) NOT NULL, 

    costo DECIMAL(10,2) NOT NULL 
); 

#Tabla de equipamiento con relación a actividades
CREATE TABLE equipamiento ( 

    id INT AUTO_INCREMENT PRIMARY KEY, 

    id_actividad INT NOT NULL, 

    descripcion VARCHAR(100) NOT NULL, 

    costo DECIMAL(10,2) NOT NULL, 

    FOREIGN KEY (id_actividad) REFERENCES actividades(id) 

); 

#Tabla de instructores
CREATE TABLE instructores ( 

    ci VARCHAR(20) PRIMARY KEY, 

    nombre VARCHAR(50) NOT NULL, 

    apellido VARCHAR(50) NOT NULL 

);

#Tabla de turnos
CREATE TABLE turnos ( 

    id INT AUTO_INCREMENT PRIMARY KEY, 

    hora_inicio TIME NOT NULL, 

    hora_fin TIME NOT NULL 

); 

#Tabla de alumnos
CREATE TABLE alumnos ( 

    ci VARCHAR(20) PRIMARY KEY, 

    nombre VARCHAR(50) NOT NULL, 

    apellido VARCHAR(50) NOT NULL, 

    fecha_nacimiento DATE NOT NULL, 

    telefono VARCHAR(20), 

    correo_electronico VARCHAR(255) 

); 

#Tabla de clases, que asocia instructores y actividades con turnos especificos
-- Tabla de clases, que asocia instructores y actividades con turnos específicos 

CREATE TABLE clase ( 

    id INT AUTO_INCREMENT PRIMARY KEY, 

    ci_instructor VARCHAR(20) NOT NULL, 

    id_actividad INT NOT NULL, 

    id_turno INT NOT NULL, 

    dictada BOOLEAN DEFAULT FALSE, 

    FOREIGN KEY (ci_instructor) REFERENCES instructores(ci), 

    FOREIGN KEY (id_actividad) REFERENCES actividades(id), 

    FOREIGN KEY (id_turno) REFERENCES turnos(id), 

    UNIQUE (ci_instructor, id_turno) -- Un instructor no puede estar en dos clases en el mismo turno 

); 


# Tabla de relación entre alumnos y clases, con opcionalidad de equipamiento alquilado 

CREATE TABLE alumno_clase ( 

    id_clase INT NOT NULL, 

    ci_alumno VARCHAR(20) NOT NULL, 

    id_equipamiento INT, 

    PRIMARY KEY (id_clase, ci_alumno), 

    FOREIGN KEY (id_clase) REFERENCES clase(id), 

    FOREIGN KEY (ci_alumno) REFERENCES alumnos(ci), 

    FOREIGN KEY (id_equipamiento) REFERENCES equipamiento(id), 

    UNIQUE (ci_alumno, id_clase) -- Un alumno no puede estar en dos clases en el mismo turno 

); 


#Agregado a la tabla login, para determinar si una cuenta esta conectada a la base de datos
ALTER TABLE login 
ADD COLUMN Actividad BOOLEAN DEFAULT FALSE;

#Inserto el usuario Administrador que puede dar de alta a otros usuarios en el sistema
INSERT INTO login (correo, contraseña) 
VALUES ('administrador', 'password');
