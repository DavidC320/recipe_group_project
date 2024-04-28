import tkinter as tk
import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath("tkinter_objects\\__init__.py"))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from tkinter_objects.ControllerMainObject import *
from TableObjects import *
from tkinter import filedialog as fd 

class InitDatabaseScreen(ChildFrame):
    '''
    Screen used to create a database for the user
    '''
    def __init__(self, master, controller, create_mode=True, **kwargs) -> None:
        super().__init__(master, controller, **kwargs)

        # values
        self.mode = create_mode
        self.file_path = ""
        self.key_path = ""

        title_text = ""
        if create_mode:
            title_text = "Create Database"
        else:
            title_text = "Load Database"
        tk.Label(self, text=title_text).pack()

        self.create_database_button = tk.Button(self, text="Select database file destination", command=self.select_destination)
        self.create_database_button.pack()
        self.filepath_label = tk.Label(self, text="//filepath/?")
        self.filepath_label.pack()

        self.create_key_button = tk.Button(self, text="Select key file destination", command=self.select_destination_key)
        self.create_key_button.pack()
        self.key_path_label = tk.Label(self, text="//filepath/?")
        self.key_path_label.pack()

        button_text = ''
        if create_mode:
            button_text = 'Create'
        else:
            button_text = 'Load'

        self.create_button = tk.Button(self, text=button_text, command=self.create_database)
        self.create_button.pack()

        self.back_button = tk.Button(self, text="Back", command=lambda: controller.open_frame("start"))
        self.back_button.pack()
    

    def on_close(self):
        self.file_path = ""
        self.key_path = ""
        self.filepath_label.config(text= "//filepath/?")
        self.key_path_label.config(text= "//filepath/?")
    

    def create_database(self):
        '''
        Creates the sqlite database with the path
        '''
        invalid_database_path = self.file_path in ["", "//filepath/?"]
        invalid_key_path = self.key_path in ["", "//filepath/?"]

        if not invalid_database_path and not invalid_key_path:
            self.controller.connect_to_file(self.file_path, self.mode)
            if self.mode:
                self.controller.generate_byte_key()
                self.controller.save_byte_key(self.key_path)
            else:
                self.controller.load_byte_key(self.key_path)

            connection : SqliteConnecter = self.controller.get_connector()
            connection.c.execute("SELECT * FROM users")

            if len(connection.c.fetchall()) == 0:
                self.controller.open_frame("create admin")
            else:
                self.controller.open_frame("main menu")

        # Errors
        if invalid_database_path:
            self.filepath_label.config(text= "Select a file path")
        else:
            self.filepath_label.config(text= "//filepath/?")
        
        if invalid_key_path:
            self.key_path_label.config(text= "Select a file path")
        else:
            self.key_path_label.config(text= "//filepath/?")


    def select_destination(self):
        '''
        Asks the user to select where they want to save the file.
        '''
        data = ''
        if self.mode:
            data = fd.asksaveasfilename(title="Select where you want to save the file.", 
                                        defaultextension="*.db",
                                        filetypes= [("Database File", "*.db")]
                                        )
        else:
            data = fd.askopenfilename(title="Select the file you want to load.", 
                                        defaultextension="*.db",
                                        filetypes= [("Database File", "*.db")]
                                        )
        if data != "":  # checks if the user didn't just close the window
            self.file_path = data
            self.filepath_label.config(text= data)
    

    def select_destination_key(self):
        '''
        Asks the user to select where they want to save the file.
        '''
        data = ''
        if self.mode:
            data = fd.asksaveasfilename(title="Select where you want to save the file.", 
                                        defaultextension="*.ky",
                                        filetypes= [("Key File", "*.ky")]
                                        )
        else:
            data = fd.askopenfilename(title="Select the file you want to load.", 
                                        defaultextension="*.ky",
                                        filetypes= [("Key File", "*.ky")]
                                        )
        if data != "":  # checks if the user didn't just close the window
            self.key_path = data
            self.key_path_label.config(text= data)
