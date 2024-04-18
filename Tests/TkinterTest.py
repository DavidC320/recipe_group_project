"""
4/1/2024
https://youtu.be/YXPyB4XeYLA?si=2Xi7yhMSZ4A5mb4k
Code based off of this video
"""
import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath("tkinter_objects\\__init__.py"))
sys.path.append(os.path.dirname(SCRIPT_DIR))
import tkinter as tk
from tkinter_objects.ControllerMainObject import *
"""
root = tk.Tk()

myLabel = tk.Label(root, text="Fun")
myLabel.pack()

root.mainloop()"""

root = FrameController()

start_screen = ChildFrame(root.frame_holder, root)
tk.Label(start_screen, text="Start Screen").pack()
tk.Button(start_screen, text="Go to page 1", command=lambda:root.open_frame("next screen")).pack()
start_screen.grid(column=0, row=0, sticky="nsew")
root.add_frame_to_dictionary("start screen", start_screen)

next_page = ChildFrame(root.frame_holder, root)
tk.Label(next_page, text="Page 1").pack()
tk.Button(next_page, text="Back to start", command=lambda:root.open_frame("start screen")).pack()
next_page.grid(column=0, row=0, sticky="nsew")
root.add_frame_to_dictionary("next screen", next_page)
print(root.dictionary_of_frames)

root.open_frame("start screen")


root.mainloop()