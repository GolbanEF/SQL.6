import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Publisher(Base):
    __tablename__ = 'publisher'

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), unique=True)

    def __str__(self):
        return f'{self.id}: {self.name}'


class Book(Base):
    __tablename__ = 'book'

    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(length=60), unique=True)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey('publisher'), nullable=False)

    publisher = relationship(Publisher, backref='books')

    def __str__(self):
        return f'{self.id}: {self.title}'


class Shop(Base):
    __tablename__ = 'shop'

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), unique=True)

    def __str__(self):
        return f'{self.id}: {self.name}'


class Stock(Base):
    __tablename__ = 'stock'

    id = sq.Column(sq.Integer, primary_key=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey('book'), nullable=False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey('shop'), nullable=False)
    count = sq.Column(sq.Integer, unique=True)

    book = relationship(Book, backref='stocks')
    shop = relationship(Shop, backref='stocks')

    def __str__(self):
        return f'{self.id}: {self.count}'


class Sale(Base):
    __tablename__ = 'sale'

    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Integer, unique=True)
    date_sale = sq.Column(sq.Date, unique=True)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey('stock'), nullable=False)
    count = sq.Column(sq.Integer, unique=True)

    stock = relationship(Stock, backref='sales')

    def __str__(self):
        return f'{self.id}: ({self.price}, {self.date_sale}, {self.count}'


def create_tables(engine):
    Base.metadata.create_all(engine)







