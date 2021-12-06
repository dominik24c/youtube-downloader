import os.path
from tkinter import Label
from tkinter.ttk import Progressbar

from pytube import YouTube, Stream
from pytube.exceptions import RegexMatchError, \
    VideoUnavailable

VIDEO_LINK_ERR_NOT_VALID_LINK = 'Video link is not valid'
VIDEO_LINK_ERR_NOT_UNAVAILABLE = 'Video is unavailable'
VIDEO_LINK_ERR_UNKNOWN_ERROR = 'Unknown error'


class YoutubeDownloader:
    def __init__(self):
        self._downloader: YouTube
        self._video_link = None
        self._error = None
        self._previous_progress = None
        self._progressbar: Progressbar
        self._progressbar_label: Label

    @property
    def error(self) -> str:
        return self._error

    @property
    def video_link(self) -> str:
        return self._video_link

    @video_link.setter
    def video_link(self, value: str):
        self._video_link = value

    def validate_video_link(self) -> None:
        try:
            self._previous_progress = 0
            self._downloader = YouTube(self._video_link, on_progress_callback=self.on_progress)
            self._downloader.check_availability()
            self._error = None
        except RegexMatchError:
            self._error = VIDEO_LINK_ERR_NOT_VALID_LINK
        except VideoUnavailable:
            self._error = VIDEO_LINK_ERR_NOT_UNAVAILABLE
        except Exception:
            self._error = VIDEO_LINK_ERR_UNKNOWN_ERROR

    def download(self, output_path: str, progressbar: Progressbar, progressbar_label: Label) -> None:
        try:
            self._progressbar = progressbar
            self._progressbar_label = progressbar_label
            mp4 = self._downloader.streams.filter(file_extension='mp4').first()
            filename = self._rename_filename_if_exists(output_path, mp4.default_filename)
            mp4.download(output_path=output_path, filename=filename)
        except Exception as e:
            print(e)
            print('error')

    def on_progress(self, stream: Stream, chunk: bytes, bytes_remaining: int) -> None:
        total_size = stream.filesize
        downloaded_data = total_size - bytes_remaining

        current_progress = int(downloaded_data / total_size * 100)
        if current_progress > self._previous_progress:
            self._previous_progress = current_progress
            self._progressbar['value'] = self._previous_progress
            self._progressbar_label['text'] = f'Downloaded data: {self._previous_progress}%'
            print(f'{self._previous_progress}%')

    def _rename_filename_if_exists(self, path: str, default_filename: str) -> str:
        filename = default_filename
        original_filename, _, _ = filename.rpartition(".mp4")
        index = 1
        while os.path.exists(os.path.join(path, filename)):
            filename_tmp, extension, _ = filename.rpartition(".mp4")
            filename = f'{original_filename}({index}){extension}'
            print(filename)
            index += 1

        return filename
