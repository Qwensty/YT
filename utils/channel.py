import json
import os
from googleapiclient.discovery import build



class Channel():
    # YT_API_KEY скопирован из гугла и вставлен в переменные окружения
    api_key: str = os.getenv('API KEY')

    def __init__(self, id):
        self.id = id
        self.json = ""
        self.get_json_by_id()

    def get_json_by_id(self):
        # создать специальный объект для работы с API
        with build('youtube', 'v3', developerKey=Channel.api_key) as youtube:
            channel = youtube.channels().list(id=self.id, part='snippet,statistics').execute()
            self.json = json.dumps(channel, indent=2, ensure_ascii=False)

    def __repr__(self):
        text = ""
        for dic in self.__dict__:
            text += dic + "=" + str(self.__dict__[dic]) + ", "
        return text[:-2]

    def print_info(self):
        print(self.json)