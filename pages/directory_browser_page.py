from tkinter import *
from tkinter import filedialog

from .base_page import BasePage


class DirectoryBrowserPage(BasePage):
    def __init__(self, parent: Frame, root, **kwargs):
        super().__init__(parent, root, **kwargs)

    def init_ui(self):
        row_weights = (1, 1, 1, 12)
        column_weights = (1, 4, 1)
        self.init_gird(row_weights, column_weights)

        label = Label(self, text='Choose directory path:')
        label.grid(row=0, column=0, padx=6, pady=10, sticky=W)

        self.directory_path_entry = Entry(self, state='disabled')
        self.directory_path_entry.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky=EW)

        self.browse_btn = Button(self, text='Browse', command=self.browse_handler)
        self.browse_btn.grid(row=2, column=2, padx=10, pady=5, sticky=E)
        from .downloader_page import DownloaderPage
        from .validator_link_page import ValidatorLinkPage
        self.next_btn = Button(self, text='Next', command=lambda: self.root.show_frame(DownloaderPage.__name__))
        self.back_btn = Button(self, text='Back', command=lambda: self.root.show_frame(ValidatorLinkPage.__name__))
        self.back_btn.grid(row=3, column=0, padx=10, pady=10, sticky=SW)

    def browse_handler(self) -> None:
        self.root.filename = filedialog.askdirectory()
        self.directory_path_entry['state'] = 'normal'
        self.directory_path_entry.delete(0, "end")
        self.directory_path_entry.insert(0, self.root.filename)
        self.directory_path_entry['state'] = 'disabled'
        if self.root.filename is None or self.root.filename == '':
            self.next_btn.forget()
        else:
            self.next_btn.grid(row=3, column=2, padx=10, pady=10, sticky=SE)
