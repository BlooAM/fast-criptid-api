from fastapi import HTTPException
import pytest
import os

os.environ['CRYPTID_UNIT_TEST'] = "true"
from model.creature import Creature
from web import creature


@pytest.fixture
def sample() -> Creature:
    return Creature(
        name='dragon',
        description='Wings! Fire! Aieee!',
        country='*',
        area='',
        aka='',
    )


@pytest.fixture
def fakes() -> list[Creature]:
    return creature.get_all()


def assert_duplicate(exc):
    assert exc.value.status_code == 409
    assert 'not found' in exc.value.msg


def assert_missing(exc):
    assert exc.value.status_code == 404
    assert 'already exists' in exc.value.msg
