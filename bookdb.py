from regex import B
from sqlalchemy import Column, Integer, Unicode, UnicodeText, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from random import choice
from string import letters

from book import Book

engine = create_engine('sqlite:///library.db', echo=True)
Base = declarative_base(bind=engine)

class SerializedBook(Base):
    __tablename__ = 'books'
    isbn = Column(Integer, primary_key=True)
    title = Column(UnicodeText)
    author = Column(UnicodeText)
    rating = Column(UnicodeText)
    genre = Column(UnicodeText)
    coverurl = Column(UnicodeText)

    def __init__(self, book):
        self.isbn = book.isbn
        self.title = book.title
        self.author = book.author
        self.rating = book.rating
        self.genre = book.genre
        self.coverUrl = book.coverUrl
    
    def deserialize(self):
        return Book(self.isbn, self.title, self.author, self.rating, self.genre, self.coverUrl)

Base.metadata.create_all()

def create_session():
    Session = sessionmaker(bind=engine)
    return Session()

def add_books(session, books):
    session.add_all([SerializedBook(b) for b in books])

def add_book(session, book):
    add_books(session, [book])

def get_books(session):
    return [b.deserialize() for b in session.query(SerializedBook)]