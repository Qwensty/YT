import os
import json

from googleapiclient.discovery import build


class Channel:

    def __init__(self, channel_id):
        self.__channel_id = channel_id
        youtube = self.get_service()
        self.channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        self.title = self.channel['items'][0]['snippet']['title']
        self.descr = self.channel['items'][0]['snippet']['description']
        self.url = 'https://www.youtube.com/channel/' + self.__channel_id
        self.subscriber_count = self.channel['items'][0]['statistics']['subscriberCount']
        self.video_count = self.channel['items'][0]['statistics']['videoCount']
        self.view_count = self.channel['items'][0]['statistics']['viewCount']

    @property
    def channel_id(self):
        return self.__channel_id

    def print_info(self):
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls):
        api_key: str = os.getenv('API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube

    def to_json(self, file_name: str):
        data = dict(id=self.__channel_id, title=self.title, description=self.descr, url=self.url, subscriber_count=self.subscriber_count, video_count=self.video_count, view_count=self.view_count)
        with open(file_name, "w", encoding="UTF-8") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

    def __str__(self):
        return f'Youtube-канал: {self.title}'

    def __add__(self, other):
        return int(self.subscriber_count) + int(other.subscriber_count)

    def __lt__(self, other):
        return int(self.subscriber_count) < int(other.subscriber_count)

    def __gt__(self, other):
        return int(self.subscriber_count) > int(other.subscriber_count)


vdud = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')
redact = Channel('UC1eFXmJNkjITxPFWTy6RsWg')
print(vdud)
print(redact)
print(vdud < redact)
print(vdud > redact)
print(vdud + redact)
vdud.to_json('vdud.json')
