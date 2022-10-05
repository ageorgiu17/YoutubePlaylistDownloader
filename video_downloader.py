"""
This python file will be responsible for downloading only one video from YouTube
"""

import pytube

class VideoDownloader():

    def __init__(self, link):
        self.link = pytube.YouTube(link)

    
    def download_link(self):
        try:
            self.link.download()
        except:
            pass
