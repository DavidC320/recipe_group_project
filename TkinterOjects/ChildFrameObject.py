""" 
3/28/2024
 Child Frame Object
"""
import tkinter as tk

class ChildFrame(tk.Frame):
    def __init__(self, master: tk.Misc | None = None, cnf: dict[str, Any] | None = ..., *, background: str = ..., bd: str | float = 0, bg: str = ..., border: str | float = 0, borderwidth: str | float = 0, class_: str = "Frame", colormap: tk.Misc | Literal['new'] | Literal[''] = "", container: bool = False, cursor: str | tuple[str] | tuple[str, str] | tuple[str, str, str] | tuple[str, str, str, str] = "", height: str | float = 0, highlightbackground: str = ..., highlightcolor: str = ..., highlightthickness: str | float = 0, name: str = ..., padx: str | float = 0, pady: str | float = 0, relief: Literal['raised'] | Literal['sunken'] | Literal['flat'] | Literal['ridge'] | Literal['solid'] | Literal['groove'] = "flat", takefocus: bool | Callable[[str], bool | None] | Literal[0] | Literal[1] | Literal[''] = 0, visual: str | tuple[str, int] = "", width: str | float = 0) -> None:
        super().__init__(master, cnf, background=background, bd=bd, bg=bg, border=border, borderwidth=borderwidth, class_=class_, colormap=colormap, container=container, cursor=cursor, height=height, highlightbackground=highlightbackground, highlightcolor=highlightcolor, highlightthickness=highlightthickness, name=name, padx=padx, pady=pady, relief=relief, takefocus=takefocus, visual=visual, width=width)

    """Updates the frame when opened. Controlled my the frame manager."""    
    def on_open():
        pass

    """
    What Happens when the frame is closed. Must return a boolean for the frame manager.
    true - Can close
    false - Can close due to something I.E. The user forgot to enter a value in the recipe.
    """
    def on_close() -> bool:
        return True

    

"""
References:
https://www.programiz.com/python-programming/inheritance
"""
