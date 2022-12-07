import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from tkinter.ttk import *
from book import *
from book import Book
from tkinter import *
from io import BytesIO
from PIL import ImageTk, Image
from tkinter import ttk
import requests
import os
import urllib
import io
import time
#coverList = ['9783426452936','9780553593716','0735219095','1791392792']
                
#from isbngui import *

import bookdb

class LibraryModel(object):
	def __init__(self):
		self.session = bookdb.create_session()
	
	def get_books(self):
		return bookdb.get_books(self.session)
	
	def add_book(self, book):
		return bookdb.add_book(self.session, book)
	
	def remove_book(self, book):
		return bookdb.remove_book(self.session, book.isbn)

libModel = LibraryModel()

class mainLibGUI(tk.Tk):
    def __init__(self, username):
        super().__init__()
        # intializes the main gui        
        self.geometry("800x800")
        self.title("Encyclomedia")
        
        
        #adds a background
        bg2 = PhotoImage(file="images/libraryBR.png")
        
        
        # set and add background
        canvas = Canvas(self, width=2000, height=2000 )
        canvas.create_image(400,400, anchor=CENTER, image = bg2)
        canvas.create_text(10,40, anchor="w", text=username + "'s Bookshelf", font=('Arial', 30, 'bold'), fill = "black")

        canvas.place(x=0, y=0, relwidth=1, relheight=1)
       
   
        label = Label(self)
        label.pack(padx=20, pady=30)
        
        
        
        # established some main library buttons
        isbnButton = tk.Button(self, text="Add a book", font=('Arial', 18), command=self.addIsbn)
        isbnButton.place(x=390, y =20)
        
        statButton = tk.Button(self, text= "View Statisics", font=('Arial', 18), command=self.viewStats)
        statButton.place(x=600, y= 20)
        
        
        # positions the grid system for book in book shelf
        bookFrame = Frame(self, bg="brown")
        bookFrame.pack()
        
        
        bookFrame.columnconfigure(0)
        bookFrame.columnconfigure(1)
        bookFrame.columnconfigure(2)
        bookFrame.columnconfigure(3)
        bookFrame.columnconfigure(4)

        self.book0 = tk.Button(bookFrame, bg="brown", command=self.goalBox, borderwidth='0')
        self.book0.grid(row=0, column=0, padx= 10, pady=10)

        self.book1 = tk.Button(bookFrame, bg="brown", command=self.goalBox, borderwidth='0')
        self.book1.grid(row=0, column=1, padx = 10)

        self.book2 = tk.Button(bookFrame, bg="brown", command=self.goalBox, borderwidth='0')
        self.book2.grid(row=0, column=2, padx= 10)

        self.book3 = tk.Button(bookFrame, bg="brown", command=self.goalBox, borderwidth='0')
        self.book3.grid(row=0, column=3,padx= 10)
        
        self.book4 = tk.Button(bookFrame, bg="brown", command=self.goalBox, borderwidth='0')
        self.book4.grid(row=0, column=4, padx=10)
        
        self.book5 = tk.Button(bookFrame, bg="brown", command=self.goalBox, borderwidth='0')
        self.book5.grid(row=0, column=5, padx=10)
        
        self.book6 = tk.Button(bookFrame, bg="brown", command=self.goalBox, borderwidth='0')
        self.book6.grid(row=1, column=0, padx=10)
        
        self.book7 = tk.Button(bookFrame, bg="brown", command=self.goalBox, borderwidth='0')
        self.book7.grid(row=1, column=1, padx=10)
        
        self.book8 = tk.Button(bookFrame, bg="brown", command=self.goalBox, borderwidth='0')
        self.book8.grid(row=1, column=2, padx=10)
        
        self.book9 = tk.Button(bookFrame, bg="brown", command=self.goalBox, borderwidth='0')
        self.book9.grid(row=1, column=3, padx=10)
        
        self.book10 = tk.Button(bookFrame, bg="brown", command=self.goalBox, borderwidth='0')
        self.book10.grid(row=1, column=4, padx=10)

        self.book11 = tk.Button(bookFrame, bg="brown", command=self.goalBox, borderwidth='0')
        self.book11.grid(row=1, column=5, padx=10)

        self.book12 = tk.Button(bookFrame, bg="brown", command=self.goalBox, borderwidth='0')
        self.book12.grid(row=2, column=0, padx=10)

        self.book13 = tk.Button(bookFrame, bg="brown", command=self.goalBox, borderwidth='0')
        self.book13.grid(row=2, column=1, padx=10)
        
        self.book14 = tk.Button(bookFrame, bg="brown", command=self.goalBox, borderwidth='0')
        self.book14.grid(row=2, column=2, padx=10)

        self.book15 = tk.Button(bookFrame, bg="brown", command=self.goalBox, borderwidth='0')
        self.book15.grid(row=2, column=3, padx=10)

        self.book16 = tk.Button(bookFrame, bg="brown", command=self.goalBox, borderwidth='0')
        self.book16.grid(row=2, column=4, padx=10)

        self.book17 = tk.Button(bookFrame, bg="brown", command=self.goalBox, borderwidth='0')
        self.book17.grid(row=2, column=5, padx=10)

        
        # added variables in charge of statistics
        self.daily = tk.IntVar()
        self.completed = tk.IntVar()
        
        self.bookCount = tk.IntVar(self, value=0, name = "bookCount")
        #counter for daily and complete to be used in statistics
        self.DCount = tk.IntVar(self, value=0, name = "Dcount")
        self.CCount = tk.IntVar(self, value=0, name = "Ccount")

        bookFrame.pack(padx =10, fill='x')
   

        # adds existing books
        for book in libModel.get_books():
            self.addCover(book)
        
        self.mainloop()

    
    #funciton for adding a new book cover image to ui
    def addCover(self, newBook):
        bookCounter = self.bookCount.get()
        newCover = newBook.getCover()
        reponse = requests.get(newCover)
        img_data = reponse.content     
        img = Image.open(BytesIO(img_data))
        img = img.resize((100, 180))   
        image = ImageTk.PhotoImage(img)
       
        
        if bookCounter == 0:
            self.book0.configure(image=image)
            self.book0.image = image
        elif bookCounter == 1:
            self.book1.configure(image=image)
            self.book1.image = image
        elif bookCounter == 2:
            self.book2.configure(image=image)
            self.book2.image = image
        elif bookCounter == 3:
            self.book3.configure(image=image)
            self.book3.image = image
        elif bookCounter == 4:
            self.book4.configure(image=image)
            self.book4.image = image
        elif bookCounter == 5:
            self.book5.configure(image=image)
            self.book5.image = image
        elif bookCounter == 6:
            self.book6.configure(image=image)
            self.book6.image = image
        elif bookCounter == 7:
            self.book7.configure(image=image)
            self.book7.image = image
        elif bookCounter == 8:
            self.book8.configure(image=image)
            self.book8.image = image
        elif bookCounter == 9:
            self.book9.configure(image=image)
            self.book9.image = image
        elif bookCounter == 10:
            self.book10.configure(image=image)
            self.book10.image = image
        elif bookCounter == 11:
            self.book11.configure(image=image)
            self.book11.image = image
        elif bookCounter == 12:
            self.book12.configure(image=image)
            self.book12.image = image
        elif bookCounter == 13:
            self.book13.configure(image=image)
            self.book13.image = image
        elif bookCounter == 14:
            self.book14.configure(image=image)
            self.book14.image = image
        elif bookCounter == 15:
            self.book15.configure(image=image)
            self.book15.image = image
        elif bookCounter == 16:
            self.book16.configure(image=image)
            self.book16.image = image
        elif bookCounter == 17:
            self.book17.configure(image=image)
            self.book17.image = image
        else:
            messagebox.showwarning(title="Error", message="Not enough books")
                    
        bookCounter = bookCounter + 1
        self.bookCount.set(bookCounter)
            
    # prompts user to add isbn of book they want to add and calls to add the cover
    def addIsbn(self):
        isbn = simpledialog.askstring("Input", "Add a ISBN",
                                 parent=self)
       #print(isbn)
        
        if isbn == None:
                return
        
        try:
            newBook = lookup_isbn(isbn)
            libModel.add_book(newBook)
            self.addCover(newBook)
        
        except Exception:
            messagebox.showwarning(title="Error", message="Couldn't find the ISBN!")

        
    def viewStats(self):
        
        print("The value of bookCount is: ", self.getvar(name="bookCount"))
        
        #how the statistics box works
        Stats = Tk()
        Stats.title("Library Statistics")
        count = self.bookCount.get()
        total_books = tk.Label(Stats, text="Books Added: " + str(count))
        total_books.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
        read_label = tk.Label(Stats, text="Books Completed: " + str(self.CCount.get()))
        read_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
        read_label = tk.Label(Stats, text="Total Daily revisits: " + str(self.DCount.get()))
        read_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)
        percDOne = 0
        #corrects a divide by zero error when there are no books added
        if count == 0:
            percDOne = 1
        else: 
            percDOne = (self.CCount.get()/count)
        
        
        read_label = tk.Label(Stats, text="Percentage Completed: " + str(percDOne*100) + "%")
        read_label.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)

        close_button = ttk.Button(Stats, text="return", command=Stats.destroy)
        close_button.grid(column=0, row=4, sticky=tk.W, padx=5, pady=5)
        

    def closebutton(Stats):
        return # destroy current window
    
    def updateDaily(self):
        #increments daily
        if self.daily.get() == 1:
            self.DCount.set(self.DCount.get()+1)
    def updateCompleted(self):
        #increments completed
        if self.completed.get() == 1:
            self.CCount.set(self.CCount.get()+1)
        

        
    # when clicking a book gives dialog to update it
    def goalBox(self):
        goalBox = Toplevel()
        goalBox.title('Book Options')
        tk.Checkbutton(goalBox, text = 'Did you read today?', variable=self.daily, onvalue= 1, offvalue=0, command=self.updateDaily).pack()
        tk.Checkbutton(goalBox, text = 'Completed a Book', variable=self.completed, onvalue= 1, offvalue=0, command=self.updateCompleted).pack()
        tk.Button(goalBox, text='OK', command=goalBox.destroy).pack()

        

