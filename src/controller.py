from fastapi_health import health
from src.service import is_app_online

def healthcheck():
    return health([is_app_online])
