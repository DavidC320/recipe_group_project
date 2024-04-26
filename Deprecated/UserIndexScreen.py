'''

This Class is deprecated
'''
import tkinter as tk
from tkinter import ttk
import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath("tkinter_objects\\__init__.py"))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from tkinter_objects.ControllerMainObject import *
from TableObjects import *

class UserIndex(ChildFrame):
    def __init__(self, master, controller, **kwargs) -> None:
        super().__init__(master, controller, **kwargs)
        tk.Label(self, text="User Index").grid(row=0, column= 0)

        self.control_frame = tk.Frame(self)
        self.control_frame.grid(row=1, column=0)

        self.search_query = tk.StringVar()
        self.search_entry = tk.Entry(self.control_frame, textvariable=self.search_query)
        self.search_entry.grid(row=0, column=0)

        self.search_button = tk.Button(self.control_frame, text="Search")
        self.search_button.grid(row=0, column=1)

        self.recipe_list_box = tk.Listbox(self.control_frame, height=10)
        self.recipe_list_box.grid(row=1, column=0)

        self.control_frame = tk.Frame(self)
        self.control_frame.grid(row=3, column=0)

        self.create_button = tk.Button(self.control_frame, text="Create User")
        self.create_button.grid(row=0, column=0)

        self.create_button = tk.Button(self.control_frame, text="Create Admin")
        self.create_button.grid(row=0, column=1)

        self.view_button = tk.Button(self.control_frame, text="View")
        self.view_button.grid(row=0, column=2)

        self.back_button = tk.Button(self.control_frame, text="Back", command=lambda: controller.open_frame("main menu"))
        self.back_button.grid(row=0, column=3)