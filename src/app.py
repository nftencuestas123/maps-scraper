from fastapi import FastAPI, Response
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API activa"}

@app.get("/download-csv")
def download_csv():
    csv_path = "results.csv"
    if not os.path.exists(csv_path):
        return Response("No existe el archivo", status_code=404)
    with open(csv_path, "rb") as f:
        content = f.read()
    return Response(content, media_type="text/csv")
