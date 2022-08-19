import sqlalchemy
from sqlalchemy.orm import sessionmaker
import os
from Models import create_tables, Shop, Stock, Sale, Publisher, Book


DSN = os.getenv('Password')

engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)

session = Session()


def shops():
    publisher_shop = input('Введите id:')
    session.qvery(Shop).join(Stock.shop).join(Stock.book).join(Book.publisher).join(Publisher).filter(Publisher.number == publisher_shop)


def publishers():
    publisher = input('Введите идификатор:')
    session.qvery(Publisher).filter(Publisher.number == publisher)


publishers()

session.close()

