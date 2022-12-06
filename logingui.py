from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox

from mainlibrarygui import mainLibGUI
import userdb

class UsersModel(object):
	def __init__(self):
		self.session = userdb.create_session()
	
	def add_user(self, username, password):
		return userdb.add_user(self.session, username, password)
	
	def contains_user(self, username, password):
		return userdb.contains_user(self.session, username, password)

users = UsersModel()

class titleScreen(tk.Tk):
    def loginButton(self):
        user = str(self.username_entry.get())
        passw = str(self.password_entry.get())
        if not users.contains_user(user, passw):
            messagebox.showwarning(title="Error", message="Invalid username or password!")
            return
        self.destroy()  # destroy current window
        self.app = mainLibGUI(user)

    #goes to new user window
    def newUser(self):
        users.add_user(self.username_entry.get(), self.password_entry.get())
        messagebox.showwarning(title="Success", message="New user created!")

    
    def __init__(self):
        super().__init__()
         
        self.geometry("800x400")
        
        #title and rest of functionality
        self.title("Encyclomedia")

        #backroundtest
        bg = PhotoImage(file="images/testimg.png")
       
        #set and add backround
        my_label = Label(self, image=bg)
      
        my_label.place(x=0, y=0, relwidth=1, relheight=1)

        #add label to top of backround
        intro_label = Label(self, text="WELCOME TO ENCYLOMEDIA", font=("Arial bold",20), fg="black",)
        intro_label.pack(pady=20)
        #create a frame
        login_frame = Frame(self)
        login_frame.pack(pady=50)
        
        #login code
        
        #making grid 
        

        # labels 
        username_label = tk.Label(login_frame, text="Username:")
        username_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

        self.username_entry = tk.Entry(login_frame)
        self.username_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)


        # password
        password_label = ttk.Label(login_frame, text="Password:")
        password_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

        self.password_entry = ttk.Entry(login_frame,  show="*")
        self.password_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

        # login button
        login_button = ttk.Button(login_frame, text="Login", command=self.loginButton)
        login_button.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)

        #new user button and action

        newuser_button = ttk.Button(login_frame, text="New User", command=self.newUser)
        newuser_button.grid(column=0, row=3, sticky=tk.E, padx=5, pady=5)

        #end test
        self.mainloop()

    def welcomeButton(self):
        self.destroy()  # destroy current window
        self.app = ()

    def start(self):
        self.mainloop()
        


titleScreen().start()