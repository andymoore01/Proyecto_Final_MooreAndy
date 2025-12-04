INSERT INTO paciente (nombre, apellido, dni, fecha_nacimiento, telefono, email, fecha_alta) VALUES
('Andy', 'Moore', '30111222', '1985-05-10', '1112345678', 'andy.moore@example.com', '2025-01-10'),
('Emiliano', 'Martinez','29123456', '1990-02-20', '1198765432', 'emiliano.martinez@example.com', '2025-01-11'),
('Nahuel', 'Molina',  '28111111', '1978-07-15', '1144445555', 'nahuel.molina@example.com',    '2025-01-12'),
('Cristian', 'Romero', '27123457', '1988-09-30', '1133332222', 'cristian.romero@example.com',   '2025-01-13'),
('Lisandro', 'Martinez', '26123458', '1995-12-12', '1166667777', 'lisandro.martinez@example.com',  '2025-01-14'),
('Nicolas', 'Tagliafico','25123459', '1983-04-18', '1155556666', 'nicolas.tagliafico@example.com',   '2025-01-15'),
('Leandro', 'Paredes',  '24123450', '1975-11-03', '1177778888', 'leandro.paredes@example.com',  '2025-01-16'),
('Enzo', 'Fernandez','23123451', '1992-06-22', '1188889999', 'enzo.fernandez@example.com',  '2025-01-17'),
('Giovanni', 'Locelso','22123452', '1987-03-29', '1199990000', 'giovanni.locelso@example.com',  '2025-01-18'),
('Lionel', 'Messi', '21123453', '1979-08-05', '1100001111', 'lionel.messi@example.com',  '2025-01-19');

INSERT INTO medico (nombre, apellido, dni, telefono, email, especialidad, fecha_alta) VALUES
('Lucas', 'Partal',  '20123454', '1122223333', 'lucas.partal@example.com', 'Clínica Médica', '2025-01-05'),
('Enzo', 'Guardia',  '19123455', '1133334444', 'enzo.guardia@example.com', 'Pediatría',      '2025-01-05'),
('Mauro',  'Martinez',    '18123456', '1144445555', 'mauro.martinez@example.com','Cardiología',    '2025-01-05'),
('Sebastian','Leguiza',  '17123457', '1155556666', 'sebastian.leguiza@example.com','Dermatología',   '2025-01-05'),
('Julian',  'Taverna', '16123458', '1166667777', 'julian.taverna@example.com',    'Traumatología',  '2025-01-05'),
('Ignacio',   'Cechi',    '15123459', '1177778888', 'ignacio.cechi@example.com', 'Neurología',     '2025-01-05'),
('Gonzalo', 'Barez',  '14123450', '1188889999', 'gonzalo.barez@example.com', 'Clínica Médica', '2025-01-05'),
('Matias',  'Sarraute', '13123451', '1199990000', 'matias.sarraute@example.com',   'Ginecología',    '2025-01-05'),
('Lautaro',   'Cerato',  '12123452', '1100001111', 'lautaro.cerato@example.com',   'Traumatología',  '2025-01-05'),
('Mariano',   'McCoubrey',  '11123453', '1111112222', 'mariano.mccoubrey@example.com',  'Pediatría',      '2025-01-05');

INSERT INTO turno (id_paciente, id_medico, fecha, hora, estado, motivo) VALUES
(1, 1, '2025-02-01', '09:00:00', 'PROGRAMADO', 'Control general'),
(1, 3, '2025-02-05', '10:00:00', 'PROGRAMADO', 'Chequeo cardiológico'),
(1, 7, '2025-02-10', '11:00:00', 'PROGRAMADO', 'Consulta clínica'),

(2, 2, '2025-02-01', '09:30:00', 'PROGRAMADO', 'Control pediátrico'),
(2, 8, '2025-02-06', '15:00:00', 'PROGRAMADO', 'Control ginecológico'),

(3, 3, '2025-02-02', '08:30:00', 'PROGRAMADO', 'Consulta cardiológica'),
(3, 1, '2025-02-08', '09:00:00', 'PROGRAMADO', 'Control clínico'),

(4, 4, '2025-02-03', '10:30:00', 'PROGRAMADO', 'Consulta dermatológica'),
(4, 6, '2025-02-09', '16:00:00', 'PROGRAMADO', 'Consulta neurológica'),

(5, 5, '2025-02-04', '11:30:00', 'PROGRAMADO', 'Dolor de rodilla'),
(5, 9, '2025-02-10', '14:00:00', 'PROGRAMADO', 'Control traumatológico'),

(6, 1, '2025-02-05', '09:00:00', 'PROGRAMADO', 'Control clínico'),
(6, 7, '2025-02-11', '12:00:00', 'PROGRAMADO', 'Seguimiento'),

(7, 2, '2025-02-06', '10:00:00', 'PROGRAMADO', 'Control pediátrico'),
(7, 10, '2025-02-12', '13:00:00', 'PROGRAMADO', 'Consulta pediátrica'),

(8, 3, '2025-02-07', '11:00:00', 'PROGRAMADO', 'Chequeo cardiológico'),
(8, 6, '2025-02-13', '09:30:00', 'PROGRAMADO', 'Consulta neurológica'),

(9, 4, '2025-02-08', '15:00:00', 'PROGRAMADO', 'Consulta dermatológica'),
(9, 8, '2025-02-14', '16:30:00', 'PROGRAMADO', 'Control ginecológico'),

(10, 5, '2025-02-09', '08:30:00', 'PROGRAMADO', 'Dolor de espalda'),
(10, 9, '2025-02-15', '10:30:00', 'PROGRAMADO', 'Control traumatológico');
