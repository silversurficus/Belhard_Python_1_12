from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float

Base = declarative_base()


class Persons(Base):

    __tablename__ = 'persons'

    id = Column(Integer(), nullable=False, primary_key=True)
    name = Column(String(100), nullable=False)
    surname = Column(String(100), nullable=False)
    birth_date = Column(DateTime, nullable=False)


class User_types(Base):

    __tablename__ = 'User_types'

    id = Column(String(100), nullable=False, primary_key=True)
    name = Column(String(100), nullable=False)


class Users(Base):

    __tablename__ = 'users'

    login = Column(String(100), nullable=False, primary_key=True)
    password = Column(String(100), nullable=False)
    user_type_id = Column(String(100), ForeignKey(User_types.id), nullable=False)
    person_id = Column(Integer(), ForeignKey(Persons.id), nullable=False)


class Emails(Base):

    __tablename__ = 'emails'

    id = Column(Integer(), nullable=False, primary_key=True)
    email = Column(String(100), nullable=False)
    user_login = Column(String(100), ForeignKey(Users.login), nullable=False)


class Genres(Base):

    __tablename__ = 'genres'

    id = Column(String(100), nullable=False, primary_key=True)
    name = Column(String(100), nullable=False)


class Films(Base):

    __tablename__ = 'films'

    id = Column(Integer(), nullable=False, primary_key=True)
    duration = Column(Integer(), nullable=False)
    name = Column(String(100), nullable=False)
    release_date = Column(DateTime, nullable=False)
    rating = Column(Float, nullable=False)
    director_id = Column(Integer(), ForeignKey(Persons.id), nullable=False)


class User_favourite_films(Base):

    __tablename__ = 'user_favourite_films'

    user_login = Column(String(), ForeignKey("users.login", ondelete="CASCADE"), nullable=False, primary_key=True)
    film_id = Column(Integer(), ForeignKey("films.id", ondelete="CASCADE"), nullable=False, primary_key=True)



class Films_genres(Base):

    __tablename__ = 'films_genres'

    film_genre_id = Column(String(), ForeignKey("genres.id", ondelete="CASCADE"), nullable=False, primary_key=True)
    film_id = Column(Integer(), ForeignKey("films.id", ondelete="CASCADE"), nullable=False, primary_key=True)




class Characters(Base):

    __tablename__ = 'characters'

    id = Column(Integer(), nullable=False, primary_key=True)
    name = Column(String(100), nullable=False)
    comment = Column(String(100))
    film_id = Column(Integer(), ForeignKey(Films.id), nullable=False)


class Characters_actors(Base):

    __tablename__ = 'characters_actors'

    character_id = Column(Integer(), ForeignKey("characters.id", ondelete="CASCADE"), nullable=False, primary_key=True)
    person_id = Column(Integer(), ForeignKey("persons.id", ondelete="CASCADE"), nullable=False, primary_key=True)





