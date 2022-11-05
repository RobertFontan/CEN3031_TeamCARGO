from tkinter import *
from tkinter import ttk
import tkinter as tk

class titleScreen(tk.Tk):
    
    def __init__(self):
        super().__init__()
         
        self.geometry("300x200")
        self.title("Encyclomedia")
        self.config(background="")
        self.button = tk.Button(self, text="WELCOME TO ENCYLOMEDIA", command=self.welcomeButton)
        self.button.pack()

    def welcomeButton(self):
        self.destroy()  # destroy current window
        self.app = loginScreen()

    def start(self):
        self.mainloop()


class loginScreen(tk.Tk):
    #makes new window
    def loginButton(self):
        self.destroy()  # destroy current window
        self.app = libraryScreen()

    def __init__(self):
        super().__init__()
        self.title("Encyclomedia")
        
        #making grid 
        self.columnconfigure(0,weight = 1)
        self.columnconfigure(1, weight= 3) 

        # lables 
        username_label = tk.Label(self, text="Username:")
        username_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

        username_entry = tk.Entry(self)
        username_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)


        # password
        password_label = ttk.Label(self, text="Password:")
        password_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

        password_entry = ttk.Entry(self,  show="*")
        password_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

        # login button
        login_button = ttk.Button(self, text="Login", command=self.loginButton)
        login_button.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)



class libraryScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("300x200")
        self.title("Encyclomedia")
        self.config(background="")      
        testlable = tk.Label(self, text="library goes here")
        testlable.pack()





    """
    class newWindow(tk.Tk):  
        def __init__(self):
            super().__init__()
            self.scoretext = tk.Label(self, text="Cancel pressed")
            self.scoretext.pack()
    """


titleScreen().start()


