import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from tkinter.ttk import *
from book import *
from tkinter import *
from io import BytesIO
from PIL import ImageTk, Image

#tempList = ['9783426452936','9780553593716','0735219095','1791392792']
                
from isbngui import *


coverList = []


class mainLibGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.geometry("800x800")
        self.title("Encyclomedia")

        #adds a background
        bg2 = PhotoImage(file="images/libraryBR.png")
        #set and add backround
        gui_bk = Label(self, image=bg2)
        gui_bk.place(x=0, y=0, relwidth=1, relheight=1)
        
        button = tk.Button(self, text="Update Books", font=('Arial', 18), command=self.replaceCovers)
        button.pack(padx=10, pady=10)
        #self.button.place()
        
        isbnButton = tk.Button(self, text="Add a book", font=('Arial', 18), command=self.addIsbn)
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
        
        self.book5 = tk.Label(bookFrame)
        self.book5.grid(row=1, column=0)
        
        self.book6 = tk.Label(bookFrame)
        self.book6.grid(row=1, column=1)
        
        self.book7 = tk.Label(bookFrame)
        self.book7.grid(row=1, column=2)
        
        self.book8 = tk.Label(bookFrame)
        self.book8.grid(row=1, column=3)
        
        self.book9 = tk.Label(bookFrame)
        self.book9.grid(row=1, column=4)
        
        

        bookFrame.pack(fill='x')
        

                
        self.mainloop()

    

    def replaceCovers(self):
        bookCounter = 0
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
            else:
                pass
            
            bookCounter = bookCounter + 1
            
    
    def addIsbn(self):
                
        isbn = simpledialog.askstring("Input", "Add a ISBN",
                                 parent=self)
       #print(isbn)
        if isbn == None:
                return
        try:
            cover = lookup_cover(isbn)
            coverList.append(cover)
            self.replaceCovers()
            

        except Exception:
            messagebox.showwarning(title="Error", message="Couldn't find the ISBN!")

        
       
         
        
mainLibGUI()


 
        # tempList = ['9780394533056',
        #             '9780553593716',
        #             '0735219095',
        #             '1791392792',
        #             '1501161938',
        #             '0062653318',
        #             '1538719843']
        



