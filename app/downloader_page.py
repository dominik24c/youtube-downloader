from tkinter import *

from .buttons import ButtonFactory
from .utils import threading_click_handler


class DownloaderPage(Frame):
    def __init__(self, parent: Frame, root, **kwargs):
        super().__init__(master=parent, **kwargs)
        self.root = root
        label = Label(self, text='Click "Download" button to start downloading file')
        label.pack()

        self.download_btn = ButtonFactory.create_button(self, text='Download File', command=self.download_handler)
        from .directory_browser_page import DirectoryBrowserPage
        self.back_btn = ButtonFactory.create_button(self, text='Back',
                                                    command=lambda: root.show_frame(DirectoryBrowserPage.__name__))

    @threading_click_handler()
    def download_handler(self) -> None:
        self.back_btn['state'] = 'disabled'
        self.download_btn['state'] = 'disabled'
        self.download_btn['text'] = 'Downloading...'
        self.root.yt_downloader.download(self.root.filename)
        self.download_btn['text'] = 'Download'
        self.download_btn['state'] = 'normal'
        self.back_btn['state'] = 'normal'
