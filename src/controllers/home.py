from fastapi import FastAPI
from src.services.home import home_service

app = FastAPI()

@app.get("/")
def home_controller():
  return home_service()