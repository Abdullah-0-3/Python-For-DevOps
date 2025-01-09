from pytube import YouTube
from pytube import Playlist

def download_video(url, dest='./videos/'):
    yt = YouTube(url)

    try:
        video = yt.streams.filter(progressive=True, file_extension='mp4').first()
        title = yt.title
        views = yt.views
        filename = f"{title} - {views}.mp4"
        video.download(output_path=dest, filename=filename)
        print(f"Downloaded {filename}")
    except Exception as e:
        print(f"Error downloading video: {e}")

if __name__ == '__main__':
    download_video('https://www.youtube.com/watch?v=9bZkp7q19f0')