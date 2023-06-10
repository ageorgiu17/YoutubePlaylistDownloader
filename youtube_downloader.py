"""
**youtube_downloader** = Python script that downloads videos or sounds from
Youtube
============================================================================
youtube_downloader is a Python script that allows downloading either videos
(mp4) or audios (mp3) from a YouTube link. The scrips allows either a normal
link or a playlist link and knows how to differentiate the 2 and in the case
of a playlist it uses Multithreded code to download the videos ar audios
faster
"""


from concurrent.futures import ThreadPoolExecutor
from typing import Union

import pytube
from pytube import Playlist, YouTube


class YoutubeDownloader:
    """
    Class that is responsible for downloading video or audio files from a
    YouTube link

    Parameters
    ----------
    link: str
        The link of the YouTube video or playlist
    type: str="audio"
        Represents the type of file to download. By default it is set to 'audio'
        but can be changed to 'video' if the user wants to download the video

    Attributes
    ----------
    link: str
        The link of the YouTube video or playlist
    type: str
        Represents the type of file to download. By default it is set to 'audio'
        but can be changed to 'video' if the user wants to download the video
    link_type: str
        Represents the type of the link offered by the user. This can be either
        a normal link, either a playlist link from YouTube

    Methods
    -------
    download_sound(self, link: Union[pytube.YouTube, pytube.Playlist]) -> None:
        Method used to download an audio file from YouTube
    download_video(self, link: Pytube.Youtube())
        Method used to download a video file from YouTube
    check_link(self) -> str:
        Method that checks if the provided link is a normal link or a playlist
        link
    download_link(self) -> None:
        Method that downloads a video or audio file for a single YouTube link
    download_playlist(self) -> None:
        Method that downloads all the video or audio files from a YouTube
        playlist link
    download(self) -> None:
        Method that starts the process of downlaoding audio or video files
        based on the link type
    """

    DOWNLOAD_DIR = "./Sounds"

    def __init__(self, link, type="audio"):
        """
        Method that initializes the class and sets the attributes of the
        instance

        Parameters
        ----------
        link: str
            The link of the YouTube video or playlist
        type: str="audio"
            Represents the type of file to download. By default it is set to
            'audio' but can be changed to 'video' if the user wants to download
            the video
        link_type: str
            Represents the type of the link offered by the user. This can be
            either a normal link, either a playlist link from YouTube
        """

        self.link = link
        self.type = type
        self.link_type = self.check_link()

    def download_sound(self, link: Union[pytube.YouTube, pytube.Playlist]) -> None:
        """
        Method used to download an audio file from YouTube

        Parameters
        ----------
        link: Union[pytube.YouTube, pytube.Playlist]
            The link of the YouTube audio to be downloaded

        Returns
        -------
        None
        """
        print(f"Downloading audio for (link method) {link.title}...")
        link.streams.filter(only_audio=True).first().download(self.DOWNLOAD_DIR)

    def download_video(self, link):
        """
        Method used to download a video file from YouTube

        Parameters
        ----------
        link: Union[pytube.YouTube, pytube.Playlist]
            The link of the YouTube video to be downloaded

        Returns
        -------
        None
        """
        print(f"Downloading video for (link method) {link.title}...")
        link.streams.get_highest_resolution().download(self.DOWNLOAD_DIR)

    def check_link(self, link: str) -> str:
        """
        Method that checks if the provided link is a normal link or a playlist
        link

        Parameters
        ----------
        link: str
            The link that needs to be verified

        Returns
        -------
        str
            A string representing the link type (normal link or playlist link)

        Example
        -------
        >>>check_link(https://www.youtube.com/watch?v=zUqxUSuCoQQ)
        'link'
        >>>check_link(
            https://www.youtube.com/watch?v=FlUCU13dJyo&list=PL4cUxeGkcC9gsJS5QgFT2IvWIX78dV3_v
        )
        'playlist'
        """
        if "list" in link:
            return "playlist"
        else:
            return "link"

    def download_link(self) -> None:
        """
        Method that downloads a video or audio file for a single YouTube link

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        link = YouTube(self.link)

        try:
            if self.type == "audio":
                self.download_sound(link)

            else:
                self.download_video()

            print(
                f'Finished downloading. The file can be found in {self.DOWNLOAD_DIR.lstrip("./")} directory'
            )
        except Exception as e:
            print("An exception ocurred while trying to download the video: ", e)

    def download_playlist(self):
        """
        Method that downloads all the video or audio files from a YouTube
        playlist link.
        The method uses Multithreaded code to speed up the download process
        for a Youtube playlist

        Parameters
        ----------
        None

        Returns
        -------
        None
        """

        playlist_link = Playlist(self.link)

        try:
            if self.type == "audio":
                with ThreadPoolExecutor() as executor:
                    executor.map(self.download_sound, playlist_link.videos)

            elif self.type == "video":
                with ThreadPoolExecutor() as executor:
                    executor.map(self.download_video, playlist_link.video)

            print(
                f'Finished downloading. The files can be found in {self.DOWNLOAD_DIR.lstrip("./")} directory'
            )
        except Exception as e:
            print("An exception ocurred while trying to download the video: ", e)

    def download(self):
        """
        Method that starts the process of downlaoding audio or video files
        based on the link type

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        if self.link_type == "link":
            self.download_link()

        elif self.link_type == "playlist":
            self.download_playlist()
