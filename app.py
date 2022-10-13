"""
The scope of this project is to be abel to download either a video from YouTube, either only the audio for that video (used for music)
To be more effective, this will have the ability to download either one video at a time, either an entire playlist

When we will dowload the entire playlist, most likely I will implement some sort of multithreading to work faster
"""

from video_downloader import VideoDownloader
from sound_downloader import SoundDownloader

if __name__ == '__main__':
    link = SoundDownloader('https://www.youtube.com/watch?v=aa4738xvHJ0')
    link.download_link_sound()

