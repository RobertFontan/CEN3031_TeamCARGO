import json
from urllib.request import urlopen

api = "https://www.googleapis.com/books/v1/volumes?q=isbn:"

#lookup functions to define books and get covers for api and db
def lookup_isbn(isbn):
        resp = urlopen(api + isbn)
        bookObject = json.load(resp)
        bookInfo = bookObject['items'][0]['volumeInfo']
        author = str(bookInfo['authors'][0])
        title = str(bookInfo['title'])
        rating = "None" #str(bookInfo['averageRating'])
        genre = "None"
        coverUrl= bookInfo['imageLinks']['smallThumbnail']
        return Book(isbn, title, author, rating, genre, coverUrl, False)
        #except Exception:
        #	return None

def lookup_cover(isbn):
        resp = urlopen(api + isbn)
        bookObject = json.load(resp)
        bookInfo = bookObject['items'][0]['volumeInfo']                
        return bookInfo['imageLinks']['smallThumbnail'] 
#defines the book object
class Book:
    def __init__(self, isbn, title, author, rating, genre, coverUrl, electronic):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.rating = rating
        self.genre = genre
        self.coverUrl = coverUrl
        self.electronic = electronic

    def getCover(self):
        return self.coverUrl

    def getISBN(self):
        return self.isbn
    
    def __str__(self):
        return ("E " if self.electronic else "  ") + format(self.isbn, '13d') + f" {self.author[:20]:<20} {self.title[:50]:<50}"