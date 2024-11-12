from .init import curs, IntegrityError
from model.creature import Creature
from errors import Missing, Duplicate

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
    name, country, area, description, aka = row
    return Creature(name=name, country=country, area=area, description=description, aka=aka)


def model_to_dict(creature: Creature) -> dict | None:
    return creature.dict() if creature else None


def get_one(name: str) -> Creature:
    query = 'select * from creature where name=:name'
    params = {'name': name}
    curs.execute(query, params)
    row = curs.fetchone()
    if row:
        return row_to_model(row)
    else:
        raise Missing(msg=f'Creature {name} not found')


def get_all() -> list[Creature]:
    query = "select * from creature"
    curs.execute(query)
    rows = list(curs.fetchall())
    return [row_to_model(row) for row in rows]


def create(creature: Creature) -> Creature:
    if not creature:
        return None

    query = """
        insert into creature (name, country, description, area, aka) 
        values (:name, :country, :description, :area, :aka)
    """
    params = model_to_dict(creature)
    try:
        curs.execute(query, params)
    except IntegrityError:
        raise Duplicate(msg=f'Creature {creature.name} already exists')
    return get_one(creature.name)


def modify(name: str, creature: Creature) -> Creature:
    if not (name and creature):
        return None

    query = """
        update creature
        set country=:country,
            name=:name,
            description=:description
            area=:area
            aka=:ala
        where name=:name_orig
    """
    params = model_to_dict(creature)
    params["name_orig"] = creature.name
    curs.execute(query, params)
    if curs.rowcount == 1:
        return get_one(creature.name)
    else:
        raise Missing(msg=f'Creature {name} not found')


def delete(name: str) -> bool:
    if not name:
        return None

    query = 'delete from creature where name=:name'
    params = {'name': name}
    curs.execute(query, params)
    if curs.rowcount != 1:
        raise Missing(msg=f'Creature {name} not found')
