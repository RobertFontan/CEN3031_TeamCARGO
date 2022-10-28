import json
from urllib.request import urlopen
from book import Book

def lookup_isbn(isbn):
    resp = urlopen("https://www.googleapis.com/books/v1/volumes?q=isbn:" + isbn)
    respJson = json.load(resp)
    bookInfo = respJson['items'][0]['volumeInfo']
    return Book(bookInfo['industryIdentifiers'][1]['identifier'], bookInfo['title'], bookInfo['authors'][0], bookInfo['averageRating'], bookInfo['categories'][0], bookInfo['imageLinks']['thumbnail'])