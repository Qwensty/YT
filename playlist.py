from datetime import timedelta as timedelta
import isodate
from googleapiclient.discovery import build
from video import Video
from youtube_class_abstract import Youtube_class
from config import api_key as key_for_youtube
class PlayList(Youtube_class):
    """
    Класс PlayList, унаследован от абстрактного класса Youtube_class.
    """

    api_key = ""
    videos = []

    @classmethod
    def set_api_key(cls):
        """метод класса возвращает ключ для работы с youtube"""
        cls.api_key = key_for_youtube
        return cls.api_key

    @classmethod
    def get_service(cls):
        """метод класса возвращает объект для работы с youtube"""
        with build('youtube', 'v3', developerKey=cls.api_key) as youtube:
            return youtube

    def __init__(self, playlist_id: str) -> None:
        """
        инициализация объекта класса PlayList
        """
        self.playlist_id = playlist_id
        self.url = "https://www.youtube.com/playlist?list=" + playlist_id
        self.set_api_key()
        self.youtube = self.get_service()
        self.get_playlist_statistic()

    def get_playlist_statistic(self) -> list:
        """
        метод получения статистики для видео из плейлиста.
         Атрибуты:
        - playlist_title: str - название плейлиста
        - videos: list - список объектов классса Video
        - title: str - название плейлиста
        - youtube - специальный объект для работы с youtube
        """
        playlist = self.youtube.playlists().\
            list(id=self.playlist_id, part='snippet').execute()
        self.title = playlist['items'][0]['snippet']['title']

        playlist_videos = self.youtube.playlistItems().\
            list(playlistId=self.playlist_id, part='contentDetails',\
            maxResults=50,).execute()
        # получить id видео из плейлиста, создать по id объекты Video
        # и записать в список
        self.videos: list = [Video(video['contentDetails']['videoId']) \
            for video in playlist_videos['items']]
        return self.videos

    def show_best_video(self) -> str:
        """
        метод возвращает ссылку на самое популярное видео
        из плейлиста (по количеству лайков)
        """
        max_video_likes = 0
        url_max_video_likes = ""
        for video in self.videos:
            if max_video_likes < int(video.video_likes):
                max_video_likes = int(video.video_likes)
                url_max_video_likes = "https://www.youtube.com/watch?v=" \
                    + video.video_id
        return url_max_video_likes

    @property
    def total_duration(self) -> timedelta:
        """
        Возвращает суммарную длительность плейлиста в формате объекта
        timedelta. Метод-геттер.
        """
        # формирует список из id видео в плейлисте для передачи его в запрос
        video_ids = [video.video_id for video in self.videos]

        # получем список объектов Video из плейлиста
        video_response = self.youtube.videos().\
            list(part='contentDetails,statistics', id=','.join(video_ids)).execute()

        # пустое начальное значение
        duration_total = timedelta(0)

        for video in video_response['items']:
            # Длятельности YouTube-видео представлены в ISO 8601 формате
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            duration_total += duration
        return duration_total