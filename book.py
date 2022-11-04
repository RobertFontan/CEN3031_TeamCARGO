import json
from urllib.request import urlopen

from numpy import cov

api = "https://www.googleapis.com/books/v1/volumes?q=isbn:"


class Book:
  def __init__(self, isbn, title, author, rating, genre, coverUrl):
    self.isbn = isbn
    self.title = title
    self.author = author
    self.rating = rating
    self.genre = genre
    self.coverUrl = coverUrl
    
    
    
def lookup_isbn(isbn):
    try:
        resp = urlopen(api + isbn)
        bookObject = json.load(resp)
        bookInfo = bookObject['items'][0]['volumeInfo']
        author = str(bookInfo['authors'][0])
        title = str(bookInfo['title'])
        rating = str(bookInfo['averageRating'])
        genre = str(bookInfo['categories'][0])
        coverUrl = bookInfo['imageLinks']['smallThumbnail'] 
        formattedInfo = json.dumps(bookObject, indent=2)    
        # if you want organized book info 
        print(coverUrl)
        newBook = Book(isbn, title, author, rating, genre, coverUrl)
        return newBook
    except Exception:
        print("Something went wrong!")
    
def getCover(self):
    return self.coverUrl
    
def lookup_cover(isbn):
    resp = urlopen(api + isbn)
    bookObject = json.load(resp)
    bookInfo = bookObject['items'][0]['volumeInfo']                
    return bookInfo['imageLinks']['smallThumbnail'] 
