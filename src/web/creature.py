import os

from fastapi import APIRouter, HTTPException

from model.creature import Creature
if os.getenv('CRYPTID_UNIT_TEST'):
    from fake import creature as service
else:
    from service import creature as service
from errors import Missing, Duplicate

router = APIRouter(prefix='/creature')


@router.get('/')
def get_all() -> list[Creature]:
    return service.get_all()


@router.get('/{name}')
def get_one(name) -> Creature:
    try:
        return service.get_one(name)
    except Missing as e:
        raise HTTPException(status_code=404, detail=e.msg)


@router.post('/', status_code=201)
def create(creature: Creature) -> Creature:
    try:
        return service.create(creature)
    except Duplicate as e:
        raise HTTPException(status_code=409, detail=e.msg)


@router.patch('/')
def modify(name: str, creature: Creature) -> Creature:
    try:
        return service.modify(name, creature)
    except Missing as e:
        raise HTTPException(status_code=404, detail=e.msg)


@router.delete('/{name}', status_code=204)
def delete(name: str) -> None:
    try:
        return service.delete(name)
    except Missing as e:
        raise HTTPException(status_code=404, detail=e.msg)
