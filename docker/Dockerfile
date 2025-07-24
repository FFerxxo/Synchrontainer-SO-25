FROM python:3.11-slim

ENV APP_HOME=/usr/src/app
WORKDIR $APP_HOME

# Dependencias
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Código
COPY app/ ./app

# Script de seeding (queda en /usr/src/app/docker/seed.sh)
COPY docker/seed.sh ./docker/seed.sh

# Cambiamos al directorio del código
WORKDIR $APP_HOME/app

# Carpetas de sincronización
RUN mkdir -p sync_files/public sync_files/private

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
