import abc
from tkinter import Frame


class BasePage(Frame):
    def __init__(self, master: Frame, root, **kwargs):
        super().__init__(master=master, **kwargs)
        self.root = root
        self.init_ui()

    @abc.abstractmethod
    def init_ui(self):
        raise NotImplemented
