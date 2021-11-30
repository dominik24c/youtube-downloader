from yt_downloader import YoutubeDownloader


def main():
    print('start')
    link = input()
    yt = YoutubeDownloader(link)
    yt.validate_video_link()
    yt.download('path')
    print('end')


if __name__ == '__main__':
    main()
