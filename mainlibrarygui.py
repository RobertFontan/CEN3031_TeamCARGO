import tkinter as tk
from tkinter import messagebox
from book import *
from io import BytesIO
from PIL import ImageTk, Image

#tempList = ['9783426452936','9780553593716','0735219095','1791392792']
                
from isbngui import *


coverList = []
bookCounter = 0


class mainLibGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.geometry("800x800")
        self.title("Encyclomedia")
        
        button = tk.Button(self, text=">", font=('Arial', 18), command=self.replaceCovers)
        button.pack(padx=10, pady=10)
        #self.button.place()
        
        isbnButton = tk.Button(self, text="Add a book!", font=('Arial', 18), command=self.addIsbn)
        isbnButton.pack(padx=10, pady=10)
        
        label = tk.Label(self, text="Your Bookshelf", font=('Arial', 18))
        label.pack(padx=20, pady=20)




        bookFrame = tk.Frame(self)
        bookFrame.columnconfigure(0)
        bookFrame.columnconfigure(1)
        bookFrame.columnconfigure(2)
        bookFrame.columnconfigure(3)
        bookFrame.columnconfigure(4)

        self.book0 = tk.Label(bookFrame)
        self.book0.grid(row=0, column=0)

        self.book1 = tk.Label(bookFrame)
        self.book1.grid(row=0, column=1)

        self.book2 = tk.Label(bookFrame)
        self.book2.grid(row=0, column=2)

        self.book3 = tk.Label(bookFrame)
        self.book3.grid(row=0, column=3)
        
        self.book4 = tk.Label(bookFrame)
        self.book4.grid(row=0, column=4)

        # counter = 0

        
        # for isbn in book:
        #     newCover = lookup_cover(isbn)   
        #     bookCover.append(newCover)    


        # for cover in bookCover:
        #     print(cover)
        #     u = urlopen(cover)
        #     raw_data = u.read()
        #     u.close()
        #     image = ImageTk.PhotoImage(data=raw_data) 
            
        #     if counter == 0:
        #         self.book0.configure(image=image)
        #         self.book0.image = image
        #     elif counter == 1:
        #         self.book1.configure(image=image)
        #         self.book1.image = image
        #     elif counter == 2:
        #         self.book2.configure(image=image)
        #         self.book2.image = image
        #     elif counter == 3:
        #         self.book3.configure(image=image)
        #         self.book3.image = image
        #     else:
        #         pass
        #     counter = counter + 1

        bookFrame.pack(fill='x')
        self.mainloop()

    def addIsbn(self):
        self.app = isbnGUI()
        coverList.append()
        


    def replaceCovers(self):
        #self = mainLibGUI()
        i = 0
        #replaceList = ['1501161938','0062653318','1538719843','9780439756686']
        # newBookCover = []
        # for isbn in replaceList:
        #     newnewCover = lookup_cover(isbn)   
        #     newBookCover.append(newnewCover)    

        for cv in coverList:
            print(cv)
            u = urlopen(cv)
            raw_data = u.read()
            u.close()
            image = ImageTk.PhotoImage(data=raw_data) 
            
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
            else:
                pass
            
            bookCounter = bookCounter + 1


#mainLibGUI()