from fastapi import Depends

def get_session():
    return True

def healthcheck_service(session: bool = Depends(get_session)):
    return session