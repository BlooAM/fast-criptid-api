from model.user import User
from .init import (curs, IntegrityError)
from errors import Missing, Duplicate


curs.execute("""
    create table if not exists user(
        name text primary key,
        hash text
    )
""")

curs.execute("""
    create table if not exists xuser(
        name text primary key,
        hash text
    )
""")


def row_to_model(row: tuple) -> User:
    name, hash = row
    return User(name=name, hash=hash)


def model_to_dict(user: User) -> User:
    return user.dict()