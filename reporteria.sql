SELECT t.idpeliculacapitulo,peliculacapitulo.titulo,count(t.idpeliculacapitulo) as cantidad,date_trunc('hour', t.hora) from informacionsesion t
join peliculacapitulo
on t.idpeliculacapitulo = peliculacapitulo.id
where t.fecha > '2022/3/31' AND t.fecha < '2022/5/01' AND date_trunc('hour', t.hora)>'09:00:00' AND date_trunc('hour', t.hora)<'13:00:00'
group by  date_trunc('hour', t.hora),t.idpeliculacapitulo, peliculacapitulo.titulo
order by date_trunc('hour', t.hora),count(t.idpeliculacapitulo) desc

select infoadmin.id_admin,cuenta.correo,count(infoadmin.id_admin)
from infoadmin
join cuenta on infoadmin.id_admin = cuenta.id
group by infoadmin.id_admin, cuenta.correo
order by count(infoadmin.id_admin) desc
LIMIT 5