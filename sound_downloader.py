"""
This python file will be responsible for downloading the sound of one youtube video
"""

import pytube

class SoundDownloader():
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

    
    def download_link_sound(self):
        """
        Downloads the video
        """

        DOWNLOAD_SOUND_DIR = './Sounds'

        try:
            print('Downloading the sound ...')
            self.link.streams.filter(only_audio=True).first().download(DOWNLOAD_SOUND_DIR)
            print(f'Finished downloading the sound. It can be seen in {DOWNLOAD_SOUND_DIR.lstrip("./")} directory')
        except Exception as e:
            print('An exception ocurred while trying to download the video: ', e)