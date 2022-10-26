import json
from urllib.request import urlopen

# sample 0439708184
# sample 9780679720201

api = "https://www.googleapis.com/books/v1/volumes?q=isbn:"
isbn = input("Enter ISBN: ")
resp = urlopen(api + isbn)

bigInfo = json.load(resp)
bookInfo = bigInfo['items'][0]['volumeInfo']

author = str(bookInfo['authors'][0])
title = str(bookInfo['title'])

# print(bookInfo) 
print(title + '\nby: ' + author)