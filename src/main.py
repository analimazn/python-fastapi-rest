from fastapi import FastAPI

from src.controllers.healthcheck import healthcheck_controller
from src.controllers.home import home_controller

app = FastAPI()

app.add_api_route('/healthcheck', healthcheck_controller())

@app.get('/')
def route_home():
  return home_controller()