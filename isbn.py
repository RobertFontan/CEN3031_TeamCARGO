import json
from urllib.request import urlopen
from book import Book

api = "https://www.googleapis.com/books/v1/volumes?q=isbn:"

def lookup_isbn(isbn):
    #try:
    resp = urlopen(api + isbn)
    bookObject = json.load(resp)
    bookInfo = bookObject['items'][0]['volumeInfo']
    author = str(bookInfo['authors'][0])
    title = str(bookInfo['title'])
    rating = str(bookInfo['averageRating'])
    genre = str(bookInfo['categories'][0])
    #coverUrl = bookInfo['imageLinks']['smallThumbnail'] 
    newBook = Book(isbn, title, author, rating, genre, "idk")
    return newBook
    # except Exception:
    #     print("Invalid ISBN!")
 