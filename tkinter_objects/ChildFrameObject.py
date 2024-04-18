""" 
3/28/2024
 Child Frame Object
"""
import tkinter as tk

class ChildFrame(tk.Frame):
    def __init__(self, master, controller, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.controller = controller

    def on_open(self):
        '''
        Does an action when the frame is opened by the frame manager.
        '''

    def can_close(self) -> bool:
        '''
        Checks if the child frame can be opened
        '''
        return True

    def on_close(self):
        '''
        Does an action when the frame is closed by the frame manager.
        '''

    

"""
References:
https://www.programiz.com/python-programming/inheritance

https://www.geeksforgeeks.org/args-kwargs-python/
I remembered something about this
"""
