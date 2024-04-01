""" 
3/28/2024
 Child Frame Object
"""
import tkinter as tk

class ChildFrame(tk.Frame):
    def __init__(self, master, controller, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.controller = controller

    """Updates the frame when opened. Controlled my the frame manager."""    
    def on_open(self):
        pass

    """
    What Happens when the frame is closed. Must return a boolean for the frame manager.
    true - Can close
    false - Can close due to something I.E. The user forgot to enter a value in the recipe.
    """
    def on_close(self) -> bool:
        return True

    

"""
References:
https://www.programiz.com/python-programming/inheritance

https://www.geeksforgeeks.org/args-kwargs-python/
I remembered something about this
"""
