from urllib import response
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import requests
import json
from urllib.request import urlopen

from torch import _fused_moving_avg_obs_fq_helper



from book import Book, lookup_isbn, lookup_cover

app = Flask(__name__)  
db = SQLAlchemy(app)

class Library(db.Model):
    isbn = db.Column(db.Integer, primary_key=True)
    coverUrl = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return '<Book %r>' % self.isbn

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/',methods=['POST', 'GET'])
def get_book():
    if request.method == 'POST':
        new_ISBN = request.form['u']
        new_cover = lookup_cover(new_ISBN)
        new_Book = Library(isbn=new_ISBN, coverUrl = new_cover)
        
        try:
            db.session.add(new_Book)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task'
    else:
        books = Library.query.order_by(Library.date_created).all()
        return render_template('index.html', books=books)
        
    # bookList =[]
    # bookList.append('http://books.google.com/books/content?id=YDzTCwAAQBAJ&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api')

    # if request.method == 'POST':
    #     isbn = request.form['u']
    #     isbn = isbn.strip()
    #     url = "https://www.googleapis.com/books/v1/volumes?q=isbn:"
    #     try:
    #         response = json.loads(requests.request("GET", url).text)
    #         resp = urlopen(url + isbn)
    #         bookObject = json.load(resp)
    #         bookInfo = bookObject['items'][0]['volumeInfo']
            
    #         author = str(bookInfo['authors'][0])
    #         title = str(bookInfo['title'])
    #         coverUrl = bookInfo['imageLinks'][' smallThumbnail']
            
    #         bookList.append(coverUrl)
            
    #         return redirect('/')
    #     except:
    #         return 'There was an error adding your book'
    # else:
    #     bookList = bookList.sort()
    #     return render_template('index.html', covers=bookList)
        




if __name__ == "__main__":
    app.run(debug=True)
            
            