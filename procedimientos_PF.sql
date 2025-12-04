DELIMITER $$

CREATE FUNCTION cantidad_turnos_medico(p_id_medico INT)
RETURNS INT
DETERMINISTIC
READS SQL DATA
BEGIN
    DECLARE cant INT;
    SELECT COUNT(*)
      INTO cant
      FROM turno
     WHERE id_medico = p_id_medico;
    RETURN cant;
END$$

CREATE PROCEDURE cancelar_turnos_medico_rango(
    IN p_id_medico INT,
    IN p_fecha_desde DATE,
    IN p_fecha_hasta DATE
)
BEGIN
    UPDATE turno
       SET estado = 'CANCELADO'
     WHERE id_medico = p_id_medico
       AND fecha BETWEEN p_fecha_desde AND p_fecha_hasta
       AND estado = 'PROGRAMADO';
END$$

-- reporte de los tres médicos con más turnos
CREATE PROCEDURE top3_medicos_mas_turnos()
BEGIN
    SELECT m.id_medico,
           m.nombre,
           m.apellido,
           m.especialidad,
           COUNT(t.id_turno) AS cantidad_turnos
      FROM medico m
      JOIN turno t ON t.id_medico = m.id_medico
     GROUP BY m.id_medico, m.nombre, m.apellido, m.especialidad
     ORDER BY cantidad_turnos DESC
     LIMIT 3;
END$$

DELIMITER ;