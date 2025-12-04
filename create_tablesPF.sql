
CREATE DATABASE IF NOT EXISTS proyecto_final;
USE proyecto_final;

CREATE TABLE paciente (
    id_paciente INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    dni CHAR(8) NOT NULL UNIQUE,
    fecha_nacimiento DATE NOT NULL,
    telefono VARCHAR(20),
    email VARCHAR(100),
    fecha_alta DATE NOT NULL DEFAULT (CURRENT_DATE)
);


CREATE TABLE medico (
    id_medico INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    dni CHAR(8) NOT NULL UNIQUE,
    telefono VARCHAR(20),
    email VARCHAR(100),
    especialidad VARCHAR(100) NOT NULL,
    fecha_alta DATE NOT NULL DEFAULT (CURRENT_DATE)
);

CREATE TABLE turno (
    id_turno INT AUTO_INCREMENT PRIMARY KEY,
    id_paciente INT NOT NULL,
    id_medico INT NOT NULL,
    fecha DATE NOT NULL,
    hora TIME NOT NULL,
    estado ENUM('PROGRAMADO', 'CANCELADO', 'REALIZADO') NOT NULL DEFAULT 'PROGRAMADO',
    motivo VARCHAR(255),
    fecha_creacion DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,


    FOREIGN KEY (id_paciente)
        REFERENCES paciente(id_paciente)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    FOREIGN KEY (id_medico)
        REFERENCES medico(id_medico)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    -- evita doble turno del mismo medico a la misma hora
    UNIQUE (id_medico, fecha, hora)
);



CREATE INDEX idx_medico_especialidad ON medico (especialidad);
CREATE INDEX idx_turno_fecha ON turno (fecha);


