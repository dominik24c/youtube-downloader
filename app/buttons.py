from tkinter import *


class ButtonFactory:
    @staticmethod
    def create_button(parent, text: str, command: callable, is_packed:bool = True) -> Button:
        btn = Button(parent, text=text, command=command)
        if is_packed:
            btn.pack()
        return btn
