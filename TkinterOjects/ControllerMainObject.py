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
        self.basic_frame = tk.Frame(self)
        self.basic_frame.pack()
        self.frame_holder = tk.Frame(self)
        self.frame_holder.pack()


    def add_frame_to_dictionary(self, name_of_frame:str, frame:tk.Frame):
        '''
        Adds a frame into the dictionary with a name key
        '''
        self.dictionary_of_frames[name_of_frame] = frame


    def add_frame_direct(self, name_of_frame:str, frame:tk.Frame):
        frame.grid(column=0, row=0, sticky="nsew")
        self.add_frame_to_dictionary(name_of_frame, frame)


    def remove_frame_from_dictionary(self, name_of_frame:str):
        '''
        Removes the frame from the dictionary with a name key
        '''
        self.dictionary_of_frames.pop(name_of_frame)
    
    # opens the new frame and closes the previous frame
    def open_frame(self, name_of_frame:str):
        '''
        Opens the new frame from the name key and closes the previous frame unless the previous frame can't be closed.
        '''
        new_frame = self.dictionary_of_frames.get(name_of_frame)

        if not new_frame:  # stops the action if the no frame is found
            print("error " + name_of_frame)
            return

        if self.current_frame:  # close the previous frame if available
            if isinstance(self.current_frame, ChildFrame):
                if self.current_frame.can_close():
                    self.current_frame.on_close()
                else:
                    print("Error with frame " + name_of_frame)
        
        if isinstance(new_frame, ChildFrame):  # activates the child frame's open action.
                new_frame.on_open()
        
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