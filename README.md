# agd-web

Campaña de AGDesign en web.agdesign.agency (página web en 72 horas por $3,990 MXN, o 12 MSI $4,950).

- `index.html`: landing (misma estructura que tcstudio.store/es, con identidad AGD). Se genera con `python3 ~/tcstudio-web/tools/agd_landing.py`; no editar a mano.
- `demo/<giro>/`: 12 demos por giro. Se generan con `MARCA=agd python3 ~/tcstudio-web/tools/gen.py`.
- `pagar/`: solo el pago (Mercado Pago, contado o 12 MSI, factura opcional; webhook n8n `agd-pago`). Todos los botones de la landing y de las demos llevan aquí.

- `sitio/`: agdesign.agency (servicios con pago en Stripe). Se genera con `python3 tools/sitio.py`. Se publica solo si existe `/home/agdesign/public_html/agdesign.agency/.agd-sitio-ok`.

El VPS tiene una deploy key de solo lectura y un cron que cada 5 minutos hace `git pull` y corre `deploy.sh`, que copia todo (menos deploy.sh y README) a la carpeta del subdominio.
