from tkinter import *
from tkinter.ttk import Progressbar

from app.utils import threading_click_handler
from .base_page import BasePage


class DownloaderPage(BasePage):
    def __init__(self, parent: Frame, root, **kwargs):
        super().__init__(parent, root, **kwargs)

    def init_ui(self):
        self.init_gird((1,), (1,))
        title_label = Label(self, text='Click "Download" button to start downloading file')
        title_label.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

        self.progressbar = Progressbar(self, orient=HORIZONTAL, length=400, mode='determinate')

        self.download_btn = Button(self, text='Download File', command=self.download_handler)
        self.download_btn.grid(row=1, column=0, padx=10, pady=5, sticky=NSEW)
        from .directory_browser_page import DirectoryBrowserPage
        self.back_btn = Button(self, text='Back',
                               command=lambda: self.root.show_frame(DirectoryBrowserPage.__name__))
        self.progressbar_label = Label(self)

    @threading_click_handler()
    def download_handler(self) -> None:
        self.back_btn['state'] = 'disabled'
        self.download_btn['state'] = 'disabled'
        self.download_btn['text'] = 'Downloading...'
        self.progressbar.grid()
        self.progressbar_label.grid()
        self.root.yt_downloader.download(self.root.filename, self.progressbar, self.progressbar_label)
        self.download_btn['text'] = 'Download'
        self.download_btn['state'] = 'normal'
        self.back_btn['state'] = 'normal'
