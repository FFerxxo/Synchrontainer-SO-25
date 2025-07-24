# Synchrontainer – Sistemas Operativos 2025

Proyecto Final de orquestación de contenedores Sistemas Operativos: tres instancias FastAPI que
comparten un volumen para sincronizar archivos públicos y almacenan
archivos privados por usuario.

---

## Requisitos

* Docker Desktop con WSL 2  
* Git  

---

## Puesta en marcha

```bash
git clone https://github.com/FFerxxo/Synchrontainer-SO-25.git
cd Synchrontainer-SO-25
docker compose up -d --build      

---

## Puertos y contenedores

| Contenedor | Puerto | Descripción            |
|------------|--------|------------------------|
| synchro1   | 8001   | Instancia FastAPI 1    |
| synchro2   | 8002   | Instancia FastAPI 2    |
| synchro3   | 8003   | Instancia FastAPI 3    |

## Endpoints principales

| Método | Ruta                                   | Descripción                          |
|--------|----------------------------------------|--------------------------------------|
| POST   | `/upload/{uid}/{filename}`             | Sube archivo público o privado       |
| GET    | `/public/`                             | Lista de archivos públicos           |
| GET    | `/storage/{uid}`                       | Lista de archivos privados del UID   |
| GET    | `/download/{filename}`                 | Descarga archivo público             |

## Estructura del proyecto
.
├─ app/                 # Código FastAPI
│  ├─ main.py
│  └─ sync_files/…      # Volumen compartido 
├─ docker/
│  ├─ Dockerfile
│  ├─ entrypoint.sh
│  └─ seed.sh           # Genera archivos demo
├─ docs/
│  ├─ samples/          # seed_example.txt
│  
├─ docker-compose.yml
└─ README.md


## Autores

| Nombre                        | Correo institucional                |
|-------------------------------|-------------------------------------|
| Andrés Barbosa                | andres.barbosa@correounivalle.edu.co |
| Yoselin Cardona               | yoselin.serna@correounivalle.edu.co  |
| Angie Valencia                | angiequenan@correounivalle.edu.co    |
| David Bravo                   | bravo.david@correounivalle.edu.co    |



