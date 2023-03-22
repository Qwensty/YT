import os
import json

from googleapiclient.discovery import build


class Video():

    api_key = ""

    @classmethod
    def get_service(cls):
        api_key: str = os.getenv('API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube


    def __init__(self, video_id):
        self.get_service
        self.video_id = video_id
        self.youtube = self.get_service()
        self.get_video_statistic()

    def get_video_statistic(self):
        """
        Метод получения статистики видео по его id.
        Атрибуты:
        - video_id - id видео из ютуб
        - video_name -название видео
        - video_count - количество просмотров
        - video_likes - количество лайков
        """
        try:
            video_response = self.youtube.videos().list(part='snippet,statistics', \
                id=self.video_id).execute()
            self.video_title: str = video_response['items'][0]['snippet']['title']
            self.view_count: int = video_response['items'][0]['statistics']['viewCount']
            self.video_likes: int = video_response['items'][0]['statistics']['likeCount']
            self.comment_count: int = video_response['items'][0]['statistics']['commentCount']
        except:
            # загрузка видео по id не удалась
            self.video_name = None
            self.video_count = None
            self.video_likes = None
            self.video_title = None
    def __repr__(self):

        text = ""
        for dic in self.__dict__:
            text += dic + "=" + str(self.__dict__[dic]) + ", "
        return text[:-2]

    def __str__(self):

        return self.video_title


class PLVideo(Video):


    def __init__(self, video_id, playlist_id):

        Video.__init__(self, video_id)
        self.playlist_id = playlist_id
        self.get_playlist_statistic()

    def get_playlist_statistic(self):
        """
        Метод получения статистики для видео из плейлиста.
        """
        playlist = self.youtube.playlists().list(id=self.playlist_id, part='snippet').execute()
        self.playlist_name = playlist['items'][0]['snippet']['title']



    def __repr__(self):

        text = ""
        for dic in self.__dict__:
            text += dic + "=" + str(self.__dict__[dic]) + ", "
        return text[:-2]

    def __str__(self):
        return f"{self.video_title} ({self.playlist_name})"