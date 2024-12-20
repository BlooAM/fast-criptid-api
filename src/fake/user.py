from model.user import User
from errors import Missing, Duplicate


fakes = [
    User(name="kwijobo", hash="abc"),
    User(name="ermagerd", hash="xyz"),
]


def find(name: str) -> User | None:
    for e in fakes:
        if e.name == name:
            return e
    return None


def check_missing(name: str):
    if not find(name):
        raise Missing(msg=f'User {name} not found')


def check_duplicate(name: str):
    if find(name):
        raise Duplicate(msg=f'User {name} already exists')


def get_all() -> list[User]:
    return fakes


def get_one(name: str) -> User:
    check_missing(name)
    return find(name)


def create(user: User) -> User:
    check_duplicate(user.name)
    return user


def modify(name: str, user: User) -> User:
    check_missing(name)
    return user


def delete(name: str) -> None:
    check_missing(name)
    return None
