from fastapi import HTTPException
import pytest
import os

os.environ['CRYPTID_UNIT_TEST'] = "true"
from model.explorer import Explorer
from web import explorer


@pytest.fixture
def sample() -> Explorer:
    return Explorer(
        name='eddie',
        country='*',
        description='Ed! Edd! Eddie!',
    )


@pytest.fixture
def fakes() -> list[Explorer]:
    return explorer.get_all()


def assert_duplicate(exc):
    print(exc)
    assert exc.value.status_code == 409
    assert 'not found' in exc.value.msg


def assert_missing(exc):
    assert exc.value.status_code == 404
    assert 'already exists' in exc.value.msg


def test_create(sample):
    assert explorer.create(sample) == sample


def test_create_duplicate(fakes):
    with pytest.raises(HTTPException) as e:
        _ = explorer.create(fakes[0])
        assert_duplicate(e)


def test_get_one(fakes):
    assert explorer.get_one(fakes[0].name) == fakes[0]


def test_get_one_missing():
    with pytest.raises(HTTPException) as e:
        _ = explorer.get_one('missingforsure')
        assert_missing(e)


def test_modify(fakes):
    assert explorer.modify(fakes[0].name, fakes[0]) == fakes[0]


def test_modify_missing(sample):
    with pytest.raises(HTTPException) as e:
        _ = explorer.modify(sample.name, sample)
        assert_missing(e)


def test_delete(fakes):
    assert explorer.delete(fakes[0].name) is None


def test_delete_missing(sample):
    with pytest.raises(HTTPException) as e:
        _ = explorer.delete('missingforsure')
        assert_missing(e)
