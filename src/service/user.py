from datetime import datetime, timedelta
import os
from jose import jwt
from model.user import User
from passlib.context import CryptContext

if os.getenv('CRYPTID_UNIT_TEST'):
    from fake import user as data
else:
    from data import user as data

SECRET_KEY = 'keep-it-secret-keep-it-safe'
ALGORITHM = 'HS256'
pwd_context = CryptContext(schemes=['bscrypt'], deprecated='auto')


def verify_password(plain: str, hash: str) -> bool:
    return pwd_context.verify(plain, hash)


def get_hah(plain: str) -> str:
    return pwd_context.hash(plain)


def get_jwt_username(token: str) -> str | None:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        if not (username := payload.get('sub')):
            return None
    except jwt.JWTError:
        return None
    return username
