import sys
from tkinter import *
from typing import Dict

from settings import *
from yt_downloader import YoutubeDownloader
from .directory_browser_page import DirectoryBrowserPage
from .downloader_page import DownloaderPage
from .validator_link_page import ValidatorLinkPage


class Window(Tk):
    def __init__(self):
        super().__init__()
        self.init_window()
        self.init_container()
        self.frames: Dict[Frame] = {}
        self.init_frames()
        self.yt_downloader = YoutubeDownloader()
        self.dir_path: str

    def init_window(self) -> None:
        self.title(WINDOW_TITLE)
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = screen_height // 2 - WINDOW_HEIGHT // 2
        y = screen_width // 2 - WINDOW_WIDTH // 2
        self.geometry(f'{WINDOW_GEOMETRY}+{y}+{x}')

        if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
            img = PhotoImage(file=WINDOW_ICON)
            print('running in a PyInstaller bundle')
        else:
            img = PhotoImage(file=os.path.join(BASE_DIR, WINDOW_ICON))
            print('running in a normal Python process')

        self.tk.call('wm', 'iconphoto', self._w, img)

    def init_container(self) -> None:
        self.container = Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

    def init_frames(self) -> None:
        for Page in (DirectoryBrowserPage, ValidatorLinkPage, DownloaderPage):
            frame = Page(self.container, self, bg='red')
            self.frames[Page.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(ValidatorLinkPage.__name__)

    def show_frame(self, page_name: str) -> None:
        self.frames[page_name].tkraise()
