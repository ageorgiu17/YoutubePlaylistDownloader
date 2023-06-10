"""
This python file will be responsible for downloading the sound of one youtube video
"""

from pytube import Playlist, YouTube
from concurrent.futures import ThreadPoolExecutor

class YoutubeDownloader():

    DOWNLOAD_DIR = './Sounds'

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

    def __init__(self, link, type="audio"):
        """
        Parameters
        ----------
        link: str
            The YouTube video link
        """

        self.link = link
        self.type = type
        self.link_type = self.check_link()

    def download_sound(self, link):
        print(f'Downloading audio for (link method) {link.title}...')
        link.streams.filter(only_audio=True).first().download(self.DOWNLOAD_DIR)

    def download_video(self, link):
        print(f'Downloading video for (link method) {link.title}...')
        link.streams.get_highest_resolution().download(self.DOWNLOAD_DIR)

    def check_link(self):
        if 'list' in self.link:
            return 'playlist'
        else:
            return 'link'
        
    
    def download_link(self):
        """
        Downloads the video
        """
        link = YouTube(self.link)

        try:
            if self.type == "audio":
                self.download_sound(link)

            else:
                self.download_video()

            print(f'Finished downloading. The file can be found in {self.DOWNLOAD_DIR.lstrip("./")} directory')
        except Exception as e:
            print('An exception ocurred while trying to download the video: ', e)

    
    def download_playlist(self):
        """
        Downloads a playlist
        """

        playlist_link = Playlist(self.link)

        try:
            if self.type == "audio":
                with ThreadPoolExecutor() as executor:
                    executor.map(self.download_sound, playlist_link.videos)

            elif self.type == "video":
                with ThreadPoolExecutor() as executor:
                    executor.map(self.download_video, playlist_link.video)

            print(f'Finished downloading. The files can be found in {self.DOWNLOAD_DIR.lstrip("./")} directory')
        except Exception as e:
            print('An exception ocurred while trying to download the video: ', e)

    
    def download(self):
        if self.link_type == 'link':
            self.download_link()
        
        elif self.link_type == 'playlist':
            self.download_playlist()

