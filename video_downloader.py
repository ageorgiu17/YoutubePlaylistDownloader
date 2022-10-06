"""
This python file will be responsible for downloading only one video from YouTube
"""

import pytube


class VideoDownloader():
    """
    Class that is responsible for downloading videos from YouTube

    Attributes
    ----------
    link: str
        The YouTube video link
    
    Methods
    -------
    download_link
        Downloads the video
    """

    def __init__(self, link):
        """
        Parameters
        ----------
        link: str
            The YouTube video link
        """

        self.link = pytube.YouTube(link)

    
    def download_link(self):
        """
        Downloads the video
        """

        DOWNLOAD_VIDEO_DIR = './Videos'

        try:
            print('Downloading the video...')
            # self.link.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(DOWNLOAD_VIDEO_DIR)
            self.link.streams.get_highest_resolution().download(DOWNLOAD_VIDEO_DIR)
            print(f'Finished downloading the video. It can be seen in {DOWNLOAD_VIDEO_DIR.lstrip("./")} directory')
        except Exception as e:
            print('An exception ocurred while trying to download the video: ', e)


