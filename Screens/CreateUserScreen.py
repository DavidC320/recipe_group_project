import tkinter as tk
from tkinter import ttk
import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath("tkinter_objects\\__init__.py"))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from tkinter_objects.ControllerMainObject import *
from TableObjects import *

class CreateUser(ChildFrame):
    def __init__(self, master, controller, create_mode, **kwargs) -> None:
        super().__init__(master, controller, **kwargs)

        label_text = ""
        if create_mode:
            label_text += "Create"
        else:
            label_text += "Update"
        tk.Label(self, text=label_text + "user").grid(row=0, column=0, columnspan=2)

        self.admin_check_button = tk.Checkbutton(self, text="User is Admin")
        self.admin_check_button.grid(row=1, column=0)
        
        tk.Label(self, text="Username").grid(row=2, column=0)
        self.username = tk.StringVar()
        self.username_entry = tk.Entry(self, textvariable=self.username)
        self.username_entry.grid(row=2, column=1)

        tk.Label(self, text="Password").grid(row=3, column=0)
        self.password = tk.StringVar()
        self.password_entry = tk.Entry(self, textvariable=self.password)
        self.password_entry.grid(row=3, column=1)

        self.control_frame = tk.Frame(self)
        self.control_frame.grid(row=4, column=0, columnspan=2)

        
        button_text = ""
        if create_mode:
            button_text += "Create"
        else:
            button_text += "Update"

        self.create_button = tk.Button(self.control_frame, text=button_text)
        self.create_button.grid(row=0, column=0)

        self.back_button = tk.Button(self.control_frame, text="Back", command=lambda: controller.open_frame("user index"))
        self.back_button.grid(row=0, column=1)
