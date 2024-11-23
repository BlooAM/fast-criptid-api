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
        country='CN',
        area='Himalayas',
        description='Hirsute Himalayan',
        aka='Abominable Snowman',
    )


def test_create(sample):
    sample.name = 'AnotherYeti'
    resp = data.create(sample)
    assert resp == sample


def test_create_dupplicate():
    with pytest.raises(Duplicate):
        resp = data.create(sample)
