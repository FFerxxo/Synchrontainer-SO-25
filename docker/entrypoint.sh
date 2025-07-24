#!/bin/bash
set -e
echo "Inicializando archivos de ejemplo..."
echo "Hola mundo" > app/sync_files/public/hello.txt
exec "$@"
