from concurrent.futures.process import BrokenProcessPool
import json
from tkinter import N
from urllib.request import urlopen
 
#from matplotlib.font_manager import json_load
 
# sample 0439708184
# sample 9780553593716


 
api = "https://www.googleapis.com/books/v1/volumes?q=isbn:"
isbn = input("Enter any 10 digit ISBN: ").strip()

try:
    resp = urlopen(api + isbn)
    bookObject = json.load(resp)
    bookInfo = bookObject['items'][0]['volumeInfo']
    formattedInfo = json.dumps(bookObject, indent=2)
    print(formattedInfo)
    author = str(bookInfo['authors'][0])
    title = str(bookInfo['title'])
    rating = str(bookInfo['averageRating'])
    genre = str(bookInfo['categories'][0])
    coverUrl = bookInfo['imageLinks']['smallThumbnail'] 

except Exception:
    print("invalid isbn")
 

 
#print('rating is: ' + rating)

