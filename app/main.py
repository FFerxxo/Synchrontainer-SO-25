from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from pathlib import Path
import shutil

BASE     = Path(__file__).parent / "sync_files"
PUBLIC   = BASE / "public"
PRIVATE  = BASE / "private"

app = FastAPI(title="Synchrontainer API")

@app.get("/storage/{uid}")
def list_private(uid: str):
    target = PRIVATE / uid
    if not target.exists():
        raise HTTPException(404, "Carpeta privada no existe")
    return {"files": [p.name for p in target.iterdir() if p.is_file()]}

@app.get("/public/")
def list_public():
    return {"files": [p.name for p in PUBLIC.iterdir() if p.is_file()]}

@app.get("/download/{filename}")
def download_file(filename: str):
    path = PUBLIC / filename
    if not path.exists():
        raise HTTPException(404, "No encontrado")
    return FileResponse(path)

@app.post("/upload/{uid}/{filename}")
async def upload_file(uid: str, filename: str, file: UploadFile = File(...)):
    dest_dir = PRIVATE / uid
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / filename
    with dest.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"msg": "Subido", "path": str(dest)}


@app.get("/download/{filename}")
async def download_file(filename: str):
    file_path = PUBLIC / filename
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="Archivo no encontrado")
    return FileResponse(file_path, filename=filename)
