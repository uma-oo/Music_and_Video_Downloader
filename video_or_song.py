import os
from pytube import Playlist
from pytube import YouTube


class Video:

    def __init__(self, link: str, destination: str):
        assert isinstance(link, str), "The type of data is incorrect"
        assert isinstance(destination, str), "The type of data is incorrect"
        self.link = link
        self.destination = destination

    def filtering(self):
        file = YouTube(self.link)
        list_streams = file.streams.filter(progressive=True)
        return list_streams

    def download_file(self):
        list_streams = self.filtering()
        video = list_streams.get_highest_resolution()
        video.download(self.destination)
        print("Downloaded")


class Audio(Video):
    def __init__(self, link: str, destination: str):
        super().__init__(link, destination)

    def filtering(self):

        file = YouTube(self.link)
        list_streams = file.streams.filter(only_audio=True)
        return list_streams

    def download_file(self):
        list_streams = self.filtering()
        audio = list_streams.first()
        old_audio_ext = audio.download(self.destination)

        base, ext = os.path.splitext(old_audio_ext)
        new_audio = base + '.mp3'
        os.rename(old_audio_ext, new_audio)
        print("The audio has been successfully downloaded.")


class PlaylistVideo:
    def __init__(self, link, destination):
        self.link = link
        self.destination = destination

    def download_playlist(self):
        url_list = []
        video_list = []
        playlist = Playlist(self.link)
        for url in playlist.video_urls:
            url_list.append(url)
        for video in playlist.videos:
            video_list.append(video)
        join_list = dict(zip(url_list, video_list))  # the keys must be hashable so
        # we chose the url to be the key instead of the video
        for key, value in join_list.items():
            vid = Video(key, self.destination)
            vid.download_file()
        print("The playlist was successfully downloaded")


class PlaylistAudio(PlaylistVideo):
    def __init__(self, link, destination):
        super().__init__(link, destination)

    def download_playlist(self):
        url_list = []
        audio_list = []
        playlist = Playlist(self.link)
        for url in playlist.video_urls:
            url_list.append(url)
        for video in playlist.videos:
            audio_list.append(video)
        join_list = dict(zip(url_list, audio_list))
        for key, value in join_list.items():
            audio = Audio(key, self.destination)
            audio.download_file()
        print("The playlist was successfully downloaded")


if __name__ == "__main__":
    video = Video("https://youtu.be/1bHXyI88we4",
                  "C://Users//Minfo//OneDrive//Documents//My Recordings")
    video.download_file()
# playlist=Playlist_Audio("https://youtube.com/playlist?list=PLZgKgfug7rBubpEXpJcGfJsZr443bg_-Z",
# "C://Users//Minfo//OneDrive//Documents//My Recordings")
# playlist.download_playlist()
