from sqlalchemy import Column, UnicodeText
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///users.db', echo=False)
Base = declarative_base(bind=engine)

# Object that stores the necessary metadata for database serialization
class SerializedUser(Base):
    __tablename__ = 'users'
    username = Column(UnicodeText, primary_key=True)
    password = Column(UnicodeText)

    def __init__(self, username, password):
        self.username = username
        self.password = password

Base.metadata.create_all()

# Create a database connection
def create_session():
    Session = sessionmaker(bind=engine)
    return Session()

# Create a new user
def add_user(session, username, password):
    session.add_all([SerializedUser(username, password)])
    session.commit()

# Authenticate a user
def contains_user(session, username, password):
    return session.query(SerializedUser).filter_by(username=username, password=password).first() is not None