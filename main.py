import sqlalchemy
from sqlalchemy.orm import sessionmaker

from Models import create_tables, Shop, Stock, Sale, Publisher, Book

DSN = 'postgresql://postgres:postgres@localhost:5432/test3'
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)

session = Session()


def publishers():
    publisher = input('Введите идификатор:')
    session.qvery(Publisher).filter(Publisher.number == publisher)


publishers()

session.close()

