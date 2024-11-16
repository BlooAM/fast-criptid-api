from datetime import timedelta
import os
from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from model.user import User
from errors import Missing, Duplicate
if os.getenv('CRYPTID_UNIT_TEST'):
    from fake import user as service
else:
    from service import user as service

ACCESS_TOKEN_EXPIRE_MINUTES = 30

router = APIRouter(prefix='/user')

oauth2_dep = OAuth2PasswordBearer(tokenUrl='token')


def unauthed():
    raise HTTPException(
        status_code=401,
        detail='Invalid user or password',
        headers={'WWW-Authenticate': 'Bearer'},
    )


@router.post
async def create_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = service.auth_user(form_data.username, form_data.password)