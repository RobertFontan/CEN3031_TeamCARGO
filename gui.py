import tkinter as tk
from tkinter import messagebox
from book import *
from io import BytesIO
from PIL import ImageTk, Image
# pip install pillow


class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("800x800")
        self.root.title("Encyclomedia")
    

        self.label = tk.Label(self.root, text="Library", font=('Arial', 18))
        self.label.pack(padx=10, pady=10)
        
        self.textbox = tk.Text(self.root, height=1, width=50, font=('Arial', 16))
        self.textbox.pack(padx=10, pady=10)
        
        # self.check_state = tk.IntVar()
        
        # self.check = tk.Checkbutton(self.root, text="Show Messagebox", font=('Arial', 18), variable=self.check_state)
        # self.check.pack(padx=10, pady=10)
        
        self.frame = tk.Frame(self.root)
        self.frame.pack()
        
        self.bookGrid = tk.Label(self.frame)
        self.bookGrid.pack(side=tk.LEFT)
        
        
        self.button = tk.Button(self.root, text="Add ISBN", font=('Arial', 18), command=self.add_cover)
        self.button.pack(padx=10, pady=10)
        
        self.root.mainloop()
        
    def add_cover(self):
        new_isbn = self.textbox.get('1.0', tk.END)
        new_cover = lookup_cover(new_isbn)        
        #print(new_cover)
           
        u = urlopen(new_cover)
        raw_data = u.read()
        u.close()
        image = ImageTk.PhotoImage(data=raw_data) 
        self.bookGrid.configure(image=image)
        self.bookGrid.image = image 
        
        #mg = tk.Label(self.bookGrid,image=photo, text= new_isbn, font=('Arial', 18))
        
        # self.newBook.grid(row=1, column=1, sticky=tk.W +tk.E)
        #self.newBook.place(x=200, y= 200)
        # self.newBook.grid(row = 0, column=0, sticky=tk.W + tk.E)
       
        
       # the stranger 9780394533056
        # Game of Thrones 9780553593716

        
        
    
            
        
    # def show_message(self):
    #     if self.check_state.get() == 0:
    #         print(self.textbox.get('1.0', tk.END))
    #     else:
    #         messagebox.showinfo(title="Message", message=self.textbox.get('1.0', tk.END))
            
    
GUI()