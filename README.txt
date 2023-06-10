This is a simple Python projects that downloads videos (video or audio) from YouTube

I decided to make this project because donwloading using free online tools 
became more and more unpleaseand. For this to work you will need to have
installed the pytube library

`- pip install pytube`

The scrips accepts as input either a single video from YouTube or a playlists.
When the users specifies a playlist, the script is using multithreaded code
in order to speed up the downloading process

How to use the scrips?

As i have mentioned you need to make sure you have the "pytube" library installed.
The script was created using the version 15.0.0

`pip install pytube==15.0.0`

Next, you need to provide a link to the YouTube video or playlist that you want
to download. This needs to be done in the "app.py" file in line 11 where the
class is instatiated

```python
link = YoutubeDownloader(youtube_link)
```

By using the above instructions, the script will download the video as an audio
file (this is made by default). If you want to change and save the video as
a video file (mp4) then after the link provided you will have to specify the
parameter "type" with the value "video" 

```python
link = YoutubeDownloader(youtube_link, type="video")
```

To start the process you need to run the "app.py" file as a Python script.
For this navigate in a command line interface in the location where you saved
the project and run the following:

`python3 app.py`

This will create a new directory in the current location with the name 
'YouTube_Downloads' where you will have all the downloaded files.