from .init import curs
from model.creature import Creature

curs.execute("""
    create table if not exists creature(
    name text primary key, 
    description text, 
    country text, 
    area text, 
    aka text
    )
""")


def row_to_model(row: tuple) -> Creature:
    name, description, country, area, aka = row
    return Creature(name=name, description=description, country=country, area=area, aka=aka)


def model_to_dict(creature: Creature) -> dict | None:
    return creature.dict() if creature else None


def get_one(name: str) -> Creature:
    query = 'select * from creature where name=:name'
    params = {'name': name}
    curs.execute(query, params)
    row = curs.fetchone()
    return row_to_model(row)


def get_all() -> list[Creature]:
    query = "select * from creature"
    curs.execute(query)
    rows = list(curs.fetchall())
    return [row_to_model(row) for row in rows]


def create(creature: Creature) -> Creature:
    query = """
        insert into creature values
        (:name, :description, :country, :area, :aka)
    """
    params = model_to_dict(creature)
    curs.execute(query, params)
    return get_one(creature.name)


def modify(creature: Creature) -> Creature:
    query = """
        update creature
        set country=:country,
            name=:name,
            description=:description,
            area=:area,
            aka=:aka
        where name=:name_orig
    """
    params = model_to_dict(creature)
    params["name_orig"] = creature.name
    _ = curs.execute(query, params)
    return get_one(creature.name)


def delete(creature: Creature) -> bool:
    query = 'delete from creature where name=:name'
    params = {'name': creature.name}
    res = curs.execute(query, params)
    return bool(res)
