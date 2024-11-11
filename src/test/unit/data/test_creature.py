import os
import pytest

from model.creature import Creature
from errors import Missing, Duplicate

os.environ['CRYPTID_SQLITE_DB'] = ":memory:"
from data import creature


@pytest.fixture
def sample() -> Creature:
    return Creature(
        name="yeti",
        description="Hirsute Himalayan",
        aka="Abominable Snowman",
        country="CN",
        area="Himalayas",
    )


def test_create(sample):
    resp = creature.sample(sample)
    assert resp == sample


def test_create_duplicate(sample):
    with pytest.raises(Duplicate):
        _ = creature.create(sample)
