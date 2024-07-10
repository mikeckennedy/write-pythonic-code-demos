import os
import random

import sqlalchemy
import sqlalchemy.orm
import sqlalchemy.ext
import sqlalchemy.ext.declarative

SqlAlchemyBase = sqlalchemy.ext.declarative.declarative_base()


class Measurement(SqlAlchemyBase):
    __tablename__ = 'Measurement'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    x = sqlalchemy.Column(sqlalchemy.Integer)
    y = sqlalchemy.Column(sqlalchemy.Integer)
    value = sqlalchemy.Column(sqlalchemy.Float)












# run this code only once per process assuming 1 database
db_file = os.path.join(
    os.path.dirname(__file__),
    'slicing_db.sqlite')

conn_str = 'sqlite:///' + db_file
engine = sqlalchemy.create_engine(conn_str, echo=True)
session_factory = sqlalchemy.orm.sessionmaker(bind=engine)
SqlAlchemyBase.metadata.create_all(engine)

session = session_factory()

count = session.query(Measurement).count()
if not count:
    print("No data, adding test data")
    for _ in range(100):
        m = Measurement()
        m.value = random.random()
        m.x = random.randint(0, 100)
        m.y = random.randint(0, 100)
        session.add(m)
    session.commit()
