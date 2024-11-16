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


@router.post('/token')
async def create_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = service.auth_user(form_data.username, form_data.password)
    if not user:
        unauthed()
    expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = service.create_access_token(data={'sub': user.username}, expires=expires)
    return {'access_token': access_token, 'token_type': 'bearer'}


@router.get('/token')
def get_access_token(token: str = Depends(oauth2_dep)) -> dict:
    return {'token': token}


