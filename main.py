import os
import json
from channel import Channel
from video import Video, PLVideo
from playlist import PlayList
from googleapiclient.discovery import build

def task6():
    """Задание 6"""
    broken_video = Video('broken_video_id')
    print(broken_video.video_title)
    print(broken_video.video_count)

def main():
    task6()


if __name__ == "__main__":
    main()

