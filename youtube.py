from pytubefix import YouTube
from pytubefix.cli import on_progress

link = input("Enter YouTube video link: ")

try:
    yt = YouTube(link, on_progress_callback=on_progress)
    stream = yt.streams.get_highest_resolution()
    stream.download(output_path="downloads")
    print(f"Downloaded: {yt.title}")
except Exception as e:
    print(f"Error: {e}")
