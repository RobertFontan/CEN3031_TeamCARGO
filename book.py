import json
from urllib.request import urlopen
from book import Book


class Book:
  def __init__(self, isbn, title, author, rating, genre, coverUrl):
    self.isbn = isbn
    self.title = title
    self.author = author
    self.rating = rating
    self.genre = genre
    self.coverUrl = coverUrl
    

  def lookup_isbn(isbn):
      resp = urlopen("https://www.googleapis.com/books/v1/volumes?q=isbn:" + isbn)
      respJson = json.load(resp)
      bookInfo = respJson['items'][0]['volumeInfo']
      return Book(bookInfo['industryIdentifiers'][1]['identifier'], bookInfo['title'], bookInfo['authors'][0], bookInfo['averageRating'], bookInfo['categories'][0], bookInfo['imageLinks']['thumbnail'])