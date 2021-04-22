from fastapi import Depends

def get_session():
    return True

def is_app_online(session: bool = Depends(get_session)):
    return session