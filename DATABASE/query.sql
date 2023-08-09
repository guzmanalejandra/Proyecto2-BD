SELECT usuarios.nombre as fan, minuto, titulo as pelicula, actor.nombre as actor
from usuarios, viendoactualmente, peliculaserie, actor
order by minuto asc