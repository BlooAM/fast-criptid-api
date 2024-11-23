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
        country="CN",
        area="Himalayas",
        aka="Abominable Snowman",
    )


def test_create(sample):
    resp = creature.create(sample)
    assert resp == sample


def test_create_duplicate(sample):
    with pytest.raises(Duplicate):
        _ = creature.create(sample)


def test_get_one(sample):
    resp = creature.get_one(sample.name)
    assert resp == sample


def test_get_missing():
    with pytest.raises(Missing):
        _ = creature.get_one("nonexisting")


def test_modify(sample):
    sample.country = "GL"
    resp = creature.modify(sample.name, sample)
    assert resp == sample


def test_modify_missing():
    bob: Creature = Creature(
        name="bob",
        description="some guy",
        country="ZZ",
        area="nowhere",
        aka="nobody",
    )
    with pytest.raises(Missing):
        _ = creature.modify(bob.name, bob)


def test_delete(sample):
    resp = creature.delete(sample.name)
    assert resp is None


def test_delete_missing(sample):
    with pytest.raises(Missing):
        _ = creature.delete(sample.name)
