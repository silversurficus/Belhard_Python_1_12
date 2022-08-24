# Занятие 12. Работа с РСУБД. SQL. SQLAlchemy

## SQL

Необходимо составить ```init_schema.sql``` файл, который будет создавать
базу данных ```film_zone``` со следующей структурой.

Описать следующие таблицы:

**persons** - таблица "человек"

* id [```NOT NULL```, ```INT```, ```PRIMARY KEY```, ```AUTOINCREMENT```] - уникальный идентификатор человека
* name [```NOT NULL```, ```VARCHAR```] - имя человека
* surname [```NOT NULL```, ```VARCHAR```] - фамилия человека
* birth_date [```NOT NULL```, ```DATETIME```] - дата рождения человека

**user_types** - таблица "типы пользователей"

* id [```NOT NULL```, ```VARCHAR```, ```PRIMARY KEY```] - уникальный идентификатор типа пользователя
* name [```NOT NULL```, ```VARCHAR```] - название типа пользователя

Вставить в таблицу ```user_types``` следующие значения:

* USER - User 
* ADMIN - Administrator

**users** - таблица "пользователи"

* login [```NOT NULL```, ```VARCHAR```, ```PRIMARY KEY```] - логин пользователя
* password [```NOT NULL```, ```VARCHAR```] - пароль пользователя
* user_type_id [```NOT NULL```, ```VARCHAR```, ```REFERENCES user_types(id)```] - тип пользователя
* person_id [```NOT NULL```, ```INT```, ```REFERENCES persons(id)```] - данные пользователя

**emails** - таблица "emailы пользователей"

* id [```NOT NULL```, ```INT```, ```PRIMARY KEY```, ```AUTOINCREMENT```] - уникальный идентификатор email
* email ```[NOT NULL```, ```VARCHAR```] - email пользователя
* user_login [```NOT NULL```, ```VARCHAR```, ```REFERENCES users(login)```] - логин пользователя

**genres** - таблица "жанры фильмов"

* id [```NOT NULL```, ```VARCHAR```, ```PRIMARY KEY```] - уникальный идентификатор жанра фильма
* name [```NOT NULL```, ```VARCHAR```] - название жанра фильма

Вставить в таблицу ```genres``` следующие значения:

* ACTION - Action 
* ADVENTURE - Adventure 
* COMEDY - Comedy
* DRAMA - Drama
* CRIME - Crime
* SCI_FI - sci-fi  
* FANTASY - fantasy
* MUSICAL - Musical 
* WESTERN - Western  
* POST_APOCALYPTIC - Post-apocalyptic  
* WAR - War 
* FAMILY - Family film 
* LOVE - Love story
* CARTOON - Cartoon
* HORROR - Horror 
* THRILLER - Thriller  
* DOCUMENTARY - Documentary

**films** - таблица "фильмы""

* id [```NOT NULL```, ```INT```, ```PRIMARY KEY```, ```AUTOINCREMENT```] - уникальный идентификатор фильма
* duration [```NOT NULL```, ```INT```] - длительность фильма в секундах
* name [```NOT NULL```, ```VARCHAR```] - название фильма
* release_date [```NOT NULL```, ```DATETIME```] - дата выхода
* rating [```NOT NULL```, ```FLOAT```] - рейтинг фильма
* director_id [```NOT NULL```, ```INT```, ```REFERENCES persons(id)```] - режиссер фильма

**user_favorite_films** - MM связь "любимые фильмы пользователя"

* user_login [```NOT NULL```, ```VARCHAR```, ```REFERENCES users(login)```] - логин пользователя
* film_id [```NOT NULL```, ```INT```, ```REFERENCES films(id)```] - id фильма

**films_genres** - MM связь "жанры фильмов"

* film_id [```NOT NULL```, ```INT```, ```REFERENCES films(id)```] - id фильма
* film_genre_id [```NOT NULL```, ```VARCHAR```, ```REFERENCES genres(id)```] - id жанра

**characters** - таблица "персонажи фильмов"
 
* id [```NOT NULL```, ```INT```, ```PRIMARY KEY```, ```AUTOINCREMENT```] - уникальный идентификатор персонажа
* name [```NOT NULL```, ```VARCHAR```] - имя персонажа
* comment [```VARCHAR```] - комментарий
* film_id [```NOT NULL```, ```INT```, ```REFERENCES films(id)```] - id фильма

**characters_actors** - MM связь "актеры, играющие персонажей"

* character_id [```NOT NULL```, ```INT```, ```REFERENCES characters(id)```] - id персонажа
* person_id [```NOT NULL```, ```INT```, ```REFERENCES persons(id)```] - id человека


***

Полученная схема должна выглядеть следующим образом:

![Database schema](schema.png)

## SQLAlchemy

1. Создать пакет ```db```.
2. Создать модуль ```base.by```:

    ```python
    from sqlalchemy.ext.declarative import declarative_base
    
    Base = declarative_base()
    ```

3. Создать модуль ```session.by```:

    ```python
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from contextlib import contextmanager
    
    
    engine = create_engine(
        'mysql+pymysql://user:password@localhost:3306/database',
        pool_pre_ping=True,
        pool_recycle=3600,
    )
    Session = sessionmaker(bind=engine)
    
    
    @contextmanager
    def session_scope():
        session = Session()
        try:
            yield session
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()
    ```

4. Создать в пакете ```db``` пакет ```tables```.
5. В пакете ```tables``` описать таблицы из задания по SQL
6. Сделать файл ```__init__.py``` в пакете ```db``` и в пакете ```tables```и описать в нем инструкции импорта пакета.
7. Сделать в корне модуль ```run.py```, в котором произвести следующие операции:

   * Вставка в таблицу
   * Удаление из таблицы
   * Выборка с условием
   * Редактирование элемента
