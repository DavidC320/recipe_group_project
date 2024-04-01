"""
4/1/2024
Frame Controller
---
This object allows for the control of child frames. Allowing swapping.
"""
import tkinter as tk
from .ChildFrameObject import ChildFrame

class FrameController(tk.Tk):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.dictionary_of_frames = {}
        self.current_frame = None
        self.frame_holder = tk.Frame(self)
        self.frame_holder.pack()


    # Adds a frame to the dictionary with the set key value
    def add_frame_to_dictionary(self, name_of_frame:str, frame:ChildFrame):
        self.dictionary_of_frames[name_of_frame] = frame


    # removes a frame from the dictionary with set key
    def remove_frame_from_dictionary(self, name_of_frame:str):
        self.dictionary_of_frames.pop(name_of_frame)
    
    # opens the new frame and closes the previous frame
    def open_frame(self, name_of_frame:str):
        new_frame = self.dictionary_of_frames.get(name_of_frame)
        if not new_frame:
            print("error " + name_of_frame)
            return

        if self.current_frame:
            if isinstance(self.current_frame, ChildFrame):
                self.current_frame.on_close()
        
        if isinstance(new_frame, ChildFrame):
                new_frame.on_open()
        print(name_of_frame)
        new_frame.tkraise()
        self.current_frame = new_frame


"""
references:

https://www.tutorialspoint.com/how-to-clear-out-a-frame-in-the-tkinter
How to clear a frame

https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
So this is how you swap

https://www.toppr.com/guides/python-guide/references/methods-and-functions/methods/built-in/isinstance/python-isinstance-2/
instance checking
"""