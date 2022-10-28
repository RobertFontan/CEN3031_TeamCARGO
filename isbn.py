import json

from book import Book
from urllib.request import urlopen
api = "https://www.googleapis.com/books/v1/volumes?q=isbn:"



def lookup_isbn(isbn):
    isbn = isbn.strip()
    resp = urlopen(api + isbn)
    
    bookObject = json.load(resp)
    bookInfo = bookObject['items'][0]['volumeInfo']
    
    author = str(bookInfo['authors'][0])
    title = str(bookInfo['title'])
    rating = str(bookInfo['averageRating'])
    genre = str(bookInfo['categories'][0])
    coverUrl = bookInfo['imageLinks']['smallThumbnail']
    
    return Book(isbn, title, author, rating, genre, coverUrl)
   # return Book("978-1250037756", "Mr. Penumbra's 24-Hour Bookstore", "Robin Sloan", 3.7, "novel", "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1345089845i/13538873.jpg")



