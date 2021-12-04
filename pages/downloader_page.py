from tkinter import *
from tkinter.ttk import Progressbar

from app.utils import threading_click_handler
from .base_page import BasePage


class DownloaderPage(BasePage):
    def __init__(self, parent: Frame, root, **kwargs):
        super().__init__(parent, root, **kwargs)

    def init_ui(self) -> None:
        self.init_gird((4, 4, 1), (1, 1))

        self.title_label = Label(self, text='Click "Download" button to start downloading file')
        self.progressbar = Progressbar(self, orient=HORIZONTAL, length=400, mode='determinate')
        self.download_btn = Button(self, text='Download File', command=self.download_handler)

        from . import DirectoryBrowserPage
        self.back_btn = Button(self, text='Back',
                               command=lambda: self.root.show_frame(DirectoryBrowserPage.__name__))

        self.progressbar_label = Label(self)
        self.back_to_beginning_page_btn = Button(self, text='Back', command=self.back_to_first_page)
        self.exit_btn = Button(self, text="Exit", command=self.root.destroy)

        self.title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=5, sticky=S)
        self.download_btn.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky=N)
        self.back_btn.grid(row=2, column=0, padx=10, pady=10, sticky=SW)

    @threading_click_handler()
    def download_handler(self) -> None:
        self.back_btn['state'] = 'disabled'
        self.download_btn['state'] = 'disabled'
        [widget.grid_forget() for widget in (self.title_label, self.download_btn, self.back_btn)]
        self.progressbar.grid(row=0, column=0, columnspan=2, padx=10, pady=5, sticky=S)
        self.progressbar_label.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky=N)
        self.root.yt_downloader.download(self.root.filename, self.progressbar, self.progressbar_label)

        self.exit_btn.grid(row=2, column=1, padx=10, pady=10, sticky=SE)
        self.back_to_beginning_page_btn.grid(row=2, column=0, padx=10, pady=10, sticky=SW)

    def back_to_first_page(self) -> None:
        self.root.init_frames()  # reset/recreate frames
