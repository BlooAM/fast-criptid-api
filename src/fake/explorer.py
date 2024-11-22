from model.explorer import Explorer
from errors import Missing, Duplicate


_explorers = [
    Explorer(name='Claude Hande', country='FR', description='Rare, during full moon'),
    Explorer(name='Noah Weiser', country='DE', description='Short-sighted men with machete'),
]


def get_all() -> list[Explorer]:
    return _explorers


def get_one(name: str) -> Explorer | None:
    for _explorer in _explorers:
        if _explorer.name == name:
            return _explorer
    raise Missing(msg=f'Explorer {name} not found')


def create(explorer: Explorer) -> Explorer:
    if explorer in _explorers:
        raise Duplicate(msg=f'Explorer {explorer.name} already exists')
    return explorer


def modify(name: str, explorer: Explorer) -> Explorer:
    if explorer not in _explorers:
        raise Missing(msg=f'Explorer {name} not found')
    return explorer


def delete(name: str) -> None:
    if name not in [explorer.name for explorer in _explorers]:
        raise Missing(msg=f'Explorer {name} not found')
