from tkinter import *
from tkinter import filedialog

from .buttons import ButtonFactory


class DirectoryBrowserPage(Frame):
    def __init__(self, parent: Frame, root, **kwargs):
        super().__init__(master=parent, **kwargs)
        self.root = root

        label = Label(self, text='Choose directory path:')
        label.pack()

        self.directory_path_entry = Entry(self, width=50, state='disabled')
        self.directory_path_entry.pack()

        self.browse_btn = ButtonFactory.create_button(self, text='Browse', command=self.browse_handler)
        from .downloader_page import DownloaderPage
        from .validator_link_page import ValidatorLinkPage
        self.next_btn = ButtonFactory.create_button(self, text='Next',
                                                    command=lambda: root.show_frame(DownloaderPage.__name__),
                                                    is_packed=False)
        ButtonFactory.create_button(self, text='Back', command=lambda: root.show_frame(ValidatorLinkPage.__name__))

    def browse_handler(self) -> None:
        self.root.filename = filedialog.askdirectory()
        self.directory_path_entry['state'] = 'normal'
        self.directory_path_entry.delete(0, "end")
        self.directory_path_entry.insert(0, self.root.filename)
        self.directory_path_entry['state'] = 'disabled'
        if self.root.filename is None or self.root.filename == '':
            self.next_btn.forget()
        else:
            self.next_btn.pack()
