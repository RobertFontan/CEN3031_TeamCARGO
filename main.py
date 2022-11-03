from isbn import lookup_isbn
import book
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy

# this does not work
bookList = []

while True:
    isbn = input("Enter an ISBN: ").strip()
    lookup_isbn(isbn)
    
    bookList.append(lookup_isbn)

    user_update = input("Want another ISBN? [Y/N] ").lower().strip()
    
    if user_update != "y":
        break 
    
print(len(bookList))


# Harry Potter 0439708184
# the stranger 9780394533056
# Game of Thrones 9780553593716

