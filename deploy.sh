#!/bin/sh
# Publica web.agdesign.agency (campaña) y agdesign.agency (sitio principal). Lo corre el cron del VPS despues de git pull.
# Uso: sh ~/agd-web/deploy.sh   (por defecto /home/agdesign/public_html/web)
set -e
DEST="${1:-/home/agdesign/public_html/web}"
cd "$(dirname "$0")"
mkdir -p "$DEST"
OWNER=$(stat -c %U:%G "$DEST")
for f in *; do
  case "$f" in deploy.sh|README.md|sitio|tools) continue ;; esac
  cp -a "$f" "$DEST/"
  chown -R "$OWNER" "$DEST/$f"
done
# Sitio principal: solo si ya se quitó el WordPress (existe el marcador .agd-sitio-ok)
MAIN=/home/agdesign/public_html/agdesign.agency
if [ -f "$MAIN/.agd-sitio-ok" ]; then
  MO=$(stat -c %U:%G "$MAIN")
  cp -a sitio/. "$MAIN/"
  chown -R "$MO" "$MAIN/index.html" "$MAIN/img" "$MAIN/aviso-de-privacidad"
fi
