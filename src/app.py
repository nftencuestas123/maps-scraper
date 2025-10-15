from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Desarrollado Por Richard Almiron!"}
