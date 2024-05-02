import tkinter as tk
from tkinter import ttk
import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath("tkinter_objects\\__init__.py"))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from cryptography.fernet import Fernet

from tkinter_objects.ControllerMainObject import *
from TableObjects import *

class Login(ChildFrame):
    def __init__(self, master, controller, **kwargs) -> None:
        super().__init__(master, controller, **kwargs)
        # values
        self.username = tk.StringVar()
        self.password = tk.StringVar()

        tk.Label(self, text="Login").grid(row=0, column=0, columnspan=2)

        tk.Label(self, text="Username").grid(row=1, column=0)
        self.username_entry = tk.Entry(self, textvariable=self.username)
        self.username_entry.grid(row=1, column=1)

        tk.Label(self, text="Password").grid(row=2, column=0)
        self.password_entry = tk.Entry(self, textvariable=self.password, show='*')
        self.password_entry.grid(row=2, column=1)

        self.error_label = tk.Label(self)
        self.error_label.grid(row=3, column=0, columnspan=2)

        self.control_frame = tk.Frame(self)
        self.control_frame.grid(row=4, column=0, columnspan=2)

        self.create_button = tk.Button(self.control_frame, text="Login", command=self.login)
        self.create_button.grid(row=0, column=0)

        self.back_button = tk.Button(self.control_frame, text="Back", command=lambda: controller.open_frame("main menu"))
        self.back_button.grid(row=0, column=1)


    def on_open(self):
        self.username.set("")
        self.password.set("")
        self.error_label.config(text="")

    def login(self):
        trim_username_check = len(self.username.get().strip()) > 5
        trim_password_check = len(self.password.get().strip()) > 5

        if not trim_username_check:
            self.error_label.config(text="Username must be at least 5 characters long")
            return
        if not trim_password_check:
            self.error_label.config(text="Password must be at least 5 characters long")
            return

        fernet : Fernet = self.controller.get_fernet()

        connection : SqliteConnecter = self.controller.get_connector()
        connection.c.execute(f"""SELECT * FROM users
                             Where username = '{self.username.get().strip()}';""")
        data = connection.c.fetchone()
        if data:
            if fernet.decrypt(data[2]).decode() == self.password.get().strip():
                self.controller.logged_in = True
                self.controller.open_frame('main menu')
            else:
                self.error_label.config(text="Username or password doesn't match")
        else:
            self.error_label.config(text="Username or password doesn't match")