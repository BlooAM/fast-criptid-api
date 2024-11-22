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
    print(exc)
    assert exc.value.status_code == 409
    assert 'not found' in exc.value.msg


def assert_missing(exc):
    assert exc.value.status_code == 404
    assert 'already exists' in exc.value.msg


def test_create(sample):
    assert creature.create(sample) == sample


def test_create_duplicate(fakes):
    with pytest.raises(HTTPException) as e:
        _ = creature.create(fakes[0])
        assert_duplicate(e)


def test_get_one(fakes):
    assert creature.get_one(fakes[0].name) == fakes[0]


def test_get_one_missing():
    with pytest.raises(HTTPException) as e:
        _ = creature.get_one('bobcat')
        assert_missing(e)


def test_modify(fakes):
    assert creature.modify(fakes[0].name, fakes[0]) == fakes[0]


def test_modify_missing(sample):
    with pytest.raises(HTTPException) as e:
        _ = creature.modify(sample.name, sample)
        assert_missing(e)


def test_delete(fakes):
    assert creature.delete(fakes[0].name) is None


def test_delete_missing(sample):
    with pytest.raises(HTTPException) as e:
        _ = creature.delete('emu')
        assert_missing(e)
