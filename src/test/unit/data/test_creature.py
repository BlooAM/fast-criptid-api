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
