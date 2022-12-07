from sqlalchemy import Column, Integer, Boolean, UnicodeText
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from book import Book

engine = create_engine('sqlite:///library.db', echo=False)
Base = declarative_base(bind=engine)

# Object that stores the necessary metadata for database serialization
class SerializedBook(Base):
    __tablename__ = 'books'
    isbn = Column(Integer, primary_key=True)
    title = Column(UnicodeText)
    author = Column(UnicodeText)
    rating = Column(UnicodeText)
    genre = Column(UnicodeText)
    coverUrl = Column(UnicodeText)
    electronic = Column(Boolean)

    def __init__(self, book):
        self.isbn = book.isbn
        self.title = book.title
        self.author = book.author
        self.rating = book.rating
        self.genre = book.genre
        self.coverUrl = book.coverUrl
        self.electronic = book.electronic
    
    def deserialize(self):
        return Book(self.isbn, self.title, self.author, self.rating, self.genre, self.coverUrl, self.electronic)

Base.metadata.create_all()

# Create a database connection
def create_session():
    Session = sessionmaker(bind=engine)
    return Session()

# Add multiple books to the database
def add_books(session, books):
    session.add_all([SerializedBook(b) for b in books])
    session.commit()

# Add one book to the database
def add_book(session, book):
    add_books(session, [book])

# Get all books in the database
def get_books(session):
    return [b.deserialize() for b in session.query(SerializedBook)]

# Remove all instances of an ISBN from the database
def remove_book(session, isbn):
    session.query(SerializedBook).filter_by(isbn=isbn).delete()
    session.commit()