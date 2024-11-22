from model.creature import Creature
from errors import Missing, Duplicate


_creatures = [
    Creature(name='Yeti', aka='Abominable Snowman', country='CN', area='Himalayas', description='Hirsute Himalayan'),
    Creature(name='Bigfoot', aka='Sasquatch', country='US', area='*', description='Yeti`s cousin Eddie'),
]


def get_all() -> list[Creature]:
    return _creatures


def get_one(name: str) -> Creature | None:
    for _creature in _creatures:
        if _creature.name == name:
            return _creature
    raise Missing(msg=f'Creature {name} not found')


def create(creature: Creature) -> Creature:
    if creature in _creatures:
        raise Duplicate(msg=f'Creature {creature.name} already exists')
    return creature


def modify(name: str, creature: Creature) -> Creature:
    if creature not in _creatures:
        raise Missing(msg=f'Creature {name} not found')
    return creature


def delete(name: str) -> None:
    if name not in [creature.name for creature in _creatures]:
        raise Missing(msg=f'Creature {name} not found')
