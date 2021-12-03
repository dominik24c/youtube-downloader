import abc
from tkinter import Frame

from itertools import zip_longest

class BasePage(Frame):
    def __init__(self, master: Frame, root, **kwargs):
        super().__init__(master=master, **kwargs)
        self.root = root
        self.init_ui()

    @abc.abstractmethod
    def init_ui(self) -> None:
        raise NotImplemented

    def init_gird(self, row_weights: tuple, column_weights: tuple) -> None:
        for index, (c, r) in enumerate(zip_longest(column_weights, row_weights)):
            if c is not None:
                self.columnconfigure(index, weight=c)
            if r is not None:
                self.rowconfigure(index, weight=r)
