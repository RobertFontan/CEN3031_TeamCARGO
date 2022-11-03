from urllib import response
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import requests
import json
from urllib.request import urlopen



from book import Book, lookup_isbn

app = Flask(__name__)  


def get_book():
    url = "https://www.googleapis.com/books/v1/volumes?q=isbn:"
    response = json.loads(requests.request("GET", url).text)
    isbn = str(9780553593716)
    resp = urlopen(url + isbn)
    bookObject = json.load(resp)
    bookInfo = bookObject['items'][0]['volumeInfo']
    
    author = str(bookInfo['authors'][0])
    title = str(bookInfo['title'])
    coverUrl = bookInfo['imageLinks']['smallThumbnail']
        
    
    return author, title, coverUrl

@app.route("/")
def index():
    author, title, coverURL = get_book()
    return render_template("index.html", author=author,title=title, coverURL=coverURL)

            
if __name__ == "__main__":
    app.run(debug=True)
            
            