import json
from urllib.request import urlopen

from numpy import cov

api = "https://www.googleapis.com/books/v1/volumes?q=isbn:"

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
			return Book(isbn, title, author, rating, genre, coverUrl)
		except Exception:
			return None

def lookup_cover(isbn):
		resp = urlopen(api + isbn)
		bookObject = json.load(resp)
		bookInfo = bookObject['items'][0]['volumeInfo']                
		return bookInfo['imageLinks']['smallThumbnail'] 

class Book:
	def __init__(self, isbn, title, author, rating, genre, coverUrl):
		self.isbn = isbn
		self.title = title
		self.author = author
		self.rating = rating
		self.genre = genre
		self.coverUrl = coverUrl
		
	def getCover(self):
		return self.coverUrl
	
	def __str__(self):
		return format(self.isbn, '13d') + f" {self.author[:20]:<20} {self.title[:50]:<50}"