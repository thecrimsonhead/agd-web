#!/bin/sh
# Publica la landing en web.agdesign.agency. Lo corre el cron del VPS despues de git pull.
# Uso: sh ~/agd-web/deploy.sh   (por defecto /home/agdesign/public_html/web.agdesign.agency)
set -e
DEST="${1:-/home/agdesign/public_html/web.agdesign.agency}"
cd "$(dirname "$0")"
mkdir -p "$DEST"
OWNER=$(stat -c %U:%G "$DEST")
for f in *; do
  case "$f" in deploy.sh|README.md) continue ;; esac
  cp -a "$f" "$DEST/"
  chown -R "$OWNER" "$DEST/$f"
done
