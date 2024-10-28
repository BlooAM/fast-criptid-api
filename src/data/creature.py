import sqlite3

from model.creature import Creature

DB_NAME = 'criptid.db'
conn = sqlite3.connect(DB_NAME)
curs = conn.cursor()


def init():
    curs.execute('create table creature(name, description, country, area, aka)')


def row_to_model(row: tuple) -> Creature:
    name, description, country, area, aka = row
    return Creature(name, description, country, area, aka)


def model_to_dict(creature: Creature) -> dict:
    return creature.dict()


def get_one(name: str) -> Creature:
    query = 'select * from creature where name=:name'
    params = {'name': name}
    curs.execute(query, params)
    row = curs.fetchone()
    return row_to_model(row)


def get_all(name: str) -> list[Creature]:
    query = "select * from creature"
    curs.execute(query)
    rows = list(curs.fetchall())
    return [row_to_model(row) for row in rows]


def create(creature: Creature):
    query = """
        insert into creature values
        (:name, :description, :country, :area, :aka)
    """
    params = model_to_dict(creature)
    curs.execute(query, params)


def modify(creature: Creature):
    return creature


def replace(creature: Creature):
    return creature


def delete(creature: Creature):
    query = 'delete from creature where name=:name'
    params = {'name': creature.name}
    curs.execute(query, params)
