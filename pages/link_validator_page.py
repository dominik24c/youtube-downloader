from tkinter import *

from app.utils import threading_click_handler
from .base_page import BasePage


class LinkValidatorPage(BasePage):
    def __init__(self, parent: Frame, root, **kwargs):
        super().__init__(parent, root, **kwargs)

    def init_ui(self)->None:
        self.init_gird((1, 1, 10), (1, 4, 1))

        Label(self, text='Enter Link:').grid(row=0, column=0, sticky=W, pady=10, padx=10)

        self.yt_link = StringVar()
        self.yt_link.trace('w', self.on_changed_entry_field)
        yt_link_entry = Entry(self, textvariable=self.yt_link)
        yt_link_entry.bind('<Control-KeyRelease-a>', self.ctrl_a_handler)
        yt_link_entry.bind('<Control-a>', self.ctrl_a_handler)
        yt_link_entry.grid(row=0, column=1, columnspan=2, pady=10, padx=10, sticky=EW)
        self.response_label = Label(self)
        self.validator_btn = Button(self, text='Validate link', command=self.validate_link)
        self.validator_btn.grid(row=1, column=2, sticky=E, pady=5, padx=10)

        from .directory_browser_page import DirectoryBrowserPage
        self.next_btn = Button(self, text='Next', command=lambda:
        self.root.show_frame(DirectoryBrowserPage.__name__))

    def on_changed_entry_field(self, *args, **kwargs) -> None:
        self.next_btn.forget()
        self.response_label.forget()

    @threading_click_handler()
    def validate_link(self) -> None:
        self.root.yt_downloader.video_link = self.yt_link.get()
        self.root.yt_downloader.validate_video_link()

        max_row, max_column = self.grid_size()

        if self.root.yt_downloader.error is not None:
            self.response_label['text'] = f'{self.root.yt_downloader.error}!'
        else:
            self.response_label['text'] = f'Your Link is valid. Click "Next" button.'
            self.next_btn.grid(row=max_row, column=2, sticky=SE, padx=10, pady=10)
        self.response_label.grid(row=1, column=1, sticky=W, pady=10, padx=10)

    def ctrl_a_handler(self, event: Event) -> None:
        event.widget.select_range(0, 'end')
        event.widget.icursor('end')
