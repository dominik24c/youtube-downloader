from pytube import YouTube
from pytube.exceptions import RegexMatchError, \
    VideoUnavailable

VIDEO_LINK_ERR_NOT_VALID_LINK = 'Video link is not valid'
VIDEO_LINK_ERR_NOT_UNAVAILABLE = 'Video is not unavailable'
VIDEO_LINK_ERR_UNKNOWN_ERROR = 'Unknown error'


class YoutubeDownloader:
    def __init__(self):
        self._downloader: YouTube
        self._video_link = None
        self._error = None

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
            self._downloader = YouTube(self._video_link)
            self._downloader.check_availability()
            self._error = None
        except RegexMatchError:
            self._error = VIDEO_LINK_ERR_NOT_VALID_LINK
        except VideoUnavailable:
            self._error = VIDEO_LINK_ERR_NOT_UNAVAILABLE
        except Exception:
            self._error = VIDEO_LINK_ERR_UNKNOWN_ERROR

    def download(self, dir_path: str) -> None:
        try:
            mp4 = self._downloader.streams.filter(file_extension='mp4').first()
            mp4.download(dir_path)
        except Exception:
            print('error')
