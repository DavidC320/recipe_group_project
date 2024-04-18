import tkinter as tk
import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath("tkinter_objects\__init__.py"))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from tkinter_objects.ControllerMainObject import *
from tkinter import filedialog as fd 

class LoadDatabaseScreen(ChildFrame):
    def __init__(self, master, controller, **kwargs) -> None:
        super().__init__(master, controller, **kwargs)
        tk.Label(self, text="load Database").pack()
        self.file_path = ""

        self.load_database_button = tk.Button(self, text="Select file destination", command=self.select_destination)
        self.load_database_button.pack()

        self.filepath_label = tk.Label(self, text="//filepath/?")
        self.filepath_label.pack()

        self.load_button = tk.Button(self, text="Load", command=self.load_database)
        self.load_button.pack()
        
        self.back_button = tk.Button(self, text="Back", command=lambda: controller.open_frame("start"))
        self.back_button.pack()
    
    def select_destination(self):
        data = fd.askopenfile()
        self.filepath_label.config(text= data)
    
    def on_close(self):
        self.file_path = ""
        self.filepath_label.config(text= "//filepath/?")
    
    def load_database(self):
        if self.file_path not in ["", "//filepath/?"]:
            self.controller.connect_to_file(self.file_path)
            self.controller.open_frame("main menu")
        else:
            self.filepath_label.config(text= "Select a file path")

    def select_destination(self):
        data = fd.askopenfilename(title="Select the file you want to load.", 
                                    defaultextension="*.db",
                                    filetypes= [("Database File", "*.db")]
                                    )
        if data != "":
            self.file_path = data
            self.filepath_label.config(text= data)