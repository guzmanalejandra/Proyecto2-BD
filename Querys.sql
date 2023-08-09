-- Ejercicio 1

SELECT *
FROM genero, informacionsesion
WHERE fecha BETWEEN '30/3/2022' AND date(now());
GROUP BY genero, hora asc LIMIT 10

-- Ejercicio 2

SELECT *
FROM genero, cuenta, informacionsesion, peliculacapitulo, peliculaserie
WHERE fecha BETWEEN '30/3/2022' AND date(now())
ORDER BY categoria, genero, tipo_cuenta, hora asc
        
-- Ejercicio 3


SELECT *
(SELECT MAX("hora" as "Mas visto" from informacionsesion where "cuenta" = "cuenta"))
FROM actor, peliculaserie, peliculacapitulo, cuenta, informacionsesion
WHERE fecha BETWEEN '30/3/2022' AND date(now());

--ejercicio 4
SELECT *
FROM registrologin, cuenta
WHERE fecha BETWEEN '18/10/2022' AND date(now());
Select(tipo_cuenta) as freemiumOnly from cuenta where tipodecuenta = 'premium'
