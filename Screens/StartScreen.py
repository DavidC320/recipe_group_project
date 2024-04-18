import tkinter as tk
import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath("tkinter_objects\__init__.py"))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from tkinter_objects.ControllerMainObject import *

class StartScreen(ChildFrame):
    def __init__(self, master, controller, **kwargs) -> None:
        super().__init__(master, controller, **kwargs)
        tk.Label(self, text="Welcome").pack()
        self.create_database = tk.Button(self, text="Create Database", command=lambda: controller.open_frame("create database"))
        self.create_database.pack()

        self.load_database = tk.Button(self, text="Load Database", command=lambda: controller.open_frame("load database"))
        self.load_database.pack()

