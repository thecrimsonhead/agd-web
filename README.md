# agd-web

Landing de AGDesign en web.agdesign.agency (página web en 72 horas por $3,500 MXN).

El VPS tiene una deploy key de solo lectura y un cron que cada 5 minutos hace `git pull` y corre `deploy.sh`, que copia todo (menos deploy.sh y README) a la carpeta del subdominio.
