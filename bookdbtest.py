from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from pyparsing import nullDebugAction

from book import Book, lookup_isbn

app = Flask(__name__)  
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class Library(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(10), nullable= False)
    #title = db.Column(db.String(200), nullable= False)
    #coverUrl = db.Column(db.String(200), nullable = False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return '<Book %r>' % self.id
    
    
@app.before_first_request
def create_tables():
    db.create_all()
    
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        newISBN = request.form['isbn']
        
   #     nB = lookup_isbn(str(newISBN))
        
        
        newBook = Library(isbn = newISBN)
     #   newCoverURL = Library(coverUrl = nB.getCover())
        
        try:
            db.session.add(newBook)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your book'
            
    else:
        books = Library.query.order_by(Library.date_created).all()
        return render_template('index.html', books=books)
            
            
if __name__ == "__main__":
    app.run(debug=True)
            
            
    # __tablename__ = 'books'
    # isbn = db.Column(db.Integer, primary_key=True)
    # title = db.Column(UnicodeText)
    # author = db.Column(UnicodeText)
    # rating = db.Column(UnicodeText)
    # genre = db.Column(UnicodeText)
    # coverurl = db.Column(UnicodeText)

    # def __init__(self, book):
    #     self.isbn = book.isbn
    #     self.title = book.title
    #     self.author = book.author
    #     self.rating = book.rating
    #     self.genre = book.genre
    #     self.coverUrl = book.coverUrl