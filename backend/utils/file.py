import uuid, os, shutil

UPLOAD_DIR = "uploads"

def save_upload(file):
    if not file:
        return None

    ext = file.filename.split(".")[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    full_path = os.path.join(UPLOAD_DIR, filename)

    with open(full_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return f"/uploads/{filename}"