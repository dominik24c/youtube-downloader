from tkinter import *

from .buttons import ButtonFactory
from .utils import threading_click_handler


class ValidatorLinkPage(Frame):
    def __init__(self, parent: Frame, root, **kwargs):
        super().__init__(master=parent, **kwargs)
        self.root = root
        label = Label(self, text='Enter Link:')
        label.pack()

        self.yt_link = StringVar()
        self.yt_link.trace('w', self.on_changed_entry_field)
        yt_link_entry = Entry(self, width=50, textvariable=self.yt_link)
        yt_link_entry.bind('<Control-KeyRelease-a>', self.ctrl_a_handler)
        yt_link_entry.bind('<Control-a>', self.ctrl_a_handler)
        yt_link_entry.pack()
        self.response_label = Label(self)
        self.validator_btn = Button(self, text='Validate link', command=self.validate_link)
        self.validator_btn.pack()

        from .directory_browser_page import DirectoryBrowserPage
        self.next_btn = ButtonFactory.create_button(self, text='Next',
                                                    command=lambda:
                                                    root.show_frame(DirectoryBrowserPage.__name__),
                                                    is_packed=False)

    def on_changed_entry_field(self, *args, **kwargs) -> None:
        self.next_btn.forget()
        self.response_label.forget()

    @threading_click_handler()
    def validate_link(self) -> None:
        self.root.yt_downloader.video_link = self.yt_link.get()
        self.root.yt_downloader.validate_video_link()

        if self.root.yt_downloader.error is not None:
            # print(self.root.yt_downloader.error)
            self.response_label['text'] = f'{self.root.yt_downloader.error}!'
            self.response_label.pack()
        else:
            self.next_btn.pack()
            self.response_label['text'] = f'Your Link is valid. Click "Next" button.'
            self.response_label.pack()
            # self.response_label.forget()

    def ctrl_a_handler(self, event: Event) -> None:
        event.widget.select_range(0, 'end')
        event.widget.icursor('end')
