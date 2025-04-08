
pip install -r requirements.txt

uvicorn main:app --reload


http://127.0.0.1:8000/generate-password

curl http://127.0.0.1:8000/generate-password


curl "http://127.0.0.1:8000/generate-password?length=20"
