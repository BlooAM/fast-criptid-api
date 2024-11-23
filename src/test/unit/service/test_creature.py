import os
os.environ['CRYPTID_UNIT_TEST'] = "true"
import pytest

from model.creature import Creature
from service import creature as data
from errors import Missing, Duplicate


@pytest.fixture
def sample() -> Creature:
    return Creature(
        name='Yeti',
        aka='Abominable Snowman',
        country='CN',
        area='Himalayas',
        description='Hirsute Himalayan',
    )


def test_create(sample):
    sample.name = 'AnotherYeti'
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
    bob: Creature = Creature(name='bob', country='US', area='*', description='desc', aka='??')
    with pytest.raises(Missing):
        _ = data.modify(bob.name, bob)
