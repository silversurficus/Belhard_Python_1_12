from db_connect import get_session
from film_zone import Genres


with get_session() as db_session:
    new_genre_1 = Genres(
        id=100,
        name='Post-ap'
    )
    new_genre_2 = Genres(
        id=200,
        name='Post-ap'
    )
    db_session.add(new_genre_1)
    db_session.add(new_genre_2)
    db_session.commit()
    result = db_session.query(Genres).all()
    for genre_obj in result:
        print(genre_obj.id)
    x_1 = db_session.query(Genres).get(100)
    x_2 = db_session.query(Genres).get(200)
    db_session.delete(x_2)
    db_session.delete(x_1)
    db_session.commit()

    result = db_session.query(Genres).filter(Genres.id == 'WESTERN')
    for row in result:
        print("ID:", row.id, "Name: ", row.name)
    x = db_session.query(Genres).get('WESTERN')
    x.name = 'Eastern'
    db_session.commit()
    print("ID:", x.id, "Name: ", x.name)