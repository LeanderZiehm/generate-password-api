from fastapi import FastAPI, Query
from pydantic import BaseModel
import secrets
import string

app = FastAPI()

SPECIAL_CHARS = "+_*&^%$#@!="
CHAR_POOL = string.ascii_letters + string.digits + SPECIAL_CHARS

@app.get("/generate-password")
def generate_password(length: int = Query(12, gt=4, le=128)):
    password = ''.join(secrets.choice(CHAR_POOL) for _ in range(length))
    return {"password": password}