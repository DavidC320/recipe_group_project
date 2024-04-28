import tkinter as tk
from tkinter import ttk
import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath("tkinter_objects\\__init__.py"))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from tkinter_objects.ControllerMainObject import *
from TableObjects import *

class MainMenu(ChildFrame):
    def __init__(self, master, controller, **kwargs) -> None:
        super().__init__(master, controller, **kwargs)
        tk.Label(self, text="Main Menu").pack()

        self.recipe_index_button = tk.Button(self, text="Go to recipes", command=lambda: controller.open_frame("recipe index"))
        self.recipe_index_button.pack()

        self.sign_button = tk.Button(self, text="Login")
        self.sign_button.pack()

        self.back_button = tk.Button(self, text="Back", command=lambda: controller.open_frame("start"))
        self.back_button.pack()


    def on_open(self):
        if self.controller.logged_in:
            self.sign_button.config(command= self.sign_out, text= "Sign Out")
        else:
            self.sign_button.config(command= self.login, text= "Login")
    
    def login(self):
        self.controller.open_frame("login")

    def sign_out(self):
        self.controller.logged_in = False
        self.on_open()