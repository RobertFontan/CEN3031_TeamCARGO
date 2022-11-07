import tkinter as tk
from tkinter import messagebox
from book import *
from io import BytesIO
from PIL import ImageTk, Image

tempList = ['9783426452936','9780553593716','0735219095','1791392792']
                
bookCover = []


class mainLibGUI:
    def __init__(self):
        self.root  = tk.Tk()
        self.root.geometry("800x800")
        self.root.title("Encyclomedia")
        
        self.button = tk.Button(self.root, text=">", font=('Arial', 18), command=self.replaceCovers)
        self.button.pack(padx=10, pady=10)
        
        self.label = tk.Label(self.root, text="Your Bookshelf", font=('Arial', 18))
        self.label.pack(padx=20, pady=20)




        self.bookFrame = tk.Frame(self.root)
        self.bookFrame.columnconfigure(0)
        self.bookFrame.columnconfigure(1)
        self.bookFrame.columnconfigure(2)
        self.bookFrame.columnconfigure(3)


        self.book0 = tk.Label(self.bookFrame)
        self.book0.grid(row=0, column=0)

        self.book1 = tk.Label(self.bookFrame)
        self.book1.grid(row=0, column=1)

        self.book2 = tk.Label(self.bookFrame)
        self.book2.grid(row=0, column=2)

        self.book3 = tk.Label(self.bookFrame)
        self.book3.grid(row=0, column=3)

        counter = 0

        
        for isbn in tempList:
            newCover = lookup_cover(isbn)   
            bookCover.append(newCover)    


        for cover in bookCover:
            print(cover)
            u = urlopen(cover)
            raw_data = u.read()
            u.close()
            image = ImageTk.PhotoImage(data=raw_data) 
            
            if counter == 0:
                self.book0.configure(image=image)
                self.book0.image = image
            elif counter == 1:
                self.book1.configure(image=image)
                self.book1.image = image
            elif counter == 2:
                self.book2.configure(image=image)
                self.book2.image = image
            elif counter == 3:
                self.book3.configure(image=image)
                self.book3.image = image

            else:
                pass
            counter = counter + 1

        self.bookFrame.pack(fill='x')
        self.root.mainloop()



    def replaceCovers(self):
        i = 0
        replaceList = ['1501161938','0062653318','1538719843','9780439756686']
        newBookCover = []
        for isbn in replaceList:
            newnewCover = lookup_cover(isbn)   
            newBookCover.append(newnewCover)    


        for cv in newBookCover:
            print(cv)
            u = urlopen(cv)
            raw_data = u.read()
            u.close()
            image = ImageTk.PhotoImage(data=raw_data) 
            
            if i == 0:
                self.book0.configure(image=image)
                self.book0.image = image
            elif i == 1:
                self.book1.configure(image=image)
                self.book1.image = image
            elif i == 2:
                self.book2.configure(image=image)
                self.book2.image = image
            elif i == 3:
                self.book3.configure(image=image)
                self.book3.image = image

            else:
                pass
            
            i = i + 1


mainLibGUI()