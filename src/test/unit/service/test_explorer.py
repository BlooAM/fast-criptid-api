import os
os.environ['CRYPTID_UNIT_TEST'] = "true"
import pytest

from model.explorer import Explorer
from service import explorer as data
from errors import Missing, Duplicate


@pytest.fixture
def sample() -> Explorer:
    return Explorer(name='Claude Hande', country='FR', description='Rare, during full moon')


def test_create(sample):
    sample.name = 'AnotherExplorer'
    resp = data.create(sample)
    assert resp == sample


def test_create_dupplicate(sample):
    with pytest.raises(Duplicate):
        _ = data.create(sample)


def test_get_exists(sample):
    resp = data.get_one(sample.name)
    assert resp == sample


def test_get_missing():
    with pytest.raises(Missing):
        _ = data.get_one('boxturtle')


def test_modify(sample):
    name = 'CA'
    resp = data.modify(name, sample)
    sample.name = name
    assert resp == sample


def test_modify_missing():
    edd: Explorer = Explorer(name='edd', country='US', description='desc')
    with pytest.raises(Missing):
        _ = data.modify(edd.name, edd)
