import tkinter as tk
from tkinter import messagebox
from book import *
from io import BytesIO
from PIL import ImageTk, Image
# pip install pillow

currentISBN = None
class isbnGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        # self.root = tk.Tk()
        self.geometry("500x500")
        self.title("Encyclomedia")
    

        label = tk.Label(self, text="Library", font=('Arial', 18))
        label.pack(padx=10, pady=10)
        
        self.textbox = tk.Text(self, height=1, width=50, font=('Arial', 16))
        self.textbox.pack(padx=10, pady=10)
        
        frame = tk.Frame(self)
        frame.pack()
        
        self.bookGrid = tk.Label(frame)
        self.bookGrid.pack(side=tk.LEFT)
        
        
        button = tk.Button(self, text="Add ISBN", font=('Arial', 18), command=self.add_cover)
        button.pack(padx=10, pady=10)
        
        self.mainloop()
        
    def add_cover(self):
        new_isbn = self.textbox.get('1.0', tk.END)
        new_cover = lookup_cover(new_isbn)        
        
        
        u = urlopen(new_cover)
        raw_data = u.read()
        u.close()
        image = ImageTk.PhotoImage(data=raw_data) 
        
        self.bookGrid.configure(image=image)
        self.bookGrid.image = image 
        
        currentISBN = new_cover

        self.destroy()
        
           
def returnCover():
    return currentISBN


#isbnGUI()



   
        # tempList = ['9780394533056',
        #             '9780553593716',
        #             '0735219095',
        #             '1791392792',
        #             '1501161938',
        #             '0062653318',
        #             '1538719843']
        