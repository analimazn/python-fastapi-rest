from fastapi import FastAPI

from src.controller import healthcheck

app = FastAPI()

app.add_api_route("/healthcheck", healthcheck())