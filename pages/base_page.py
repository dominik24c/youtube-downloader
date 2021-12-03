import abc
from tkinter import Frame


class BasePage(Frame):
    def __init__(self, master: Frame, root, **kwargs):
        super().__init__(master=master, **kwargs)
        self.root = root
        self.init_ui()

    @abc.abstractmethod
    def init_ui(self) -> None:
        raise NotImplemented

    def init_gird(self, row_weights: tuple, column_weights: tuple) -> None:
        for index, (c, r) in enumerate(zip(column_weights, row_weights)):
            self.columnconfigure(index, weight=c)
            self.rowconfigure(index, weight=r)
