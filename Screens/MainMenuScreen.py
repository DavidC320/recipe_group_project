import tkinter as tk
from tkinter import ttk
import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath("tkinter_objects\__init__.py"))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from tkinter_objects.ControllerMainObject import *
from TableObjects import *

class MainMenu(ChildFrame):
    def __init__(self, master, controller, **kwargs) -> None:
        super().__init__(master, controller, **kwargs)
        tk.Label(self, text="Main Menu").pack()

        self.recipe_index_button = tk.Button(self, text="Go to recipes", command=lambda: controller.open_frame("recipe index"))
        self.recipe_index_button.pack()

        self.user_index_button = tk.Button(self, text="Go to users", command=lambda: controller.open_frame("user index"))
        self.user_index_button.pack()

        self.sign_out_button = tk.Button(self, text="Sign out")
        self.sign_out_button.pack()

        self.back_button = tk.Button(self, text="Back", command=lambda: controller.open_frame("start"))
        self.back_button.pack()