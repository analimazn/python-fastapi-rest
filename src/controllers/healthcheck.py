from fastapi_health import health
from src.services.healthcheck import healthcheck_service

def healthcheck_controller():
    return health([healthcheck_service])