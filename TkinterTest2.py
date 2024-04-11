import tkinter as tk
from TkinterOjects.ControllerMainObject import *

class IntroPage(ChildFrame):
    def __init__(self, master, controller, **kwargs) -> None:
        super().__init__(master, controller, **kwargs)
        tk.Label(self, text="Home Page").pack()
        self.next_page_button = tk.Button(self, text="Next page", command=lambda:controller.open_frame("page 1"))
        self.next_page_button.pack()

class CountPage(ChildFrame):
    def __init__(self, master, controller, **kwargs) -> None:
        super().__init__(master, controller, **kwargs)
        self.count = 0
        tk.Label(self, text="Page 1").pack()
        self.count_label = tk.Label(self, text= "You have entered this page 0 times")
        self.count_label.pack()
        self.next_page_button = tk.Button(self, text="page 1", command=lambda:controller.open_frame("intro"))
        self.next_page_button.pack()
    
    def on_close(self):
        self.count += 1
    
    def on_open(self):
        self.count_label.config(text=f"You have entered this page {self.count} times")



root = FrameController()

intro_page = IntroPage(root.frame_holder, root)
intro_page.grid(column=0, row=0, sticky="nsew")
root.add_frame_to_dictionary("intro", intro_page)

count_page = CountPage(root.frame_holder, root)
count_page.grid(column=0, row=0, sticky="nsew")
root.add_frame_to_dictionary("page 1", count_page)

root.open_frame("intro")
root.mainloop()